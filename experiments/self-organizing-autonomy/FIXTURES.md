# Self-organizing autonomy fixture corpus

**Status:** experimental plan  
**Normative effect:** none

This corpus tests the candidate `S` publication-state distinction in [`SPEC.md`](SPEC.md). It is not a parallel assessment database and MUST NOT write experimental findings into canonical Index vectors.

The corpus is centered on **per-function endogenous functional self-improvement**. Recursive self-organization is one important realization to test, but it is not the definition of `S` and is not a prerequisite for a positive per-function witness.

## Required fixture classes

Before the experiment can become stable, the corpus must contain at least:

| Fixture | Required role |
| --- | --- |
| Clear `C` case | Function-specific construction path exists, but material new functional logic still requires an external constructor. |
| Clear `A` case | Novel in-domain variety is absorbed autonomously using the existing repertoire; no endogenous functional improvement is needed. |
| Self-modifying non-`S` case | The system edits code/prompts/configuration or adds tools but does not materially improve the relevant function's later decision/feedback closure. |
| Escalation-boundary-shift case | A function increases its local requisite variety so a disturbance class that previously required another function/parent is later absorbed locally. |
| Repertoire-change non-recursive case | The system materially improves a function's repertoire without creating a new viable recursion. This directly tests that per-function `S` is independent from recursive reproduction. |
| Recursive realization case | The system creates/reorganizes and integrates a lower viable recursion that absorbs variety the prior organization could not. This tests recursion as one realization of self-improvement, not as an `S` prerequisite. |
| S3* counterexample | Apparent self-improvement of audit destroys or fails to establish complementary independence. |
| S5 counterexample | Apparent self-governance lacks legitimate identity/ultimate-policy authority or actually belongs to a higher recursion. |

Additional fixtures are encouraged when they expose disagreement between the proposed distinction and concepts already captured by the released Profile/Methodology.

## Initial real-system candidate

### `razzant/ouroboros`

Ouroboros is the first real-system candidate because its current canonical Index assessment at pinned revision `86806ee123ce8e26cc063cc1a618f975eea64f26` establishes autonomous base coverage across all six functions and includes first-party self-evolution/protected self-rewrite surfaces.

That makes it useful precisely because it is easy to over-classify. The experiment MUST NOT treat these as sufficient evidence:

- self-evolution campaigns;
- code rewriting;
- adding tools or specialists;
- spawning/nesting subagents;
- changing constitution/configuration;
- selecting a different runtime mode.

The review question is broader than code or organizational reconstruction but stricter than ordinary adaptation:

> At the pinned Ouroboros revision and declared operating boundary, is there primary evidence that an eligible VSM function encounters material in-domain adaptation pressure, that Ouroboros endogenously learns or constructs a materially changed decision/feedback repertoire for that function, integrates the change under legitimate authority, and later absorbs relevant variety differently or more locally through that changed repertoire without an external constructor supplying the missing functional logic?

Reviewers should specifically inspect whether any disturbance class changes its escalation boundary after learning or self-improvement.

Until that complete witness is reconstructed, Ouroboros is only a **candidate fixture** and has no experimental `S` finding.

## Fixture record format

Each fixture should be a separate Markdown artifact under `fixtures/` and record:

```text
Fixture ID
Repository / synthetic fixture identity
Pinned revision or immutable fixture version
Review date
Reviewer/context declaration
System-in-focus and recursion
Operating/deployment boundary
Baseline VSM function
Baseline released Methodology state
Target in-domain disturbance / adaptation pressure
Prior functional repertoire
Evidence of repertoire inadequacy
Recognition / learning owner
Changed or newly constructed repertoire
Internal contributing functions, if any
Authorization owner / authority boundary
Integration path
Post-change closure
Escalation boundary before / after, when relevant
External-constructor check
Strong recursive witness: yes | no | inconclusive
Experimental finding:
  supports-S-hypothesis | does-not-support-S | inconclusive
Alternative interpretation under released Profile/Methodology
Primary evidence
Caveats
```

## Per-function screening for real-system fixtures

`S` is tested per VSM function. A real-system fixture with more than one released positive function MUST explicitly screen every such function before producing its overall experimental finding. Reviewers must not restrict the search to the function suggested by feature names such as evolution, review, delegation, management, policy, learning, or recursion.

For each released positive function (`S1`, `S2`, `S3`, `S3*`, `S4`, `S5` as applicable), record exactly one screening result:

- `candidate-witness` — primary evidence is sufficient to run the complete candidate `S` test in `SPEC.md` for that function;
- `no-candidate-witness` — inspected primary evidence positively establishes that the proposed behavior stays within the existing repertoire or otherwise fails a required `S` condition;
- `insufficient-evidence` — the pinned evidence does not reconstruct a qualifying transition either way.

### Released-`A` eligibility gate

`candidate-witness` is available only when the released baseline already satisfies the `A` prerequisite from `SPEC.md §3.1` in the reviewed operating mode.

- `A` is eligible for the candidate test.
- `A(P)` is eligible only for its autonomous base mode; the experiment does not infer `S(P)`.
- `C`, `C(P)` and `P` fail the released-`A` prerequisite and therefore cannot receive `candidate-witness` unless a separate canonical reassessment first changes the released baseline. When the non-`A` baseline is established, record `no-candidate-witness` for the `S` screen and keep the constructor/parent path as the released interpretation.
- `—` fails the function/ownership prerequisite and cannot receive `candidate-witness`.
- `?` remains `insufficient-evidence`; resolve the ordinary assessment uncertainty before testing `S`.

