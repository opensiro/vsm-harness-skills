# Closed-source observational assessments

**Status:** experimental draft  
**Normative effect:** none  
**Canonical Index effect:** none

This experiment asks a narrow question:

> How much of the VSM Harness Profile can be assessed when an agent harness is operationally observable and documented by its vendor, but its implementation repository is not publicly reviewable?

The released Methodology remains repository-relative and revision-relative. Nothing in this directory relaxes that contract. Artifacts here are **non-canonical observational assessments** and MUST NOT be admitted to `vsm-harness-index`, consumed as canonical vectors, or presented as equivalent to a repository-pinned assessment.

## Why this experiment exists

Some important production agent harnesses are closed-source. Excluding them from all analysis hides a meaningful part of the agent ecosystem, but pretending public product documentation provides the same evidentiary strength as source-level review would weaken the assessment contract.

This directory preserves that distinction explicitly.

The experiment is intended to test whether a useful secondary publication class can exist with the following properties:

- VSM functions keep exactly the same semantic definitions as the released Profile;
- the released ownership states remain unchanged;
- positive findings require specific first-party evidence of function, decision right, owner, and closure;
- implementation opacity is represented as uncertainty rather than as negative evidence;
- the result is clearly separated from the canonical repository-backed corpus.

## Evidence boundary

Allowed evidence is public, attributable, first-party material such as:

- product and engineering documentation;
- architecture posts;
- official help-center material;
- observable product behavior documented by the vendor;
- public demos, traces, examples, or API documentation;
- other immutable or dateable first-party artifacts when available.

Third-party descriptions may be used only as discovery leads. They do not establish a positive state by themselves.

Because there is no reviewable repository revision, every assessment MUST declare:

- the system/product version or named architecture being assessed;
- the observation date;
- all credited first-party sources;
- adjacent products or historical architecture material that is not being treated as current implementation proof;
- implementation details that remain inaccessible.

## Conservative-state rule

Closed source does **not** mean absent.

When a positive path cannot be reconstructed because implementation evidence is unavailable, publish:

```text
?
```

not:

```text
—
```

A negative `—` is allowed only if the declared observable boundary itself is broad and explicit enough to support the narrower no-material-path conclusion. Mere inability to inspect source code is never negative evidence.

The same rule applies to positive states. Marketing language such as “multi-agent,” “autonomous,” “self-improving,” “manager,” or “governance” does not establish a VSM function without the function-specific disturbance, decisive right, owner, and closure path required by the released Profile/Methodology.

## Relationship to the released Methodology

These artifacts use the currently released Profile and Methodology as **reference semantics**, but they intentionally do not satisfy the released canonical artifact contract because they lack a repository-relative pinned revision.

They therefore MUST NOT use canonical `status: included` / `status: excluded-no-agentic-vsm` frontmatter or be placed under canonical `assessments/`.

A closed-source observational artifact should instead identify itself explicitly, for example:

```yaml
experimental_assessment: closed-source-observational
system_id: example-system
product_version: Example 2.0
reviewed_at: YYYY-MM-DD
profile_reference: 0.2.4
methodology_reference: 0.3.6
observational_vector: "A / ? / ? / ? / P / P"
```

The versions above identify the semantics used to perform the experiment; they are not canonical generation provenance.

## Promotion questions

Before any concept from this experiment can affect released Methodology, the project must resolve at least:

1. whether observational assessments deserve a formal publication class at all;
2. how source snapshots or evidence manifests should replace a repository commit pin;
3. which positive states can be reproduced without source access;
4. whether any negative state can be sufficiently defended for a proprietary system;
5. how canonical and observational results must be separated in downstream indexes and UI;
6. what happens when a previously closed system later publishes source code;
7. how re-observation works when a hosted product changes without a stable versioned artifact.

Until those questions are resolved through an explicit Methodology release, this directory remains research only.

## Current fixtures

- [`assessments/manus-2-0-cascade.md`](assessments/manus-2-0-cascade.md) — observational assessment of Manus 2.0 / Cascade from public first-party documentation; provisional vector `S1=A · S2=? · S3=? · S3*=? · S4=P · S5=P`.
