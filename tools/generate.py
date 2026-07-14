#!/usr/bin/env python3
"""Generate the OWASP AISVS 1.0 throughline source from the vendored spec markdown.

OWASP publishes AISVS as one markdown file per category (vendored here under
``tools/aisvs-1.0/0x10-C*.md``, from https://github.com/OWASP/AISVS). This script turns
that prose into throughline items, mirroring the WCAG generator's discipline:

* **UIDs are permanent.** The mapping from a category/sub-section/clause to a throughline
  UID is derived from the items already on disk, keyed by ``attrs.source_ref`` (the AISVS
  handle: ``"C2"``, ``"C2.1"``, ``"2.1.1"``). Anything without an item yet gets a freshly
  allocated UID in document order; a UID, once allocated, never moves. Bodies regenerate
  from the markdown each run.

**The "why" spine is genuinely multi-root — the point of putting AISVS on the list.**
AISVS publishes a distinct **Control Objective** for each of its 12 categories, and those
are 12 genuinely different reasons an AI system must behave (training-data integrity is not
the same "why" as agentic-action containment or adversarial robustness). So there are
**12 co-equal root intents** (INT-0001..INT-0012 = C1..C12), never a single umbrella that
flattens every clause's reason-for-existing into one bland "…exists". Each category's
Control Objective prose *is* that root's ``text`` — the source's own words for why the
category earns its place.

Each sub-section (``## C2.1 Prompt Injection Defenses``) is a ``user_requirement`` that
``derives_from`` its own category root; the sub-section's own prose becomes its
``rationale`` — the mid-level "why" AISVS actually publishes. Each numbered clause
(``Verify that …``) is a ``system_requirement`` that ``implements`` its sub-section, with
the AISVS number in ``attrs.source_ref`` and the assurance level (1/2/3) in ``attrs.level``.
AISVS's hierarchy is strict (one category per sub-section, one sub-section per clause), so a
clause grounds to its category up implements→derives_from with no extra edge.

**The "various guises" are the levels, on one graph — not forks.** AISVS grades every
clause at level 1/2/3; that grade is an attribute, so a single graph carries all three
profiles at once. Editions (1.0, and future releases) are git tags of this one repo — the
same editions-as-tags model as standard-asvs and standard-wcag.

Usage:  python tools/generate.py
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SPEC_DIR = REPO / "tools" / "aisvs-1.0"
INTENTS_DIR = REPO / "intents"        # intent (category roots), prefix INT
SECTIONS_DIR = REPO / "sections"      # user_requirement (sub-sections), prefix UR
REQS_DIR = REPO / "requirements"      # system_requirement (clauses), prefix SR
SPEC = REPO / "docs" / "spec.md"

CATEGORY_RE = re.compile(r"^#\s+C(\d+)\s+(.+?)\s*$")
SUBSECTION_RE = re.compile(r"^##\s+C(\d+\.\d+)\s+(.+?)\s*$")
CLAUSE_NUM_RE = re.compile(r"^\d+\.\d+\.\d+$")


def _debold(s: str) -> str:
    return re.sub(r"\*\*", "", s).strip()


def _squash(lines: list[str]) -> str:
    return re.sub(r"\s+", " ", " ".join(l.strip() for l in lines)).strip()


def parse_category(path: Path) -> dict:
    """Parse one 0x10-C*.md into {num, title, objective, subsections:[...]}."""
    lines = path.read_text(encoding="utf-8").splitlines()
    num = title = None
    objective: list[str] = []
    subsections: list[dict] = []

    state = None  # None | "objective" | "sub-prose" | "sub-table"
    cur: dict | None = None

    for raw in lines:
        line = raw.rstrip()
        m = CATEGORY_RE.match(line)
        if m:
            num, title = m.group(1), m.group(2).strip()
            continue
        if line.strip() == "## Control Objective":
            state = "objective"
            continue
        ms = SUBSECTION_RE.match(line)
        if ms:
            cur = {"ref": f"C{ms.group(1)}", "handle": ms.group(2).strip(),
                   "prose": [], "clauses": []}
            subsections.append(cur)
            state = "sub-prose"
            continue
        if line.startswith("## "):  # References or any other trailing section
            state = None
            cur = None
            continue
        if line.strip() == "---":
            if state == "objective":
                state = None
            continue

        if state == "objective":
            if line.strip():
                objective.append(line)
        elif state in ("sub-prose", "sub-table") and cur is not None:
            if line.startswith("|"):
                state = "sub-table"
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) < 3:
                    continue
                clause_num = _debold(cells[0])
                if not CLAUSE_NUM_RE.match(clause_num):
                    continue  # header row (`#`) or separator (`:---`)
                cur["clauses"].append({
                    "num": clause_num,
                    "text": _debold(cells[1]),
                    "level": _debold(cells[2]),
                })
            elif state == "sub-prose" and line.strip():
                cur["prose"].append(line)

    return {"num": num, "title": title, "objective": _squash(objective),
            "subsections": subsections}


def load_categories() -> list[dict]:
    cats = []
    for path in sorted(SPEC_DIR.glob("0x10-C*.md")):
        cats.append(parse_category(path))
    return sorted(cats, key=lambda c: int(c["num"]))


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=90),
        encoding="utf-8",
    )


def _scan(dir_: Path) -> dict[str, str]:
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max(ref2uid: dict[str, str], prefix: str) -> int:
    return max((int(u.split("-")[1]) for u in ref2uid.values()
               if u.startswith(prefix + "-")), default=0)


def generate() -> dict[str, int]:
    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(SECTIONS_DIR)
    sr_ref = _scan(REQS_DIR)
    n_int = _max(int_ref, "INT") + 1
    n_ur = _max(ur_ref, "UR") + 1
    n_sr = _max(sr_ref, "SR") + 1
    counts = {"int": 0, "ur": 0, "sr": 0}

    for cat in load_categories():
        cref = f"C{cat['num']}"
        int_uid = int_ref.get(cref)
        if int_uid is None:
            int_uid = f"INT-{n_int:04d}"; n_int += 1; int_ref[cref] = int_uid
            counts["int"] += 1
        _dump(INTENTS_DIR / f"{int_uid}.yml", {
            "uid": int_uid,
            "type": "intent",
            "status": "approved",
            "title": f"{cref} — {cat['title']}",
            "text": cat["objective"],
            "normative": False,
            "attrs": {"source_ref": cref},
        })

        for sub in cat["subsections"]:
            ur_uid = ur_ref.get(sub["ref"])
            if ur_uid is None:
                ur_uid = f"UR-{n_ur:04d}"; n_ur += 1; ur_ref[sub["ref"]] = ur_uid
                counts["ur"] += 1
            _dump(SECTIONS_DIR / f"{ur_uid}.yml", {
                "uid": ur_uid,
                "type": "user_requirement",
                "status": "approved",
                "title": f"{sub['ref']} — {sub['handle']}",
                "text": sub["handle"],
                "rationale": _squash(sub["prose"]),
                "links": [{"target": int_uid, "type": "derives_from"}],
                "attrs": {"source_ref": sub["ref"]},
            })

            for cl in sub["clauses"]:
                sr_uid = sr_ref.get(cl["num"])
                if sr_uid is None:
                    sr_uid = f"SR-{n_sr:04d}"; n_sr += 1; sr_ref[cl["num"]] = sr_uid
                    counts["sr"] += 1
                _dump(REQS_DIR / f"{sr_uid}.yml", {
                    "uid": sr_uid,
                    "type": "system_requirement",
                    "status": "approved",
                    "title": f"AISVS {cl['num']}",
                    "text": cl["text"],
                    "links": [{"target": ur_uid, "type": "implements"}],
                    "attrs": {"source_ref": cl["num"], "level": cl["level"]},
                })

    return counts


SPEC_HEADER = """\
# OWASP AISVS 1.0 — throughline source

