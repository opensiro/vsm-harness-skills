# Self-organizing autonomy fixture corpus

**Status:** experimental plan  
**Normative effect:** none

This corpus tests the candidate `S` publication-state distinction in [`SPEC.md`](SPEC.md). It is not a parallel assessment database and MUST NOT write experimental findings into canonical Index vectors.

## Required fixture classes

Before the experiment can become stable, the corpus must contain at least:

| Fixture | Required role |
| --- | --- |
| Clear `C` case | Function-specific construction path exists, but material new organizational logic still requires an external constructor. |
| Clear `A` case | Novel in-domain variety is absorbed autonomously using the existing repertoire; no endogenous reconstruction is needed. |
| Self-modifying non-`S` case | The system edits code/prompts/configuration or adds tools but does not reconstruct the relevant organizational repertoire with closure. |
| Repertoire-change non-recursive case | The system changes organizational repertoire, but evidence does not establish a new viable recursion. This tests whether per-function `S` should be weaker than the strong recursive witness. |
| Strong recursive candidate | The system autonomously creates/reorganizes and integrates a viable recursion that absorbs variety the prior organization could not. |
| S3* counterexample | Apparent self-reconstruction of audit destroys or fails to establish complementary independence. |
| S5 counterexample | Apparent self-governance lacks legitimate identity/ultimate-policy authority or actually belongs to a higher recursion. |

Additional fixtures are encouraged when they expose disagreement between the proposed classification distinction and concepts already captured by the released Profile/Methodology.

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

The review question is narrower:

> At the pinned Ouroboros revision and declared operating boundary, is there primary evidence that an existing organizational/regulatory repertoire became insufficient for material in-domain variety, that Ouroboros itself recognized that insufficiency, reconstructed the relevant repertoire without an external constructor supplying the missing organizational logic, integrated the reconstruction under legitimate authority, and then used it to absorb the target variety?

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
Target in-domain disturbance
Prior repertoire
Evidence of repertoire insufficiency
Recognition owner
Reconstructed repertoire
Authorization owner / authority boundary
Integration path
Post-change closure
External-constructor check
Strong recursive witness: yes | no | inconclusive
Experimental finding:
  supports-S-hypothesis | does-not-support-S | inconclusive
Alternative interpretation under released Profile/Methodology
Primary evidence
Caveats
```

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
2. whether repertoire insufficiency is established;
3. whether reconstruction is endogenous rather than externally supplied;
4. whether authority and integration close;
5. whether post-change operation absorbs the target variety;
6. the experimental finding;
7. whether a strong recursive witness exists.

Disagreements must remain visible in the fixture record; they are evidence about reproducibility.

## Corpus completion

The fixture corpus is complete enough for a stability decision only when all required classes are represented and no positive case depends only on repository-development/dogfood behavior outside the declared operating distribution.

Synthetic fixtures may isolate boundary cases, but at least one `supports-S-hypothesis` candidate, if any exists, should be grounded in a real public harness repository before normative adoption is proposed.
