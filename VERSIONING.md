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
- local `A/C/P/—/?` classification procedure;
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

A change to Profile semantics may require reassessment. A change to Methodology semantics may require reassessment, re-synthesis, re-ranking, or regeneration depending on the affected procedure. In every case the resulting exact state is captured by a new Index Git revision.

## Current contract

At this release boundary:

```text
Profile:     0.2.1
Methodology: 0.2.3
Index:       exact Git revision
```

The bundled Profile is synchronized to exact upstream revision `e1aaff7d2cd50d5d5ed9ab76c3606a6ef39d1976`.

The Profile and Methodology are versioned contracts. The Index commit is the immutable identity of a particular corpus/output state.

Frozen downstream work keeps its declared historical contract. In particular, Index Reassessment R1 remains on Profile `0.2.0` / Methodology `0.2.1`; releasing this active contract does not silently migrate that round.
