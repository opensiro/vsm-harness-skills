# ref/vsm-theory.md — Viable System Model (Beer), domain-agnostic summary

> Canon: Stafford Beer, *Brain of the Firm* / *The Heart of Enterprise*.
> What follows is an operational summary sufficient for working with vsmlite.
> Domain-specific examples are removed; vsmlite applies VSM to the **maturation**
> of a child VSM, not to running a particular project.

## The core idea

The Viable System Model (VSM) describes the **invariant structure** any
organization needs to remain viable in a changing environment. It is a
cybernetic model: which functions must exist so the system stays alive and can
adapt. Not an org chart, but a **functional topology**.

## Five systems + S3\*

| System | Name | Time horizon | Role |
|---|---|---|---|
| **S1** | Operations | now | The real work. May consist of several autonomous units. |
| **S2** | Coordination | now | Anti-oscillation: dampens conflicts between S1 units, synchronizes, isolates. |
| **S3** | Control / Optimization | inside-and-now | Executive: resources, KPIs, budget, reallocation. Balances S1. |
| **S3\*** | Audit | inside-and-now | Independent read-only channel verifying what is happening in operations. A **different** observer than S1/S3. |
| **S4** | Intelligence | outside-and-then | Scans the external environment, threats/opportunities, R&D, future scenarios. |
| **S5** | Policy / Identity | meta | Who we are; values; balance of S3↔S4; decisions requiring identity. |

The **S3↔S4 homeostasis** is the key idea: S3 is "inside and now", S4 is "outside
and then"; S5 balances between them. A skew leads either to strategic myopia
(without S4) or operational blindness (without S3).

### Beer's ideal universe (counterfactual)

If the environment were unchanging, information perfect, operations coordinated,
goals never conflicting, and identity never requiring a choice — only
`Environment + S1` would remain. All other systems **compensate for imperfections**:

| System | Compensates for |
|---|---|
| S2 | dynamic conflicts between operations |
| S3 | the limits of local optimization |
| S3\* | imperfect information |
| S4 | environmental volatility |
| S5 | ambiguity of goals and identity |

This explains **why** systems emerge across OSM phases: each appears when the
imperfection it compensates for becomes significant. See
[`../synthesis/phases.yaml`](../synthesis/phases.yaml).

## Channels (communication topology)

Who may speak to whom (permission matrix):

| From ↓ / To → | S1 | S2 | S3 | S3\* | S4 | S5 | human |
|---|---|---|---|---|---|---|---|
| **S1** | — | ✅ only | — | — | — | ⚡algedonic | — |
| **S2** | ✅ | — | ✅ | ✅ | ✅ | ✅ | — |
| **S3** | ✅ | ✅ | — | — | — | — | digest |
| **S3\*** | ✅ ro | — | — | — | — | — | ⚡critique |
| **S4** | — | ✅ | — | — | — | ✅ | brief |
| **S5** | — | ✅ | ✅ | — | ✅ | — | ⚡decisions |

Key rules:
- **S1 → S2 only**: operational units do not talk to each other directly, only
  through the coordinator.
- **S3\* read-only**: the auditor observes, never modifies; different provider.
- **S4 → S2, S5**: intelligence reports to coordination and policy.

## The algedonic channel (emergency bypass)

`S1 → S5` directly, **bypassing** S2/S3/S4 — on a critical threat
(`severity S0/S1`). This is the "pain channel": a signal of pain reaches the
highest level without hierarchical delay. In vsmlite it is implemented as
`issues/VSM-NNN.yaml` with `signal_type: algedonic` or `severity S0/S1` →
`needs_human_decision: true` → REPL digest.

## Variety engineering (Ashby's law)

*Law of Requisite Variety*: the controlling system must have at least as much
variety as the controlled. Practical techniques:

- **Attenuation** — fold noise into signal: deviation-only reporting, cadence
  grouping, `summary` fields.
- **Amplification** — grow variety: subagent fan-out, parallel sessions.
- **Transduction** — transform at boundaries without losing variety:
  `../vsm/.kilo + ISSUES.md → state/status.json` (read-only fold).

## Recursion

Each S1 unit, if complex enough, can itself be modeled as a VSM with its own
S1–S5. An organization is a **recursive tree** of viable systems. This is the
basis of OSM (the Recursion axiom) and the reason for progressive-reveal phases
in vsmlite: the child VSM is grown until it can become a full node of the tree.

## The basta constraint

S5 **prepares** decisions; it does not make them for the human. A VSM agent
collects options, evaluates, recommends — but the final decision (especially one
touching identity) stays with the human. In vsmlite this is
`basta_constraint: prepare_only` and the REPL-digest pattern: a cycle ends with a
question to the user, not an action.

---

## Further

- OSM (how new VSMs are synthesized from VSMs): [`../synthesis/osm.md`](../synthesis/osm.md)
- Telemetry contract for the future fleet consumer: [`telemetry-contract.md`](telemetry-contract.md)
- Sources: [`bibliography.md`](bibliography.md)