Generated from the graph. Prose between `tl:item` / `tl:table` markers is injected by
`tl docs` — edit the YAML items (or `tools/aisvs-1.0/*.md` + `tools/generate.py`), not the
injected regions.

The "why" spine is **multi-root by design**: AISVS's 12 categories carry 12 distinct
Control Objectives — 12 root `intent`s, not one umbrella. Each sub-section is a
`user_requirement` that `derives_from` its category and carries the sub-section's own prose
as its `rationale`; each numbered clause is a `system_requirement` that `implements` its
sub-section. The AISVS number lives in `attrs.source_ref` (`"2.1.1"`) and the assurance
level in `attrs.level` (1/2/3), so one graph carries all three profiles at once.
"""


def generate_spec() -> None:
    parts = [SPEC_HEADER]
    for cat in load_categories():
        cref = f"C{cat['num']}"
        int_uid = _scan(INTENTS_DIR)[cref]
        parts.append(f"# {cref} {cat['title']} — the root\n")
        parts.append(f"<!-- tl:item {int_uid} -->\n<!-- tl:end -->\n")
        for sub in cat["subsections"]:
            ur_uid = _scan(SECTIONS_DIR)[sub["ref"]]
            parts.append(f"## {sub['ref']} {sub['handle']}\n")
            parts.append(f"<!-- tl:item {ur_uid} -->\n<!-- tl:end -->\n")
            flt = ("type == 'system_requirement' and "
                   f"attrs.get('source_ref').startswith('{sub['ref'][1:]}.')")
            parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.parent.mkdir(parents=True, exist_ok=True)
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    c = generate()
    generate_spec()
    print(f"intents:      {c['int']} new (categories / Control Objectives)")
    print(f"sections:     {c['ur']} new (user_requirements)")
    print(f"requirements: {c['sr']} new (system_requirements)")
    print(f"totals: {len(list(INTENTS_DIR.glob('INT-*.yml')))} INT, "
          f"{len(list(SECTIONS_DIR.glob('UR-*.yml')))} UR, "
          f"{len(list(REQS_DIR.glob('SR-*.yml')))} SR")
    print("next: run `tl docs` to inject content, then `tl check --strict`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
