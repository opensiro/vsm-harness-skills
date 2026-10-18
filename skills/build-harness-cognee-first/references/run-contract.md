# New-run contract — Cognee-first harness construction

This is an **input/checklist for a new experiment**, not historical evidence. Fill it *before* Cognee search and publish it as part of C1. Do not copy the Flash API sample, source shortlist, architecture choice, or evaluation outcomes into a new experiment.

## 1. Task and baseline (C1)

| Field | Value to declare before architecture discovery |
| --- | --- |
| Experiment ID / new repository | Unique ID and intended public Git URL |
| Concrete task | Operational input, output, and task boundary |
| Success/failure oracle | How an external check determines whether the task succeeded |
| Baseline behavior | Minimal behavior and acceptance criteria, without selecting an adaptation |
| Safe execution | Allowed target files, tools, network destinations, and trust boundary |
| Runtime | OS / language / package and model client versions |
| Models / provider | Available backend(s), credentials source by env var **name only**, fallback if unavailable |
| Limits | Allowed model/tool calls, tokens, wall time, hardware, disk/memory, estimated cost |
| Evaluation plan | Dataset/fixture(s), split if relevant, task outcome and model-resource metrics, replication policy |
| No-model path | What deterministic or scripted tests can prove; what they cannot prove |

A missing optional live-model provider may reduce evaluation strength; it must not silently become a fake completed real-model run.

## 2. Corpus and Cognee scope (C1 → C2)

| Field | Minimum record |
| --- | --- |
| Index / Profile / Methodology pins | Immutable commit/release and evidence links; never auto-retrofit old pins |
| Connector pin | Immutable commit, version and disclosed compatibility patch |
| Canonical admission | Included vs excluded/proposed and how membership was verified |
| Selection | Prefer full included corpus if feasible; if sampled, deterministic rule, source-ID list/digest, resource reason and coverage bias |
| Native query plan | Query IDs, full strings, method, limits and negative control, frozen **before first search** |
| Ingested scope | Exact included Markdown source documents and digests |
| Searchable scope | Which chunks/fields were indexed, lexical vs semantic mode, and known omissions |
| Source-inspection scope | Which full assessments and pinned upstream code were *actually* read afterwards |
| Freshness / retry | New dataset identity; first attempt ID and failure policy; never silently reuse cached results |
| Native receipts | Full import, separate audit, query outputs, errors, irrelevant and zero results |

Note: the Flash API example ingested complete assessments but indexed **only six function-section chunks per assessment** for its native lexical queries. Full-body architectural search requires newly implemented and validated indexing. `TLDR.md` is not primary assessment evidence.

## 3. Causal checkpoints (C1 → C4)

| Commit reference | Contents |
| --- | --- |
| `C1_SHA` | Preflight, frozen query plan, source pins and task/baseline contract |
| `C2_SHA` | Actual Cognee import, independent audit, native query receipts and coverage |
| `COMPARISON_SHA` | Post-Cognee candidate shortlist, full assessment/upstream inspection, alternatives |
| `DECISION_SHA` | Separate source-backed decision that cites `COMPARISON_SHA` |
| `FIRST_ADAPTED_CODE_SHA` | First implementation of selected mechanism; must be after decision |
| `C4_SHA` | Runnable result, tests, evaluation receipts, hash manifest and limitations |

Review [Decision Trace contract](decision-trace.md) and verify all five chronological ancestry edges. Report missed/unreachable commits or preselected mechanisms as gate failures, not harmless clerical omissions. Do not use this checklist itself as proof of execution.

## 4. Final result contract (C4)

Always report:

- `process_status`: PASS / PARTIAL / FAIL, with evidence for C1–C4.
- `build_status`: PASS / PARTIAL / FAIL, including exact runnable commands. If the source comparison justifies **no adaptation**, describe that null decision and avoid fabricating a modified variant.
- `evaluation_level`: NOT_RUN / DETERMINISTIC_ONLY / SCRIPTED_PROTOCOL / REAL_MODEL_RUN, and all actual evidence types when multiple exist.
- `model_quality_claim`: NOT_EVALUATED by default; an improvement claim requires a relevant comparable real-model evaluation and appropriate uncertainty.
- Baseline/adapted **observed** task outcomes, model/tool calls and token use when available, elapsed time/resources and costs when available, errors/retries, negatives, and scope limits.
- Original receipts and file SHA256 manifest; correct prior records with new append-only events, never overwrite their history.

## 5. Required output paths

```text
README.md
reports/discovery.md
reports/candidate-comparison.md
reports/architecture-decision.md
reports/evaluation.md
traces/decision-trace.jsonl
receipts/
```

Files may be organized into subdirectories with explicit cross-links, but do not conflate an unchanged retrospective report with a newly executed run.

## 6. Stop conditions

Stop and publish a bounded partial report if native Cognee import, independent audit, or native retrieval fails; if essential upstream code/source pins cannot be verified; or if a mandatory chronology gate is broken. No grep/embeddings-only imitation, saved shortlist, task-specific source reuse, invented data, or architectural implementation can be offered as a surrogate for Cognee-first evidence.

This contract is **experimental**, outside the released `assess-vsm-harness` Methodology; it neither changes canonical assessment grades nor defines VSM function semantics.
