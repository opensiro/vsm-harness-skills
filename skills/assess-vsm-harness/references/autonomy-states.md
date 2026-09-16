# Local autonomy states

**Methodology version:** 0.3.0

Methodology v0.3.0 expands the existing parent-governed ownership state `P` from S5 to S3, S4, and S5. This is a classification-procedure change, not a change to VSM Harness Profile semantics.

These states are a publication notation for harness assessments. They are not Stafford Beer concepts and do not redefine S1-S5.

| State | Meaning |
| --- | --- |
| `A` | The VSM function is established and its **decisive organizational decision/feedback loop is closed by an autonomous agent** through the standard documented setup. Deterministic runtime machinery may transport or enforce the agent's decision without changing ownership. |
| `C` | The VSM function is established and a first-party primitive specifically exposes the relevant decisive decision or feedback path, but the developer must still compose the autonomous actor, authority, independence, or closure loop. |
| `P` | **S3, S4, or S5 only.** The function is established, but its decisive organizational right remains owned by a legitimate parent human, institution, higher recursion, or explicitly evidenced distributed parent arrangement; the resulting decision/feedback returns to govern subsequent operation. |
| `—` | Within the reviewed standard-distribution boundary, no material first-party path for the function is supplied. This does not prove that the function can never be built. |
| `?` | The reviewed primary evidence is insufficient to establish either a positive path or a defensible no-path conclusion. |

`A`, `C`, and `P` are ownership arrangements, not maturity levels. Do not interpret them as `C < P < A` or assign fractional scores to `P`.

## Decision order

Do not choose a state from component names or feature lists. Use this order:

1. establish the VSM function at the declared system boundary;
2. identify the disturbance or variety it regulates;
3. identify the decisive decision right or feedback path that closes the function;
4. identify the owner of that right;
5. separate supporting/enforcement machinery from ownership;
6. establish the return/closure path into subsequent operation where required;
7. apply the local state.

The new `P` scope does not relax the function-first rule. A human, maintainer, approval gate, roadmap, or issue tracker does not establish S3, S4, or S5 merely because it is present.

## S2 constructor threshold

`C` does not mean "this framework has communication or orchestration primitives from which S2 could be programmed." The S2 function must already be established before any positive state is assigned.

For positive S2, first reconstruct the Profile witness:

1. distinct S1 operational units at the declared recursion level;
2. a specific actual or structurally evidenced interference, conflict, or oscillation arising from their interaction;
3. a first-party coordination relation specifically capable of attenuating that disturbance;
4. a feedback path by which the coordination result can alter subsequent S1 behaviour.

Only after that functional witness exists should ownership determine the state:

- `A` when an autonomous agent owns the decisive coordination discretion and the loop is closed in the standard setup;
- `C` when a first-party **S2-specific** decision/feedback path is present but the developer must still compose the autonomous actor, authority, or closure;
- `—` when the reviewed boundary supplies only generic communication/routing/shared-state primitives with no material first-party S2-specific path;
- `?` when evidence is insufficient to decide.

Methodology v0.3.0 does not extend `P` to S2. Human coordination practices remain evidence for the S2 function and ownership analysis, but this release is deliberately limited to the parent-governed current-control, adaptation, and identity/policy paths that motivated the migration.

A mailbox, queue, shared task board, graph edge, speaker selector, lifecycle API, or dependency field is not enough for `C` merely because it could participate in a future coordination design. Evidence must tie the primitive to regulation of the identified inter-S1 disturbance.

## Ownership rules

**Decision authority is not enforcement authority.** A runtime can meter, block, kill, queue, serialize, persist, or validate an already-selected constraint without owning the organizational choice behind it. Do not award `A` because deterministic machinery has hard enforcement power; award `A` only when an autonomous agent owns the decisive organizational discretion for the mapped function.

When ownership is ambiguous, use the Profile's counterfactual owner test: conceptually remove the candidate owner while leaving supporting machinery in place. If materially the same discretionary organizational decision still occurs, the removed actor probably did not own that right. If only enforcement of a preselected rule remains, that supports ownership elsewhere.

Hybrid implementation is normal. An `A` function does not require every line of the closure loop to be agentic; it requires the relevant organizational discretion to be agent-owned and operationally closed.

A `P` function may be operationally strong and well closed while deliberately retaining its decisive right at the parent recursion. This is not a defect by itself.

## Parent-governed S3

Use `S3=P` only when the S3 function is already established at the declared recursion. Evidence must show:

1. a whole-system view of relevant current operations at that recursion;
2. a real current-control decision over resources, commitments, priorities, constraints, accountability, synergy, or intervention;
3. a legitimate parent human, institution, higher recursion, or distributed parent arrangement owns that decisive right;
4. supporting machinery is separated from the parent decision owner;
5. the decision returns to and changes subsequent current operation.

An isolated human edit, approval, merge, emergency stop, or local task correction is not automatically S3. The cited decision must actually regulate current operations on behalf of the whole at the declared boundary.

## Parent-governed S4

Use `S4=P` only when the S4 function is already established at the declared recursion. Evidence must show:

1. externally or future-relevant distinctions are sensed;
2. adaptation options are developed from those distinctions;
3. a legitimate parent human, institution, higher recursion, or distributed parent arrangement owns the decisive adaptation judgment or feedback right;
4. there is a path back into present capability / S3;
5. subsequent operation or capability can change under the returned decision.

A roadmap, research note, issue, backlog, learning loop, or human idea is not automatically S4. The evidence must reconstruct an outside-and-then adaptation loop.

## Parent-governed S5

For `S5=P`, the parent-governed path remains identity/ultimate-policy specific. It requires:

1. the disputed/proposed matter is genuinely identity- or ultimate-policy-level at the chosen recursion;
2. the matter reaches a legitimate parent human, institution, higher recursion, or distributed parent arrangement;
3. the parent makes the authoritative decision;
4. the decision returns into the harness/system;
5. subsequent operation is governed by that returned decision.

An ordinary task approval, permission prompt, verifier escalation, or accept/retry/abandon choice does not become S5 merely because a human has final say over that operational event.

## Distributed OSS parent arrangements

Open-source harnesses may be operated or developed by multiple independent contributors whose local agent runs, transcripts, credentials, and runtime state are not centrally visible. Lack of shared private execution context does not force all human authority into S5.

A distributed parent arrangement may therefore own S3, S4, or S5 rights when primary evidence establishes the relevant function, the legitimate decision holders, and the return/closure path at the declared recursion. Examples of evidence may include maintainer decisions, accepted proposals, issue/PR governance, release decisions, public operating constraints, or other repository-visible closure paths.

Do not infer organization-level `P` from the mere existence of multiple contributors. A contributor's local intervention may establish ownership only at a lower recursion if no organization-level function/closure can be reconstructed.

`C` is intentionally narrow. General framework expressiveness is not enough. A generic graph, tool API, hook, callback, or extension point does not receive `C` merely because a developer could build the VSM function with custom code.

For included autonomous harnesses, S1 should normally be `A`; if the standard distribution does not establish an autonomous operational decision/action loop, use the index exclusion state rather than forcing an S1 classification.
