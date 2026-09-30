# VSM Skills

## I'm human

- **Web overview:** [opensiro.com](https://opensiro.com)
- **How do I contribute?** [Contribute to OpenSiro with AI](https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTE_WITH_AI.md)

You can inspect and use the assessment methodology directly without first learning the OpenSiro control structure. The contribution guide gives you a copy-paste route for handing an idea, issue, or open-ended contribution to an AI agent.

## I'm AI

Treat this README as the public handoff surface, then continue with the current shared [`START_HERE.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md). For already tracked work use the shared [`TODO.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md); for new, unclassified, cross-repository, or authority-sensitive work use [`CONTRIBUTOR_START.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md).

If the bootstrap resolves Methodology or skill work to this repository, repository-local assessment procedure, skill contracts, references, tooling, validation, evidence, and acceptance remain authoritative here.

VSM Skills applies the [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) without redefining it.

The Profile answers **what the organizational concepts mean**. This repository owns **assessment specifications**: procedures that map evidence about a declared system-in-focus into reviewable conclusions under a pinned Profile dependency.

The currently released general stack is:

```text
VSM Harness Profile version
        ↓
VSM Harness Methodology version
        ↓
vsm-harness-index @ exact Git revision
        ↓
TLDR.md / RANKINGS.md generated views
```

The exact Index Git revision identifies the concrete general-assessment corpus, schema/implementation state, signatures, and generated views.

## Assessment specifications are extensible

`assess-vsm-harness` is the canonical **general VSM harness assessment** used by `opensiro/vsm-harness-index`. It is not intended to prevent additional assessment specifications.

This repository may host or accept additional assessment skills that use the same Profile while asking a more specific question, for example a domain-, purpose-, evidence-, or deployment-specific assessment. Such a skill may define additional:

- admission requirements;
- declared operating purpose and system boundary;
- evidence thresholds;
- capability requirements;
- required or permitted ownership arrangements;
- result schema and downstream index contract.

Those additions do not redefine Profile-owned S1-S5 semantics. If an assessment requires a genuinely new organizational concept, the semantic change belongs in `vsm-harness-profile` first.

Community or experimental assessment specifications may coexist with the canonical general skill without becoming part of the released general Methodology merely by living in this repository. Their authority, versioning, and downstream corpus must be explicit.

A target system also does not need to claim VSM conformance before it can be assessed. The general skill may map **emergent VSM functions** in an arbitrary harness or in another formally specified system. Conversely, when a system intentionally claims to realize the Profile, the same assessment layer can provide evidence about whether that claimed realization is actually present at the declared boundary.

## Profile dependency and consumer compatibility

Each assessment specification owns its compatibility with Profile versions. Profile SemVer identifies changes in the normative organizational model; an assessment skill decides whether and how those changes affect its own evidence contract, classification procedure, or downstream migration.

Therefore:

```text
Profile version change
        ≠ universal reassessment order
```

The current released general Methodology continues to preserve its historical Profile dependency and frozen provenance. Existing compatibility metadata remains valid for those historical contracts. New domain-specific or community assessments must not assume that the general Index's reassessment policy is automatically theirs.

See [VERSIONING.md](VERSIONING.md) for the released Methodology boundary and compatibility rules.

## General assessment workflows

The released repository separates two workflows inside the same general Methodology release:

```text
one repository @ pinned revision
        ↓
assess-vsm-harness
        ↓
standalone general assessment

ordered standalone assessments
        ↓
SYNTHESIS.md
        ↓
cohort-relative signatures
        ↓
deterministic ranking projection
```

## Skill catalog

| Skill | Purpose |
| --- | --- |
| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Produce a detailed evidence-backed **general** repository assessment with out-of-the-box autonomy states. |

The general assessment skill owns repository evidence collection and classification. It does not generate cohort-relative signatures or rankings.

[SYNTHESIS.md](SYNTHESIS.md) defines the ordered comparison procedure and deterministic ranking projection consumed by the **general** `vsm-harness-index`. Assessment, synthesis, ranking, and their validation contract share the single released general Methodology version in `skills/assess-vsm-harness/VERSION`; they do not have independent semantic versions.

`TLDR.md` and `RANKINGS.md` are generated general-Index views, not separately versioned products.

## Assessment contract

The general assessment workflow first maps the organizational function and only then classifies who owns the relevant decision right. This prevents feature-name shortcuts such as delegation→S2, manager→S3, verifier→S3*, learning→S4, or prompt→S5.

The detailed artifact format lives in [assessment-format.md](skills/assess-vsm-harness/references/assessment-format.md), and the local `A/C/P/—/?` notation lives in [autonomy-states.md](skills/assess-vsm-harness/references/autonomy-states.md).

These publication states belong to this Methodology. They are not part of the Profile and other assessment specifications are not required to expose the same result surface unless they explicitly adopt it.

## Methodology experiments

Non-normative experiments for possible future classification/publication distinctions live under [`experiments/`](experiments/README.md).

These experiments do not change the released Methodology or canonical general Index assessments. A distinction becomes publishable only through an explicit Methodology release and downstream migration contract. If an experiment requires new organizational semantics rather than only a classification distinction, the semantic change must be made separately in `vsm-harness-profile` first.

## Profile tracking

The general assessment skill packages a generated `references/profile/PROFILE.md` snapshot for portability. The source remains [`vsm-harness-profile/PROFILE.md`](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md).

```bash
python scripts/sync_profile.py
python scripts/sync_profile.py --check
python scripts/validate_skills.py
```

The bundled snapshot is part of the Methodology's recorded dependency, not an implicit alias for the latest Profile `main`. CI resolves the Profile version declared by `SKILL.md`, checks out the matching immutable `v<version>` Profile tag, and validates the snapshot against that release.

Do not edit the generated snapshot by hand outside an explicit synchronized Methodology dependency update.

## Consumers

[vsm-harness-index](https://github.com/opensiro/vsm-harness-index) stores the published **general** assessment corpus and materializes its TLDR signatures and autonomy rankings under the released general Methodology. An exact Index Git revision is the identity of a particular corpus/output state.

Future domain-specific assessment specifications may have separate indexes. They may consume the same Profile and may reuse public identity/provenance facts, but they own their additional domain contract and conclusions. A domain-specific index must not silently overwrite the general Index assessment for the same upstream system.

## Contributing and organization

Contribute assessment procedures, skills, references, synchronization/provenance tooling, validators, and repository-local Methodology maintenance here.

The shared bootstrap/current-work/routing links are kept near the top of this README so they remain directly discoverable without duplicating Organization policy here. `TODO.md` owns current selection/order only; this repository remains authoritative for Methodology/skill task scope, evidence and acceptance.

For questions or proposals about **the organization that coordinates the OpenSiro VSM Harness OSS repositories** — contributor roles, authority boundaries, cross-repository control, escalation, milestone sequencing, or shared contribution workflow — use [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization). Organization-wide policy should not be duplicated into this Methodology repository.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The generated profile snapshot at `skills/assess-vsm-harness/references/profile/PROFILE.md` is licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt), matching its source repository.
