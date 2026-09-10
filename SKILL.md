---
name: vsmskill
description: Assess agentic VSM adoption for AI-native systems, reject agentic VSM for conventional or merely AI-assisted projects, identify bounded potential AI insertion points, estimate token-compute and duplicated context when evidence permits, diagnose existing VSM maturity, persist comparable assessment artifacts, and maintain groupable harness metric tables. Use for VSM feasibility, AI-native readiness, VSM status, autonomy, agent topology, token duplication, or migration questions. Do not treat microservices, ordinary ML, CI, or repository size as proof that agents are needed.
---

# VSM project assessment

Evaluate a project in one or both modes:

1. **Adoption feasibility** — should this project be translated into a VSM, at what depth, and at what token/coordination cost?
2. **Current VSM status** — how complete, operational, autonomous, and evidence-backed is its existing VSM?

The result is a decision instrument, not a generic architecture essay. Inspect the repository before judging it. Separate observations, calculations, external facts, assumptions, and recommendations.


## AI-native gate — run this first

This skill evaluates **agentic VSM for AI-native systems**. Distributed software architecture, microservices, CI pipelines, ordinary ML inference, and organizational complexity do not by themselves justify agents or an agentic VSM.

Classify the project before applying any VSM readiness score:

| Class | Definition | Typical evidence |
|---|---|---|
| **NOT AI-NATIVE** | The primary value loop is deterministic software or human-operated workflows. AI is absent. | services, queues, APIs, schedulers, rules, conventional analytics |
| **AI-ASSISTED** | AI performs a bounded optional feature but does not own the system's primary decisions or autonomous work loop. | one LLM enrichment call, copy generation, classifier fallback, operator-invoked assistant |
| **AI-NATIVE** | Models/agents are indispensable operational actors: they perceive context, make non-trivial decisions, use tools or coordinate work, and their behavior must be governed and evaluated. | agent loops, tool calls, planning, model routing, memory/state, evals, autonomous recovery, multi-agent handoffs |

Ask four gating questions:

1. If the AI component is replaced by a deterministic stub, does the project's defining value proposition disappear?
2. Does an AI actor choose actions or merely return bounded content/predictions inside a conventional program?
3. Is there a persistent or repeated AI work loop with state, tools, feedback, retries, or delegation?
4. Are model behavior, context, autonomy, and evaluation first-class operational risks?

Classification rules:

- A recommendation model, ranking model, MAB, computer-vision model, or LLM endpoint is not automatically an **agent**.
- A single prompt used to generate text or JSON is normally **AI-assisted**, not AI-native.
- Microservices are software deployment units, not agentic S1 units, unless an AI actor inside them has meaningful local autonomy.
- Tests and CI are ordinary verification. They become S3* in an agentic VSM only when they independently verify AI/agent claims or autonomous outcomes.
- Do not award agentic-VSM readiness points for complexity that standard software architecture, workflow orchestration, SRE, or governance already handles well.

### Gate outcomes

- **NOT AI-NATIVE → NO AGENTIC VSM.** Stop the agent-topology score. Briefly note whether ordinary VSM is useful as an organizational metaphor, but recommend conventional engineering controls.
- **AI-ASSISTED → NO AGENTIC VSM or EXPLORE.** Assess the bounded AI feature and potential insertion points. Cap the topology at MIN until an autonomous loop is proven valuable.
- **AI-NATIVE → continue** to the full feasibility and status rubrics.

Never hide this gate inside the final score. Put the AI-native classification beside the headline verdict.

## Potential AI insertion scan

For NOT AI-NATIVE and AI-ASSISTED projects, do not end at “no”. Identify only plausible places where AI could add value, while preserving deterministic systems where they are superior.

Evaluate candidate insertion points for:

- unstructured inputs that resist stable rules;
- repeated human judgment or investigation bottlenecks;
- planning or coordination across changing constraints;
- external intelligence synthesis where sources and premises change;
- anomaly explanation, incident triage, or experiment interpretation;
- adaptive content/decision generation requiring evaluation and rollback.

Reject or downgrade candidates when:

- exact rules, SQL, optimization, schemas, tests, or standard ML solve the task more reliably;
- the action is high-impact but no independent verifier or human approval is available;
- there is no feedback signal for evaluating model behavior;
- latency, privacy, determinism, or unit economics make AI inappropriate;
- “add an agent” merely wraps an existing API or cron job.

