# Standalone assessment format

**Procedure version:** 0.2.1

An assessment is repository-relative and revision-relative. It must not contain cohort-relative signatures, rank positions, or claims that depend on which other harnesses happen to be indexed.

Use flat frontmatter so deterministic index tooling can parse it without a YAML dependency:

```yaml
---
harness_id: langgraph
project_name: LangGraph
repository: https://github.com/langchain-ai/langgraph
review_ref: <40-character commit SHA>
reviewed_at: YYYY-MM-DD
generated_profile_version: 0.2.0
generated_assessment_procedure_version: 0.2.1
profile_version: 0.2.0
assessment_procedure_version: 0.2.1
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---
```

`generated_profile_version` and `generated_assessment_procedure_version` record the versions that produced the original artifact. They are immutable origin metadata: once written, reassessment or correction must not rewrite them.

`profile_version` records the normative VSM Harness Profile under which the current classification was most recently successfully produced or revalidated. `assessment_procedure_version` records the assessment procedure/autonomy notation used for that current accepted classification. These current-version fields may advance during later reassessment while the `generated_*` pair remains fixed.

For legacy assessments whose generation versions were never recorded, omit both `generated_*` fields rather than guessing. Generation provenance is optional only for such legacy artifacts; every assessment newly created by procedure v0.2.1 or later must emit the pair.

Allowed final `status` values for canonical index entries are `included` and `excluded-no-agentic-vsm`. A downstream intake workflow may temporarily use its own pre-admission status outside the canonical assessment contract; do not confuse that lifecycle status with an accepted assessment state. For excluded rows, omit positive autonomy claims and explain the exclusion in the body.

## Required body

```markdown
# <Project name>

## Review boundary

- System in focus:
- Purpose and identity:
- Relevant environment:
- Standard-distribution boundary:
- Recursion level:
- Reviewed revision:
- Observation date:
- Generated Profile version:
- Generated assessment procedure version:
- Current Profile version:
- Current assessment procedure version:

## Repository architecture

Describe enough of the repository to preserve the assessment context: runtime, agent loop, state, tools, delegation, persistence, scheduling, evaluation, human involvement, and external integration when material.

## Operational model

Identify the actual operational outcomes and S1 units. Separate agent decision rights from runtime, developer, human, and parent authority.

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

Use the same fields.

## S3 — Inside-and-now control

Use the same fields. Explicitly distinguish resource/commitment decisions from deterministic budget, scheduler, concurrency, or termination enforcement.

## S3* — Complementary audit

Use the same fields, and make explicit:
- claim being audited;
- ordinary reporting path;
- complementary access path;
- independence boundary;
- who acts on findings.

## S4 — Outside-and-then intelligence

Use the same fields, and make explicit:
- external distinction;
- future/prospective distinction;
- adaptation option generated;
- path back into current capability / S3.

## S5 — Policy and identity

Use the same fields, and additionally make explicit:
- identity / ultimate-policy issue;
- ultimate authority;
- return-to-operation path.

For `P`, show the complete parent closure: identity/policy issue → legitimate parent authority → authoritative decision → decision returned → subsequent operation governed by it.

## Recursion

## Variety and escalation

## Evidence gaps
```

`Closure path` may be `not applicable` when the function or negative finding does not require a distinct returned decision, but positive S3*, S4, and S5 claims should normally make the relevant feedback path explicit.

## Evidence requirements

Prefer immutable primary-source permalinks at the reviewed revision. Evidence may include maintainer documentation, source, examples, architecture material, tests, or observable traces. Positive `A`, `C`, or `P` states require enough cited evidence for a second reviewer to reproduce both the function mapping and the ownership/closure classification.

A deterministic support mechanism is evidence that a decision can be operationally enforced; it is not, by itself, evidence that the mechanism owns the organizational decision. When the owner is ambiguous, record that ambiguity and apply the counterfactual owner test rather than inferring agent ownership from the existence of hard enforcement.

`?` means evidence is insufficient. `—` requires a reviewed boundary broad enough to support the narrower claim that no material first-party path is supplied there; it is not a universal impossibility claim.
