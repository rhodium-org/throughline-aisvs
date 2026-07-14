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

# C1 Training Data Integrity & Traceability — the root

<!-- tl:item INT-0001 -->
**INT-0001 — C1 — Training Data Integrity & Traceability** — `intent`, status `approved`

> This chapter addresses protecting the integrity and traceability of training data as it is sourced, handled, and maintained.

**source_ref**: C1
<!-- tl:end -->

## C1.1 Training Data Origin & Data Security

<!-- tl:item UR-0001 -->
**UR-0001 — C1.1 — Training Data Origin & Data Security** — `user_requirement`, status `approved`

> Training Data Origin & Data Security

*Rationale:* Training data origin and security are critical to the trustworthiness of any AI system. Datasets must be sourced from verifiable origins, tracked across their full lifecycle, and protected against tampering, corruption, and poisoning so that unauthorized modification can be detected.

**source_ref**: C1.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('1.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | AISVS 1.1.1 |
| SR-0002 | system_requirement | approved | AISVS 1.1.2 |
| SR-0003 | system_requirement | approved | AISVS 1.1.3 |
| SR-0004 | system_requirement | approved | AISVS 1.1.4 |
| SR-0005 | system_requirement | approved | AISVS 1.1.5 |
<!-- tl:end -->

## C1.2 Data Labeling and Annotation Security

<!-- tl:item UR-0002 -->
**UR-0002 — C1.2 — Data Labeling and Annotation Security** — `user_requirement`, status `approved`

> Data Labeling and Annotation Security

*Rationale:* Labeling and annotation processes must be protected against unauthorized modification, data leakage, and integrity compromise. Annotation platforms should enforce access control, preserve auditability, and protect labeling artifacts and sensitive label content throughout the training pipeline.

**source_ref**: C1.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('1.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0006 | system_requirement | approved | AISVS 1.2.1 |
| SR-0007 | system_requirement | approved | AISVS 1.2.2 |
| SR-0008 | system_requirement | approved | AISVS 1.2.3 |
<!-- tl:end -->

## C1.3 Training Data Quality and Security Assurance

<!-- tl:item UR-0003 -->
**UR-0003 — C1.3 — Training Data Quality and Security Assurance** — `user_requirement`, status `approved`

> Training Data Quality and Security Assurance

*Rationale:* Quality and security assurance controls help detect corruption, poisoning, labeling errors, and exploitable dataset patterns before they affect model behavior. Pipelines should combine automated validation, poisoning detection, label quality checks, and bias analysis.

**source_ref**: C1.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('1.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0009 | system_requirement | approved | AISVS 1.3.1 |
| SR-0010 | system_requirement | approved | AISVS 1.3.2 |
| SR-0011 | system_requirement | approved | AISVS 1.3.3 |
| SR-0012 | system_requirement | approved | AISVS 1.3.4 |
| SR-0013 | system_requirement | approved | AISVS 1.3.5 |
<!-- tl:end -->

# C2 Input Validation — the root

<!-- tl:item INT-0002 -->
**INT-0002 — C2 — Input Validation** — `intent`, status `approved`

> This chapter addresses validation of all inputs as a first-line defense against prompt injection, one of the most damaging attacks on AI systems.

**source_ref**: C2
<!-- tl:end -->

## C2.1 Prompt Injection Defenses

<!-- tl:item UR-0004 -->
**UR-0004 — C2.1 — Prompt Injection Defenses** — `user_requirement`, status `approved`

> Prompt Injection Defenses

*Rationale:* Prompt injection is one of the top risks for AI systems, and defending against it requires a combination of pattern filters, data classifiers, and instruction hierarchy enforcement.

**source_ref**: C2.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('2.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0014 | system_requirement | approved | AISVS 2.1.1 |
| SR-0015 | system_requirement | approved | AISVS 2.1.2 |
| SR-0016 | system_requirement | approved | AISVS 2.1.3 |
| SR-0017 | system_requirement | approved | AISVS 2.1.4 |
| SR-0018 | system_requirement | approved | AISVS 2.1.5 |
| SR-0019 | system_requirement | approved | AISVS 2.1.6 |
| SR-0020 | system_requirement | approved | AISVS 2.1.7 |
| SR-0021 | system_requirement | approved | AISVS 2.1.8 |
<!-- tl:end -->

## C2.2 Content & Policy Screening

<!-- tl:item UR-0005 -->
**UR-0005 — C2.2 — Content & Policy Screening** — `user_requirement`, status `approved`

> Content & Policy Screening

*Rationale:* Syntactically valid prompts may still request disallowed content such as policy-violating instructions, harmful material, or restricted information. Input-side content screening prevents such prompts from reaching the model.

**source_ref**: C2.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('2.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0022 | system_requirement | approved | AISVS 2.2.1 |
| SR-0023 | system_requirement | approved | AISVS 2.2.2 |
| SR-0024 | system_requirement | approved | AISVS 2.2.3 |
| SR-0025 | system_requirement | approved | AISVS 2.2.4 |
<!-- tl:end -->

# C3 Model Lifecycle Management & Change Control — the root

<!-- tl:item INT-0003 -->
**INT-0003 — C3 — Model Lifecycle Management & Change Control** — `intent`, status `approved`

> This chapter addresses control of model changes so that unauthorized or unsafe modifications cannot reach production.

**source_ref**: C3
<!-- tl:end -->

## C3.1 Model Authorization & Integrity

<!-- tl:item UR-0006 -->
**UR-0006 — C3.1 — Model Authorization & Integrity** — `user_requirement`, status `approved`

> Model Authorization & Integrity

*Rationale:* Only authorized models with verified integrity should reach production environments.

**source_ref**: C3.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('3.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0026 | system_requirement | approved | AISVS 3.1.1 |
| SR-0027 | system_requirement | approved | AISVS 3.1.2 |
| SR-0028 | system_requirement | approved | AISVS 3.1.3 |
<!-- tl:end -->

## C3.2 Model Validation & Testing

<!-- tl:item UR-0007 -->
**UR-0007 — C3.2 — Model Validation & Testing** — `user_requirement`, status `approved`

> Model Validation & Testing

*Rationale:* Models must pass defined security and safety validations before deployment.

**source_ref**: C3.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('3.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0029 | system_requirement | approved | AISVS 3.2.1 |
| SR-0030 | system_requirement | approved | AISVS 3.2.2 |
| SR-0031 | system_requirement | approved | AISVS 3.2.3 |
<!-- tl:end -->

## C3.3 Controlled Deployment & Rollback

<!-- tl:item UR-0008 -->
**UR-0008 — C3.3 — Controlled Deployment & Rollback** — `user_requirement`, status `approved`

> Controlled Deployment & Rollback

*Rationale:* Model deployments must be controlled, monitored, and reversible to support lifecycle management.

**source_ref**: C3.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('3.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0032 | system_requirement | approved | AISVS 3.3.1 |
| SR-0033 | system_requirement | approved | AISVS 3.3.2 |
| SR-0034 | system_requirement | approved | AISVS 3.3.3 |
<!-- tl:end -->

## C3.4 Secure Development Practices

<!-- tl:item UR-0009 -->
**UR-0009 — C3.4 — Secure Development Practices** — `user_requirement`, status `approved`

> Secure Development Practices

*Rationale:* Model development environments must be separated from production environments.

**source_ref**: C3.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('3.4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0035 | system_requirement | approved | AISVS 3.4.1 |
| SR-0036 | system_requirement | approved | AISVS 3.4.2 |
<!-- tl:end -->

## C3.5 Pipeline Fine-Tuning

<!-- tl:item UR-0010 -->
**UR-0010 — C3.5 — Pipeline Fine-Tuning** — `user_requirement`, status `approved`

> Pipeline Fine-Tuning

*Rationale:* Fine-tuning pipelines are high-privilege operations that can alter deployed model behavior at scale. Multi-stage pipelines compound this risk because a compromise at any intermediate stage produces a subtly altered artifact that subsequent stages accept.

**source_ref**: C3.5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('3.5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0037 | system_requirement | approved | AISVS 3.5.1 |
| SR-0038 | system_requirement | approved | AISVS 3.5.2 |
| SR-0039 | system_requirement | approved | AISVS 3.5.3 |
| SR-0040 | system_requirement | approved | AISVS 3.5.4 |
<!-- tl:end -->

# C4 Infrastructure, Configuration & Deployment Security — the root

<!-- tl:item INT-0004 -->
**INT-0004 — C4 — Infrastructure, Configuration & Deployment Security** — `intent`, status `approved`

> This chapter addresses hardening AI-specific infrastructure components against model theft, data leakage, and cross-tenant contamination.

**source_ref**: C4
<!-- tl:end -->

## C4.1 AI Workload Sandboxing & Validation

<!-- tl:item UR-0011 -->
**UR-0011 — C4.1 — AI Workload Sandboxing & Validation** — `user_requirement`, status `approved`

> AI Workload Sandboxing & Validation

*Rationale:* Untrusted AI models must be isolated in secure sandboxes, and sensitive AI workloads protected using trusted execution environments (TEEs) and confidential computing technologies.

**source_ref**: C4.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('4.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0041 | system_requirement | approved | AISVS 4.1.1 |
| SR-0042 | system_requirement | approved | AISVS 4.1.2 |
| SR-0043 | system_requirement | approved | AISVS 4.1.3 |
| SR-0044 | system_requirement | approved | AISVS 4.1.4 |
<!-- tl:end -->

## C4.2 AI Hardware Security

<!-- tl:item UR-0012 -->
**UR-0012 — C4.2 — AI Hardware Security** — `user_requirement`, status `approved`

> AI Hardware Security

*Rationale:* AI-specific hardware components, including GPUs, TPUs, and specialized AI accelerators, must be secured.

**source_ref**: C4.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('4.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0045 | system_requirement | approved | AISVS 4.2.1 |
| SR-0046 | system_requirement | approved | AISVS 4.2.2 |
| SR-0047 | system_requirement | approved | AISVS 4.2.3 |
| SR-0048 | system_requirement | approved | AISVS 4.2.4 |
| SR-0049 | system_requirement | approved | AISVS 4.2.5 |
<!-- tl:end -->

## C4.3 Edge & Distributed AI Security

<!-- tl:item UR-0013 -->
**UR-0013 — C4.3 — Edge & Distributed AI Security** — `user_requirement`, status `approved`

> Edge & Distributed AI Security

*Rationale:* Distributed AI deployments, including edge computing, federated learning, and multi-site architectures, must be secured.

**source_ref**: C4.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('4.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0050 | system_requirement | approved | AISVS 4.3.1 |
| SR-0051 | system_requirement | approved | AISVS 4.3.2 |
| SR-0052 | system_requirement | approved | AISVS 4.3.3 |
| SR-0053 | system_requirement | approved | AISVS 4.3.4 |
| SR-0054 | system_requirement | approved | AISVS 4.3.5 |
<!-- tl:end -->

# C5 Access Control & Identity for AI Components & Users — the root

<!-- tl:item INT-0005 -->
**INT-0005 — C5 — Access Control & Identity for AI Components & Users** — `intent`, status `approved`

> This chapter addresses access control challenges that AI systems introduce beyond traditional application security.

**source_ref**: C5
<!-- tl:end -->

## C5.1 Authentication

<!-- tl:item UR-0014 -->
**UR-0014 — C5.1 — Authentication** — `user_requirement`, status `approved`

> Authentication

*Rationale:* AI agents and human users accessing resources must be properly authenticated and authorized for their level of access.

**source_ref**: C5.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('5.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0055 | system_requirement | approved | AISVS 5.1.1 |
| SR-0056 | system_requirement | approved | AISVS 5.1.2 |
<!-- tl:end -->

## C5.2 AI Resource Authorization & Classification

<!-- tl:item UR-0015 -->
**UR-0015 — C5.2 — AI Resource Authorization & Classification** — `user_requirement`, status `approved`

> AI Resource Authorization & Classification

*Rationale:* The caller's authorization context must be enforced through AI-specific query pipelines (RAG retrieval, embedding lookups, inference chains) so the system does not return data the caller is not entitled to access.

**source_ref**: C5.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('5.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0057 | system_requirement | approved | AISVS 5.2.1 |
| SR-0058 | system_requirement | approved | AISVS 5.2.2 |
| SR-0059 | system_requirement | approved | AISVS 5.2.3 |
| SR-0060 | system_requirement | approved | AISVS 5.2.4 |
| SR-0061 | system_requirement | approved | AISVS 5.2.5 |
| SR-0062 | system_requirement | approved | AISVS 5.2.6 |
| SR-0063 | system_requirement | approved | AISVS 5.2.7 |
<!-- tl:end -->

## C5.3 Multi-Tenant Isolation

<!-- tl:item UR-0016 -->
**UR-0016 — C5.3 — Multi-Tenant Isolation** — `user_requirement`, status `approved`

> Multi-Tenant Isolation

*Rationale:* Cross-tenant information leakage through AI-specific shared infrastructure, such as inference caches and shared model state, must be prevented.

**source_ref**: C5.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('5.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0064 | system_requirement | approved | AISVS 5.3.1 |
| SR-0065 | system_requirement | approved | AISVS 5.3.2 |
<!-- tl:end -->

# C6 Supply Chain Security for Models — the root

<!-- tl:item INT-0006 -->
**INT-0006 — C6 — Supply Chain Security for Models** — `intent`, status `approved`

> This chapter addresses defending against AI supply chain attacks that exploit third-party models, frameworks, or datasets to embed backdoors, bias, or exploitable code.

**source_ref**: C6
<!-- tl:end -->

## C6.1 Model Artifact Integrity

<!-- tl:item UR-0017 -->
**UR-0017 — C6.1 — Model Artifact Integrity** — `user_requirement`, status `approved`

> Model Artifact Integrity

*Rationale:* Third-party model origins must be authenticated and checked for hidden behavior before fine-tuning or deployment, and AI artifacts should be downloaded only from approved sources.

**source_ref**: C6.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('6.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0066 | system_requirement | approved | AISVS 6.1.1 |
| SR-0067 | system_requirement | approved | AISVS 6.1.2 |
| SR-0068 | system_requirement | approved | AISVS 6.1.3 |
| SR-0069 | system_requirement | approved | AISVS 6.1.4 |
<!-- tl:end -->

## C6.2 AI BOM & Supply Chain Monitoring

<!-- tl:item UR-0018 -->
**UR-0018 — C6.2 — AI BOM & Supply Chain Monitoring** — `user_requirement`, status `approved`

> AI BOM & Supply Chain Monitoring

*Rationale:* Detailed AI-specific bills of materials must be generated and signed, with readiness to respond to supply chain compromise events.

**source_ref**: C6.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('6.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0070 | system_requirement | approved | AISVS 6.2.1 |
| SR-0071 | system_requirement | approved | AISVS 6.2.2 |
| SR-0072 | system_requirement | approved | AISVS 6.2.3 |
<!-- tl:end -->

# C7 Model Behavior, Output Control & Safety Assurance — the root

<!-- tl:item INT-0007 -->
**INT-0007 — C7 — Model Behavior, Output Control & Safety Assurance** — `intent`, status `approved`

> This chapter addresses constraining, validating, and monitoring model outputs so that unsafe, malformed, or high-risk responses cannot reach users or downstream systems.

**source_ref**: C7
<!-- tl:end -->

## C7.1 Output Format Enforcement

<!-- tl:item UR-0019 -->
**UR-0019 — C7.1 — Output Format Enforcement** — `user_requirement`, status `approved`

> Output Format Enforcement

*Rationale:* Model outputs must be structured and validated to reduce downstream injection risk.

**source_ref**: C7.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('7.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0073 | system_requirement | approved | AISVS 7.1.1 |
| SR-0074 | system_requirement | approved | AISVS 7.1.2 |
<!-- tl:end -->

## C7.2 Hallucination Detection & Mitigation

<!-- tl:item UR-0020 -->
**UR-0020 — C7.2 — Hallucination Detection & Mitigation** — `user_requirement`, status `approved`

> Hallucination Detection & Mitigation

*Rationale:* Potentially inaccurate or fabricated content must be detected so unreliable outputs do not reach users or downstream systems.

**source_ref**: C7.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('7.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0075 | system_requirement | approved | AISVS 7.2.1 |
| SR-0076 | system_requirement | approved | AISVS 7.2.2 |
| SR-0077 | system_requirement | approved | AISVS 7.2.3 |
<!-- tl:end -->

## C7.3 Output Safety

<!-- tl:item UR-0021 -->
**UR-0021 — C7.3 — Output Safety** — `user_requirement`, status `approved`

> Output Safety

*Rationale:* Technical controls must detect and remove unsafe content before it is shown to the user.

**source_ref**: C7.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('7.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0078 | system_requirement | approved | AISVS 7.3.1 |
| SR-0079 | system_requirement | approved | AISVS 7.3.2 |
| SR-0080 | system_requirement | approved | AISVS 7.3.3 |
| SR-0081 | system_requirement | approved | AISVS 7.3.4 |
<!-- tl:end -->

## C7.4 Source Attribution & Citation Integrity

<!-- tl:item UR-0022 -->
**UR-0022 — C7.4 — Source Attribution & Citation Integrity** — `user_requirement`, status `approved`

> Source Attribution & Citation Integrity

*Rationale:* RAG-grounded outputs must be traceable to their source documents, with cited claims verifiably supported by retrieved content.

**source_ref**: C7.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('7.4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0082 | system_requirement | approved | AISVS 7.4.1 |
| SR-0083 | system_requirement | approved | AISVS 7.4.2 |
| SR-0084 | system_requirement | approved | AISVS 7.4.3 |
| SR-0085 | system_requirement | approved | AISVS 7.4.4 |
<!-- tl:end -->

# C8 Memory, Embeddings & Vector Database Security — the root

<!-- tl:item INT-0008 -->
**INT-0008 — C8 — Memory, Embeddings & Vector Database Security** — `intent`, status `approved`

> This chapter addresses securing the embeddings and vector stores that act as semi-persistent and persistent "memory" for AI systems through Retrieval-Augmented Generation (RAG).

**source_ref**: C8
<!-- tl:end -->

## C8.1 Access Controls on Memory & RAG Indices

<!-- tl:item UR-0023 -->
**UR-0023 — C8.1 — Access Controls on Memory & RAG Indices** — `user_requirement`, status `approved`

> Access Controls on Memory & RAG Indices

*Rationale:* Fine-grained access controls and query-time scope enforcement must be applied to every vector collection.

**source_ref**: C8.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('8.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0086 | system_requirement | approved | AISVS 8.1.1 |
| SR-0087 | system_requirement | approved | AISVS 8.1.2 |
| SR-0088 | system_requirement | approved | AISVS 8.1.3 |
<!-- tl:end -->

## C8.2 Embedding Sanitization & Validation

<!-- tl:item UR-0024 -->
**UR-0024 — C8.2 — Embedding Sanitization & Validation** — `user_requirement`, status `approved`

> Embedding Sanitization & Validation

*Rationale:* Content must be pre-screened before vectorization, and memory writes treated as untrusted input, to prevent ingestion of unsafe payloads.

**source_ref**: C8.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('8.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0089 | system_requirement | approved | AISVS 8.2.1 |
| SR-0090 | system_requirement | approved | AISVS 8.2.2 |
| SR-0091 | system_requirement | approved | AISVS 8.2.3 |
| SR-0092 | system_requirement | approved | AISVS 8.2.4 |
| SR-0093 | system_requirement | approved | AISVS 8.2.5 |
<!-- tl:end -->

## C8.3 Memory Expiry & Revocation

<!-- tl:item UR-0025 -->
**UR-0025 — C8.3 — Memory Expiry & Revocation** — `user_requirement`, status `approved`

> Memory Expiry & Revocation

*Rationale:* Retention and revocation must be explicit and enforceable for memory and RAG indices.

**source_ref**: C8.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('8.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0094 | system_requirement | approved | AISVS 8.3.1 |
| SR-0095 | system_requirement | approved | AISVS 8.3.2 |
| SR-0096 | system_requirement | approved | AISVS 8.3.3 |
<!-- tl:end -->

# C9 Orchestration & Agentic Security — the root

<!-- tl:item INT-0009 -->
**INT-0009 — C9 — Orchestration & Agentic Security** — `intent`, status `approved`

> This chapter addresses ensuring autonomous and multi-agent systems execute only authorized, intended, and bounded actions.

**source_ref**: C9
<!-- tl:end -->

## C9.1 Execution Budgets, Loop Control, and Circuit Breakers

<!-- tl:item UR-0026 -->
**UR-0026 — C9.1 — Execution Budgets, Loop Control, and Circuit Breakers** — `user_requirement`, status `approved`

> Execution Budgets, Loop Control, and Circuit Breakers

*Rationale:* Runtime expansion (recursion, concurrency, cost) must be bounded, with safe halting on runaway behavior.

**source_ref**: C9.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('9.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0097 | system_requirement | approved | AISVS 9.1.1 |
| SR-0098 | system_requirement | approved | AISVS 9.1.2 |
| SR-0099 | system_requirement | approved | AISVS 9.1.3 |
<!-- tl:end -->

## C9.2 High-Impact Action Approval and Irreversibility Controls

<!-- tl:item UR-0027 -->
**UR-0027 — C9.2 — High-Impact Action Approval and Irreversibility Controls** — `user_requirement`, status `approved`

> High-Impact Action Approval and Irreversibility Controls

*Rationale:* Privileged, high-impact, or hard-to-reverse agent actions must require trusted approval checkpoints.

**source_ref**: C9.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('9.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0100 | system_requirement | approved | AISVS 9.2.1 |
| SR-0101 | system_requirement | approved | AISVS 9.2.2 |
| SR-0102 | system_requirement | approved | AISVS 9.2.3 |
| SR-0103 | system_requirement | approved | AISVS 9.2.4 |
| SR-0104 | system_requirement | approved | AISVS 9.2.5 |
| SR-0105 | system_requirement | approved | AISVS 9.2.6 |
| SR-0106 | system_requirement | approved | AISVS 9.2.7 |
| SR-0107 | system_requirement | approved | AISVS 9.2.8 |
| SR-0108 | system_requirement | approved | AISVS 9.2.9 |
| SR-0109 | system_requirement | approved | AISVS 9.2.10 |
<!-- tl:end -->

## C9.3 Component Isolation and Tool Authorization

<!-- tl:item UR-0028 -->
**UR-0028 — C9.3 — Component Isolation and Tool Authorization** — `user_requirement`, status `approved`

> Component Isolation and Tool Authorization

*Rationale:* Tool and plugin execution, loading, and outputs must be constrained to prevent unauthorized system access and unsafe side effects.

**source_ref**: C9.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('9.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0110 | system_requirement | approved | AISVS 9.3.1 |
| SR-0111 | system_requirement | approved | AISVS 9.3.2 |
| SR-0112 | system_requirement | approved | AISVS 9.3.3 |
| SR-0113 | system_requirement | approved | AISVS 9.3.4 |
| SR-0114 | system_requirement | approved | AISVS 9.3.5 |
| SR-0115 | system_requirement | approved | AISVS 9.3.6 |
| SR-0116 | system_requirement | approved | AISVS 9.3.7 |
| SR-0117 | system_requirement | approved | AISVS 9.3.8 |
<!-- tl:end -->

## C9.4 Agent and Orchestrator Identity

<!-- tl:item UR-0029 -->
**UR-0029 — C9.4 — Agent and Orchestrator Identity** — `user_requirement`, status `approved`

> Agent and Orchestrator Identity

*Rationale:* Every action must be attributable and every mutation detectable.

**source_ref**: C9.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('9.4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0118 | system_requirement | approved | AISVS 9.4.1 |
| SR-0119 | system_requirement | approved | AISVS 9.4.2 |
| SR-0120 | system_requirement | approved | AISVS 9.4.3 |
| SR-0121 | system_requirement | approved | AISVS 9.4.4 |
<!-- tl:end -->

## C9.5 Agent Authorization, Delegation, and Continuous Enforcement

<!-- tl:item UR-0030 -->
**UR-0030 — C9.5 — Agent Authorization, Delegation, and Continuous Enforcement** — `user_requirement`, status `approved`

> Agent Authorization, Delegation, and Continuous Enforcement

*Rationale:* Every action must be authorized at execution time and constrained by scope.

**source_ref**: C9.5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('9.5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0122 | system_requirement | approved | AISVS 9.5.1 |
| SR-0123 | system_requirement | approved | AISVS 9.5.2 |
| SR-0124 | system_requirement | approved | AISVS 9.5.3 |
| SR-0125 | system_requirement | approved | AISVS 9.5.4 |
| SR-0126 | system_requirement | approved | AISVS 9.5.5 |
| SR-0127 | system_requirement | approved | AISVS 9.5.6 |
<!-- tl:end -->

## C9.6 Shutdown and Graceful Degradation

<!-- tl:item UR-0031 -->
**UR-0031 — C9.6 — Shutdown and Graceful Degradation** — `user_requirement`, status `approved`

> Shutdown and Graceful Degradation

*Rationale:* Shutdown and graceful degradation paths must remain under human control, with mechanisms that stay reliable and are exercised over time.

**source_ref**: C9.6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('9.6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0128 | system_requirement | approved | AISVS 9.6.1 |
| SR-0129 | system_requirement | approved | AISVS 9.6.2 |
| SR-0130 | system_requirement | approved | AISVS 9.6.3 |
<!-- tl:end -->

# C10 Model Context Protocol (MCP) Security — the root

<!-- tl:item INT-0010 -->
**INT-0010 — C10 — Model Context Protocol (MCP) Security** — `intent`, status `approved`

> This chapter addresses secure discovery, authentication, authorization, transport, and use of MCP-based tool and resource integrations.

**source_ref**: C10
<!-- tl:end -->

## C10.1 Component Integrity

<!-- tl:item UR-0032 -->
**UR-0032 — C10.1 — Component Integrity** — `user_requirement`, status `approved`

> Component Integrity

*Rationale:* Only trusted MCP components must be used, and locally launched servers must be secured.

**source_ref**: C10.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('10.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0131 | system_requirement | approved | AISVS 10.1.1 |
| SR-0132 | system_requirement | approved | AISVS 10.1.2 |
| SR-0133 | system_requirement | approved | AISVS 10.1.3 |
<!-- tl:end -->

## C10.2 Authentication & Authorization

<!-- tl:item UR-0033 -->
**UR-0033 — C10.2 — Authentication & Authorization** — `user_requirement`, status `approved`

> Authentication & Authorization

*Rationale:* Callers must be authenticated and access to MCP servers authorized, following protocol best practices.

**source_ref**: C10.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('10.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0134 | system_requirement | approved | AISVS 10.2.1 |
| SR-0135 | system_requirement | approved | AISVS 10.2.2 |
| SR-0136 | system_requirement | approved | AISVS 10.2.3 |
| SR-0137 | system_requirement | approved | AISVS 10.2.4 |
| SR-0138 | system_requirement | approved | AISVS 10.2.5 |
| SR-0139 | system_requirement | approved | AISVS 10.2.6 |
| SR-0140 | system_requirement | approved | AISVS 10.2.7 |
<!-- tl:end -->

## C10.3 Secure Transport

<!-- tl:item UR-0034 -->
**UR-0034 — C10.3 — Secure Transport** — `user_requirement`, status `approved`

> Secure Transport

*Rationale:* MCP communications must be secured following protocol best practices.

**source_ref**: C10.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('10.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0141 | system_requirement | approved | AISVS 10.3.1 |
| SR-0142 | system_requirement | approved | AISVS 10.3.2 |
| SR-0143 | system_requirement | approved | AISVS 10.3.3 |
| SR-0144 | system_requirement | approved | AISVS 10.3.4 |
| SR-0145 | system_requirement | approved | AISVS 10.3.5 |
<!-- tl:end -->

## C10.4 Schema, Message, and Input Validation

<!-- tl:item UR-0035 -->
**UR-0035 — C10.4 — Schema, Message, and Input Validation** — `user_requirement`, status `approved`

> Schema, Message, and Input Validation

*Rationale:* Schema, message, and input validation must be enforced in both MCP servers and clients.

**source_ref**: C10.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('10.4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0146 | system_requirement | approved | AISVS 10.4.1 |
| SR-0147 | system_requirement | approved | AISVS 10.4.2 |
| SR-0148 | system_requirement | approved | AISVS 10.4.3 |
| SR-0149 | system_requirement | approved | AISVS 10.4.4 |
| SR-0150 | system_requirement | approved | AISVS 10.4.5 |
| SR-0151 | system_requirement | approved | AISVS 10.4.6 |
| SR-0152 | system_requirement | approved | AISVS 10.4.7 |
| SR-0153 | system_requirement | approved | AISVS 10.4.8 |
<!-- tl:end -->

# C11 Adversarial Robustness — the root

<!-- tl:item INT-0011 -->
**INT-0011 — C11 — Adversarial Robustness** — `intent`, status `approved`

> This chapter addresses keeping AI systems reliable and abuse-resistant when facing evasion, inference, extraction, or poisoning attacks.

**source_ref**: C11
<!-- tl:end -->

## C11.1 Model Alignment, Safety, and Robustness Testing and Training

<!-- tl:item UR-0036 -->
**UR-0036 — C11.1 — Model Alignment, Safety, and Robustness Testing and Training** — `user_requirement`, status `approved`

> Model Alignment, Safety, and Robustness Testing and Training

*Rationale:* Model resilience to manipulated inputs designed to cause misclassification or policy bypass must be increased, primarily through adversarial testing and robustness benchmarking.

**source_ref**: C11.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('11.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0154 | system_requirement | approved | AISVS 11.1.1 |
| SR-0155 | system_requirement | approved | AISVS 11.1.2 |
| SR-0156 | system_requirement | approved | AISVS 11.1.3 |
| SR-0157 | system_requirement | approved | AISVS 11.1.4 |
| SR-0158 | system_requirement | approved | AISVS 11.1.5 |
<!-- tl:end -->

## C11.2 Membership-Inference and Model-Inversion Mitigation

<!-- tl:item UR-0037 -->
**UR-0037 — C11.2 — Membership-Inference and Model-Inversion Mitigation** — `user_requirement`, status `approved`

> Membership-Inference and Model-Inversion Mitigation

*Rationale:* The ability to determine whether a specific record was in the training data must be limited, and reconstruction of private training data or sensitive attributes from model outputs prevented.

**source_ref**: C11.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('11.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0159 | system_requirement | approved | AISVS 11.2.1 |
| SR-0160 | system_requirement | approved | AISVS 11.2.2 |
| SR-0161 | system_requirement | approved | AISVS 11.2.3 |
| SR-0162 | system_requirement | approved | AISVS 11.2.4 |
| SR-0163 | system_requirement | approved | AISVS 11.2.5 |
<!-- tl:end -->

## C11.3 Model-Extraction Defense

<!-- tl:item UR-0038 -->
**UR-0038 — C11.3 — Model-Extraction Defense** — `user_requirement`, status `approved`

> Model-Extraction Defense

*Rationale:* Unauthorized model cloning through API abuse must be detected and deterred using rate limiting, query-pattern analysis, and watermarking.

**source_ref**: C11.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('11.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0164 | system_requirement | approved | AISVS 11.3.1 |
| SR-0165 | system_requirement | approved | AISVS 11.3.2 |
| SR-0166 | system_requirement | approved | AISVS 11.3.3 |
| SR-0167 | system_requirement | approved | AISVS 11.3.4 |
<!-- tl:end -->

## C11.4 Model Runtime Anomaly Detection

<!-- tl:item UR-0039 -->
**UR-0039 — C11.4 — Model Runtime Anomaly Detection** — `user_requirement`, status `approved`

> Model Runtime Anomaly Detection

*Rationale:* Manipulated, backdoored, or adversarial data entering the model context at inference time via external sources must be identified and neutralized.

**source_ref**: C11.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('11.4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0168 | system_requirement | approved | AISVS 11.4.1 |
| SR-0169 | system_requirement | approved | AISVS 11.4.2 |
| SR-0170 | system_requirement | approved | AISVS 11.4.3 |
<!-- tl:end -->

# C12 Monitoring, Logging & Anomaly Detection — the root

<!-- tl:item INT-0012 -->
**INT-0012 — C12 — Monitoring, Logging & Anomaly Detection** — `intent`, status `approved`

> This chapter addresses real-time and forensic visibility into what the model and other AI components see, do, and return, so that AI-specific threats can be detected and triaged.

**source_ref**: C12
<!-- tl:end -->

## C12.1 Request & Response Logging

<!-- tl:item UR-0040 -->
**UR-0040 — C12.1 — Request & Response Logging** — `user_requirement`, status `approved`

> Request & Response Logging

*Rationale:* AI requests and responses must be logged to create an audit trail and support incident response.

**source_ref**: C12.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('12.1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0171 | system_requirement | approved | AISVS 12.1.1 |
| SR-0172 | system_requirement | approved | AISVS 12.1.2 |
| SR-0173 | system_requirement | approved | AISVS 12.1.3 |
| SR-0174 | system_requirement | approved | AISVS 12.1.4 |
<!-- tl:end -->

## C12.2 Detection and Alerting

<!-- tl:item UR-0041 -->
**UR-0041 — C12.2 — Detection and Alerting** — `user_requirement`, status `approved`

> Detection and Alerting

*Rationale:* AI-specific attack patterns (jailbreak, prompt injection, model extraction, multi-turn trajectory attacks, covert channels over LLM endpoints) must be detected, and security events enriched with AI-specific context so downstream detection and response systems can act on them.

**source_ref**: C12.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('12.2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0175 | system_requirement | approved | AISVS 12.2.1 |
| SR-0176 | system_requirement | approved | AISVS 12.2.2 |
| SR-0177 | system_requirement | approved | AISVS 12.2.3 |
| SR-0178 | system_requirement | approved | AISVS 12.2.4 |
| SR-0179 | system_requirement | approved | AISVS 12.2.5 |
| SR-0180 | system_requirement | approved | AISVS 12.2.6 |
<!-- tl:end -->

## C12.3 Model, Data, and Performance Drift Detection

<!-- tl:item UR-0042 -->
**UR-0042 — C12.3 — Model, Data, and Performance Drift Detection** — `user_requirement`, status `approved`

> Model, Data, and Performance Drift Detection

*Rationale:* Drift and degradation across model outputs, input distributions, and data schemas must be monitored to identify quality regressions and security-relevant behavioral shifts.

**source_ref**: C12.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('12.3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0181 | system_requirement | approved | AISVS 12.3.1 |
| SR-0182 | system_requirement | approved | AISVS 12.3.2 |
| SR-0183 | system_requirement | approved | AISVS 12.3.3 |
| SR-0184 | system_requirement | approved | AISVS 12.3.4 |
<!-- tl:end -->

## C12.4 Proactive Security Behavior Monitoring

<!-- tl:item UR-0043 -->
**UR-0043 — C12.4 — Proactive Security Behavior Monitoring** — `user_requirement`, status `approved`

> Proactive Security Behavior Monitoring

*Rationale:* Security threats arising from proactive (agent-initiated) behavior must be detected and prevented, including pre-execution validation, behavior pattern analysis, and audit trails for approval of security-critical actions.

**source_ref**: C12.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('12.4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0185 | system_requirement | approved | AISVS 12.4.1 |
| SR-0186 | system_requirement | approved | AISVS 12.4.2 |
| SR-0187 | system_requirement | approved | AISVS 12.4.3 |
<!-- tl:end -->

## C12.5 Training Data & Model Lifecycle Audit

<!-- tl:item UR-0044 -->
**UR-0044 — C12.5 — Training Data & Model Lifecycle Audit** — `user_requirement`, status `approved`

> Training Data & Model Lifecycle Audit

*Rationale:* The provenance and change history of training data, model artifacts, and knowledge sources must be auditable throughout the AI development lifecycle.

**source_ref**: C12.5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('12.5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0188 | system_requirement | approved | AISVS 12.5.1 |
| SR-0189 | system_requirement | approved | AISVS 12.5.2 |
| SR-0190 | system_requirement | approved | AISVS 12.5.3 |
| SR-0191 | system_requirement | approved | AISVS 12.5.4 |
<!-- tl:end -->

