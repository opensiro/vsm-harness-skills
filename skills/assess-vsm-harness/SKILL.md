---
name: assess-vsm-harness
description: Produce a standalone evidence-backed VSM assessment of one autonomous AI agent harness at a pinned repository revision, including first-party ownership modes.
---

# Assess a Harness as a Viable System

**Methodology version:** 0.3.0

Use the bundled [VSM Harness Profile](references/profile/PROFILE.md) as the sole definition of S1-S5, S3*, recursion, autonomy, variety, homeostasis, and algedonic signalling. The bundled Profile for this methodology is **v0.2.1**. The output is a standalone repository assessment, not a cross-catalog comparison.

Read [assessment-format.md](references/assessment-format.md) for the required artifact and [autonomy-states.md](references/autonomy-states.md) for local ownership notation. The same Methodology release also governs cohort synthesis and deterministic ranking through the repository-level [SYNTHESIS.md](../../SYNTHESIS.md).

## Workflow

1. Pin the repository revision and declare system-in-focus, purpose, environment, standard-distribution boundary, first-party operating/deployment modes considered, recursion level, review date, Profile version, and Methodology version. On first creation, also record the immutable generation-origin pair: `generated_profile_version` and `generated_assessment_procedure_version`.
2. Describe repository architecture before VSM mapping: runtime, agent loop, state, tools, delegation, persistence, scheduling, evaluation, human involvement, maintainer/contributor governance, self-hosted/operator modes, and external integration when material.
3. Identify operational outcomes and real S1 units.
4. For each VSM function, first establish the organizational function from behavior and relationships. State the disturbance or variety being regulated.
5. For S2 specifically, identify the distinct S1 units, the specific actual or structurally evidenced inter-S1 interference/conflict/oscillation, the coordination relation that attenuates it, and the feedback/closure path into subsequent S1 behaviour. Generic messaging, shared state, sequencing, routing, or speaker selection is not enough by itself.
6. Identify the **decisive decision right or feedback path** that closes the function.
7. Identify who owns that right in every first-party mode being claimed: agent, deterministic runtime, developer/configuration, human, parent system, or an explicitly described distributed arrangement.
8. Record supporting/enforcement mechanisms separately. A scheduler, budget monitor, policy engine, queue, database, kill switch, interrupt, or deterministic controller does not inherit ownership merely because it executes the decision.
9. Record the closure path where the result must affect subsequent regulation or operation. For parent-governed S3/S4/S5 modes, show the relevant matter reaching legitimate parent authority and the returned decision/feedback changing subsequent operation.
10. When ownership is ambiguous, apply the Profile's counterfactual owner test: remove the candidate owner conceptually while leaving supporting machinery in place and ask whether materially the same discretionary organizational decision still occurs.
11. For every material mapping record primary evidence, basis (`explicit`, `structural`, `inferred`, or `unknown`), confidence, and caveat.
12. Assign the local state only after function, decisive right, ownership, support, and closure are separated. For S3/S4/S5, encode a separately evidenced first-party parent mode with `(P)` on `A` or `C`, or standalone `P` when no first-party `A`/`C` autonomous mode is established.
13. Record recursion, variety, escalation, and unresolved evidence gaps separately from the six-state vector.
14. Write `assessments/<harness_id>.md` for index work. Do not generate a cohort-relative signature in this skill.

## Generation provenance

Every assessment newly created by Methodology v0.2.1 or later must preserve which semantic/tooling versions produced the original artifact:

```yaml
generated_profile_version: 0.2.1
generated_assessment_procedure_version: 0.3.0
```

These two fields are **immutable origin metadata**. Do not change them during reassessment, same-ref correction, methodology migration, or later Methodology upgrades.

The separate fields:

```yaml
profile_version: ...
assessment_procedure_version: ...
```

record the semantics/procedure under which the current canonical classification was most recently successfully produced or revalidated. They may therefore advance while the `generated_*` pair remains unchanged.

