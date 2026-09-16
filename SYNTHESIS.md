# Index synthesis

**Methodology version:** 0.3.0

This procedure operates on completed standalone harness assessments. It does not reassess repositories and must not change their recorded `A/A(P)/C/C(P)/P/—/?` states merely to make rows look different.

Synthesis and ranking are procedures within the same VSM Harness Methodology release as assessment. They do not have independent semantic versions. See [VERSIONING.md](VERSIONING.md).

## Ordered comparison

Process assessments in ascending `catalog_position`. For candidate `N`:

1. read its complete assessment;
2. compare it with assessments `1..N-1`;
3. preserve the six-state ownership vector exactly;
4. identify the smallest evidence-backed architectural distinction that is informative relative to the earlier cohort;
5. write one compact signature sentence.

Two harnesses may legitimately have the same vector. Do not manufacture categorical differences. The textual signature may distinguish actor, decision right, coordination mechanism, feedback path, authority boundary, persistence model, audit path, adaptation loop, or supported parent-governed mode when those differences are already evidenced in the assessments.

## Signature rules

- A signature is cohort-relative and may change when an older harness is inserted into the catalog.
- A signature must be derivable from the standalone assessment and must not introduce new repository claims.
- Prefer organizational distinctions over product features or marketing language.
- Keep it short enough for a comparison table.
- Never alter an assessment to preserve signature uniqueness.
- Do not infer overall product quality, maturity, or VSM viability from a signature.

## Deterministic ranking projection

Ranking is a deterministic projection of canonical assessment states, not a qualitative score and not a second assessment layer.

For ranking only, parse each state into an autonomous base plus an optional parent-mode flag:

```text
A      → base A, parent no
A(P)   → base A, parent yes
C      → base C, parent no
C(P)   → base C, parent yes
P      → no A/C base, parent yes
—      → no material first-party path
?      → insufficient evidence
```

For each included canonical assessment:

- `total A` is the count of functions whose base state is `A`, so both `A` and `A(P)` count as agent-owned coverage;
- `metasystem A` is the same count across S2, S3, S3*, S4, and S5;
- `C` count includes both `C` and `C(P)`;
- `P` count reports the number of functions with a qualifying parent-governed mode, so `A(P)`, `C(P)`, and standalone `P` all contribute to that descriptive count;
- `?` count is unchanged;
- the categorical six-state vector is preserved exactly.

Rank by `(metasystem A, total A)` in descending order. Harnesses with the same pair receive the same rank. `C`, parent-mode presence, and `?` are never converted to fractional weights or used as tie-breakers. Presentation order inside an equal rank may use non-semantic metadata such as repository creation date; that does not change the rank key.

This preserves the meaning of the ranking: it measures first-party agent-owned mode coverage, not product quality, maturity, organizational viability, or an ordering of `— < C < P < A`. `A(P)` is not ranked above `A`, and `C(P)` is not ranked above `C`; the modifier records another supported ownership configuration.

## Generated views

`vsm-harness-index` owns the materialized `TLDR.md` and `RANKINGS.md` files and the implementation that renders them. Those files do not receive independent semantic versions. Their exact corpus/output identity is the Git revision of the Index repository that contains them.

A Methodology change may require reassessment, re-synthesis, re-ranking, or regeneration depending on which procedure changed. Methodology v0.3.0 specifically requires the Index parser/validator/ranking projection to understand `A(P)` and `C(P)` before canonical assessments using those symbols are admitted.
