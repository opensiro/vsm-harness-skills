# Local autonomy states

These states are a publication notation for harness assessments. They are not Stafford Beer concepts and do not redefine S1-S5.

| State | Meaning |
| --- | --- |
| `A` | The VSM function is established and ready agent-owned enactment is available through the standard documented setup. |
| `C` | The VSM function is established and a first-party primitive specifically exposes the relevant decision or feedback path, but the developer must still compose the autonomous actor, authority, independence, or closure loop. |
| `P` | Parent-assisted runtime closure returns an identity or ultimate-policy decision to subsequent operation. Valid only for S5 and not equivalent to autonomous S5. |
| `—` | Within the reviewed standard-distribution boundary, no material first-party path for the function is supplied. This does not prove that the function can never be built. |
| `?` | The reviewed primary evidence is insufficient to establish either a positive path or a defensible no-path conclusion. |

## Decision order

Do not choose a state from component names or feature lists. Use this order:

1. establish the VSM function at the declared system boundary;
2. identify the actor or mechanism responsible for that function;
3. identify the relevant decision right or feedback path;
4. determine runtime ownership of that right;
5. apply the local state.

`C` is intentionally narrow. General framework expressiveness is not enough. A generic graph, tool API, hook, callback, or extension point does not receive `C` merely because a developer could build the VSM function with custom code.

For included autonomous harnesses, S1 should normally be `A`; if the standard distribution does not establish an autonomous operational decision/action loop, use the index exclusion state rather than forcing an S1 classification.
