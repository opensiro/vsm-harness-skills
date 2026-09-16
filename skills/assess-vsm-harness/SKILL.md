---
name: assess-vsm-harness
description: Produce a standalone evidence-backed VSM assessment of one autonomous AI agent harness at a pinned repository revision, including out-of-the-box autonomy states.
---

# Assess a Harness as a Viable System

**Methodology version:** 0.2.2

Use the bundled [VSM Harness Profile](references/profile/PROFILE.md) as the sole definition of S1-S5, S3*, recursion, autonomy, variety, homeostasis, and algedonic signalling. The bundled Profile for this methodology is **v0.2.0**. The output is a standalone repository assessment, not a cross-catalog comparison.

Read [assessment-format.md](references/assessment-format.md) for the required artifact and [autonomy-states.md](references/autonomy-states.md) for local autonomy notation. The same Methodology release also governs cohort synthesis and deterministic ranking through the repository-level [SYNTHESIS.md](../../SYNTHESIS.md).

## Workflow

1. Pin the repository revision and declare system-in-focus, purpose, environment, standard-distribution boundary, recursion level, review date, Profile version, and Methodology version. On first creation, also record the immutable generation-origin pair: `generated_profile_version` and `generated_assessment_procedure_version`.
2. Describe repository architecture before VSM mapping: runtime, agent loop, state, tools, delegation, persistence, scheduling, evaluation, human involvement, and external integration when material.
3. Identify operational outcomes and real S1 units.
4. For each VSM function, first establish the organizational function from behavior and relationships. State the disturbance or variety being regulated.
5. Identify the **decisive decision right or feedback path** that closes the function.
6. Identify who owns that right: agent, deterministic runtime, developer/configuration, human, parent system, or an explicitly described distributed arrangement.
7. Record supporting/enforcement mechanisms separately. A scheduler, budget monitor, policy engine, queue, database, kill switch, interrupt, or deterministic controller does not inherit ownership merely because it executes the decision.
8. Record the closure path where the result must affect subsequent regulation or operation. For S5 parent closure, show the identity/policy issue reaching legitimate parent authority and the returned decision governing later operation.
9. When ownership is ambiguous, apply the Profile's counterfactual owner test: remove the candidate owner conceptually while leaving supporting machinery in place and ask whether materially the same discretionary organizational decision still occurs.
10. For every material mapping record primary evidence, basis (`explicit`, `structural`, `inferred`, or `unknown`), confidence, and caveat.
11. Assign the local autonomy state only after function, decisive right, ownership, support, and closure are separated.
12. Record recursion, variety, escalation, and unresolved evidence gaps separately from the six-state vector.
13. Write `assessments/<harness_id>.md` for index work. Do not generate a cohort-relative signature in this skill.

## Generation provenance

Every assessment newly created by Methodology v0.2.1 or later must preserve which semantic/tooling versions produced the original artifact:

```yaml
generated_profile_version: 0.2.0
generated_assessment_procedure_version: 0.2.2
```

These two fields are **immutable origin metadata**. Do not change them during reassessment, same-ref correction, or later Methodology upgrades.

The separate fields:

```yaml
profile_version: ...
assessment_procedure_version: ...
```

record the semantics under which the current canonical classification was most recently successfully produced or revalidated. They may therefore advance while the `generated_*` pair remains unchanged.

`assessment_procedure_version` and `generated_assessment_procedure_version` remain the compatibility storage-key names in the assessment schema. Their values identify the VSM Harness **Methodology version as applied to the assessment**; no separate assessment-only release line exists from v0.2.2 onward.

For legacy artifacts whose original generation versions were never recorded, do not guess or backfill them. Absence means generation provenance is unknown.

## Hard distinctions

- Delegation, routing, sequencing, or handoff alone is not S2; require evidence of interference or oscillation regulation among operational units.
- A manager is not S3; require a whole-system current view plus authority over shared resources, commitments, priorities, or constraints.
- **Runtime enforcement is not S3 ownership.** A hard budget, concurrency gate, scheduler, or kill mechanism may enforce an S3 decision while the decisive resource/commitment choice belongs to an agent, developer, human, or another actor.
- A routine verifier is not S3*; require complementary and sufficiently independent access to operational reality.
- Deterministic verdict parsing/gating does not automatically own S3* if the independent audit judgment is made elsewhere; record both separately.
- Planning, learning, self-improvement, or event reaction alone is not S4; require an external-and-prospective adaptation loop whose options can affect current capability.
- A prompt, static policy, guardrail, or approval step alone is not S5; require runtime identity or ultimate-policy closure.
- **Generic human approval is not `S5=P`.** Parent-governed S5 requires an identity/ultimate-policy issue, legitimate parent authority, and a return-to-operation path under the parent's decision.
- Spawning or nesting is not VSM recursion.
- Missing evidence is `?`, not `—`.

A second reviewer must be able to reconstruct every positive autonomy state from cited primary evidence, including the function, decisive right, owner, support/enforcement split, closure path where applicable, and declared boundary.
