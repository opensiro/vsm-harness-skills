# assess-vsm-harness changelog

## 0.2.2 — 2026-09-16

- define the existing `0.2.x` release line as the unified VSM Harness Methodology version;
- make assessment, cohort-relative synthesis, deterministic ranking projection, and validation part of one procedural release boundary;
- keep the existing `assessment_procedure_version` and `generated_assessment_procedure_version` field names as compatibility storage keys whose values identify the Methodology version when applied to assessment artifacts;
- explicitly avoid independent semantic versions for synthesis, ranking, TLDR, or RANKINGS while they are released as one methodology and materialized in a Git-versioned Index state;
- move the ranking projection rule into the Methodology contract without changing the current ranking output.

This is a release-boundary/provenance clarification. It does not change VSM Profile semantics or any `A/C/P/—/?` classification rule.

## 0.2.1 — 2026-09-16

- add immutable generation-origin provenance for newly created assessments;
- distinguish `generated_profile_version` / `generated_assessment_procedure_version` from the current accepted `profile_version` / `assessment_procedure_version`;
- require new v0.2.1+ artifacts to preserve their generation pair while allowing current semantic provenance to advance through reassessment;
- keep legacy origin unknown rather than fabricating historical generator versions.

This is a provenance/schema patch. It does not change VSM function semantics or autonomy-state classification rules.

## 0.2.0 — 2026-09-16

- align the procedure with VSM Harness Profile v0.2.0;
- separate organizational function, decisive decision/feedback right, owner, supporting enforcement, and closure;
- tighten `A` around agent ownership of the decisive organizational discretion;
- tighten `P` around complete parent-governed S5 return-to-operation closure;
- add the counterfactual owner test;
- add Profile/procedure provenance fields to the version-aware assessment format;
- resync the bundled Profile and record its immutable source revision.

The pre-0.2.0 procedure was not explicitly versioned. Do not fabricate a historical procedure version in existing assessments; record `0.2.0` when an assessment is first successfully reviewed under this procedure.
