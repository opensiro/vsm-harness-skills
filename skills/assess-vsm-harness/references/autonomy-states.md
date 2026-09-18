# Local autonomy states

**Methodology version:** 0.3.4

Methodology `0.3.x` adds a parent-governed mode modifier for S3, S4, and S5. This is a classification/publication procedure layered on unchanged VSM Harness Profile semantics.

These symbols are publication notation for autonomous AI agent harness assessments. They are not Stafford Beer concepts and do not attempt to enumerate every ownership arrangement possible in a real organization.

| State | Meaning |
| --- | --- |
| `A` | The VSM function is established and its **decisive organizational decision/feedback loop is closed by an autonomous agent** through a first-party standard-distribution mode. Deterministic runtime machinery may transport or enforce the agent's decision without changing ownership. |
| `A(P)` | The `A` condition is established **and** the same function has a distinct first-party parent-governed mode that is operationally closed. The two modes need not be active simultaneously; in any concrete deployment/run the decisive right must still have a reconstructable owner. |
| `C` | The VSM function is established and a first-party primitive specifically exposes the relevant decisive decision or feedback path, but the developer must still compose the autonomous actor, authority, independence, or closure loop. |
| `C(P)` | The `C` condition is established **and** the same function also has a distinct first-party parent-governed mode that is operationally closed. |
| `P` | **S3, S4, or S5 only.** The function is established and an operationally closed parent-governed mode exists, but no first-party `A` or `C` autonomous mode is established at the reviewed boundary. |
| `—` | Within the reviewed standard-distribution boundary, no material first-party path for the function is supplied. Under Methodology `0.3.3`, the assessment records the surfaces inspected, plausible first-party paths checked, and why none closes the function. This does not prove that the function can never be built. |
| `?` | The reviewed primary evidence is insufficient to establish either a positive path or a defensible no-path conclusion. |

`A`, `C`, and `P` describe ownership arrangements, not maturity levels. `A(P)` and `C(P)` add a supported parent-governed mode; they do not mean partial autonomy and must not be converted to numeric weights.

Under Methodology `0.3.3`, `—` is a documented absence conclusion rather than a fallback for incomplete search. If the inspected boundary cannot support the required absence scope, use `?`.

For `A(P)` and `C(P)`, the assessment also records a two-row mode matrix (base mode and parent mode) with decisive owner, trigger, closure, and evidence. This makes the already-existing multi-mode semantics reconstructable without changing the state meaning.

A parent-governed mode is not established merely because a human can edit configuration, stop a process, approve a PR, or invoke an extension point. The relevant S3/S4/S5 function must first be established, and the parent path must itself contain a legitimate decisive right plus a return/closure path into subsequent operation.

## Publication boundary

The Methodology intentionally distinguishes **what can exist organizationally** from **what it publishes as a useful ownership state for an autonomous agent harness**.

- **S1:** `P` is not published. Included harnesses are expected to establish autonomous operational ownership; a system whose ordinary S1 decision right remains human-owned does not receive `S1=P` merely to keep it inside the autonomy table.
- **S2:** `P` is not published. Human coordination can exist in real organizations, but ordinary parent/human coordination between S1 units is outside the Methodology's parent-mode notation for autonomous harnesses.
- **S3:** `P`, `A(P)`, and `C(P)` are permitted as explicit supervisory/current-control topologies.
- **S3*:** parent-mode notation is not published in the `0.3.x` line. Audit is classified through complementary access, independence, audit judgment, ownership, and feedback.
- **S4:** `P`, `A(P)`, and `C(P)` are permitted as explicit parent-assisted adaptation topologies.
- **S5:** parent governance is the canonical `P` case because identity / ultimate-policy authority can legitimately remain at a parent recursion while the return-to-operation loop is complete.

This boundary is methodological, not ontological. It does not claim that human-owned S1, S2, or S3* are impossible. It says those cases are not useful `P` publication states for the autonomous-harness assessment target.

## Decision order

Do not choose a state from component names or feature lists. Use this order:

1. establish the VSM function at the declared system boundary;
2. identify the disturbance or variety it regulates;
3. identify the decisive decision right or feedback path that closes the function;
4. identify the owner of that right in each first-party mode being claimed;
5. separate supporting/enforcement machinery from ownership;
6. establish the return/closure path into subsequent operation where required;
7. classify the autonomous base mode as `A`, `C`, `—`, or `?`;
8. for S3/S4/S5, add `(P)` only when a distinct parent-governed mode is independently established; use standalone `P` when the parent mode is the only positive ownership mode established.

The notation does not relax the function-first rule. A human, maintainer, approval gate, roadmap, or issue tracker does not establish S3, S4, or S5 merely because it is present.

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

A mailbox, queue, shared task board, graph edge, speaker selector, lifecycle API, or dependency field is not enough for `C` merely because it could participate in a future coordination design. Evidence must tie the primitive to regulation of the identified inter-S1 disturbance.

## Ownership rules

