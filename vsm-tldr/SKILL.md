---
name: vsm-tldr
description: Summarize an AI harness relative to the Viable System Model in one compact, comparison-ready sentence. Use when filling a VSM harness table, assessment artifact, catalog, or short architecture description; do not perform a full VSM assessment when evidence or scores are absent.
---

# VSM TL;DR

Write one neutral sentence describing what an AI harness is relative to VSM.

Use evidence already present in a VSM assessment. Do not infer missing functions from product marketing or run a new repository audit unless the user also asks for one.

## Required shape

```text
<harness type and operating shape>; <strongest VSM functions>; <decisive gaps or constraints>; <recommended depth when material>.
```

Apply these rules:

- normally use 18–45 words and exactly one sentence;
- name the operating shape, such as single-agent loop, manager–worker framework, graph orchestrator, eval harness, or persistent multi-agent runtime;
- mention at most two demonstrated strengths and two decisive gaps;
- use S1–S5 labels only when they make the sentence shorter or more precise;
- distinguish independent S3* from ordinary tests and S4 from internal QA;
- describe `unknown` as unverified, not absent;
- omit scores, percentages, repository name, praise, roadmap language, and generic phrases such as “implements VSM”;
- end with `MIN`, `MODULAR`, or `MAX` only when the assessment makes that recommendation material.

Examples:

```text
Lightweight manager–worker LLM harness with strong S1 and basic S2; resource control and independent audit are not established, so MODULAR is appropriate.

Single-agent tool-use loop with observable S1; coordination pressure and the need for independent S3* are unproven, so MIN is sufficient.
```

## Table integration

When an assessment artifact is being persisted, write the sentence to `summary.vsm_tldr` and the `vsm_tldr` column of `harnesses.csv`. Treat the JSON field as authoritative; regenerate the table instead of editing the CSV prose independently.

Return only the sentence when the user asks solely for a TL;DR. When filling a table, preserve the table's existing columns and identifiers.
