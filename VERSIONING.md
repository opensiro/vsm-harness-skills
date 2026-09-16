# Methodology versioning

The OpenSiro VSM pipeline has two semantic release lines and one exact data-state identity:

```text
VSM Harness Profile version
        ↓
VSM Harness Methodology version
        ↓
vsm-harness-index @ Git revision
        ↓
TLDR.md / RANKINGS.md generated views
```

## Profile version

`vsm-harness-profile` owns the normative meaning of S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, escalation, organizational function, decision ownership, and closure.

A Profile version answers:

> What do the organizational concepts mean?

## Methodology version

This repository has one Methodology release line. Its version is stored in:

```text
skills/assess-vsm-harness/VERSION
```

The Methodology version covers the procedural contract used to turn evidence into corpus outputs:

- repository assessment and evidence requirements;
- local ownership notation and classification procedure (`A`, `A(P)`, `C`, `C(P)`, `P`, `—`, `?` in `0.3.x`);
- assessment artifact/provenance contract;
- ordered cohort-relative signature synthesis;
- deterministic ranking projection rules;
- validation rules that enforce those procedures.

Assessment, synthesis, and ranking do **not** receive independent semantic versions while they are released and consumed as one methodology. A change to any of those procedural semantics bumps the single Methodology version and is described in the changelog.

The Methodology version answers:

> How do we turn repository evidence into assessments and corpus views?

### Compatibility field names

Existing assessment front matter uses:

```yaml
generated_assessment_procedure_version: ...
assessment_procedure_version: ...
```

These names are retained as compatibility storage keys to avoid a corpus-wide schema migration. Their values identify the VSM Harness **Methodology version as applied to assessment generation or current assessment validation**. Renaming the keys is not required to simplify the release model.

`generated_assessment_procedure_version` is immutable origin metadata. A reassessment under a newer Methodology updates only the current `assessment_procedure_version` after the assessment has actually been revalidated; it does not rewrite the generation version.

## Methodology 0.3 ownership-mode boundary

Methodology `0.3.0` introduced composite parent-governed mode notation for S3, S4, and S5 while keeping Profile `0.2.1` semantics unchanged. Methodology `0.3.1` clarifies the intended publication boundary without changing that state set.

The composite symbols:

```text
A(P)
C(P)
```

mean that the base autonomous mode (`A` or `C`) is established and a distinct first-party parent-governed mode for the same function is also operationally closed. Standalone `P` remains available when a parent-governed mode is established but no first-party `A` or `C` autonomous mode is established at the reviewed boundary.

This is multi-mode capability notation, not simultaneous ownership. In any concrete deployment/run the decisive organizational right still has one reconstructable owner at a time.

The parent-mode publication boundary is intentionally asymmetric:

- S1 and S2 do not publish `P`, because the Methodology targets autonomous AI agent harnesses rather than every human-owned organizational topology that can exist in practice;
- S3 and S4 permit `P`/`A(P)`/`C(P)` as explicit supervisory/current-control and adaptation exceptions, including self-hosted and distributed OSS cases;
- S3* does not publish the parent modifier in the `0.3.x` line; audit remains classified through complementary access, independence, judgment ownership, and feedback;
- S5 is the canonical parent-governed case because identity / ultimate-policy authority may legitimately remain at a parent recursion while the return-to-operation loop is complete.

This is a Methodology publication decision, not a claim that human ownership of S1, S2, or S3* is impossible in broader organizations.

Because the `0.3.0` change can alter canonical assessment vectors without any upstream repository change, migration into the `0.3.x` ownership notation is a Methodology reassessment event, not a textual version bump. Existing assessments must not receive `(P)` by search-and-replace from human involvement, self-hosting, approval hooks, or maintainer activity. The relevant S3/S4/S5 function and each encoded ownership mode must be reconstructed from primary evidence.

Methodology `0.3.1` is patch-level clarification of that boundary. Correct `0.3.0` assessments do not require vector changes merely because the patch was released; an assessment advances its current Methodology provenance only after normal successful revalidation.

Downstream Index tooling must support `A(P)` and `C(P)` parsing, validation, rendering, and ranking projection before canonical assessments using those symbols are admitted.

## Index revision

`vsm-harness-index` does not need an independent semantic version for every corpus or schema change. An exact Git revision identifies the complete published state, including:

- catalog and admission state;
- canonical assessments and their provenance;
- reassessment history;
- cohort-relative signatures;
- validation/rendering implementation;
- generated `TLDR.md` and `RANKINGS.md`.

An Index revision answers:

> What exact corpus and generated result state are we looking at?

If the Index later exposes a separately consumed stable external schema/API, that interface may justify its own format version. Do not introduce one before such a compatibility boundary exists.

## Generated views

`TLDR.md` and `RANKINGS.md` are materialized views of one Index revision. They do not have independent semantic versions.

- `TLDR.md` combines canonical assessment vectors with cohort-relative signatures produced under the Methodology.
- `RANKINGS.md` is the deterministic ranking projection defined by the Methodology and implemented by the Index.

Under Methodology `0.3.x`, ranking still measures agent-owned mode coverage: `A(P)` has base `A`, `C(P)` has base `C`, and parent-mode presence remains descriptive rather than weighted.

A change to Profile semantics may require reassessment. A change to Methodology semantics may require reassessment, re-synthesis, re-ranking, or regeneration depending on the affected procedure. In every case the resulting exact state is captured by a new Index Git revision.

## Current contract

At this release boundary:

```text
Profile:     0.2.1
Methodology: 0.3.1
Index:       exact Git revision
```

The bundled Profile is synchronized to exact upstream revision `e1aaff7d2cd50d5d5ed9ab76c3606a6ef39d1976`.

The Profile and Methodology are versioned contracts. The Index commit is the immutable identity of a particular corpus/output state.

Frozen downstream work keeps its declared historical contract. In particular, Index Reassessment R1 remains on Profile `0.2.0` / Methodology `0.2.1`; releasing this active contract does not silently migrate that round or any existing canonical assessment.