For every credible candidate report:

```text
candidate · current human/deterministic bottleneck · proposed AI role · required tools/data
decision authority · verifier · failure containment · measurable pilot · expected token/latency class
```

Use `EXPLORE` only when at least one candidate has a measurable outcome, bounded authority, available evidence, and a reversible pilot.

## Core model

Use Stafford Beer's functional topology:

| Function | Question | Software/agent evidence |
|---|---|---|
| S1 Operations | Where is value actually produced? | independently useful services, packages, workflows, agents, products, or teams |
| S2 Coordination | What prevents oscillation and collisions between S1 units? | routing, queues, locks, shared contracts, scheduling, conflict resolution, handoffs |
| S3 Control | How are current resources and performance regulated? | budgets, KPIs, allocation, operational state, prioritization, intervention rules |
| S3* Audit | How is operational truth checked independently? | read-only probes, tests, evals, external verifier, reconciliation against raw evidence |
| S4 Intelligence | How does the system observe the outside and the future? | dependency/security scanning, market or user signals, model/benchmark scouting, scenarios |
| S5 Policy | What preserves identity and resolves S3↔S4 tension? | mission, invariants, authority boundaries, human-only decisions, risk appetite |

Also inspect:

- **Channels:** information paths are explicit, bounded, and usable.
- **Algedonic path:** urgent harm/benefit can bypass normal routing.
- **Variety balance:** coordination complexity is attenuated; capabilities are amplified where required.
- **Recursion:** a complex S1 unit becomes its own VSM only when it needs independent viability.
- **Evidence loop:** status derives from observable artifacts and behavior, not filenames alone.

S1–S5 are functions, not a management hierarchy. A folder named `s4` is not proof of intelligence; a behavior, cadence, owner, input, output, and trace are proof.

## Authority and safety

- Read-only assessment is the default.
- Do not install a VSM, create agents, change prompts, contact providers, or run paid model calls unless the user asked for implementation or measurement.
- Never expose secrets found in repository files or logs. Report only the path and secret type.
- Do not infer permission to upload private code, prompts, traces, or telemetry.
- Mark destructive organizational transformations (`Remove`, identity-changing `Reconfigure`, irreversible split/merge) as human decisions.
- Treat model prices, context limits, provider cache rules, and benchmark leaderboards as time-sensitive. Verify current values from official provider documentation when the report depends on them. Record the URL and retrieval date.

## Choose the mode

Infer the mode from the request. Run both when the user asks for a general VSM review or migration plan.

### Adoption feasibility

Answer:

- Is the project NOT AI-NATIVE, AI-ASSISTED, or AI-NATIVE?
- Which components are actual AI actors, and which are only conventional services or ML models?
- Is there enough operational variety to justify VSM?
- Which existing units map to S1?
- Which coordination pathologies already exist?
- Which VSM functions are needed now, later, or not at all?
- Would a single general prompt, a modular single-agent prompt, or multi-agent VSM be proportionate?
- What compute, token duplication, latency, and governance overhead would the proposed topology add?
- What is the smallest reversible pilot?

### Current VSM status

Answer:

- Which functions exist in files and which operate in reality?
- Is the VSM structural, executable, observed, or autonomous?
- What has changed since the previous snapshot, if history exists?
- Where are blind spots, bottlenecks, false-positive metrics, or stale state?
- What is the next smallest intervention that increases viability?

## Evidence ladder

Classify every material claim:

| Level | Label | Examples |
|---:|---|---|
| E0 | absent | no artifact found |
| E1 | declared | README, prompt, YAML, diagram |
| E2 | implemented | executable code/config realizes the function |
| E3 | exercised | logs, tests, commits, runs, or traces show use |
| E4 | verified | independent check or external ground truth confirms behavior |

Never score E1 as operational maturity. When evidence conflicts, prefer E4→E3→E2→E1 and describe the conflict.

For each observation retain:

```text
claim · evidence level · repository path/line or URL · observation date · caveat
```

Use `unknown`, not zero, when data is unavailable.

## Repository scan

