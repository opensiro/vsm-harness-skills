# Positive-evidence calibration — reachable owners, complementary audits, and witness identity

**Status:** informative positive-evidence calibration for a proposed `0.3.8` patch; not an independent Index adjudication or executable semantic oracle. Based on cross-case review dated 2026-10-13; comparison confidence varies by case.

**Source-analysis baseline:** Profile `0.2.4` / released Methodology `0.3.7`. Proposed `0.3.8` preserves their semantics. The authoritative rules remain [SKILL.md](../SKILL.md), [autonomy-states.md](autonomy-states.md), [assessment-format.md](assessment-format.md), and the [Profile](https://github.com/opensiro/vsm-harness-profile/blob/v0.2.4/PROFILE.md). For bounded negatives and unknowns see [negative-state-calibration.md](negative-state-calibration.md).

This guide illustrates how to **apply existing** function-first, decision-owner, boundary-reachability, and return/closure requirements when a positive witness looks plausible but the exact operational path may be missing or misidentified. It does **not** change S1–S5/S3* semantics, states `A/A(P)/C/C(P)/P/—/?`, positive thresholds, mandatory fields, the `—`/ `?` distinction, or synthesis/ranking rules. It does not assign or overwrite any Index grade.

## A source-based reconstruction technique (optional)

For a disputed positive claim, try to reconstruct one representative first-party operating path. This is a source-inspection aid, **not a universal necessary executable trace for a composable `C`**:

```text
supported entry point / declared mode
  → feature flag and dependency initialization
  → actor, provider, parent and tool binding
  → runtime guard / actual invocation
  → function-specific decision or alternative observation
  → feedback returned to a legitimate owner
  → change to subsequent operation or capability
```

This is an **analytical trace**, not a required diagram, artifact field, whole-system integration run, or replacement for the existing function-relative evidence tests.

- **`A`**: confirm the autonomous decisive actor and material closure are reachable in a supported claimed mode. A named class, setter, registration, configuration default, passing unit test, or API schema alone does not establish that mode's runtime execution. Inspect initialization order, early-return guards, optional enablement, and feedback consumption. Static primary-source tracing can support a claim with appropriate caveats; provider-backed execution is not universally mandatory.
- **`C`**: examine the **function-specific**, intentionally first-party exposed constructor separately. It may require a developer to compose actor, authority, independence or closure by definition. Do **not** silently downgrade a challenged `A` to `C`, and do **not** disqualify `C` merely because ordinary `A` execution is incomplete. Generic extensibility is not sufficient.
- **Boundary**: credit only declared shipped, installed or supported optional modes. A test fixture, blog vignette, development/dogfood agent, external host/CI, or user-authored plugin cannot donate ownership merely by repository co-location or because a future configuration is conceivable. A documented optional mode may be valid even when not always enabled.
- **Evidence identity**: link the evidence to the **actual event and artifact claimed**. A local `git rev-parse HEAD`, current default branch, nearest CI result, cached diff, or similarly named task may not identify a pushed ref, reviewed commit, executed worker, or sampled operational artifact. Explain conditional paths and what cannot be identified; do not impose a universal event-ID schema.
- **S3***: distinguish the producing agent's normal QA or self-report, generic judging/consensus over that report, and truly complementary inspection of operational reality. Establish claim-relative independence, alternative evidence access, identifiable audit judgment and returned findings affecting control. A different vendor, dedicated class, independent human, GitHub approval, always-on gate or separate GitHub account is **not** universally required.
- **S3/S4**: a scheduler or task router need not be S3; identify current whole-system commitments, legitimate discretionary authority, and feedback. Memory, planning or extension files need not be S4; identify outside/future-relevant sensing, prospective adaptation judgment and a path to changed capability. Keep recursion and optional mode explicit.

These checks are aids for spotting misapplied existing requirements, **not additional necessary conditions for every positive assessment**. An unresolved alternative first-party path merits investigation and may support `?` under the existing negative-state procedure; this guide never determines that result by itself.

## Frozen contrast workbook (R1–R10)

Cases are **questions about evidence sufficiency**, not accepted state labels or gold grading fixtures. The named assessments, including those already canonically admitted, are not certified correct by inclusion. Preserve the **exact upstream revision in each URL** and the original historical Methodology when re-reading. The [source-pinned admission and targeted sample manifest](positive-evidence-sample-2026-10-13.md) makes the selection reproducible (20 recent admissions, 12 distinct targeted, 23 unique across both cohorts).

### R1 — Dedicated complementary review, same provider allowed

Pinned sources: [AtomCode coding assembly](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-coding/src/parts.rs), [review tool](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/review_tool.rs).

- **Expected evidence decision:** reconstruct mounted `code_review`, live Git diff, fresh read-only reviewer, findings and return. A shared provider is not itself failure of independence.
- **Counter-check:** the tool is optional per call and may fail when its provider slot or Git context is unavailable; do not assert review happens on every normal turn.

### R2 — Plan approval versus implementation-artifact review

Pinned source: [OpenHuman plan-review module](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/plan_review/mod.rs), [delegation](https://github.com/tinyhumansai/openhuman/blob/eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d/crates/openhuman-core/src/agent/orchestration/delegation.rs).

- **Expected evidence decision:** separate a user-facing plan approval/revision gate from the delegation `review` stage in the accepted S3* assessment. Inspect what the reviewer actually receives or samples: plan approval is not itself independent operational-artifact audit. Check other supported modes before settling presence or bounded absence.
- **Counter-check:** a different shipped reviewer path could alter the evidence conclusion; do not automatically turn this into a negative grade.

### R3 — Consensus on reports versus operational evidence

Pinned source: [Swarms majority voting](https://github.com/kyegomez/swarms/blob/3009364a7e44dc3e55fec238b56b3a4fa6949a05/swarms/structs/majority_voting.py).

- **Expected evidence decision:** identify what each voter/judge actually observes. A second agent receiving prior answers is not automatically a complementary first-party primary-artifact audit.
- **Counter-check:** independently inspect other packaged Swarms auditing modes instead of generalizing from one voting constructor.

### R4 — Available component but broken ordinary runtime binding

Pinned sources: [SuisuiCode CLI](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py), [TUI app](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/tui/app.py), [subagent guard](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py), [memory manager](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory/manager.py). Original Methodology **0.3.6**, not 0.3.7.

- **Expected evidence decision:** compare `set_parent` before TUI `on_mount` against the subagent `_parent is None` rejection; independently compare exposed `set_provider` with `update_async` early return when provider is missing. Ask whether any other supported shipped path closes the claimed function.
- **Counter-check:** static ordinary-path evidence does not prove every alternate mode is impossible; `C` constructor eligibility and negative-state choices remain separate Index-owner semantic questions, not predetermined grades.

### R5 — CI observation must match the triggering event

Pinned sources: [Rum push detection](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/tui.rs#L561-L566), [CI watcher](https://github.com/KAJdev/rum/blob/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd/src/main.rs#L866-L923). Original Methodology **0.3.7**.

- **Expected evidence decision:** distinguish command text containing `git push` from a verified push event; distinguish local `HEAD` from the actual pushed ref. Attribute CI judgment to its configured owner separately from Rum's deterministic transport.
- **Counter-check:** this does not prove all CI is non-independent or that a narrower configured TUI case cannot provide complementary evidence. Exact grade remains for the Index owner.

### R6 — Generic reviewer composition is not automatically first-party S3*

Pinned sources: [bb first-party reviewer vignette](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/web/src/blog/posts/building-a-restrained-software-factory.md), [child-thread notifications](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/server/src/services/threads/child-thread-notifications.ts), contrasted with [AtomCode review tool](https://github.com/karlorz/atomcode/blob/152b2cc132dda9b177c3a030e21cfacd95494ea3/crates/atomcode-review/src/review_tool.rs). Original bb Methodology **0.3.6**; its Index assessment was **proposed**, not canonical, when sampled.

- **Expected evidence decision:** distinguish bb's genuine first-party child-thread primitives and documented user-requested review from a fully evidenced installed audit-specific function with complementary access and feedback. Inspect possible first-party configured modes before judging.
- **Counter-check:** do not require a specially named reviewer class, different model vendor or automatic trigger. This is an unresolved comparator, not a bb regrade.

### R7 — Whole-current S3 discretion versus delegation

Pinned sources: [KairoCode opt-in coordinator](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/coordinator/__init__.py), [CLI mode wiring](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/cli.py), [TUI runtime](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/tui/app.py), [team task and message tools](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/tools/__init__.py), contrasted with [Capstan child dispatch](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tools.lua).

- **Expected evidence decision:** trace actual supported team mode, view of current commitments, agent-owned intervention and returned reassignments, rather than awarding S3 to any subagent queue.
- **Counter-check:** no artificial crisis, minimum agent count, mandatory event journal or Organization-specific transaction state is required.

### R8 — S4 future capability versus extension scaffolding

Pinned sources: [Capstan conditional self-improvement](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/skills/self-improvement/SKILL.md), [plugin runtime](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/src/plugins_runtime.c), contrasted with [Xoder create-extension skill](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/data/skills/create-xoder-extension/SKILL.md) and [extension runtime](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/extensions/runtime.py).

- **Expected evidence decision:** distinguish an enabled first-party pathway to durable, future-reusable capability change from generic user-directed plugin authoring and static configuration. For Capstan, distinguish the user's reason or authorization for initiating self-improvement from the agent's discretionary choice and design of the reusable capability; confirm that the installed runtime can load it.
- **Counter-check:** Capstan's capability is opt-in; neither automatic self-evolution nor unconditional permission bypass is implied.

### R9 — Cross-cutting provenance safeguard (not a positive-state example)

Frozen anchors: [Claw Code](https://github.com/ultraworkers/claw-code/tree/08106b0c3771ef5b4a5aa176acccd460e88b7325) and [SuisuiCode](https://github.com/Yangtianspike/suisui-code/tree/c9017b0613b22151325a5904a521aefe4c62abbc) assessed under **0.3.6**; [Rum](https://github.com/KAJdev/rum/tree/9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd) under **0.3.7**.

- **Expected evidence decision:** keep original `review_ref` and immutable `generated_*` origin; a separate successful governed reassessment may advance current methodology provenance, not the generation pair.
- **Counter-check:** a newly written guide alone is not a reassessment, a migration trigger, or a reason to repin sources.

### R10 — Cross-cutting negative/unknown safeguard (not a positive-state example)

Pinned anchors: [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent/tree/04d809ceab9df28f9adaed044884180159172930) and [AgentScope](https://github.com/agentscope-ai/agentscope/tree/5ff52f877de12d66a30d55af279dd4f42b1590f3).

- **Expected evidence decision:** document actual inspected S1/other function boundaries before a bounded no-path conclusion, while preserving uncertainty when a plausible supported reviewer path is insufficiently traced.
- **Counter-check:** do not optimize state frequencies or copy existing canonical `—`/`?` as immutable gold labels.

## Application / governance boundary

These ten contrasts are a **reviewer worksheet**, not an executable semantic oracle or a second Methodology. Their cited upstream revisions remain frozen; cases with live Index correction disputes (notably Rum, SuisuiCode and bb) remain unresolved until separately authorized same-ref reviews and admissions. An existing accepted or proposed assessment is evidence to inspect, not proof of truth.

A future reviewer can record for each case: examined operating mode; reachable invocation and guards; primary artifact/event identity; function/owner/return; counterevidence and unresolved alternate routes. These are **suggested notes**, not a required new artifact schema.

No corpus-wide prevalence or false-positive rate can be inferred from the nonrandom 20 recent admissions plus 12 distinct targeted harnesses (23 unique across both cohorts). The frozen manifest documents the selection, not fresh complete independent re-execution of all 23 source trees. The proposed `0.3.8` introduces no new Profile semantics, classification threshold, assessment field, ranking/synthesis procedure or automatic Index correction. Disputed assessments require their own owner-controlled reviews; frozen experiments retain their pinned Methodology.
