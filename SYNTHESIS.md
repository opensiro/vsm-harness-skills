# Index synthesis

**Methodology version:** 0.2.3

This procedure operates on completed standalone harness assessments. It does not reassess repositories and must not change their recorded `A/C/P/—/?` states merely to make rows look different.

Synthesis and ranking are procedures within the same VSM Harness Methodology release as assessment. They do not have independent semantic versions. See [VERSIONING.md](VERSIONING.md).

## Ordered comparison

Process assessments in ascending `catalog_position`. For candidate `N`:

1. read its complete assessment;
2. compare it with assessments `1..N-1`;
3. preserve the six-state autonomy vector exactly;
4. identify the smallest evidence-backed architectural distinction that is informative relative to the earlier cohort;
5. write one compact signature sentence.

Two harnesses may legitimately have the same autonomy vector. Do not manufacture categorical differences. The textual signature may distinguish actor, decision right, coordination mechanism, feedback path, authority boundary, persistence model, audit path, or adaptation loop when those differences are already evidenced in the assessments.

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

Order ranking rows by:

1. descending `total A`;
2. descending `metasystem A`;
3. ascending canonical `catalog_position` as the deterministic tie-break.

Do not assign numeric weights to `C`, `P`, `—`, or `?`. In particular, do not treat the state space as `— < C < P < A`: `C` and `P` describe different ownership arrangements, while `?` is an evidence state.

A ranking change may therefore result from a canonical assessment change or a catalog-order tie-break change; it is not an independent semantic judgment.
