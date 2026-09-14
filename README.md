# VSM Skills

VSM Skills applies the [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) without redefining it.

The repository separates two different workflows:

```text
one repository @ pinned revision
        ↓
assess-vsm-harness
        ↓
standalone assessment

ordered standalone assessments
        ↓
SYNTHESIS.md procedure
        ↓
cohort-relative signatures
```

## Skill catalog

| Skill | Purpose |
| --- | --- |
| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Produce a detailed evidence-backed repository assessment with out-of-the-box autonomy states. |

The assessment skill owns repository evidence collection and classification. It does not own cohort-relative signatures or rankings.

[SYNTHESIS.md](SYNTHESIS.md) defines the separate ordered comparison procedure used by `vsm-harness-index`. Ranking remains a deterministic projection of the assessment states rather than an LLM score.

## Assessment contract

The assessment workflow first maps the organizational function and only then classifies who owns the relevant decision right. This prevents feature-name shortcuts such as delegation→S2, manager→S3, verifier→S3*, learning→S4, or prompt→S5.

The detailed artifact format lives in [assessment-format.md](skills/assess-vsm-harness/references/assessment-format.md), and the local `A/C/P/—/?` notation lives in [autonomy-states.md](skills/assess-vsm-harness/references/autonomy-states.md).

## Profile tracking

The assessment skill packages a generated `references/profile/PROFILE.md` snapshot for portability. The source remains [`vsm-harness-profile/PROFILE.md`](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md).

```bash
python scripts/sync_profile.py
python scripts/sync_profile.py --check
python scripts/validate_skills.py
```

CI checks the profile repository owned by the same GitHub organization and rejects drift. Do not edit the generated snapshot by hand outside a synchronized profile update.

## Consumer

[vsm-harness-index](https://github.com/opensiro/vsm-harness-index) stores the published assessment corpus and derives its TLDR signatures and autonomy rankings from those assessments.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The generated profile snapshot at `skills/assess-vsm-harness/references/profile/PROFILE.md` is licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt), matching its source repository.
