# Promotion and downstream reindex contract for experimental `S`

**Status:** experimental process contract  
**Normative effect:** none

This file defines how the self-organizing-autonomy experiment may leave `experiments/` without silently changing the released VSM Harness ecosystem.

## 1. Lifecycle states

```text
draft experiment
      ↓
stable experiment
      ↓
released Methodology adoption
```

### Draft experiment

The candidate classification distinction is still being tested. No released Methodology state changes and no canonical Index artifact changes.

### Stable experiment

The experimental contract has passed the stability gates in `SPEC.md` and is frozen enough to prepare adoption. `stable` is **not** a Methodology release and does not change the active publication state set.

The stable transition MUST trigger preparation of an explicit adoption/migration work item so downstream impact is known before release.

### Released Methodology adoption

The distinction becomes part of canonical assessment publication only through an explicit Methodology release.

If adoption requires any new or changed organizational semantics rather than only a classification distinction, the necessary Profile change must be proposed and released separately first. Skills must not redefine the Profile in order to adopt `S`.

## 2. Adoption transaction

A promotion PR must explicitly decide at least:

1. final name and notation (`S` may still be renamed);
2. whether the distinction is per-function, system-level, or both;
3. exact relationship to released `A`, `C`, and `P` semantics;
4. any allowed parent-governed composition such as a future `S(P)`;
5. minimum positive witness and required negative/counterfactual checks;
6. whether strong recursive viability is required and at what level;
7. Methodology version and artifact/schema changes;
8. whether any Profile semantic change is required;
9. migration/reassessment scope for the Index;
10. deterministic downstream view behavior.

The experiment itself does not preselect a Methodology version number or Profile release-impact value.

## 3. Profile compatibility gate

Before Methodology adoption, reviewers must answer:

> Can `S` be defined entirely as a classification/publication distinction over already-established Profile concepts such as autonomy, requisite variety, recursion, authority, and closure?

If **yes**, Profile remains unchanged and the Methodology release records the exact Profile version it requires.

If **no**, the missing organizational semantics must first be proposed in `vsm-harness-profile`, released through its own versioning/release-impact contract, and then consumed by the adopting Methodology release.

## 4. Index reindex boundary

The downstream sequence is:

```text
experimental S reaches stable
        ↓
freeze experimental classification contract
        ↓
prepare explicit Methodology adoption + migration round
        ↓
release any required Profile change (only if needed)
        ↓
release adopting Methodology
        ↓
pin migration contract in vsm-harness-index
        ↓
reassess/reindex against released Profile/Methodology pair
        ↓
regenerate derived views
        ↓
validate corpus consistency
```

Canonical Index vectors MUST NOT acquire `S` from the experimental directory alone.

## 5. Historical assessments

Adoption must preserve historical provenance.

An older assessment that recorded `A` under its original Profile/Methodology remains a valid historical artifact under that contract. A later migration may determine that the same pinned repository revision also satisfies the new distinction, but it must do so through an explicit same-ref migration/revalidation or a new-ref reassessment as appropriate.

Do not rewrite generation provenance to make an old artifact appear to have been produced under the future `S` contract.

## 6. Reindex strategy

Migration must separate:

1. **baseline validity** — does the existing function/ownership assessment remain valid under the released transition?
2. **new-state enrichment** — has evidence unique to the new distinction actually been reviewed?

A row not yet reviewed for `S` must not be silently downgraded, treated as `—`, or assumed not to qualify.

If the future Methodology needs a machine-readable representation for `S`-review coverage, it must be designed before corpus migration.

## 7. Candidate migration cohort

If released `A` remains a prerequisite, autonomous rows are the natural first review cohort. The released adoption/migration contract—not this experiment—must define the authoritative scope.

Where a same-ref canonical assessment already proves the function, owner, boundary, and closure required as prerequisites, migration should avoid re-proving unchanged baseline claims and focus on evidence unique to `S`:

- repertoire insufficiency;
- system recognition of insufficiency;
- endogenous reconstruction;
- legitimate authorization;
- integration;
- post-change absorption;
- external-constructor check.

## 8. Derived views

No canonical `FULL_S.md`, ranking field, signature state, website badge, or similar projection should exist before normative Methodology adoption and sufficient migration coverage.

Experimental comparisons may exist only under an experimental path and must use `supports-S-hypothesis`, `does-not-support-S`, or `inconclusive` rather than writing `S` into canonical assessment vectors.

After adoption, any derived view must remain a deterministic projection of canonical states/evidence, not a subjective product-quality or maturity score.

## 9. Rollback / negative result

If the experiment fails reproducibility or information-value tests, close it as a documented negative result. No canonical rollback is needed because draft/stable experimental work has no normative effect.

If problems are discovered after released adoption, repair must follow the ordinary Profile/Methodology versioning and migration contracts rather than editing the experiment to retroactively change released semantics.
