# Assessment families

This document defines how `vsm-harness-skills` may host more than one assessment specification while preserving a single upstream source of VSM semantics.

## Boundary

The VSM Harness Profile defines the organizational model. Assessment skills consume that model and define how evidence is collected, classified, and published for a particular assessment purpose.

```text
VSM Harness Profile
        ↓
assessment specification
        ↓
assessment artifact / corpus
```

An assessment specification may narrow the system boundary, require additional evidence, or impose domain-specific requirements. It must not silently redefine S1, S2, S3, S3*, S4, S5, recursion, variety, closure, or other Profile semantics.

If a proposed assessment requires a new VSM concept, change the Profile first. If it only changes how an existing Profile is tested or what a domain requires, the change belongs here or in another assessment-skill package.

## Canonical general assessment

`skills/assess-vsm-harness/` remains the canonical general OpenSiro assessment specification for agent harnesses.

It owns:

- evidence collection procedure;
- standalone assessment artifact contract;
- local publication notation such as `A`, `C`, `P`, `A(P)`, `C(P)`, `—`, and `?`;
- general assessment classification rules;
- the general cohort synthesis contract consumed by `opensiro/vsm-harness-index`.

The canonical general assessment is not a universal requirement for every future OpenSiro assessment use case.

## Domain-specific and community assessments

Additional assessment skills may be contributed for a bounded purpose, for example:

```text
skills/
  assess-vsm-harness/          canonical general assessment
  assess-vsm-<domain>/         possible domain-specific assessment
  ...                          other reviewable assessment contracts
```

A domain-specific or community assessment may define its own:

- system-in-focus and operating purpose;
- admission criteria;
- evidence requirements;
- domain-specific capability requirements;
- required, permitted, or insufficient ownership arrangements;
- benchmark or operational witnesses;
- output schema and publication surface.

These are assessment-contract choices. They do not create new meanings for Profile-defined functions.

## Assessing different kinds of systems

An assessment is not restricted to systems intentionally designed as VSM implementations.

The same Profile vocabulary may be used to inspect:

1. an intentional VSM realization;
2. an arbitrary harness in which VSM functions emerge from its organization;
3. a system formally specified under a non-VSM architecture.

The assessment must preserve the declared system boundary and evidence discipline in every case. A positive mapping means that the relevant VSM function is evidenced at that boundary; it does not imply that the upstream project adopted VSM terminology or intended to conform to an OpenSiro Profile.

Conversely, a project that claims to implement a VSM Profile does not receive positive findings merely from that claim. The assessment still reconstructs function, decisive right, ownership, support, and closure from evidence.

## Profile versioning and assessment migration

Profile versions are independent semantic provenance. An assessment specification records which Profile revision it consumes.

A Profile change may be relevant to an assessment specification, but the **assessment specification owns the decision about whether and how its artifacts or corpus require migration or revalidation**.

Therefore:

```text
Profile release
    ↓ semantic input
assessment specification
    ↓ compatibility / migration decision
assessment corpus
```

A general Index, domain-specific index, or other corpus must not infer its complete migration procedure solely from the existence of a newer Profile version.

Historical artifacts retain their original Profile and assessment-specification provenance.

## Corpus relationship

The canonical `opensiro/vsm-harness-index` consumes the canonical general assessment specification.

A future domain-specific assessment may publish into a separate domain-specific index or another corpus owned by that assessment system. Such a corpus is not a filtered view of the general Index; it is the output of a distinct assessment contract, even when it reuses general evidence.

This permits multiple assessment ecosystems to share the same Profile while preserving explicit methodology and provenance boundaries.
