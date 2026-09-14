# Index publication and VSM/OSM Autonomy TL;DR

For `vsm-harness-index`, `data/catalog.psv` is the sole maintained dataset and `TLDR.md` is its generated projection. Do not create scored assessment JSON, derived CSVs, or separate entry pages.

Update catalog candidates in ascending `catalog_position`, beginning with position 1. Preserve source provenance, `review_ref`, and `reviewed_at`; then regenerate the public view with `python scripts/render_tldr.py` and run `python scripts/check_index.py`.

## VSM/OSM Autonomy TL;DR

Generate a compact, six-line VSM snapshot from the completed evidence. VSM defines
the six organizational functions. The local, non-canonical OSM lens describes how
far the standard distribution has transferred those functions from a parent or
developer to autonomous agents; it does not redefine S1-S5. The
harness name is already a separate index field and should not be repeated. Every
core system stays visible so readers can compare rows without guessing which field
was omitted.

Use the standard-distribution boundary: built-in and first-party components reached
through documented installation and configuration. Exclude arbitrary custom code,
user-invented control agents, and third-party plugins.

Before writing, establish that the harness supports agent autonomy: an AI agent has
a bounded decision/action loop, uses context or state, chooses actions, tools, or
delegation, and receives feedback that can affect subsequent action. A single model
call, static workflow, or deterministic router alone is not autonomous S1.

```text
S1 · A: <ready agent-owned operational work>
S2 · C: <first-party coordination primitive requiring composition>
S3: —
S3*: ?
S4: —
S5 · P: <parent-assisted identity/policy closure>
```

Autonomy states are categorical, not scores:

| State | Meaning |
| --- | --- |
| `A` | Agent-owned enactment is ready through the standard documented setup. |
| `C` | A first-party primitive is shipped, but the developer must compose the agent, authority, or feedback loop. |
| `P` | Parent-assisted runtime closure; permitted only for S5 and not equivalent to autonomous S5. |
| `—` | No material first-party path is supplied within the review boundary. |
| `?` | The reviewed evidence cannot establish the state. |

Rules:

- process harnesses by the index's current chronological `catalog_position`,
  starting with position 1; use `harness_id`, not the ordinal, as stable identity;
- compare each candidate internally with all lower positions and retain the most
  informative architectural distinction; do not force uniqueness when systems match;
- use exactly six compact lines in canonical S1, S2, S3, S3*, S4, S5 order;
  write claims as `Sx · A: ...`, `Sx · C: ...`, or for S5 only `S5 · P: ...`;
  hard maximum 420 characters;
- write `Sx: —` when no first-party path is supplied, and `Sx: ?` when evidence
  cannot establish the state;
  the dash means unasserted here, not proven absence;
- do not mention another S1–S5 label inside a line's description; use that system's
  own line, or `—` there when no claim is warranted;
- S1 must establish the operational autonomy boundary and cannot be `—`;
- identify which autonomous agent absorbs variety, what it may decide, and which
  harness mechanism sustains that autonomy;
- distinguish agent-owned roles from functions retained by runtime, humans, or a
  parent system; configuration-time authorship is not runtime ownership;
- for S1-S4 and S3*, use `A` only for ready agent-owned enactment and `C` when a
  developer must still compose the role, authority, independence, or feedback loop;
- for S5, require a runtime identity/ultimate-policy closure path whose decision
  can alter subsequent operation; parent-assisted closure uses `P` and is not full
  autonomy;
- static goals, prompts, constitutions, permissions, guardrails, approval gates,
  and configuration are not S5 without that closure path;
- write concrete architectural statements, not `strong`, `partial`, or scores;
- keep supported descriptions selective and short; completeness comes from explicit
  dashes, not filler claims;
- distinguish independent S3* from observability and S4 from internal planning;
- describe `unknown` as unverified, not absent;
- omit scores, percentages, praise, roadmap language, and “implements VSM”;
- keep recursion and escalation in detailed mappings rather than treating them as
  additional numbered systems in this compact fingerprint;
- preserve the six catalog field boundaries and render them as separate lines in tables.

Example:

```text
S1 · A: Agent nodes perform operational work against durable, checkpointed state.
S2 · C: Edges, Commands, and shared state require developer-composed coordination.
S3: —
S3*: ?
S4: —
S5 · P: Interrupts can return parent policy decisions to suspended work.
```

The six catalog fields are authoritative; `TLDR.md` is generated from them.
