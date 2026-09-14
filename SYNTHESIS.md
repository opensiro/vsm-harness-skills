# Index synthesis

This procedure operates on completed standalone harness assessments. It does not reassess repositories and must not change their recorded `A/C/P/—/?` states merely to make rows look different.

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

## Separation from ranking

Signature synthesis is qualitative comparison. Ranking is a separate deterministic projection of assessment states. Do not assign weights such as `A=1`, `C=0.5`, or `P=0.25` inside synthesis.

`vsm-harness-index` owns the final `TLDR.md` and `RANKINGS.md` rendering.
