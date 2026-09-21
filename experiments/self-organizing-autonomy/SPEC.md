# Experimental Methodology specification: self-organizing autonomy (`S`)

**Status:** experimental draft  
**Methodology work item:** [#22](https://github.com/opensiro/vsm-harness-skills/issues/22)  
**Conceptual source:** [`vsm-harness-profile#13`](https://github.com/opensiro/vsm-harness-profile/issues/13)  
**Normative effect:** none

## 1. Purpose

This experiment tests whether the Methodology needs a publication/classification distinction beyond ordinary autonomous closure.

Current released states remain unchanged:

```text
A / A(P) / C / C(P) / P / — / ?
```

The candidate distinction is provisionally:

```text
C — the established function exposes a first-party function-specific construction
    path, but material organizational logic still requires external composition.

A — an autonomous agent owns the decisive organizational decision/feedback right
    and closes the function using the available organizational/regulatory repertoire.

S — A-level closure is established, and when that existing repertoire is materially
    insufficient for in-domain variety, the system can endogenously reconstruct or
    extend the relevant repertoire, integrate the change under legitimate authority,
    and then close the function through the reconstructed repertoire.
```

`S` is experimental publication notation, not a Stafford Beer concept and not an active Methodology state.

## 2. Profile boundary

This experiment does not redefine S1, S2, S3, S3*, S4, S5, recursion, autonomy, requisite variety, legitimate authority, or closure. Those semantics continue to come from the released VSM Harness Profile.

Function-first remains mandatory:

1. establish the VSM function at the declared boundary;
2. identify the disturbance or variety regulated;
3. identify the decisive decision/feedback right and owner;
4. separate support/enforcement from ownership;
5. establish return/closure into subsequent operation;
6. classify the released ownership state under the active Methodology;
7. only then test the experimental `S` distinction.

If applying this experiment reveals that existing Profile semantics are insufficient, record that as a Profile question rather than silently changing the meaning here.

## 3. Candidate `S` test

A per-function fixture may support the `S` hypothesis only if all of the following are reconstructed from primary evidence at one declared boundary and operating mode.

### 3.1 Released `A` prerequisite

The function already satisfies the released Methodology's `A` condition: an autonomous agent owns the relevant organizational discretion and the first-party loop is operationally closed.

`S` is not a substitute for proving the function or its ordinary autonomous ownership.

### 3.2 Material repertoire insufficiency

Evidence identifies a material disturbance that remains inside the declared operating domain but cannot be adequately absorbed by the currently available organizational/regulatory repertoire.

Distinguish repertoire insufficiency from:

- an ordinary hard task;
- transient failure;
- missing data or compute;
- retry/recovery inside an existing mechanism;
- a case already supported by another pre-authored operating branch.

### 3.3 Endogenous reconstruction

The system itself recognizes the insufficiency and forms a materially new or altered organizational/regulatory response without an external constructor supplying the missing organizational logic.

The change must alter the repertoire relevant to the mapped function, not merely choose another existing template or route.

### 3.4 Legitimate authorization

The reconstruction occurs within the legitimate authority available at the declared recursion.

If a parent or higher recursion must supply the decisive authorization or design choice, record that boundary explicitly. Permission to execute a parent-designed change is not autonomous reconstruction of the missing organizational logic.

### 3.5 Integration

The reconstructed repertoire is integrated into the operating organization. A generated patch, workflow, prompt, agent, configuration, or proposal that never becomes part of subsequent operation does not close the witness.

### 3.6 Post-change closure

After integration, the function actually absorbs the target variety through the reconstructed repertoire and returns to subsequent operation.

A capability to self-modify without evidence that the modification closes the original organizational insufficiency is insufficient.

### 3.7 External-constructor check

The review must test whether a maintainer, developer, parent, external agent, pre-authored template, or other actor supplied the material missing organizational logic.

If so, the positive `S` witness fails even if the system autonomously applies or executes the supplied construction.

## 4. Strong recursive witness

The strongest system-level witness is recursive self-organization. It shows that the organization can:

1. recognize that current organizational variety is insufficient;
2. define a new bounded operational purpose/domain for the unresolved variety;
3. create or reorganize an operational unit for that domain;
4. establish enough local coordination, control, complementary audit, adaptation, and policy relations for that unit to remain viable for the delegated purpose;
5. grant the unit bounded autonomy;
6. connect the new recursion to the parent without duplicate authority;
7. demonstrate that the new recursion absorbs variety the prior organization could not.

Literal components named S1-S5 are not required. Functional viability is.

The experiment does not yet decide whether this strong recursive witness is required for every per-function `S`, only for a future system-level `S`, or neither. The fixture corpus must resolve that question before stability.

## 5. Per-function interpretation

Each function needs its own reconstruction witness.

- **S1:** reconstruct the operational process, tooling, or local organization when the existing operational repertoire is insufficient.
- **S2:** reconstruct the coordination regime when the existing interference/oscillation attenuation repertoire is insufficient.
- **S3:** reconstruct current-control, resource-allocation, accountability, or escalation organization when the existing regulatory repertoire lacks requisite variety.
- **S3\*:** reconstruct audit strategy, probes, sampling, evidence access, or auditor composition while preserving complementary independence.
- **S4:** reconstruct how external/future distinctions are sensed, modeled, experimented with, or translated into adaptation options when the existing adaptation repertoire is insufficient.
- **S5:** reconstruct identity/ultimate-policy machinery or legitimate rules for self-revision. This is the hardest case because apparent self-revision may reveal that ultimate authority actually resides at a higher recursion.

A positive witness for one function does not imply `S` for another.

## 6. Parent-governed modes

`P` answers a different question: where legitimate decisive authority resides.

This experiment does not yet add `S(P)` or any other composite notation. Lower-level self-organization may in principle occur inside a parent-governed constitutional envelope, but any eventual composition rule must be defined and fixture-tested before normative adoption.

A future `S5=S`, if meaningful, would be a constitutional capability; it would not transitively prove `S` for S1-S4 or S3*.

## 7. Non-evidence

None of the following establishes `S` by itself:

- self-editing code;
- modifying prompts or configuration;
- adding or selecting tools;
- generating a workflow;
- spawning or nesting agents/subagents;
- choosing among pre-authored organizational templates;
- ordinary retry/recovery;
- ordinary S4 learning/adaptation;
- ordinary `A` discretion over a case already supported by the existing repertoire;
- human approval of a generated organizational change;
- repository-development or dogfood behavior outside the assessed operating boundary.

The experiment specifically tests **endogenous reconstruction or increase of regulatory variety with organizational closure**.

## 8. Experimental findings

Fixture reviews MUST NOT write `S` into canonical Index assessment vectors.

Use only:

- `supports-S-hypothesis` — all candidate-test conditions are positively reconstructed;
- `does-not-support-S` — evidence establishes that the candidate remains within released distinctions or fails a required `S` condition;
- `inconclusive` — the evidence boundary is insufficient to decide.

A report may separately record `strong_recursive_witness: yes | no | inconclusive`.

These are experimental findings, not released autonomy states.

## 9. Evidence record

A fixture report should record at least:

- repository and pinned revision, or immutable synthetic fixture identity;
- review date and reviewer/context declaration;
- system-in-focus, recursion, purpose, environment, and operating/deployment mode;
- baseline VSM function and released Methodology state;
- target in-domain disturbance;
- prior organizational/regulatory repertoire;
- evidence of repertoire insufficiency;
- recognition owner;
- reconstructed repertoire;
- authorization owner and authority boundary;
- support/enforcement mechanisms separately;
- integration path;
- post-change closure evidence;
- external-constructor check;
- strong recursive witness finding;
- alternative interpretation under released Profile/Methodology;
- caveats and primary evidence.

## 10. Stability gates

This experiment may be marked `stable` only when:

1. the required fixture classes in [`FIXTURES.md`](FIXTURES.md) are represented;
2. at least one strong positive witness exists, or the experiment explicitly records that the strong form is not empirically supported;
3. self-modification-without-self-organization and repertoire-change-without-viable-recursion counterexamples are demonstrated;
4. S3* independence and S5 legitimate-authority counterexamples are demonstrated;
5. two independent reviewers can apply the candidate test with materially reproducible results;
6. the distinction provides information not already captured by released autonomy, recursion, S4, ownership, and closure concepts;
7. per-function versus system-level semantics are resolved;
8. composition with parent-governed modes is resolved or explicitly excluded;
9. an adoption and downstream migration plan is ready.

`stable` freezes the experiment for adoption work. It does not itself alter the released Methodology.

## 11. Promotion boundary

Promotion follows [`PROMOTION.md`](PROMOTION.md).

Canonical Index vectors remain on the released state set until an explicit Methodology release adopts the new distinction. Historical provenance remains unchanged. Any downstream migration/reassessment must run against the released adopting contract, not this experiment directory.
