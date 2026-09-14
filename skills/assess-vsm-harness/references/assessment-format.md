# Standalone assessment format

An assessment is repository-relative and revision-relative. It must not contain cohort-relative signatures, rank positions, or claims that depend on which other harnesses happen to be indexed.

Use flat frontmatter so deterministic index tooling can parse it without a YAML dependency:

```yaml
---
harness_id: langgraph
project_name: LangGraph
repository: https://github.com/langchain-ai/langgraph
review_ref: <40-character commit SHA>
reviewed_at: YYYY-MM-DD
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---
```

Allowed `status` values are `included` and `excluded-no-agentic-vsm`. For excluded rows, omit positive autonomy claims and explain the exclusion in the body.

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

## Repository architecture

Describe enough of the repository to preserve the assessment context: runtime, agent loop, state, tools, delegation, persistence, scheduling, evaluation, human involvement, and external integration when material.

## Operational model

Identify the actual operational outcomes and S1 units. Separate agent decision rights from runtime, developer, human, and parent authority.

## S1 — Operations

- State:
- Function:
- Responsible actor:
- Decision rights:
- Supporting mechanisms:
- Evidence:
- Basis:
- Confidence:
- Caveats:

## S2 — Coordination

Use the same fields.

## S3 — Inside-and-now control

Use the same fields.

## S3* — Complementary audit

Use the same fields.

## S4 — Outside-and-then intelligence

Use the same fields.

## S5 — Policy and identity

Use the same fields.

## Recursion

## Variety and escalation

## Evidence gaps
```

## Evidence requirements

Prefer immutable primary-source permalinks at the reviewed revision. Evidence may include maintainer documentation, source, examples, architecture material, tests, or observable traces. Positive `A`, `C`, or `P` states require enough cited evidence for a second reviewer to reproduce the classification.

`?` means evidence is insufficient. `—` requires a reviewed boundary broad enough to support the narrower claim that no material first-party path is supplied there; it is not a universal impossibility claim.