`assessment_procedure_version` and `generated_assessment_procedure_version` remain compatibility storage-key names. Their values identify the VSM Harness **Methodology version as applied to the assessment**.

For legacy artifacts whose original generation versions were never recorded, do not guess or backfill them. Absence means generation provenance is unknown.

## Methodology v0.3.0 ownership notation

Methodology v0.3.0 keeps the Profile's function semantics unchanged and changes only how first-party ownership arrangements are published for S3, S4, and S5.

Allowed publication symbols are:

```text
A  A(P)  C  C(P)  P  —  ?
```

For S3/S4/S5:

- `A(P)` = an autonomous `A` mode is established and a distinct first-party parent-governed mode for the same function is also operationally closed;
- `C(P)` = a constructor `C` mode is established and a distinct first-party parent-governed mode for the same function is also operationally closed;
- `P` = an operationally closed parent-governed mode is established, but no first-party `A` or `C` autonomous mode is established at the reviewed boundary.

The parent modifier is **multi-mode capability notation**, not simultaneous dual ownership. A concrete deployment/run still has one reconstructable decisive owner for the function at a time.

This is especially relevant to self-hosted OSS harnesses and distributed open-source organizations. A harness may deliberately support both autonomous and operator-governed S3/S4/S5 modes. Conversely, a non-human organization such as a swarm may close S3/S4/S5 autonomously without exposing any qualifying parent mode; plain `A` remains correct in that case.

Open-source contributors may also run agents in private/local execution contexts that are not centrally visible. Missing centralized access does not imply that every human decision is S5. Current-control decisions may be S3, adaptation decisions may be S4, and identity/ultimate-policy decisions may be S5, each mapped by function first and ownership second.

A contributor's local intervention does not automatically establish organization-level `(P)`. The reviewer must reconstruct the relevant function and closure at the declared recursion. If only a lower-recursion contribution cell is evidenced, classify only that boundary.

## Hard distinctions

- Delegation, routing, sequencing, or handoff alone is not S2; require evidence of a specific actual or structurally evidenced interference/conflict/oscillation among distinct operational units plus a path that attenuates it and feeds the result back into later S1 behaviour.
- A generic mailbox, shared task state, queue, graph edge, speaker selector, or lifecycle API does not receive `S2=C` merely because a developer could build coordination from it. The S2 function itself must first be established.
- Methodology v0.3.0 does not apply `(P)` or standalone `P` to S2 or S3*.
- A manager is not S3; require a whole-system current view plus authority over shared resources, commitments, priorities, constraints, accountability, synergy, or intervention. Any S3 parent-mode claim additionally requires legitimate parent ownership and returned closure.
- **Runtime enforcement is not S3 ownership.** A hard budget, concurrency gate, scheduler, or kill mechanism may enforce an S3 decision while the decisive choice belongs to an agent, developer, human, or another actor.
- A routine verifier is not S3*; require complementary and sufficiently independent access to operational reality.
- Deterministic verdict parsing/gating does not automatically own S3* if the independent audit judgment is made elsewhere; record both separately.
- Planning, learning, self-improvement, or event reaction alone is not S4; require an external-and-prospective adaptation loop whose options can affect current capability. Any S4 parent-mode claim additionally requires parent ownership of the decisive adaptation right and return into current capability.
- A prompt, static policy, guardrail, or approval step alone is not S5; require runtime identity or ultimate-policy closure.
- **Generic human approval is not `(P)`.** The cited human/parent path must close the specific established S3, S4, or S5 function at the declared recursion.
- `A(P)` does not mean parent assistance occurs during every autonomous run; it means the standard distribution exposes both evidenced first-party ownership configurations.
- `C(P)` does not mean `P` is halfway from `C` to `A`; `C` and the parent mode must each be established independently.
- Spawning or nesting is not VSM recursion.
- Missing evidence is `?`, not `—`.

A second reviewer must be able to reconstruct every positive state from cited primary evidence, including the function, decisive right, owner, support/enforcement split, closure path, declared boundary, and every ownership mode encoded by the symbol.
