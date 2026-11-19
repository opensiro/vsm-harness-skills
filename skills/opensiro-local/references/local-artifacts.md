# OpenSiro Local — local artifact handoff (experimental)

This is a **lightweight local adaptation**, not the public Upstream `proposal-gate` receipt schema. Follow the current public [Capability Roadmap](https://github.com/opensiro/upstream/blob/main/docs/CAPABILITY_ROADMAP.md) for research semantics and use the canonical [assessment format](../../assess-vsm-harness/references/assessment-format.md) for the standalone initial/reassessment artifact. Do not claim that `scripts/validate_capability_roadmap.py` validates this local layout.

## Authorized local layout

```text
<project>/
└── .opensiro/
    ├── assessments/
    │   ├── <run-id>.md
    │   └── <later-run-id>.md
    └── roadmap/
        └── <case-id>/
            ├── roadmap.md
            ├── issue.md
            └── constructor-sufficiency.md
```

Without explicit local-file-write permission, keep drafts in the conversation instead. Do not treat this directory as ignored, encrypted, or private just because it starts with a dot.

## One source of truth — roadmap.md

Record:

- `mode: LOCAL_UNREVIEWED`, case ID, observation date, source identity, exact Git HEAD and dirty state (or snapshot manifest/hash and limitation);
- local assessment path and exact source/procedure/Profile/Methodology pins; no accepted Index claim;
- system-in-focus, supported operating mode and exclusions;
- **one six-function census**: S1/S2/S3/S3*/S4/S5 with local assessed state, current source owner/closure, evidence, proposed C or no-target disposition, priority and uncertainty;
- Track A/Track B with source-native coverage, closest simpler alternative, missing full C chain and falsifier;
- selected `Sx=[local assessed] → Sx=C` or `NO_QUALIFIED_C_TARGET`, P0/P1/P2, dependencies, legal/authority boundaries and test plan;
- independent `proposal_gate: GO|NO_GO|BLOCKED`, `research_disposition: DECISION_READY|NEEDS_EVIDENCE|NO_USEFUL_CHANGE`, `validation: NOT_RUN|RUN|PASS|FAIL`, `cost_evidence: NOT_MEASURED|MEASURED`;
- `persistence: PREPARED|PERSISTED_LOCAL`, implementation status, actual test references, remaining blocker and next permitted action.

These strings are *local display fields*, not new Index or Upstream schema enums. A proposal GO is not a product implementation or validated outcome.

## Human — issue.md

Render one short explanation of who the system serves, what exists now, an **exactly once** six-row historical/local-current/priority view derived from `roadmap.md`, the selected change or justified no-target, expected owner benefit, simplest alternative, proposal/research/validation status and next action. Link to `roadmap.md` and `constructor-sufficiency.md`; do not independently maintain another grade source.

## AI/developer — constructor-sufficiency.md

Link to `roadmap.md` and `issue.md`. Document the pinned first-party source and mode, disturbance, decisive owner/right, possible decisions, enforced first-party effects, feedback into later operations, legal/parent authority, source-native Track A/B mapping, minimum missing C-sufficiency implementation and native positive/negative/compatibility tests. Consider competing architectures. No fixed number of ports/tests or a copied Paperclip example. Mark unexecuted hypotheses `NOT_RUN`.

## Implementation and validation provenance

When independently authorized and actually executed, link the change commit/diff, native command/test output, baseline, actual result and reassessment to the same case. Keep old assessment files intact; do not silently relabel their observed source as current. Re-run independent local assessment for a new claim of changed function ownership.

## Publication

No local document, commit, test result or GO is permission to contact third parties. If an owner opts into a public Upstream contribution, apply its current Index admission and exact publication gates separately; these local files can be supporting evidence only.
