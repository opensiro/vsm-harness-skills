---
name: assess-vsm-harness
description: Reconstruct an evidence-backed VSM/OSM Autonomy TL;DR for an autonomous AI agent harness at a pinned revision. Use for vsm-harness-index entries, categorical harness comparisons, autonomy boundaries, or VSM function mapping.
---

# Assess a Harness as a Viable System

Use the bundled [VSM Harness Profile](references/profile/PROFILE.md) as the sole definition of S1–S5, S3*, recursion, autonomy, variety, homeostasis, and algedonic signalling. The profile snapshot is generated from `vsm-harness-profile`; do not redefine it here.

## Set the review boundary

Declare the system-in-focus, purpose, standard-distribution boundary, recursion level, reviewed version/ref, and observation date. For public index work, assess only what the standard documented installation supplies: ready agent-owned enactment, first-party primitives that still require composition, parent-assisted S5 closure, no supplied path, or insufficient evidence. Use only the categorical states defined in `tldr.md`; do not introduce a parallel comparison scale.

Read [tldr.md](references/tldr.md) for the categorical states, chronological review order, and index update procedure. Read [token-compute.md](references/token-compute.md) only when a separate token/coordination estimate is requested, and [interventions.md](references/interventions.md) only when designing changes after the review.

## Evidence workflow

1. Declare the system-in-focus, purpose, relevant environment, standard-distribution boundary, recursion level, reviewed version/ref, and observation date.
2. Prefer primary maintainer documentation, source, architecture descriptions, examples, traces, and observed behaviour.
3. Identify operational outcomes and autonomous agent decision rights before mapping software components.
4. Map S1, S2, S3, S3*, S4, and S5 separately by asking which agent absorbs variety and exercises each role; record deterministic or human mechanisms only as supporting constraints.
5. For every material claim record evidence, basis (`explicit`, `structural`, `inferred`, or `unknown`), confidence, and caveat.
6. Reconstruct a selective, out-of-the-box VSM/OSM Autonomy TL;DR from the evidence, never from marketing copy.
7. For index work, update the matching row in `data/catalog.psv`, preserve its review ref and date, regenerate `TLDR.md`, and run the index validators.

## Non-negotiable distinctions

- A manager is not automatically S3; a planner is not automatically S4; a prompt is not automatically S5.
- A router, scheduler, graph edge, log, interrupt, or human gate is not agentic VSM enactment unless an autonomous agent holds the corresponding decision rights.
- For S1-S4 and S3*, distinguish ready agent-owned enactment from first-party
  primitives that a developer must compose. For S5 only, parent-assisted closure
  may also be reported, but it is not full agent autonomy.
- S5 requires a runtime path for identity or ultimate-policy decisions that can
  close otherwise unresolved tension and bind subsequent operation. Static goals,
  constitutions, permissions, guardrails, approval gates, and configuration only
  bound autonomy; they are not S5 by themselves.
- Logs, tracing, and ordinary tests are not automatically S3*.
- Agent spawning, teams, and subgraphs are not automatically VSM recursion.
- Missing evidence is `unknown`, not zero or `no`.
- The categorical autonomy states are a local publication notation, not Stafford Beer constructs or an external harness standard.
- Do not reward terminology or prescribe a VSM protocol, manifest, runtime, transport, or required number of agents.

## Output order

Lead with:

1. verdict and VSM/OSM Autonomy TL;DR;
2. review boundary and evidence coverage;
3. VSM function mappings with evidence basis and confidence;
4. decisive gaps, unknowns, and alternative interpretations;
5. smallest next evidence or intervention step;
6. updated catalog and generated TL;DR paths for index work.

A second reviewer should be able to reproduce every categorical state from the cited primary evidence.
