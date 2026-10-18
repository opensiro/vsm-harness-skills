---
name: build-harness-cognee-first
status: experimental
description: Build a new agent harness through verifiable Cognee-first architectural discovery, source inspection, engineering decisions, and traceable implementation; runtime benchmarking is optional.
---

# Cognee-first harness construction

**Skill version:** 0.1.0

**Status:** experimental draft v0.1.0; reusable build-time workflow, not a released VSM assessment specification.

## Purpose and scope

Use this skill for a *new harness construction* experiment, not for producing or changing a canonical VSM assessment. Choose and implement an architecture from actual build-time research: define a task, retrieve a pinned assessment corpus through Cognee, inspect upstream code, compare alternative mechanisms, record the architecture decision, and produce an inspectable new harness. **The experiment concerns the harness development cycle, not game-playing or model performance.** Cognee must not become an implicit runtime dependency.

This is an **experimental build-time skill in opensiro/vsm-harness-skills**. It is independently versioned and not a release of the canonical VSM assessment Methodology. It does not amend assess-vsm-harness, the VSM Profile, or the Index admission rules. Its historical [Flash API case](references/case-study.md) illustrates process and failure modes, not a recommended architectural outcome.

## Stage 0 — task and source preflight

1. Read the current public [Opensiro bootstrap](https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md) and follow its owning-repository routing.
2. Declare the harness construction task, acceptance criteria for the built artifact, allowed source/tools, available build-time resources, cost/time limits, and a minimal starting scaffold. Model execution and benchmark design are optional. Do not preselect an adapted mechanism or upstream winners.
3. Pin the Index Git commit, connector commit, assessment/Profile dependency versions, and available public sources. Verify canonical inclusion against the pinned Index. Record all pins and connector fixes. Preserve historical references; do not silently upgrade frozen sources.
4. Plan dataset selection by a stated, reproducible rule **before retrieval**; disclose exclusions and how the selection may miss relevant systems. **Prefer the entire included corpus when feasible.** Sampling is allowed only with recorded compute/storage limits and a deterministic selection policy. The historical 128-record sample is not a default or target.
5. Freeze a task-specific [run contract](references/run-contract.md): construction outcome criteria, starting scaffold, OS/runtime/dependencies, optional model/API configuration, resource budgets, Cognee coverage, planned source/static validation, permissions, and safe construction boundary. Never record credentials in receipts.
6. Publish **C1 — preflight checkpoint**: source pins, admission/sample policy, task/baseline contract and preregistered query plan at an immutable Git commit *before the first native query*. Record the exact commit SHA. If no shared remote can publish, preserve local Git ancestry and label the weaker evidence explicitly; do not claim independently verifiable public precommit.

## Gate 1 — execute real Cognee discovery

1. Before construction, prepare a **fresh, isolated** Cognee dataset, respecting the connector's fresh-only and failed-attempt restrictions.
2. Import the pinned included assessment records through an actual Cognee source ingestion. Record document identities, counts, hashes, index and connector pins, elapsed time, failures, and importer receipt.
3. Independently audit the resulting dataset's source identity, provenance, graph facts, and exact literal autonomy grades. A failed audit blocks Cognee-dependent claims.
4. Use only the previously frozen query plan from C1 for the first discovery pass; any later query expansion must be separately identified and timestamped. Run task-grounded native queries and at least one useful negative/control query using actual native Cognee search, recording search mode, indexed fields/chunks, all raw hits and ranks, irrelevant results, errors, and empty hits. Do not substitute grep, a cached answer, a mock graph, or a retrospective replay for a passing Cognee-first gate.
5. Explicitly distinguish:
   - **Ingested source:** which full assessment documents are stored.
   - **Indexed retrieval:** exactly which sections/text/fields the search can return.
   - **Later source inspection:** which complete assessments and upstream files are actually read.
   The first example ingested full Markdown but indexed only six S1–S5 function sections for lexical search. Its TLDR.md was not the search corpus. Never present section-only lexical retrieval as full-document search.
6. If a broader architectural search needs full-body indexing, implement and validate it as a **new** experiment/dataset. Do not claim it happened in the historical case. If native ingestion, audit, or search is blocked, stop Gate 1 and report partial work without inventing results.

**Gate 1 pass / C2 — discovery checkpoint:** original native import, independent audit PASS, the C1 query plan, actual native search results including negative and irrelevant hits, and explicit searchable-scope documentation have been saved and published with a Git commit SHA **before candidate comparison and mechanism selection**. A document being ingested does not imply its entire body was indexed. Preserve the failed original attempt if repair/retry is needed, and require a fresh isolated dataset for another attempt.

## Gate 2 — source-backed shortlist and design

