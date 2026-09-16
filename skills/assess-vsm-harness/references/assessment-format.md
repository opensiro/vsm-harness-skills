# Standalone assessment format

**Methodology version:** 0.3.0

An assessment is repository-relative and revision-relative. It must not contain cohort-relative signatures, rank positions, or claims that depend on which other harnesses happen to be indexed.

Use flat frontmatter so deterministic index tooling can parse it without a YAML dependency:

```yaml
---
harness_id: example-harness
project_name: Example Harness
repository: https://github.com/example/harness
review_ref: <40-character commit SHA>
reviewed_at: YYYY-MM-DD
generated_profile_version: 0.2.1
generated_assessment_procedure_version: 0.3.0
profile_version: 0.2.1
assessment_procedure_version: 0.3.0
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: ?
autonomy_s4: C(P)
autonomy_s5: P
---
```

`generated_profile_version` and `generated_assessment_procedure_version` record the versions that produced the original artifact. They are immutable origin metadata: once written, reassessment, correction, or Methodology migration must not rewrite them.

`profile_version` records the normative VSM Harness Profile under which the current classification was most recently successfully produced or revalidated. `assessment_procedure_version` records the VSM Harness Methodology version used for that current accepted classification.

The `*_assessment_procedure_version` names are retained as compatibility storage keys. From Methodology v0.2.2 onward they do not imply a separately versioned assessment-only procedure: the same Methodology release also governs synthesis, ranking projection, and validation.

For legacy assessments whose generation versions were never recorded, omit both `generated_*` fields rather than guessing. Generation provenance is optional only for such legacy artifacts; every assessment newly created by Methodology v0.2.1 or later must emit the pair.

Allowed final `status` values for canonical index entries are `included` and `excluded-no-agentic-vsm`. A downstream intake workflow may temporarily use its own pre-admission status outside the canonical assessment contract; do not confuse that lifecycle status with an accepted assessment state. For excluded rows, omit positive autonomy claims and explain the exclusion in the body.

## State notation

The allowed publication symbols are:

```text
A  A(P)  C  C(P)  P  —  ?
```

`A(P)`, `C(P)`, and standalone `P` are valid only for S3, S4, and S5 in Methodology v0.3.0.

- `A(P)` means the autonomous `A` mode is established and a distinct first-party parent-governed mode for the same function is also operationally closed.
- `C(P)` means the constructor `C` mode is established and a distinct first-party parent-governed mode for the same function is also operationally closed.
- `P` means the parent-governed mode is the only positive ownership mode established at the reviewed boundary; no first-party `A` or `C` autonomous mode is established there.

The composite notation records supported first-party ownership modes, not simultaneous dual ownership. For each concrete mode used as evidence, the decisive right must still have a reconstructable owner and closure path.

## Required body

