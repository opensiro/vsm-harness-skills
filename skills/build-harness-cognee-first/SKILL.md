---
name: build-harness-cognee-first
status: experimental
description: Research and build a new AI agent harness by using real Cognee search over pinned Opensiro VSM assessments before selecting an architecture, with source inspection, decision trace, and reproducible evaluation.
---

# Cognee-first harness construction

**Skill version:** 0.1.0

**Status:** experimental draft v0.1.0; reusable build-time workflow, not a released VSM assessment specification.

## Purpose and scope

Use this skill for a *new harness construction* experiment, not for producing or changing a canonical VSM assessment. Choose and implement an architecture from actual build-time research: a defined task, a pinned assessment corpus imported into Cognee, native retrieval, source-backed comparisons, an explicit design decision, then a baseline/adapted evaluation. Cognee must not become an implicit runtime dependency.

This is an **experimental build-time skill in opensiro/vsm-harness-skills**. It is independently versioned and not a release of the canonical VSM assessment Methodology. It does not amend assess-vsm-harness, the VSM Profile, or the Index admission rules. Its historical [Flash API case](references/case-study.md) illustrates process and failure modes, not a recommended architectural outcome.

## Stage 0 — task and source preflight

1. Read the current public [Opensiro bootstrap](https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md) and follow its owning-repository routing.
2. Declare the target task, success/failure criteria, safe execution boundary, model/backend availability, call and cost budgets, evaluation design, and a deliberately minimal baseline *contract*. Do not preselect an adapted mechanism or upstream winners.
3. Pin the Index Git commit, connector commit, assessment/Profile dependency versions, and available public sources. Verify canonical inclusion against the pinned Index. Record all pins and connector fixes. Preserve historical references; do not silently upgrade frozen sources.
4. Plan dataset selection by a stated, reproducible rule **before retrieval**; disclose exclusions and how the selection may miss relevant systems. **Prefer the entire included corpus when feasible.** Sampling is allowed only with recorded compute/storage limits and a deterministic selection policy. The historical 128-record sample is not a default or target.
5. Freeze a task-specific [run contract](references/run-contract.md): task outcome and failure oracle, baseline behavior, OS/runtime and dependency versions, model/API availability, compute/time/token/cost/tool-call limits, Cognee search coverage, intended evaluation backend, permissions, and safe execution boundary. Never record credentials in receipts.
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
3. Compare task fit, complexity, expected benefit, licensing, failure modes, and available evaluation evidence. Include a no-adaptation baseline, plausible alternatives, and rejected choices. Neither S4 presence nor A/C/P values are performance rankings; feedback inside one task is not automatically S4.
4. Publish a candidate comparison and alternatives at a pinned Git commit **before** choosing a mechanism. Include which Cognee result produced each candidate, the source files actually inspected, and an honest coverage gap for potentially missed candidates.
5. Record the architecture decision at a **subsequent distinct Git commit** referring to the comparison SHA, with selected/rejected options and source support. Select the smallest justified adaptation, or explicitly select none. Do not cherry-pick code or retroactively edit the comparison to imply prior selection.

**Gate 2 pass / C3 — decision checkpoint:** traceable retrieved hits → complete assessments and pinned GitHub inspection → published comparison → subsequent decision commit. The comparison commit must be an ancestor of the decision commit. The decision commit must precede the first adapted-implementation commit; check Git ancestry and record these SHAs. Existing case-study conclusions are not reusable as fresh findings.

## Stage 3 — implementation and measurement

- Build the smallest executable baseline and add only the selected adaptation. A task fixture or baseline scaffold may be prepared before Gate 1, but no adaptation or architecture-choice code before Gates 1 and 2.
- Keep model, initial task, tool surface, resource budgets, and conditions comparable. Log where enforced tests/additional tool calls legitimately make actual usage differ.
- Evaluate with real tests and preserved action/observation receipts. Distinguish offline deterministic checks, scripted doubles, and actual model-backed runs. No fake model/benchmark performance, no statistical claims from a single fixture.
- Preserve implementation and evaluation revisions, failure cases, source permissions/licensing, and exact commands. Do not alter third-party upstream repositories without separate authorization.

## C4 — implementation and evaluation checkpoint

Publish runnable baseline/adapted source, exact evaluation commands, task outcomes, errors/retries, actual model and tool calls, **token and cost measurements when available (else NOT AVAILABLE)**, runtime/resource limits, native action receipts, checksum manifest, and independently inspectable results. Freeze an evaluation commit **after C3**; verify ancestry. Keep negative/null/incomplete outcomes. Revisions append new receipts instead of changing historical ones.

Git anchors prove the sequence of **published artifacts**, not private thoughts or unobserved intent. If a pre-decision mechanism was implemented despite the stated gate, report the violation and mark the independent Cognee-first claim failed instead of retrofitting timestamps.

## Mandatory observable Decision Trace

Preserve at least: task definition; pinned source and coverage; precommitted dataset/query plan; import/audit; raw native query receipts; shortlisted and rejected candidates; full-source inspection; explicit architectural decision; implementation; baseline/adapted evaluation; and subsequent corrections.

Use an append-only event log with timestamps, source references, decision IDs, rejected options, related commits and artifact paths. Record what was *actually observed*; do not invent hidden reasoning or re-time earlier actions. See [Decision Trace contract](references/decision-trace.md).

## Completion states and evidence strength

Record these orthogonal fields in the final report:

- `process_status`: `PASS` only if C1→C2→C3→C4 are evidenced in order; otherwise `PARTIAL` or `FAIL` with the specific missing/violated gate.
- `build_status`: `PASS` for a working baseline, implemented selected adaptation and observed tests; `PARTIAL` for incomplete construction; `FAIL` for unusable build.
- `evaluation_level`: `DETERMINISTIC_ONLY`, `SCRIPTED_PROTOCOL`, `REAL_MODEL_RUN`, or `NOT_RUN`; list all levels executed when multiple apply.
- `model_quality_claim`: `NOT_EVALUATED` unless a reproducible, relevant real-model evaluation was actually executed. If executed, report observed results and uncertainty; a single model run is not automatically evidence of improvement.

The overall skill can succeed as a **build-process/protocol demonstration** with `SCRIPTED_PROTOCOL` evidence; it must not be described as **model-quality improvement** without appropriately matched real-model evidence. Missing/failed mandatory Cognee steps cannot be compensated by strong later harness tests.

## Deliverables and completion

- A task README with reproducible commands and environmental limits; the [run contract](references/run-contract.md) records declared inputs and execution prerequisites.
- Discovery and retrieval-coverage report, source manifest, native import/search results, and audit receipt.
- Source-backed candidate comparison and architecture decision with distinct C1/C2/C3/C4 Git commit anchors.
- Append-only Decision Trace, links to relevant implementation commits, and baseline/adapted evaluation receipts.
- Explicit process/build/evaluation-level/model-quality statuses; a real-model run is NOT RUN until its own receipt exists.

**Full build-process success** requires passing Cognee and source-selection gates, a runnable baseline, implementation and exercise of the chosen adaptation **when one was actually selected**, and a recorded evaluation with honest claims. A source-grounded no-adaptation decision can complete as a transparent null finding; do not invent a modified variant or call it evidence of uplift. If a gate fails, publish a bounded partial report instead of calling the entire workflow successful.
