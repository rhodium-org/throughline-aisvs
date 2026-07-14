# standard-aisvs

The **OWASP Artificial Intelligence Security Verification Standard (AISVS) 1.0** expressed
as a [throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/rhodium-org/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its clauses as `aisvs:SR-0014`.

## Status

A grounded graph of
<!-- tl:count type == 'intent' -->
12
<!-- tl:end --> category intents,
<!-- tl:count type == 'user_requirement' -->
44
<!-- tl:end --> sub-section requirements and
<!-- tl:count type == 'system_requirement' -->
191
<!-- tl:end --> verification clauses, published to [`docs/spec.md`](docs/spec.md). The
counts are rendered from the live graph by `tl:count`, so they cannot drift.

## Why this source is multi-root

A throughline source gets **as many root intents as the standard has genuine "why"s** — a
single umbrella root would throw away the reason each clause exists, which is the whole
point of IDD. A single artificial `INT-0001` that every requirement ultimately hangs off is
the **anti-pattern**: it flattens twelve distinct security concerns into one bland "…exists".

AISVS publishes a distinct **Control Objective** for each of its 12 categories, and those
are twelve genuinely different reasons an AI system must behave — training-data integrity is
not the same "why" as agentic-action containment or adversarial robustness. So this graph
has **12 co-equal root intents** (all `normative: false`), each carrying its category's own
Control Objective as its `text`:

| Root | Category |
|---|---|
| `INT-0001` | **C1** — Training Data Integrity & Traceability |
| `INT-0002` | **C2** — Input Validation |
| `INT-0003` | **C3** — Model Lifecycle Management & Change Control |
| `INT-0004` | **C4** — Infrastructure, Configuration & Deployment Security |
| `INT-0005` | **C5** — Access Control & Identity for AI Components & Users |
| `INT-0006` | **C6** — Supply Chain Security for Models |
| `INT-0007` | **C7** — Model Behavior, Output Control & Safety Assurance |
| `INT-0008` | **C8** — Memory, Embeddings & Vector Database Security |
| `INT-0009` | **C9** — Orchestration & Agentic Security |
| `INT-0010` | **C10** — Model Context Protocol (MCP) Security |
| `INT-0011` | **C11** — Adversarial Robustness |
| `INT-0012` | **C12** — Monitoring, Logging & Anomaly Detection |

- Each of AISVS's **44 sub-sections** is a `user_requirement` that `derives_from` **its own
  category** (not a catch-all), and carries the sub-section's published prose as its
  `rationale` — the mid-level *why* AISVS actually writes down.
- Each **verification clause** is a `system_requirement` that `implements` its sub-section.
  AISVS's hierarchy is strict (one category per sub-section), so a clause grounds up to a
  category through `implements` → `derives_from` with no extra edge.

## The "various guises" — levels are attributes, not forks

AISVS grades every clause at assurance **level 1, 2 or 3** (increasing rigour). That grade
is an attribute, so **one graph carries all three profiles at once** — you don't fork the
repo or duplicate clauses per level:

- `attrs.level` — the assurance level (`1` / `2` / `3`). Filter `level in {1}` for the
  entry-level profile, `level in {1, 2}` for the standard profile, and so on.
- `attrs.source_ref` — the published AISVS number (`2.1.1` for a clause, `C2.1` for a
  sub-section, `C2` for a category), never the UID.

**Editions are git tags of this one repo.** `v1.0.0` tags the AISVS 1.0 edition; a future
AISVS release would be `v2.0.0` on this same repo. A consumer pins `aisvs@v1.0.0`. This is
the same editions-as-tags model as `standard-asvs` and `standard-wcag`.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0014`…), immutable and never the AISVS
  number. The AISVS number lives in `attrs.source_ref`.
- **Clause `text`** is the clause's normative "Verify that …" statement; a category root's
  `text` is its Control Objective; a sub-section's `rationale` is its published description.
  All come from the authoritative OWASP source (see `NOTICE`).
- The graph is generated from the vendored AISVS markdown under `tools/aisvs-1.0/` by
  `tools/generate.py` (permanent-UID, additive). Editing the spec means editing the vendored
  data + generator, not the YAML by hand.

## Composing it

In a consuming project's `throughline.toml`:

```toml
[sources.aisvs]
url = "https://github.com/rhodium-org/standard-aisvs"
ref = "v1.0.0"
```

Then reference a clause as `aisvs:SR-0014` (input normalization before tokenization) from
your own items.

## Licence

Repository structure, tooling and configuration: Apache-2.0 (see `LICENSE`). The AISVS
clause text, Control Objectives and sub-section descriptions are © the OWASP Foundation,
reused under CC BY-SA 4.0 with attribution — see `NOTICE`. Authoritative source:
https://github.com/OWASP/AISVS.