**Decision authority is not enforcement authority.** A runtime can meter, block, kill, queue, serialize, persist, or validate an already-selected constraint without owning the organizational choice behind it. Do not award `A` because deterministic machinery has hard enforcement power; award `A` only when an autonomous agent owns the decisive organizational discretion for the mapped function.

When ownership is ambiguous, use the Profile's counterfactual owner test: conceptually remove the candidate owner while leaving supporting machinery in place. If materially the same discretionary organizational decision still occurs, the removed actor probably did not own that right. If only enforcement of a preselected rule remains, that supports ownership elsewhere.

Hybrid implementation is normal. An `A` function does not require every line of the closure loop to be agentic; it requires the relevant organizational discretion to be agent-owned and operationally closed.

`A(P)` and `C(P)` are **multi-mode capability notation**, not simultaneous dual ownership. For example, a self-hosted harness may support an autonomous S3 mode and a separately selectable operator-governed S3 mode. The assessment may record `S3=A(P)` when both are first-party and evidenced, while a concrete deployment still has one reconstructable decisive owner at a time.

A `P` mode may be operationally strong and intentionally retained at the parent recursion. This is not a defect by itself.

## Parent-governed S3 mode

Use `P` or add `(P)` to S3 only when the S3 function is already established at the declared recursion. Evidence must show:

1. a whole-system view of relevant current operations at that recursion;
2. a real current-control decision over resources, commitments, priorities, constraints, accountability, synergy, or intervention;
3. a legitimate parent human, institution, higher recursion, or explicitly evidenced distributed parent arrangement owns that decisive right in the parent mode;
4. supporting machinery is separated from the parent decision owner;
5. the decision returns to and changes subsequent current operation.

An isolated human edit, approval, merge, emergency stop, or local task correction is not automatically S3 parent governance. The cited decision must actually regulate current operations on behalf of the whole at the declared boundary.

## Parent-governed S4 mode

Use `P` or add `(P)` to S4 only when the S4 function is already established at the declared recursion. Evidence must show:

1. externally or future-relevant distinctions are sensed;
2. adaptation options are developed from those distinctions;
3. a legitimate parent human, institution, higher recursion, or explicitly evidenced distributed parent arrangement owns the decisive adaptation judgment or feedback right in the parent mode;
4. there is a path back into present capability / S3;
5. subsequent operation or capability can change under the returned decision.

A roadmap, research note, issue, backlog, learning loop, or human idea is not automatically S4. The evidence must reconstruct an outside-and-then adaptation loop.

## Parent-governed S5 mode

Use `P` or add `(P)` to S5 only for an identity/ultimate-policy path. It requires:

1. the disputed/proposed matter is genuinely identity- or ultimate-policy-level at the chosen recursion;
2. the matter reaches a legitimate parent human, institution, higher recursion, or explicitly evidenced distributed parent arrangement;
3. the parent makes the authoritative decision in the parent mode;
4. the decision returns into the harness/system;
5. subsequent operation is governed by that returned decision.

`S5=A(P)` is valid when the standard distribution genuinely supports both an internally agent-owned S5 closure mode and a distinct parent-governed S5 mode. This does not mean two ultimate authorities act simultaneously; it means the harness exposes two evidenced first-party ownership configurations.

An ordinary task approval, permission prompt, verifier escalation, or accept/retry/abandon choice does not become S5 merely because a human has final say over that operational event.

## Distributed OSS parent arrangements

Open-source harnesses may be operated or developed by multiple independent contributors whose local agent runs, transcripts, credentials, and runtime state are not centrally visible. Lack of shared private execution context does not force all human authority into S5.

A distributed parent arrangement may own S3, S4, or S5 rights when primary evidence establishes the relevant function, legitimate decision holders, and return/closure path at the declared recursion. Examples of evidence may include maintainer decisions, accepted proposals, issue/PR governance, release decisions, public operating constraints, or other repository-visible closure paths.

Do not infer organization-level parent governance from the mere existence of multiple contributors. A contributor's local intervention may establish ownership only at a lower recursion if no organization-level function/closure can be reconstructed.

## Self-hosted and non-human organizations

A self-hosted OSS harness may intentionally expose parent-governed S3/S4/S5 modes to the operator while also supporting autonomous modes. `A(P)` and `C(P)` make that optional parent path visible without collapsing it into the autonomous base state.

Conversely, an intentionally non-human organization such as a swarm may establish `S3=A`, `S4=A`, or `S5=A` without any parent-governed mode. Absence of `(P)` is not evidence that the function is absent; it means no qualifying first-party parent mode is established at the reviewed boundary.

`C` is intentionally narrow. General framework expressiveness is not enough. A generic graph, tool API, hook, callback, or extension point does not receive `C` merely because a developer could build the VSM function with custom code.

For included autonomous harnesses, S1 should normally be `A`; if the standard distribution does not establish an autonomous operational decision/action loop, use the index exclusion state rather than forcing an S1 classification.
