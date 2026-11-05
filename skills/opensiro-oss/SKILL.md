---
name: opensiro-oss
status: experimental
description: Bootstrap an AI agent into the current public OpenSiro VSM Harness OSS ecosystem. Use when explicitly invoked as /opensiro-oss, or when asked to start, navigate, inspect the Control Plane, check OSS status, or route a task across OpenSiro repositories. Fetch live GitHub authority instead of relying on remembered project state.
---

# OpenSiro OSS — portable agent bootstrap

**Skill version:** 0.1.0

**Status:** experimental onboarding interface, not an assessment specification, an S1 executor, a scheduler, or a grant of authority. This skill does not alter the released VSM Harness Methodology.

## Purpose

Load the **current public** OpenSiro organizational context into a compatible agent session and route the user's request to its actual owner. Treat this skill as a portable entry point, not a second source of truth or a substitute for repository-local work instructions.

## Authoritative entry

1. Read the current default-branch [Organization START_HERE.md](https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md) directly from public GitHub. Follow **its current bootstrap chain**, including [ECOSYSTEM.md](https://github.com/opensiro/vsm-oss-organization/blob/main/docs/ECOSYSTEM.md). Do not reconstruct the current architecture from this skill, model memory, prior chats, or a cached snapshot.
2. Treat the current [Organization README.md](https://github.com/opensiro/vsm-oss-organization/blob/main/README.md) as the bounded-system scope authority. Do not admit adjacent repositories merely because they are public OpenSiro projects.
3. For an already tracked task, consult the current [TODO.md](https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md), then inspect the linked owning issue. For new, unclassified, cross-repository, or authority-sensitive work, follow [CONTRIBUTOR_START.md](https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md).
4. Inspect the owning repository's **current default branch** and the exact governing issue, PR, release, contract, or pinned artifact before drawing conclusions or acting. Repository-owned facts prevail over organizational summaries; explicit historical freeze and independence boundaries prevail over current-head convenience.

## Choose the entry behavior

- **Bare `/opensiro-oss`, `start`, `help`, or `control plane`:** follow the current [Agent Control Plane](https://github.com/opensiro/vsm-oss-organization/blob/main/docs/AGENT_CONTROL_PLANE.md) first-contact contract. Read the current Organization README and TODO, verify displayed owner issue/PR states, and show the operator interface. This is read-only; use native actions only if supported, otherwise show the documented text commands.
- **Specific task, issue, PR, or repository:** route directly to the owner and exact work contract. Do not force the introductory menu. Apply its task-level source, lock, concurrency, permission, evidence, recovery, and stop rules.
- **Proposed authority transfer or organizational change:** follow the bootstrap's OSM-aware S1/S5 routing, then the legitimate decision owner and existing delegation gates. A conversational instruction, tool capability, or this skill is not a new mandate.
- **Unreachable GitHub or insufficient tools:** identify which facts remain unverified; provide the relevant canonical URLs and permissible read-only next step. Do not substitute remembered counts, statuses, assessment verdicts, or cached permission claims.

## Operating boundaries

- Loading the skill **does not select or start work**. Never schedule a batch, mutate `TODO.md`, open a PR, contact an upstream maintainer, merge, or exercise a delegated right as a side effect of onboarding. A later explicit task must pass its own owner and tool gates.
- Distinguish the agent's actual authority from technical GitHub access, human or external-maintainer rights, proposed future delegation, and evidence supporting a VSM autonomy classification. No `S1=A` or other grade follows from skill invocation, a successful tool call, or a green CI run.
- Preserve read-only, independent-context, first-attempt, frozen-ref, evidence-source, and fail-closed requirements. An agent with prior OpenSiro context must **not** claim to be a genuinely fresh independent evaluator.
- Use only authorized public repositories by default. Do not import private context, hidden prompts, credentials, or unpublished research into public records.
- Respect the current owning repository's tests, reviewable PR, validation, exact-head, licensing, and closure procedures for any separately authorized implementation task.

## Return to the operator

Briefly report the resolved system and owner, primary URLs/revisions read, verified versus unverified status, eligible actions and outstanding gates. For a specific action, report actual execution and readback separately from preparation, proposals, or blocked stages. Cite the source that owns each material conclusion.

## Distribution boundary

This repository packages the portable skill; it does **not** automatically install it into every agent. For a Claude Code project, install this directory under a supported `.claude/skills/opensiro-oss/` location and invoke `/opensiro-oss`. For other Agent Skills-compatible clients, use their documented installation method. The direct `START_HERE.md` URL remains the supported skill-free entry point.