1. Only after Gate 1, derive a shortlist from its actual hits. Consider additional public research/GitHub evidence explicitly as *outside-Index sources*, not fabricated indexed hits or VSM grades.
2. Read the **full canonical assessment** for each shortlisted system; then inspect the relevant upstream implementation at its actual pinned reviewed SHA. Record file/line links and evidence for the claimed mechanism. Relevance in one chunk is not implementation proof.
3. Compare implementation fit, complexity, architecture tradeoffs, licensing, failure modes, and source-evidence strength. Consider minimal/no-adaptation construction, alternatives, and rejected choices. Neither S4 presence nor A/C/P values are performance rankings; feedback inside one task is not automatically S4.
4. Publish a candidate comparison and alternatives at a pinned Git commit **before** choosing a mechanism. Include which Cognee result produced each candidate, the source files actually inspected, and an honest coverage gap for potentially missed candidates.
5. Record the architecture decision at a **subsequent distinct Git commit** referring to the comparison SHA, with selected/rejected options and source support. Select the smallest justified adaptation, or explicitly select none. Do not cherry-pick code or retroactively edit the comparison to imply prior selection.

**Gate 2 pass / C3 — decision checkpoint:** traceable retrieved hits → complete assessments and pinned GitHub inspection → published comparison → subsequent decision commit. The comparison commit must be an ancestor of the decision commit. The decision commit must precede implementation of the selected mechanism; check Git ancestry and record these SHAs. If the decision is no-adaptation, record the null outcome without fabricating an adapted-code commit. Existing case-study conclusions are not reusable as fresh findings.

## Stage 3 — construct the harness

- After C3 implement the chosen bounded mechanisms and record exactly which source-backed decisions shaped the new files. A minimal fixture/scaffold may precede Cognee discovery only when it does not preselect a preferred adaptation.
- Publish inspectable harness source, dependencies and entry points; link each adapted mechanism to its source, decision ID, and local implementation. Make licensing and excluded features explicit.
- Use source inspection, AST/static checks, dependency checks or ordinary unit tests **only if permitted**. Keep the meaning of each verification method separate from runtime functionality claims.
- **Do not require running the harness, a gameplay episode, a model API call, a baseline/adapted performance benchmark, a win rate, or model-quality improvement** to finish the development-cycle demonstration.
- If runtime execution is not authorized, preserve `NOT_RUN` and do not trigger it indirectly through CI. Never treat an unexecuted implementation as proven functionally working.

## C4 — constructed artifact and provenance checkpoint

Publish the resulting source (or an explicitly supported null/no-adaptation decision), dependencies/entry points, a source-to-code mapping, source/static validation if actually performed, remaining risks, and artifact hashes at a commit after C3. Verify ancestry.

The primary C4 evidence is **Cognee output → inspected upstream source → alternatives → recorded decision → produced harness code**. Runtime and model evaluations are optional follow-ups, **not a mandatory C4 gate**. Preserve historical receipts; never retrofit chronology. Git commits prove public artifact order rather than private intent or performance.

## Mandatory observable Decision Trace

Preserve at least: task definition; pinned source and coverage; precommitted dataset/query plan; import/audit; raw native query receipts; shortlisted and rejected candidates; full-source inspection; explicit architectural decision; produced implementation; verification if actually performed; and subsequent corrections.

Use an append-only event log with timestamps, source references, decision IDs, rejected options, related commits and artifact paths. Record what was *actually observed*; do not invent hidden reasoning or re-time earlier actions. See [Decision Trace contract](references/decision-trace.md).

## Completion states and evidence strength

The **primary measured object is the development process**, not the resulting harness's win rate or model performance. Report independently:

- `process_status`: PASS only when C1→C2→C3→C4 are evidenced chronologically; otherwise PARTIAL or FAIL with missing gates.
- `build_status`: PASS if the constructed source artifact and its design-source mapping are complete and inspectable; PARTIAL / FAIL if incomplete. A source-complete build is **not automatically runtime-verified**.
- `verification_level`: SOURCE_ONLY, STATIC_CHECKED, UNIT_TESTED, RUNTIME_SMOKE, or NOT_RUN; report only levels actually observed.
- `evaluation_level`: NOT_RUN is acceptable. Optional DETERMINISTIC_ONLY / SCRIPTED_PROTOCOL / REAL_MODEL_RUN may be documented separately.
- `model_quality_claim`: NOT_EVALUATED unless a separately authorized and appropriately matched real-model evaluation exists.

**A successful Cognee-first construction trace does not depend on running the constructed harness.** Strong gameplay results also cannot substitute for missing Cognee-first evidence.

## Deliverables and completion

- Declared construction task, constraints, source pins, dependencies, and an inspectable produced harness.
- Cognee connector import, independent audit and raw native search receipts with exact indexed-vs-ingested scope.
- Full assessments and pinned upstream code inspection, compared alternatives and a decision made before adapted code.
- A trace linking source → Cognee retrieval → comparison → decision → code; frozen C1/C2/C3/C4 Git anchors.
- Optional source/static/runtime checks labeled accurately; agent/model evaluation is **not required**.

**Full development-process success** requires both discovery/source-selection gates and produced implementation evidence, not a game or coding task success rate. A justified no-adaptation outcome is a legitimate explicit null result. Any unexecuted harness is `NOT_RUN` for runtime correctness; an incomplete Cognee gate remains a process failure even if the source code appears useful.