Start broad and become selective. Respect repository instructions and ignore vendor, generated, cache, binary, and secret-bearing trees unless directly relevant.

### 1. Establish boundaries

Identify:

- repository root and nested repositories;
- product/code roots and deployment units;
- existing `vsm`, `vsmlite`, agent, prompt, workflow, state, issue, telemetry, benchmark, and eval directories;
- repository instructions and ownership boundaries;
- dirty working tree and whether historical comparison is meaningful.

### 2. Build a project inventory

Inspect manifests, README files, architecture docs, prompt files, agent definitions, CI workflows, tests/evals, observability, issue templates, state snapshots, and recent history. Prefer fast filename/text search before opening many files.

Extract:

- mission and actual delivered capabilities;
- independently operable units;
- shared resources and collision points;
- external environment and rate/latency constraints;
- model/provider configuration;
- token/cost/usage telemetry;
- human approval boundaries;
- failure and escalation paths.

Keep domain capabilities distinct from runtime technology. “Processes claims” is a capability; “FastAPI service” is an implementation.

### 3. Detect an existing VSM

Search both explicit and implicit forms. Explicit markers include `S1`, `system_1`, `coordination`, `S3*`, `algedonic`, `autonomy`, and `maturation`. Implicit equivalents may be queues, controllers, audit pipelines, strategic scanners, governance documents, or incident escalation.

Map actual behavior first; map names second.

### 4. Capture a snapshot

Record commit/ref, working-tree state, scan time, relevant model IDs, and evidence coverage. If comparison data exists, keep the current and previous snapshots separate.

## Adoption feasibility rubric

Apply this rubric only after the AI-native gate passes. For AI-assisted projects, use it only as a hypothetical score for a named insertion-point pilot and label it `candidate`, never as the current project's VSM readiness.

Score each dimension 0–4 using evidence, then apply the gating rules.

| Dimension | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Agentic operational plurality | one AI action or none | weakly separated AI steps | 2 AI actors/loops with shared dependencies | 3+ semi-autonomous AI units | recursive AI units with independent environments |
| Coordination pressure | none | occasional | recurring collisions/handoffs | costly oscillation/contention | coordination dominates delivery risk |
| Environmental volatility | stable | rare changes | regular dependency/user changes | several changing external domains | continuous strategic adaptation required |
| Information asymmetry | direct observable work | small gaps | self-report differs from tests sometimes | independent audit is regularly needed | false positives or adversarial evidence are material |
| Identity/policy tension | one obvious objective | minor tradeoffs | recurring product/quality tradeoffs | multiple authorities or risk boundaries | unresolved S3↔S4 conflict threatens identity |
| Persistence | one-shot | short project | maintained workflow | long-lived product/system | fleet/ecosystem expected to outlive operators |
| Observability readiness | none | prose only | basic tests/logs | structured state and metrics | versioned telemetry + independent verification |
| Economic headroom | no budget | unclear | tight but measurable | overhead acceptable | coordination savings likely exceed overhead |

Calculate:

```text
readiness = sum(dimension scores) / 32 × 100
```

This percentage is a communication aid, not a scientific probability.

### Gating rules

- Recommend **NO AGENTIC VSM** when the AI-native gate fails. Do not let microservice count, test volume, or repository size override this.
- Recommend **EXPLORE** when the current project is not AI-native but one or more bounded AI insertion points warrant a measured pilot.
- Recommend **NO VSM** when there is only one meaningful S1 unit, no persistent coordination problem, and no credible need for independent S3* or S4.
- Recommend **MIN** when VSM is useful as one agent's reasoning/control frame but separate agents would mainly duplicate context.
- Recommend **MODULAR** when one orchestrator should load function-specific prompt sections on demand.
- Recommend **MAX** when at least two S1 units act independently, coordination/audit must run concurrently or independently, durable state exists, and the token/latency budget can support multiple contexts.
- A high readiness score cannot override the AI-native gate or absent agentic S1 plurality for MAX.
- Low observability caps the recommendation at a reversible pilot.

Suggested verdict bands:

| Readiness | Default interpretation |
|---:|---|
| 0–24 | do not adopt; improve ordinary engineering controls |
| 25–49 | use selected VSM concepts or MIN |
| 50–69 | pilot MIN/MODULAR and instrument it |
| 70–84 | VSM is justified; stage MAX only where independence matters |
| 85–100 | strong candidate for recursive or multi-agent VSM |

