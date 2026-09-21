# VSM Skills

VSM Skills applies the [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) without redefining it.

The ecosystem deliberately keeps only two semantic release lines:

```text
VSM Harness Profile version
        ↓
VSM Harness Methodology version
        ↓
vsm-harness-index @ exact Git revision
        ↓
TLDR.md / RANKINGS.md generated views
```

The Profile answers **what the organizational concepts mean**. This repository's Methodology answers **how repository evidence becomes assessments and corpus views**. The exact Index Git revision identifies the concrete corpus, schema/implementation state, signatures, and generated views.

See [VERSIONING.md](VERSIONING.md) for the release-boundary contract.

The repository separates two workflows inside the same Methodology release:

```text
one repository @ pinned revision
        ↓
assess-vsm-harness
        ↓
standalone assessment

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
| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Produce a detailed evidence-backed repository assessment with out-of-the-box autonomy states. |

The assessment skill owns repository evidence collection and classification. It does not generate cohort-relative signatures or rankings.

[SYNTHESIS.md](SYNTHESIS.md) defines the ordered comparison procedure and deterministic ranking projection consumed by `vsm-harness-index`. Assessment, synthesis, ranking, and their validation contract share the single Methodology version in `skills/assess-vsm-harness/VERSION`; they do not have independent semantic versions.

`TLDR.md` and `RANKINGS.md` are generated Index views, not separately versioned products.

## Assessment contract

The assessment workflow first maps the organizational function and only then classifies who owns the relevant decision right. This prevents feature-name shortcuts such as delegation→S2, manager→S3, verifier→S3*, learning→S4, or prompt→S5.

The detailed artifact format lives in [assessment-format.md](skills/assess-vsm-harness/references/assessment-format.md), and the local `A/C/P/—/?` notation lives in [autonomy-states.md](skills/assess-vsm-harness/references/autonomy-states.md).

## Methodology experiments

Non-normative experiments for possible future classification/publication distinctions live under [`experiments/`](experiments/README.md).

These experiments do not change the released Methodology or canonical Index assessments. A distinction becomes publishable only through an explicit Methodology release and downstream migration contract. If an experiment requires new organizational semantics rather than only a classification distinction, the semantic change must be made separately in `vsm-harness-profile` first.

## Profile tracking

The assessment skill packages a generated `references/profile/PROFILE.md` snapshot for portability. The source remains [`vsm-harness-profile/PROFILE.md`](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md).

```bash
python scripts/sync_profile.py
python scripts/sync_profile.py --check
python scripts/validate_skills.py
```

CI checks the profile repository owned by the same GitHub organization and rejects drift. Do not edit the generated snapshot by hand outside a synchronized profile update.

## Consumer

[vsm-harness-index](https://github.com/opensiro/vsm-harness-index) stores the published assessment corpus and materializes its TLDR signatures and autonomy rankings under the Methodology. An exact Index Git revision is the identity of a particular corpus/output state; the Index does not need a second semantic release line merely because its cohort or generated files changed.

## Contributing and organization

Contribute assessment procedure, skills, references, synchronization/provenance tooling, validators, and repository-local Methodology maintenance here.

For questions or proposals about **the organization that coordinates the OpenSiro VSM Harness OSS repositories** — contributor roles, authority boundaries, cross-repository control, escalation, milestone sequencing, or shared contribution workflow — use [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization). Organization-wide policy should not be duplicated into this Methodology repository.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The generated profile snapshot at `skills/assess-vsm-harness/references/profile/PROFILE.md` is licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt), matching its source repository.
