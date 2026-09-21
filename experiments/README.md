# Methodology experiments

This directory contains **non-normative experiments** for possible future VSM Harness Methodology classification/publication semantics.

Nothing under `experiments/` changes the released Methodology, the active autonomy-state notation, the bundled Profile snapshot, or any canonical Index assessment. Consumers MUST NOT treat an experimental state, symbol, fixture, or projection as part of the active Methodology until it is promoted through an explicit Methodology release.

The released assessment/classification source remains `skills/assess-vsm-harness/` and, for autonomy publication states, `skills/assess-vsm-harness/references/autonomy-states.md`.

## Ownership boundary

The ecosystem keeps these responsibilities separate:

```text
vsm-harness-profile
  owns VSM organizational semantics
        ↓
vsm-harness-skills
  owns evidence/classification procedure and publication notation
        ↓
vsm-harness-index
  owns canonical evidence-backed assessment corpus and derived views
```

An experiment belongs here when it primarily changes **how established VSM functions are classified or published**, rather than redefining what the VSM functions themselves mean.

If an experiment exposes a genuine gap in Profile semantics, that semantic change must be proposed separately in `vsm-harness-profile`; the experiment directory must not silently redefine the Profile.

## Lifecycle

```text
issue / hypothesis
        ↓
experimental draft
        ↓
fixture corpus + counterexamples
        ↓
independent reproducibility review
        ↓
stable experimental specification
        ↓
explicit Methodology adoption release
        ↓
Index migration / reassessment / reindex
```

`stable` means the experimental classification contract is frozen and reproducible enough to prepare adoption. It does **not** extend the released state set.

## Promotion rule

Promotion MUST NOT:

- rewrite historical assessment provenance;
- silently reinterpret existing `A/C/P/—/?` findings;
- mutate canonical Index vectors from the experiment;
- make downstream consumers infer migration scope from prose alone;
- redefine Profile semantics from this repository.

When an experiment reaches `stable`, the next step is an explicit Methodology adoption transaction. If adoption also requires Profile changes, those must be released through the Profile's own versioning/release-impact contract before the new Methodology is released.

Canonical Index migration begins only against a released adopting Profile/Methodology pair.

## Current experiments

- [`self-organizing-autonomy/`](self-organizing-autonomy/) — candidate `S` publication state for endogenous reconstruction of organizational/regulatory repertoire; Methodology work item: [#22](https://github.com/opensiro/vsm-harness-skills/issues/22); conceptual source discussion: [`vsm-harness-profile#13`](https://github.com/opensiro/vsm-harness-profile/issues/13).
