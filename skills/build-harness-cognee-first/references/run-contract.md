# New-run contract — Cognee-first harness construction

This is an **input/checklist for a new experiment**, not historical evidence. Fill it and publish C1 **before the first Cognee connector import, dataset index build, or discovery query**. Commit the predeclared source selection and query plan before access to import outcomes. Do not copy the Flash API sample, source shortlist, architecture choice, or evaluation outcomes into a new experiment.

## 1. Task and baseline (C1)

| Field | Value to declare before architecture discovery |
| --- | --- |
| Experiment ID / new repository | Unique ID and intended public Git URL |
| Concrete task | Operational input, output, and task boundary |
| Construction acceptance | What source/interfaces constitute the required harness artifact, including a minimal **NO_ADAPTATION** result |
| Baseline / scaffold | Minimal initial design without a selected adaptation |
| Safe execution | Allowed target files, tools, network destinations, and trust boundary |
| Runtime | OS / language / package and model client versions |
| Models / provider (optional) | Only if separately needed; credentials referenced by env var **name only** |
| Limits | Allowed model/tool calls, tokens, wall time, hardware, disk/memory, estimated cost |
| Verification plan | Source/static validation; runtime or gameplay evaluations only if expressly authorized |
| No-execution path | Source/provenance verification and its limits, without model or game execution |

Model or gameplay execution is not required for development-process completion. Never claim it ran when it did not.

## 2. Corpus and Cognee scope (C1 → C2)

| Field | Minimum record |
| --- | --- |
| Index / Profile / Methodology pins | Immutable commit/release and evidence links; never auto-retrofit old pins |
| Connector pin | Exact OpenSiro Cognee connector repository, immutable SHA/version, entry point/API invoked, declared configuration and hashed compatibility patch |
| Canonical admission | Included vs excluded/proposed and how membership was verified |
| Selection | Prefer full included corpus if feasible; if sampled, deterministic rule, source-ID list/digest, resource reason and coverage bias |
| Native query plan | Query IDs, full strings, method, limits and negative control, frozen **before first search** |
| Ingested scope | Exact included Markdown source documents and digests |
| Searchable scope | Which chunks/fields were indexed, lexical vs semantic mode, and known omissions |
| Source-inspection scope | Which full assessments and pinned upstream code were *actually* read afterwards |
| Freshness / retry | New dataset identity; first attempt ID and failure policy; never silently reuse cached results |
| Connector vs native receipts | Distinct original connector invocation/import receipt and native Cognee search/query receipt, independent audit, errors, irrelevant and zero results; direct-SDK-only import is not a connector-first PASS |

Note: the Flash API example ingested complete assessments but indexed **only six function-section chunks per assessment** for its native lexical queries. Full-body architectural search requires newly implemented and validated indexing. `TLDR.md` is not primary assessment evidence.

## 3. Causal checkpoints (C1 → C4)

| Commit reference | Contents |
| --- | --- |
| `C1_SHA` | Published preflight, frozen query plan, source pins and task/baseline contract **before first connector import/index build** |
| `C2_SHA` | Actual OpenSiro connector import receipt, independent audit, native Cognee query receipts and coverage |
| `COMPARISON_SHA` | Post-Cognee candidate shortlist, full assessment/upstream inspection, alternatives |
| `DECISION_SHA` | Separate source-backed decision that cites `COMPARISON_SHA` and declares `discovery_contribution` with query/hit/decision evidence |
| `FIRST_IMPLEMENTATION_SHA` (conditional) | First implementation commit for a selected **new mechanism**; omit for a documented NO_ADAPTATION decision only, **not** as permission to omit the final minimal harness |
| `C4_SHA` | Built harness code even if NO_ADAPTATION, source-to-code mapping or justified no-added-mechanism record, verification receipts if any, hash manifest and limitations |

Review [Decision Trace contract](decision-trace.md) and verify the required C1→C2→comparison→decision→C4 ancestry. If an adaptation was chosen, verify its first implementation commit also follows the decision and precedes C4. Report missed/unreachable commits or preselected mechanisms as gate failures, not harmless clerical omissions. Do not use this checklist itself as proof of execution.

## 4. Final result contract (C4)

Report `process_status` (PASS/PARTIAL/FAIL) for C1–C4 and `build_status` (PASS/PARTIAL/FAIL) for the produced inspectable **harness** source. State separately `verification_level` (SOURCE_ONLY/STATIC_CHECKED/UNIT_TESTED/RUNTIME_SMOKE/NOT_RUN). Declare `adaptation_outcome` (ADAPTED/NO_ADAPTATION/NOT_DECIDED) and `discovery_contribution` (DIRECT/CORROBORATIVE/NONE/INDETERMINATE) with source-retrieval and decision IDs. A NO_ADAPTATION choice may still pass C4 if the declared minimal harness was constructed; **no constructed harness** means C4 incomplete and process_status cannot be PASS.

`evaluation_level=NOT_RUN` and `model_quality_claim=NOT_EVALUATED` are **acceptable final states**: no gameplay, model-backed execution, or baseline-versus-adapted benchmark is mandatory. If such checks are separately executed, retain their original receipts and distinguish measured outcomes from architecture-source evidence.

The principal output is an auditable map from **pinned OpenSiro connector import → native Cognee retrieval → full assessment/upstream inspection → alternatives → decision → constructed harness**. **DIRECT** requires Cognee first surfacing a chosen mechanism and a cited native hit; **CORROBORATIVE** means an independently found choice was subsequently confirmed by Cognee; **NONE** means no demonstrated design influence; **INDETERMINATE** means origin cannot be established. Only DIRECT justifies a Cognee-*driven discovery* claim. `process_status=PASS` with NONE/INDETERMINATE can indicate a complete, honestly reported development process, not a positive Cognee discovery outcome. Do not claim runtime correctness solely from source construction or infer Cognee-caused task-performance improvement.

## 5. Required output paths

```text
README.md
reports/discovery.md
reports/candidate-comparison.md
reports/architecture-decision.md
reports/construction-verification.md
traces/decision-trace.jsonl
receipts/
```

Files may be organized into subdirectories with explicit cross-links, but do not conflate an unchanged retrospective report with a newly executed run.

## 6. Stop conditions

Stop and publish a bounded partial report if the pinned OpenSiro connector import, independent audit, or native Cognee retrieval fails; if essential upstream code/source pins cannot be verified; or if a mandatory chronology gate is broken. No grep/embeddings-only imitation, saved shortlist, task-specific source reuse, invented data, or architectural implementation can be offered as a surrogate for Cognee-first evidence.

This contract is **experimental**, outside the released `assess-vsm-harness` Methodology; it neither changes canonical assessment grades nor defines VSM function semantics.
