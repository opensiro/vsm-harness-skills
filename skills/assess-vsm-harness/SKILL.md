---
name: assess-vsm-harness
description: Produce a standalone evidence-backed VSM assessment of one autonomous AI agent harness at a pinned repository revision, including out-of-the-box autonomy states.
---

# Assess a Harness as a Viable System

Use the bundled [VSM Harness Profile](references/profile/PROFILE.md) as the sole definition of S1-S5, S3*, recursion, autonomy, variety, homeostasis, and algedonic signalling. The output is a standalone repository assessment, not a cross-catalog comparison.

Read [assessment-format.md](references/assessment-format.md) for the required artifact and [autonomy-states.md](references/autonomy-states.md) for local autonomy notation.

## Workflow

1. Pin the repository revision and declare system-in-focus, purpose, environment, standard-distribution boundary, recursion level, and review date.
2. Describe repository architecture before VSM mapping: runtime, agent loop, state, tools, delegation, persistence, scheduling, evaluation, human involvement, and external integration when material.
3. Identify operational outcomes and real S1 units.
4. For each VSM function, first establish the organizational function from behavior and relationships; only then identify the responsible actor and decision right.
5. Record supporting mechanisms separately from the actor that owns the decision right.
6. For every material mapping record primary evidence, basis (`explicit`, `structural`, `inferred`, or `unknown`), confidence, and caveat.
7. Assign the local autonomy state only after the function mapping is complete.
8. Record recursion, variety, escalation, and unresolved evidence gaps separately from the six-state vector.
9. Write `assessments/<harness_id>.md` for index work. Do not generate a cohort-relative signature in this skill.

## Hard distinctions

- Delegation, routing, sequencing, or handoff alone is not S2; require evidence of interference or oscillation regulation among operational units.
- A manager is not S3; require a whole-system current view plus authority over shared resources, commitments, priorities, or constraints.
- A routine verifier is not S3*; require complementary and sufficiently independent access to operational reality.
- Planning, learning, self-improvement, or event reaction alone is not S4; require an external-and-prospective adaptation loop whose options can affect current capability.
- A prompt, static policy, guardrail, or approval step alone is not S5; require runtime identity or ultimate-policy closure.
- Spawning or nesting is not VSM recursion.
- Missing evidence is `?`, not `—`.

A second reviewer must be able to reconstruct every positive autonomy state from cited primary evidence and the declared boundary.