## Token-compute assessment

Perform this section when the repository exposes relevant data or the model/topology is known. Do not fabricate precision.

### Data priority

Use the strongest available source:

1. provider-reported usage per request/run;
2. repository traces with input, cached-input, reasoning/output, and call counts;
3. exact model tokenizer over reconstructed messages;
4. compatible tokenizer or provider token-count endpoint;
5. calibrated characters/token estimate with a wide range;
6. qualitative result only.

Record which level was used for each number. Model name alone does not reveal reasoning tokens, cache hits, tool-schema overhead, or dynamically retrieved context.

### Unit of analysis

Define one representative workload before calculating:

```yaml
workload:
  task_class: <name>
  runs: <count or 1>
  topology: single | modular | multi-agent
  model_by_role: { role: model-id }
  shared_context: <files/messages>
  role_context: <files/messages>
  expected_turns: <observed or range>
  tool_schema_tokens: <observed or estimate>
  output_tokens: <observed or estimate>
```

Do not mix totals from different task classes or benchmark harnesses.

### Token accounting

For call `i`:

```text
T_i = I_new_i + I_cached_i + O_i + R_i
```

where `R_i` is hidden/reasoning tokens only when reported. Present both raw token traffic and provider-billed equivalents when cache discounts matter. Do not silently treat cached input as zero compute.

For an agent role `a` with `n_a` calls:

```text
T_a = Σ T_i
T_run = Σ_a T_a
```

For a proposed topology without traces, calculate low/base/high scenarios. Vary call count, context growth, output length, cache hit rate, and retry rate. State assumptions beside the table.

### Static prompt/context inventory

If the model tokenizer is available, tokenize the exact serialized messages, including system prompt, tool schemas, role prompt, shared policies, and injected repository context. If serialization is unavailable, report “content tokens” and state that protocol overhead is excluded.

If only text size is known, use a labeled approximation such as:

```text
estimated_tokens = characters / calibrated_chars_per_token
```

Calibrate against at least one representative repository sample when possible. Otherwise use a broad language-aware range and label confidence low.

### Duplication estimate

Measure duplicate context before estimating savings.

1. Normalize line endings and trailing whitespace; preserve code and meaning.
2. Split prompt/context files into stable semantic blocks (headings, paragraphs, fenced blocks, or message fields).
3. Hash exact normalized blocks for the conservative lower bound.
4. Optionally detect near-duplicates using token shingles or sequence similarity; never combine them silently with exact duplicates.
5. Build the invocation matrix: which block is sent to which role, call, and turn.
6. Separate **required replication** (safety, identity, permissions) from **avoidable replication** (the same long background, examples, schemas, or status copied everywhere).

Compute:

```text
sent_tokens = Σ_b tokens(b) × transmissions(b)
exact_duplicate_tokens = Σ_b tokens(b) × max(transmissions(b) - 1, 0)
avoidable_duplicate_tokens = Σ_b avoidable_share(b) × tokens(b) × max(transmissions(b) - 1, 0)
duplication_rate = avoidable_duplicate_tokens / sent_tokens
```

For near-duplicates report a range, never a single exact number:

```text
lower = exact avoidable duplicates
upper = lower + reviewable near-duplicate overlap
```

When caching applies, show two views:

- **traffic duplication:** all repeated tokens;
- **effective billed duplication:** repeated tokens weighted by the provider's current cache pricing;

and keep latency/context-window duplication separate from monetary savings.

### Baseline and VSM scenarios

Compare at least:

| Scenario | Shape | What repeats |
|---|---|---|
| Current | observed repository topology | measured |
| MIN | one general prompt, one context | nearly no cross-agent repetition |
| MODULAR | shared core + loaded role module | only selected modules |
| MAX | orchestrator + independent S1/S2/S3/S3*/S4/S5 prompts | shared constitution, task state, schemas, handoffs |

Include the break-even statement:

```text
MAX is justified only if the expected reduction in retries, collisions, missed failures,
or human coordination is worth more than its additional token, latency, and governance cost.
```