```markdown
# <Project name>

## Review boundary

- System in focus:
- Purpose and identity:
- Relevant environment:
- Standard-distribution boundary:
- First-party operating / deployment modes considered:
- Recursion level:
- Reviewed revision:
- Observation date:
- Generated Profile version:
- Generated Methodology version:
- Current Profile version:
- Current Methodology version:

## Repository architecture

Describe enough of the repository to preserve the assessment context: runtime, agent loop, state, tools, delegation, persistence, scheduling, evaluation, human involvement, maintainer/contributor governance, supported self-hosted/operator modes, and external integration when material.

## Operational model

Identify the actual operational outcomes and S1 units. Separate agent decision rights from runtime, developer, human, parent, and distributed governance authority. When a composite state is claimed, describe the autonomous/constructor mode and parent-governed mode separately.

## S1 — Operations

- State:
- Function:
- Disturbance / variety regulated:
- Decisive decision or feedback right:
- Decision owner:
- Supporting / enforcement mechanisms:
- Closure path:
- Why this is / is not agent-owned:
- Evidence:
- Basis:
- Confidence:
- Caveats:

## S2 — Coordination

Use the same fields, and additionally make explicit:
- distinct S1 operational units at the declared recursion level;
- specific actual or structurally evidenced inter-S1 interference / conflict / oscillation;
- coordination relation that attenuates that disturbance;
- feedback / closure path into subsequent S1 behaviour;
- why the cited primitive is S2-specific rather than generic communication, routing, sequencing, shared state, or delegation.

For `S2=C`, the S2 function itself must already be established. `C` means a first-party S2-specific decision/feedback path exists but the autonomous actor, authority, or closure still requires composition; it does not mean a generic framework could be programmed into S2. Methodology v0.3.0 does not apply `(P)` or standalone `P` to S2.

## S3 — Inside-and-now control

Use the same fields. Explicitly distinguish resource/commitment decisions from deterministic budget, scheduler, concurrency, or termination enforcement.

For `S3=P`, `S3=A(P)`, or `S3=C(P)`, additionally establish the parent mode:
- whole-system current view at the declared recursion;
- current-control decision over resources, commitments, priorities, constraints, accountability, synergy, or intervention;
- legitimate parent human/institution/higher recursion/distributed parent arrangement as decision owner in that mode;
- returned decision changing subsequent current operation.

For `S3=A(P)`, separately establish the autonomous `A` closure. For `S3=C(P)`, separately establish the S3-specific constructor path that justifies `C`.

A local human intervention, generic operator UI, or merge approval alone is not sufficient for the `(P)` modifier.

## S3* — Complementary audit

Use the same fields, and make explicit:
- claim being audited;
- ordinary reporting path;
- complementary access path;
- independence boundary;
- who acts on findings.

Methodology v0.3.0 does not apply the parent-mode modifier to S3*.

## S4 — Outside-and-then intelligence

Use the same fields, and make explicit:
- external distinction;
- future/prospective distinction;
- adaptation option generated;
- path back into current capability / S3.

For `S4=P`, `S4=A(P)`, or `S4=C(P)`, additionally establish the parent mode:
- parent ownership of the decisive adaptation judgment/feedback right;
- return of that parent decision into present capability;
- subsequent operational/capability change under that returned decision.

For `S4=A(P)`, separately establish the autonomous `A` adaptation closure. For `S4=C(P)`, separately establish the S4-specific constructor path that justifies `C`.

A roadmap, research issue, backlog, or human idea alone is not sufficient for the `(P)` modifier.

## S5 — Policy and identity

Use the same fields, and additionally make explicit:
- identity / ultimate-policy issue;
- ultimate authority in each claimed mode;
- return-to-operation path.

For `S5=P`, `S5=A(P)`, or `S5=C(P)`, show the complete parent mode: identity/policy issue → legitimate parent authority → authoritative decision → decision returned → subsequent operation governed by it.

For `S5=A(P)`, separately establish a first-party mode in which the agent/system internally closes S5 and owns the decisive identity/ultimate-policy right. The notation describes alternative supported ownership configurations; it does not claim two simultaneous ultimate authorities.

For `S5=C(P)`, separately establish the S5-specific constructor path that justifies `C`.

## Distributed OSS parent arrangement

When the reviewed system is open-source and multiple independent contributors operate local agents without a shared private runtime context, record whether parent governance is local to one contribution cell or established at the organization/project recursion. Do not infer organization-level `(P)` merely from multiple human contributors. Positive parent-mode notation requires function-specific legitimate ownership and a reconstructable return/closure path at the declared boundary.

## Self-hosted and non-human modes

For self-hosted harnesses, inspect first-party operator/supervised modes when they materially alter S3/S4/S5 ownership. A supported operator mode can justify `(P)` only when the function-specific parent loop is complete; generic extensibility is not enough.

For intentionally non-human organizations, absence of `(P)` is not a deficiency. `S3=A`, `S4=A`, or `S5=A` may be correct when those functions close autonomously and no qualifying parent-governed mode is established.

## Recursion

## Variety and escalation

## Evidence gaps
```

`Closure path` may be `not applicable` when the function or negative finding does not require a distinct returned decision, but positive S2, S3, S3*, S4, and S5 claims should make the relevant feedback path explicit enough for a second reviewer to reconstruct the regulation loop.

## Evidence requirements

Prefer immutable primary-source permalinks at the reviewed revision. Evidence may include maintainer documentation, source, examples, architecture material, tests, governance artifacts, issues/PRs, releases, or observable traces. Positive `A`, `A(P)`, `C`, `C(P)`, or `P` states require enough cited evidence for a second reviewer to reproduce the function mapping and every ownership/closure mode encoded by the symbol.

A deterministic support mechanism is evidence that a decision can be operationally enforced; it is not, by itself, evidence that the mechanism owns the organizational decision. When the owner is ambiguous, record that ambiguity and apply the counterfactual owner test rather than inferring agent or parent ownership from the existence of hard enforcement.

`?` means evidence is insufficient. `—` requires a reviewed boundary broad enough to support the narrower claim that no material first-party path is supplied there; it is not a universal impossibility claim.