An experimental fixture MUST NOT use `S` to jump directly from `C`, `P`, `—`, or `?` to a stronger-looking state. If experimental inspection exposes evidence that the released baseline is wrong, route that evidence into the normal reassessment process and keep the experimental review frozen to its declared baseline.

For each eligible row record:

- candidate disturbance / adaptation pressure;
- prior functional repertoire;
- evidence of inadequacy;
- recognition/learning owner;
- changed repertoire;
- internal contributing functions, if any;
- authority boundary;
- integration/closure evidence;
- escalation boundary before/after, when relevant;
- external-constructor check;
- primary evidence and caveats.

A `candidate-witness` is not a positive `S` finding. It only advances that function to the complete candidate test.

### Internal cross-function contribution

A qualifying functional improvement does not have to be produced by one VSM function in isolation.

For example:

```text
S4 senses / models a recurring pattern
        ↓
internal learning produces a new S1 local regulator
        ↓
S1 integrates the regulator
        ↓
subsequent equivalent disturbance closes inside S1
instead of escalating to S3
```

This may support `S1=S` because S1's future operational repertoire changed. It does not automatically establish `S4=S`; that would require evidence that S4's own sensing/adaptation repertoire was itself improved.

The external-constructor test is about actors outside the declared assessed system supplying the missing functional logic. Internal functional collaboration must be mapped, not misclassified as external construction.

### Evidence is non-transitive across functions

In particular:

- using an unchanged S4 evolution/adaptation repertoire to improve another function does not by itself establish `S4=S`;
- spawning, nesting, adding or reconfiguring operational units does not by itself establish `S1=S`, `S2=S`, `S3=S`, or a viable recursion;
- changing audit/reviewer configuration does not establish `S3*=S` unless the improved audit function retains complementary independence and closes corrective feedback;
- changing identity, constitution, prompts, settings or policy does not establish `S5=S` unless legitimate ultimate-policy improvement and later governance closure are established;
- parameter learning does not establish `S` unless it materially changes later functional closure rather than merely tuning behavior inside the same effective regulator.

The overall fixture finding MUST identify which function-specific witness, if any, supports it. A positive per-function witness remains separate from the recursive diagnostic field.

## Escalation-boundary-shift witness

The corpus must include at least one candidate specifically testing whether endogenous learning changes where variety is absorbed.

A canonical pattern is:

```text
T0:
S1 encounters disturbance class D
→ S1 cannot absorb D with its current local repertoire
→ D escalates to S3 / parent / other legitimate authority
→ higher function resolves or supplies intervention

T1:
S1 learns or constructs a durable new local regulator R
without an external constructor supplying R's missing logic

T2:
materially equivalent D' occurs
→ S1 uses R
→ S1 closes D' locally
→ previous escalation is no longer required for that class
```

This is a strong `S1` candidate because the system changed its variety-distribution boundary. It does not imply that S3 is unnecessary generally; S3 continues to regulate whole-system present-time variety outside the newly expanded S1 repertoire.

Equivalent before/after escalation shifts may be tested for other functions where function boundaries make sense.

## Recursive realization diagnostic

`strong_recursive_witness` remains a separate field:

```text
yes | no | inconclusive
```

A positive recursive realization may be important evidence, but:

- it is not required for per-function `S`;
- its absence does not defeat an otherwise complete non-recursive per-function witness;
- nested agents, manager trees, delegation depth, or generated roles are not sufficient;
- a lower recursion must establish enough functional viability and parent integration for its bounded purpose.

This fixture class exists to test one possible self-improvement mechanism and to prevent recursion from being accidentally conflated with the definition of `S`.

## Independent review protocol

A stability-grade fixture needs two independent judgments.

The second reviewer should receive:

- the frozen experimental `SPEC.md` revision;
- the frozen fixture/repository revision;
- the declared evidence boundary;
- primary evidence references.

The second reviewer should **not** receive the first reviewer's reasoning or proposed finding before producing its own judgment.

Agreement does not require identical prose. It is sufficient when both reviewers materially agree on:

1. baseline function and released state;
2. whether material adaptation pressure / repertoire inadequacy is established;
3. whether the functional improvement is endogenous rather than externally supplied;
4. whether authority and integration close;
5. whether post-change operation absorbs the relevant variety through the changed repertoire;
6. whether an escalation boundary changes, when claimed;
7. the experimental finding;
8. the separately recorded recursive witness.

For a multi-function real-system fixture, reproducibility also requires materially compatible per-function screening: disagreements about which function contains a `candidate-witness`, `no-candidate-witness`, or `insufficient-evidence` row must remain visible and be adjudicated rather than collapsed into the overall finding.

Disagreements must remain visible in the fixture record; they are evidence about reproducibility.

## Corpus completion

The fixture corpus is complete enough for a stability decision only when all required classes are represented and no positive case depends only on repository-development/dogfood behavior outside the declared operating distribution.

At least one positive candidate, if the distinction is empirically supported, must demonstrate real **per-function endogenous functional self-improvement** in a public harness. That positive witness does not need to create a new viable recursion.

The corpus should still include a recursive-realization candidate so that recursion and `S` can be tested as distinct dimensions.

Synthetic fixtures may isolate boundary cases, but at least one `supports-S-hypothesis` candidate, if any exists, should be grounded in a real public harness repository before normative adoption is proposed.
