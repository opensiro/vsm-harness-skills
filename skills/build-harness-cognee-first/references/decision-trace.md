# Observable Decision Trace contract (experimental)

This reference belongs to the build-harness-cognee-first skill, **not** to the canonical VSM assessment format.

## Minimal event envelope

Use newline-delimited JSON in traces/decision-trace.jsonl, written append-only. Event types may vary, but meaningful decisions and observations should contain:

- event ID, event type, observation/recording timestamp (UTC), and experiment/run identity;
- task/problem being addressed, current gate/stage, and status;
- relevant source identity and pinned Git SHA/assessment content digest;
- input artifact references (original pinned OpenSiro connector invocation/import receipts, independent audit, native Cognee query receipts, construction/verification) and output artifact references;
- candidate alternatives and externally inspectable reasons for selection/rejection **when an explicit design decision is made**, including the query/hit IDs or separately identified outside-Cognee discovery source and `discovery_contribution`;
- linked commit or file change and optional verification outcome as the workflow proceeds;
- explicit uncertainty, failures, and limitations.

Not every event needs every field: an import event records dataset facts; an architecture_decision event records considered options; an optional model-run event records backend and execution evidence, if a model was actually run.

## Required chronology

1. Problem, constraints, and precommitted source/query plan **published before first connector import/index build** (C1).
2. Actual pinned OpenSiro connector invocation/import → independent audit → native Cognee queries, including raw negative hits (C2).
3. Post-search candidates → full assessment reading → pinned upstream code comparison (C3 comparison).
4. Recorded decision, rejections, and Cognee discovery contribution → adapted implementation **or explicit NO_ADAPTATION** (C3 decision).
5. **Produced harness** even for NO_ADAPTATION → construction/source verification (if allowed) → later corrections and reviews (C4).

Keep previously published receipts immutable. For corrections append a new event pointing to the superseded record; never silently overwrite or fabricate the earlier state. If a trace starts after an action, label the entry as **retrospective record**, not contemporaneous evidence.

## Git-anchored checkpoints (C1–C4)

Use four immutable commit SHA anchors belonging to the **new experiment repository**, not the historical Flash API case:

| Checkpoint | Minimum published evidence | Must precede |
| --- | --- | --- |
| C1 / preflight | Task baseline and constraints, pinned source revisions, canonical admission and corpus policy, query plan | **First connector import/index build** (not just first query) |
| C2 / discovery | Pinned connector invocation/import receipt, independent audit receipts, raw native Cognee query results (including negatives), coverage limits | Candidate comparison |
| C3 / design | Pinned full-assessment/upstream inspection and published alternatives comparison, then a **separate** architecture-decision commit recording `discovery_contribution` | First selected-mechanism implementation (if any) |
| C4 / construction | **Produced harness source** (also for NO_ADAPTATION), source-to-code map/no-added-mechanism explanation, optional validation, limitations and hashes | Final completion report |

Track both `comparison_commit` and `decision_commit` inside C3. Publish C1 **before first source ingestion/index build**, and publish C2 before comparing mechanisms. Publish full baseline/fixture provenance and C1/C2 commits *before* claiming causal selection. Never use an uncommitted local file's modification time as a substitute for independently accessible Git order.

Confirm in Git (the implementation-specific ancestry checks are conditional on an actual adaptation):

```bash
git merge-base --is-ancestor "$C1_SHA" "$C2_SHA"
git merge-base --is-ancestor "$C2_SHA" "$COMPARISON_SHA"
git merge-base --is-ancestor "$COMPARISON_SHA" "$DECISION_SHA"
git merge-base --is-ancestor "$DECISION_SHA" "$C4_SHA"
# Conditional: only if a new mechanism was implemented; C4 harness still required for NO_ADAPTATION
git merge-base --is-ancestor "$DECISION_SHA" "$FIRST_IMPLEMENTATION_SHA"
git merge-base --is-ancestor "$FIRST_IMPLEMENTATION_SHA" "$C4_SHA"
```

These tests validate commit ancestry only, **not** truthfulness of source inspection, Cognee native results, or the timing of unpublished actions. Independently examine the artifacts in those commits. Fail closed if any reference is missing/unreachable or chronology contradicts claimed causal ordering. If no remote publishing was possible, label the evidence as locally anchored, not independently published.

## Discovery contribution classification (required)

The C3 architecture-decision event must include `discovery_contribution` and a compact rationale with query/hit IDs, independently encountered candidate URLs (when applicable) and the selected/rejected option IDs:

- `DIRECT` — an actual Cognee native query was the first recorded source of the selected mechanism and C3 cites that result. Supports the narrow claim **Cognee-driven discovery**; does not show performance superiority over other tools.
- `CORROBORATIVE` — the selected mechanism had already been found through an independently identified source, and Cognee later provided matching evidence. Supports only corroboration, not original discovery.
- `NONE` — no observed material contribution to the final architecture, including a NO_ADAPTATION result without a Cognee-driven rejection rationale. A complete process can still be PASS, but **not** a positive Cognee architecture-discovery result.
- `INDETERMINATE` — available chronology/receipts cannot establish the origin or influence; do not present it as DIRECT.

Do not classify a preselected choice as DIRECT merely because the same name later appeared among 48/128/... search hits. Treat post-hoc source review separately; no manual re-labeling of originally external candidates as Cognee-originated hits. An unsuccessful/absent connector gate cannot be repaired by a strong-looking DIRECT label.

## NO_ADAPTATION versus no built harness

A **NO_ADAPTATION** decision skips the optional `FIRST_IMPLEMENTATION_SHA` for added mechanisms but still requires a C4 source-complete minimal harness meeting the predeclared acceptance criteria. A research-only trace that stops before constructing any harness is a **PARTIAL or FAIL** process, not a completed C4; a baseline scaffold by itself is not automatically a completed deliverable.

## Three search coverage fields

Always report source_ingested_scope, lexical_or_semantic_index_scope, and inspected_source_scope separately.

Example (historical Flash API case, not a template for every implementation):

- source_ingested_scope: 128 complete pinned assessment Markdown files.
- lexical_or_semantic_index_scope: six VSM function sections per assessment (768 DocumentChunks), CHUNKS_LEXICAL only.
- inspected_source_scope: selected full assessments and upstream files at pinned reviewed SHA.

Do not equate imported raw documents to an automatically searchable full-document index.

## Verification

The auditor should be able to follow receipt references and Git history in both directions: source → evidence → alternative comparison → decision → code change → any actual verification. Gameplay or model-performance tests are not required for this chain. If a receipt or chronology gate is missing, mark it incomplete.