If open data is needed, prefer official model/tokenizer/pricing documentation. Public open-source estimators may be used as reproducible tooling or cross-checks, with version/date recorded:

- TokenCost: https://github.com/AgentOps-AI/tokencost
- TokenTally: https://github.com/TikiTribe/TokenTally
- Tokenometer: https://github.com/faraa2m/tokenometer

Do not import a current price table into this skill; it will become stale.

### Confidence

Assign token-estimate confidence:

- **high:** provider usage or exact tokenizer + known message serialization and call counts;
- **medium:** exact static prompt counts with observed or bounded call counts;
- **low:** compatible tokenizer or calibrated character estimate;
- **unavailable:** model, context, or invocation data is insufficient.

## Existing VSM status rubric

Run the existing-status rubric as an **agentic VSM** assessment only for AI-native systems. For other projects, you may map implicit organizational VSM functions separately, but label the result `organizational VSM analogy`; do not describe ordinary tests, services, or deployment control as evidence of an existing agentic VSM.

Score every function on two axes:

- **design (0–3):** absent, declared, implemented, coherent;
- **operation (0–3):** no evidence, exercised once, recurring, independently verified.

Then record freshness and confidence.

| Function | Design max | Operation max | Critical evidence |
|---|---:|---:|---|
| S1 | 3 | 3 | useful work and artifacts |
| S2 | 3 | 3 | actual collision prevention/routing |
| S3 | 3 | 3 | resource/KPI decisions change operations |
| S3* | 3 | 3 | independent read-only check against raw truth |
| S4 | 3 | 3 | external/future signal changes priorities or premises |
| S5 | 3 | 3 | identity boundaries govern real decisions |
| Channels | 3 | 3 | messages/handoffs follow defined paths |
| Algedonic | 3 | 3 | urgent signal bypass is tested or exercised |
| Recursion | 3 | 3 | recursive unit has real independent viability need |
| Observability | 3 | 3 | state is generated, current, and reconcilable |

Calculate separate, transparent summaries:

```text
structural_completeness = Σ design / 30 × 100
operational_maturity = Σ operation / 30 × 100
```

Do not average them into one number unless the user asks. A beautiful dashboard with one misleading score is still misleading.

### Maturity stage

Assign the highest stage whose evidence is satisfied:

| Stage | Meaning |
|---|---|
| Initial | no stable intent or operational boundary |
| Phase 0 — Intent | mission, scope, authority, and target autonomy are explicit |
| Phase 1 — S1 | operational unit(s) exist and deliver artifacts |
| Phase 2 — S2 | recurring coordination is exercised |
| Phase 3 — S3 | control uses KPIs/resources to regulate work |
| Phase 4 — S3* | independent audit observes operations |
| Phase 5 — S4 | environment/future scanning changes the model |
| Phase 6 — S5 | identity and S3↔S4 balance govern decisions |
| Autonomous | all functions recur without parent compensation; escalation remains bounded |

Do not advance a stage because files for later stages exist. Later functions may coexist early; the stage identifies the weakest required preceding function.

### Assisted autonomy A(t)

Use `A(t)` only when the project has a defined parent/child or operator/system boundary. Otherwise report autonomy qualitatively.

Assess six signs, each `0`, `0.5`, or `1`:

1. S1 produces useful results without parent intervention.
2. S2 resolves ordinary conflicts without parent intervention.
3. S3 reallocates resources or corrects deviations using current evidence.
4. S3* independently detects false reporting or blind spots.
5. S4 closes at least one external signal into a changed premise/priority.
6. S5 contains human escalation to identity/risk decisions rather than routine work.

```text
A(t) = sum(signs) / 6
```

This is a local operationalization, not a canonical Beer metric. Report the six signs so the number is auditable.

Verdict:

- `DEPENDENT`: A < 0.34
- `ASSISTED`: 0.34 ≤ A < 0.67
- `SEMI-AUTONOMOUS`: 0.67 ≤ A < 0.9
- `AUTONOMOUS`: A ≥ 0.9 and no critical function is below E3

Cap at `SEMI-AUTONOMOUS` if S3* is not independent, S4 only performs QA, state is stale, or the algedonic path is blocked.

## Detect common VSM pathologies

Flag these explicitly:

- **Ceremonial VSM:** S1–S5 names exist but do not affect work.
- **S3 dominance:** rich control/metrics, weak external intelligence.
- **S4 theatre:** browsing/research exists but never changes premises or priorities.
- **Audit capture:** S3* uses the same evidence, prompt, model, or write authority as operations.
- **Dashboard truth:** generated status is trusted without reconciliation to source artifacts.
- **Agent multiplication:** each function is an agent although workload is sequential and shared context dominates.
- **Context tax:** shared constitution/status/schema is copied into every agent and every turn.
- **Recursive inflation:** every folder is modeled as a VSM without independent viability.
- **Blocked algedonic path:** urgent evidence must traverse ordinary queues.
- **Human micro-management:** S5 escalates routine choices instead of identity/risk decisions.
- **Stale snapshot:** maturity claims are older than the operational evidence.

## Recommendation design

Recommend the smallest topology that satisfies requisite variety.

### NO VSM

Use ordinary architecture, tests, ownership, and incident handling. Mention which VSM ideas remain useful without adopting the vocabulary.

### NO AGENTIC VSM

State that the project is not AI-native enough to justify agent governance. Preserve deterministic architecture. If useful, list candidate AI insertion points separately; do not install agents merely to make the project appear AI-native.

### EXPLORE

Run one bounded AI-native pilot around a named insertion point. Keep authority narrow, add a deterministic or human verifier, collect token/latency/quality data, and define rollback before considering MIN/MODULAR/MAX.

### MIN

Use one general prompt containing mission, S1–S5 questions, evidence rules, a single state snapshot, and escalation boundary. Best when one agent can hold the whole task and independence is not essential.

Start from `vsm-template/min/VSM.md`.

### MODULAR

Keep one general agent and load only the function module needed for the current phase. Prefer this when context cost is material but specialized checklists improve decisions.

Use the MAX prompts as modules without spawning agents.

### MAX

Use an orchestrator and function-specific agents only where concurrency, information separation, or independent verification is valuable. S3* must remain read-only and should differ from S1 in model/provider or at least evidence path when feasible.

Start from `vsm-template/max/`.

### Migration increments

Propose reversible steps:

1. define mission, system boundary, human authority, and observable S1;
2. instrument baseline task/token/latency/failure data;
3. add S2 only for observed collisions;
4. add S3 when real allocation/KPI decisions exist;
5. add independent S3* when information asymmetry matters;
6. add S4 when external change must feed decisions;
7. formalize S5 when identity tradeoffs recur;
8. split into agents only after modular single-agent evidence shows a benefit.

Every step needs a success criterion, rollback condition, and measurement window.

## Durable assessment artifact

When the user asks to save, compare, benchmark, track, or retain an assessment, emit a machine-readable artifact in addition to the human report. Do not silently write files for an ordinary read-only assessment.

Default paths when the user does not choose them:

```text
.vsm/assessments/<project-slug>/<ISO-date>-<short-ref>.json
.vsm/harnesses.csv
.vsm/harness-metrics.csv
```

The JSON artifact is the source of truth. The CSV files are derived comparison indexes and may be rebuilt. Use `scripts/upsert_harness.py <artifact.json> --output-dir <dir>` when this repository's helper is available.

### Artifact contract

Use schema version `vsm-assessment/v1`. Preserve missing observations as `null` with `availability: unknown`; never coerce unknown to zero. Store raw sub-scores as well as percentages so every aggregate can be reconstructed.

```json
{
  "schema_version": "vsm-assessment/v1",
  "assessment_id": "<stable project-ref-date id>",
  "generated_at": "<ISO-8601>",
  "snapshot": {
    "project_name": "<name>",
    "repository": "<path-or-url>",
    "ref": "<commit/ref>",
    "dirty": null,
    "assessment_mode": "feasibility|status|both",
    "rubric_version": "vsmskill/v1"
  },
  "harness": {
    "harness_id": "<stable normalized id>",
    "harness_kind": "single-agent|multi-agent|framework|eval-harness|runtime|hybrid",
    "execution_model": "one-shot|loop|graph|manager-workers|swarm|mixed",
    "state_mode": "stateless|session|persistent|mixed|unknown",
    "tool_mode": "none|fixed|dynamic|mixed|unknown",
    "human_gate": "none|optional|required|mixed|unknown",
    "audit_independence": "none|same-agent|separate-prompt|separate-model|external-ground-truth|unknown"
  },
  "summary": {
    "ai_native_class": "NOT AI-NATIVE|AI-ASSISTED|AI-NATIVE",
    "verdict": "NO AGENTIC VSM|EXPLORE|MIN|MODULAR|MAX|HOLD",
    "recommended_topology": "none|min|modular|max",
    "maturity_stage": "<stage>",
    "vsm_tldr": "<one sentence produced under the vsm-tldr contract>"
  },
  "metrics": [],
  "functions": [],
  "compute": [],
  "pathologies": [],
  "evidence": [],
  "caveats": []
}
```

