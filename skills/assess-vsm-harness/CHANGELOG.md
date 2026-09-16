# assess-vsm-harness changelog

## 0.3.0 — 2026-09-16

- keep VSM Harness Profile `0.2.1` as the normative semantic dependency; this release does not redefine S1–S5, S3*, recursion, autonomy, or variety;
- extend the Methodology publication notation for S3, S4, and S5 from mutually exclusive `A/C/P/—/?` states to support composite first-party ownership modes `A(P)` and `C(P)`;
- define `A(P)` as an established autonomous `A` mode plus a distinct operationally closed parent-governed mode for the same function;
- define `C(P)` as an established constructor `C` mode plus a distinct operationally closed parent-governed mode for the same function;
- retain standalone `P` for S3/S4/S5 when a parent-governed mode is operationally closed but no first-party `A` or `C` autonomous mode is established at the reviewed boundary;
- require each encoded ownership mode to be independently reconstructable from primary evidence; composite notation never means simultaneous dual ownership of one decisive right in one concrete deployment/run;
- make self-hosted/operator modes and distributed OSS parent arrangements explicit assessment evidence surfaces without inferring organization-level parent governance from generic human involvement;
- explicitly allow non-human organizations to remain plain `A` for S3/S4/S5 when those functions close autonomously and no qualifying parent-governed mode is established;
- preserve the ranking key on agent-owned coverage by treating `A(P)` as base `A` and `C(P)` as base `C`; parent-mode presence remains descriptive and unweighted;
- require downstream Index tooling to understand the composite notation before assessments using it are admitted.

This is a substantive Methodology classification change. Existing canonical assessments do not automatically acquire `(P)` from historical mentions of humans, maintainers, approvals, or self-hosting. Reassessment must first re-establish the relevant S3/S4/S5 function and then independently establish the parent-governed closure at the declared recursion. Existing generation-origin metadata remains immutable; successfully migrated assessments advance only their current `assessment_procedure_version` to `0.3.0`.

## 0.2.3 — 2026-09-16

- sync the bundled normative dependency to VSM Harness Profile `0.2.1` at exact source revision `e1aaff7d2cd50d5d5ed9ab76c3606a6ef39d1976`;
- make the existing S2 evidence threshold mechanically reconstructable in the assessment workflow and artifact format;
- require positive S2 mappings to identify distinct S1 units, a specific actual or structurally evidenced inter-S1 disturbance, the coordination relation that attenuates it, and feedback into later S1 behaviour;
- clarify that `S2=C` requires an already-established S2 function plus a first-party S2-specific decision/feedback path; generic communication, routing, shared state, sequencing, or extension points remain insufficient;
- keep ownership separate from function evidence so deterministic coordination support does not become agent-owned `A` by enforcement alone.

This is a procedural clarification aligned with Profile `0.2.1`. It does not redefine the `A/C/P/—/?` states. Existing canonical assessments that violate the already-frozen Profile `0.2.0` / Methodology `0.2.1` S2 rule may be corrected as same-ref corrections rather than treated as migrations caused by this release.

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
