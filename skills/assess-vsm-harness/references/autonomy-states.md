# Local autonomy states

**Procedure version:** 0.2.1

**Autonomy-state semantics:** unchanged from procedure v0.2.0; v0.2.1 is a provenance/schema-only procedure patch.

These states are a publication notation for harness assessments. They are not Stafford Beer concepts and do not redefine S1-S5.

| State | Meaning |
| --- | --- |
| `A` | The VSM function is established and its **decisive organizational decision/feedback loop is closed by an autonomous agent** through the standard documented setup. Deterministic runtime machinery may transport or enforce the agent's decision without changing ownership. |
| `C` | The VSM function is established and a first-party primitive specifically exposes the relevant decisive decision or feedback path, but the developer must still compose the autonomous actor, authority, independence, or closure loop. |
| `P` | **S5 only.** An identity/ultimate-policy issue reaches a legitimate parent authority, the parent decides, and that decision returns to govern subsequent operation. Ultimate S5 authority remains parent-owned. |
| `—` | Within the reviewed standard-distribution boundary, no material first-party path for the function is supplied. This does not prove that the function can never be built. |
| `?` | The reviewed primary evidence is insufficient to establish either a positive path or a defensible no-path conclusion. |

## Decision order

Do not choose a state from component names or feature lists. Use this order:

1. establish the VSM function at the declared system boundary;
2. identify the disturbance or variety it regulates;
3. identify the decisive decision right or feedback path that closes the function;
4. identify the owner of that right;
5. separate supporting/enforcement machinery from ownership;
6. establish the return/closure path into subsequent operation where required;
7. apply the local state.

## Ownership rules

**Decision authority is not enforcement authority.** A runtime can meter, block, kill, queue, serialize, persist, or validate an already-selected constraint without owning the organizational choice behind it. Do not award `A` because deterministic machinery has hard enforcement power; award `A` only when an autonomous agent owns the decisive organizational discretion for the mapped function.

When ownership is ambiguous, use the Profile's counterfactual owner test: conceptually remove the candidate owner while leaving supporting machinery in place. If materially the same discretionary organizational decision still occurs, the removed actor probably did not own that right. If only enforcement of a preselected rule remains, that supports ownership elsewhere.

Hybrid implementation is normal. An `A` function does not require every line of the closure loop to be agentic; it requires the relevant organizational discretion to be agent-owned and operationally closed.

## Parent-governed S5

`P` is not shorthand for "a human approves something." It requires all of the following:

1. the disputed/proposed matter is genuinely identity- or ultimate-policy-level at the chosen recursion;
2. a runtime path transfers that matter to a legitimate parent human, institution, or higher recursion;
3. the parent makes the authoritative decision;
4. the decision returns into the harness;
5. subsequent operation is governed by that returned decision.

An ordinary task approval, permission prompt, verifier escalation, or accept/retry/abandon choice does not become S5 merely because a human has final say over that operational event.

`C` is intentionally narrow. General framework expressiveness is not enough. A generic graph, tool API, hook, callback, or extension point does not receive `C` merely because a developer could build the VSM function with custom code.

For included autonomous harnesses, S1 should normally be `A`; if the standard distribution does not establish an autonomous operational decision/action loop, use the index exclusion state rather than forcing an S1 classification.