Represent metrics in long form so results can be grouped without parsing prose:

```json
{
  "metric_id": "vsm.structural_completeness",
  "metric_group": "vsm_completeness",
  "vsm_function": null,
  "axis": "design",
  "scenario": null,
  "workload_id": null,
  "value": 14,
  "max_value": 30,
  "unit": "score",
  "status": "observed",
  "confidence": "medium",
  "evidence_level": "E2",
  "availability": "available"
}
```

Use stable metric identifiers:

- `gate.ai_native`;
- `adoption.readiness` and `adoption.<dimension>`;
- `vsm.structural_completeness`, `vsm.operational_maturity`, and `vsm.<s1|s2|s3|s3star|s4|s5|channels|algedonic|recursion|observability>.<design|operation>`;
- `autonomy.assisted`;
- `compute.calls`, `compute.tokens.sent`, `compute.tokens.avoidable_duplicate`, `compute.duplication_rate`, and `compute.latency`.

For each entry in `functions`, retain `function`, `design`, `operation`, `status`, `evidence_level`, `confidence`, and evidence references. For each compute scenario retain `scenario`, `workload_id`, model-by-role, calls, token fields, duplication bounds, assumptions, source level, and confidence. Do not compare token metrics across different `workload_id` values without prominently stating the mismatch.

### Harness comparison tables

`harnesses.csv` is one row per assessment and contains categorical dimensions plus headline metrics and `vsm_tldr`. It is intended for filtering and joins.

`harness-metrics.csv` is one row per metric and is the preferred group-by table. Its stable dimensions are:

```text
assessment_id, harness_id, project_name, ref, generated_at,
ai_native_class, verdict, recommended_topology,
harness_kind, execution_model, state_mode, tool_mode,
metric_id, metric_group, vsm_function, axis, scenario, workload_id,
value, max_value, unit, status, confidence, evidence_level, availability
```

Compare completeness using raw VSM function/axis rows or normalized `value / max_value`. Keep AI-native class, rubric version, evidence level, and availability in the grouping context; otherwise a sparse repository can look worse than a measured one merely because unknowns were flattened to zero.

### VSM TL;DR contract

Generate `summary.vsm_tldr` for every persisted harness assessment. If the separate `vsm-tldr` skill is available, use it; otherwise apply this same contract:

```text
<what kind of AI harness it is>; <strongest VSM functions>; <decisive missing or constrained functions>; <recommended VSM depth when material>.
```

Keep it to one neutral sentence, normally 18–45 words. Describe observed structure, not marketing intent. Mention no more than two strengths and two decisive gaps. Do not repeat percentages, the project name, or generic phrases such as “uses VSM”.

Before finalizing a persisted assessment:

1. validate required fields and unique `(metric_id, scenario, workload_id)` keys within the artifact;
2. derive tables from the JSON rather than manually copying scores;
3. upsert by `assessment_id`, making reruns idempotent;
4. sort comparison tables deterministically;
5. report the written paths to the user.

## Beautiful result format

Lead with the verdict. Make the report scannable, evidence-rich, and honest about uncertainty. Use Unicode symbols only as supplements to words.

