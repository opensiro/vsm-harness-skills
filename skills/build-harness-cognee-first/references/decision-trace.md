# Observable Decision Trace contract (experimental)

This reference belongs to the build-harness-cognee-first skill, **not** to the canonical VSM assessment format.

## Minimal event envelope

Use newline-delimited JSON in traces/decision-trace.jsonl, written append-only. Event types may vary, but meaningful decisions and observations should contain:

- event ID, event type, observation/recording timestamp (UTC), and experiment/run identity;
- task/problem being addressed, current gate/stage, and status;
- relevant source identity and pinned Git SHA/assessment content digest;
- input artifact references (native import/query/evaluation receipts) and output artifact references;
- candidate alternatives and externally inspectable reasons for selection/rejection **when an explicit design decision is made**;
- linked commit or file change and evaluation outcome as the workflow proceeds;
- explicit uncertainty, failures, and limitations.

Not every event needs every field: an import event records dataset facts; an architecture_decision event records considered options; a model-run event records backend and execution evidence.

## Required chronology

1. Problem, constraints, and precommitted source/query plan.
2. Actual Cognee import → independent audit → native queries, including raw negative hits.
3. Post-search candidates → full assessment reading → pinned upstream code comparison.
4. Recorded decision and rejections → adapted implementation.
5. Reproducible baseline/adapted test receipts → late corrections and reviews.

Keep previously published receipts immutable. For corrections append a new event pointing to the superseded record; never silently overwrite or fabricate the earlier state. If a trace starts after an action, label the entry as **retrospective record**, not contemporaneous evidence.

## Git-anchored checkpoints (C1–C4)

Use four immutable commit SHA anchors belonging to the **new experiment repository**, not the historical Flash API case:

| Checkpoint | Minimum published evidence | Must precede |
| --- | --- | --- |
| C1 / preflight | Task baseline and constraints, pinned source revisions, canonical admission and corpus policy, query plan | First native Cognee query |
| C2 / discovery | Import and independent audit receipts, raw native query results (including negatives), coverage limits | Candidate comparison |
| C3 / design | Pinned full-assessment/upstream inspection and published alternatives comparison, then a **separate** architecture-decision commit | First adaptation implementation |
| C4 / build & evaluation | Baseline/adapted (or explicitly no-adaptation) source, tests, evaluation receipts, final limitations and hashes | Final completion report |

Track both `comparison_commit` and `decision_commit` inside C3. Publish the full baseline/fixture provenance and C1/C2 commits *before* claiming causal selection. Never use an uncommitted local file's modification time as a substitute for independently accessible Git order.

Confirm in Git:

```bash
git merge-base --is-ancestor "$C1_SHA" "$C2_SHA"
git merge-base --is-ancestor "$C2_SHA" "$COMPARISON_SHA"
git merge-base --is-ancestor "$COMPARISON_SHA" "$DECISION_SHA"
git merge-base --is-ancestor "$DECISION_SHA" "$FIRST_ADAPTED_CODE_SHA"
git merge-base --is-ancestor "$FIRST_ADAPTED_CODE_SHA" "$C4_SHA"
```

These tests validate commit ancestry only, **not** truthfulness of source inspection, Cognee native results, or the timing of unpublished actions. Independently examine the artifacts in those commits. Fail closed if any reference is missing/unreachable or chronology contradicts claimed causal ordering. If no remote publishing was possible, label the evidence as locally anchored, not independently published.

## Three search coverage fields

Always report source_ingested_scope, lexical_or_semantic_index_scope, and inspected_source_scope separately.

Example (historical Flash API case, not a template for every implementation):

- source_ingested_scope: 128 complete pinned assessment Markdown files.
- lexical_or_semantic_index_scope: six VSM function sections per assessment (768 DocumentChunks), CHUNKS_LEXICAL only.
- inspected_source_scope: selected full assessments and upstream files at pinned reviewed SHA.

Do not equate imported raw documents to an automatically searchable full-document index.

## Verification

The auditor should be able to follow receipt references and Git history in both directions: source → evidence → alternative comparison → decision → code change → test outcome. If a receipt or chronology gate is missing, mark it incomplete.
