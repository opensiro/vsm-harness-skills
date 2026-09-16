# Index synthesis

**Methodology version:** 0.3.0

This procedure operates on completed standalone harness assessments. It does not reassess repositories and must not change their recorded `A/C/P/—/?` states merely to make rows look different.

Synthesis and ranking are procedures within the same VSM Harness Methodology release as assessment. They do not have independent semantic versions. See [VERSIONING.md](VERSIONING.md).

## Ordered comparison

Process assessments in ascending `catalog_position`. For candidate `N`:

1. read its complete assessment;
2. compare it with assessments `1..N-1`;
3. preserve the six-state autonomy vector exactly;
4. identify the smallest evidence-backed architectural distinction that is informative relative to the earlier cohort;
5. write one compact signature sentence.

Two harnesses may legitimately have the same autonomy vector. Do not manufacture categorical differences. The textual signature may distinguish actor, decision right, coordination mechanism, feedback path, authority boundary, persistence model, audit path, adaptation loop, or parent-governed closure when those differences are already evidenced in the assessments.

## Signature rules

- A signature is cohort-relative and may change when an older harness is inserted into the catalog.
- A signature must be derivable from the standalone assessment and must not introduce new repository claims.
- Prefer organizational distinctions over product features or marketing language.
- Keep it short enough for a comparison table.
- Never alter an assessment to preserve signature uniqueness.
- Do not infer overall product quality, maturity, or VSM viability from a signature.

## Deterministic ranking projection

Ranking is a deterministic projection of canonical assessment states, not a qualitative score and not a second assessment layer.

For each included canonical assessment:

- `total A` is the count of `A` across S1, S2, S3, S3*, S4, and S5;
- `metasystem A` is the count of `A` across S2, S3, S3*, S4, and S5;
- counts of `C`, `P`, and `?` are descriptive only;
- the categorical six-state vector is preserved exactly.

Rank by `(metasystem A, total A)` in descending order. Harnesses with the same pair receive the same rank. `C`, `P`, and `?` are never converted to fractional weights or used as tie-breakers. Presentation order inside an equal rank may use non-semantic metadata such as repository creation date; that does not change the rank key.

Methodology v0.3.0 permits `P` for S3, S4, and S5. This does not alter the ranking key: `P` reports parent-governed ownership and is not treated as partial `A`.

This ranking measures recorded out-of-box agent ownership coverage only. It is not product quality, maturity, organizational viability, or an ordering of `— < C < P < A`.

## Generated views

`vsm-harness-index` owns the materialized `TLDR.md` and `RANKINGS.md` files and the implementation that renders them. Those files do not receive independent semantic versions. Their exact corpus/output identity is the Git revision of the Index repository that contains them.

A Methodology change may require re-synthesis or re-ranking without changing repository-relative assessments. An assessment or cohort change may also require regeneration without changing the Methodology version.