```markdown
# VSM assessment — <project>

> **Verdict: <NO AGENTIC VSM | EXPLORE | MIN | MODULAR | MAX | HOLD>**
> <one sentence explaining why>

| Snapshot | Value |
|---|---|
| Repository / ref | `<repo>` · `<commit>` |
| Assessment mode | feasibility / status / both |
| AI-native class | NOT AI-NATIVE / AI-ASSISTED / AI-NATIVE |
| Evidence coverage | <high/medium/low> |
| Model/topology | <known values or unknown> |
| Generated | <ISO date> |
| Artifact | `<path or not persisted>` |
| VSM TL;DR | <one neutral sentence> |

## Executive scorecard

| Lens | Result | Confidence | Meaning |
|---|---:|---|---|
| Adoption readiness | <0–100 or n/a> | <...> | <...> |
| Structural completeness | <0–100 or n/a> | <...> | <...> |
| Operational maturity | <0–100 or n/a> | <...> | <...> |
| Assisted autonomy A(t) | <0–1 or n/a> | <...> | <...> |
| Avoidable token duplication | <range or unavailable> | <...> | <...> |

## VSM map

| Function | Status | E-level | Evidence | Gap |
|---|---|---:|---|---|
| S1 | green/yellow/red/unknown | E0–E4 | `<path:line>` | ... |
| S2 | ... | ... | ... | ... |
| S3 | ... | ... | ... | ... |
| S3* | ... | ... | ... | ... |
| S4 | ... | ... | ... | ... |
| S5 | ... | ... | ... | ... |

## Token-compute and duplication

| Scenario | Input | Cached | Output/reasoning | Calls | Duplicate range | Confidence |
|---|---:|---:|---:|---:|---:|---|
| Current | ... | ... | ... | ... | ... | ... |
| MIN | ... | ... | ... | ... | ... | ... |
| MODULAR | ... | ... | ... | ... | ... | ... |
| MAX | ... | ... | ... | ... | ... | ... |

Assumptions: ...
Open-data snapshot: <source, version/date>.

## Decisive evidence

- **For:** <observed reason>
- **Against:** <observed reason>
- **Unknown:** <missing evidence that could change verdict>

## Potential AI insertion points

| Candidate | Why AI | Why not deterministic | Authority | Verifier | Pilot metric |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## Recommended target

<small diagram or prose describing the chosen topology>

## Next 3 moves

1. <action> — success: <metric>; rollback: <condition>.
2. ...
3. ...

## Risks and caveats

<only material limitations>

## Evidence appendix

<claim → path/URL → E-level → date>
```

Status vocabulary:

- `green` — evidence supports correct recurring behavior;
- `yellow` — partial, stale, or only declared;
- `red` — missing or contradicted behavior that materially harms viability;
- `unknown` — insufficient access/data.

Use compact diagrams only when topology is clearer visually, for example:

```text
Environment ⇄ S4 ⇄ S5 ⇄ S3 ⇄ S1 units
                    │     ▲
                    │     └─ S3* audit (read-only)
                    └──── S2 coordination across S1
Urgent S1 evidence ─────────► S5/human (algedonic)
```

## Quality gate

Before delivering, verify:

- verdict appears first and is actionable;
- AI-native classification is explicit and precedes VSM scoring;
- ordinary services, ML models, queues, tests, and microservices are not counted as agents;
- a failed AI-native gate produces NO AGENTIC VSM, not a high readiness score;
- every score can be reconstructed from visible sub-scores;
- `unknown` is not counted as zero;
- filenames are not mistaken for operation;
- token figures identify model, workload, source, cache treatment, and confidence;
- duplication distinguishes exact, near, required, and avoidable repetition;
- current prices/specifications are cited with retrieval date if used;
- S3* independence is tested, not assumed;
- S4 is external/future intelligence, not another QA agent;
- recommended topology is the smallest adequate one;
- next actions have success and rollback conditions;
- no private content was sent outside the user's environment.

## Reference orientation

The local `literature/` directory contains the theory and provenance extracted from the source project. For external implementation patterns, useful public orientations include:

- ViableOS: https://github.com/philipp-lm/ViableOS
- VSM agent kernel: https://github.com/uint4/vsm-agent-kernel
- Nucleus VSM prompt structure: https://github.com/michaelwhitford/nucleus
- PACT VSM-enhanced orchestration: https://github.com/al34n1x/PACT-prompt
- Terminal-Bench evidence/reporting: https://github.com/harbor-framework/terminal-bench
- AgentLite single/multi-agent patterns: https://github.com/SalesforceAIResearch/AgentLite

Treat these as patterns, not authorities for project-specific facts.
