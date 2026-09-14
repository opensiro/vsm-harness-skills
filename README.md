# VSM Skills

VSM Skills contains portable Agent Skills that apply the [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) without redefining it.

## Skill catalog

| Skill | Purpose |
| --- | --- |
| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Reconstruct an evidence-backed categorical VSM/OSM Autonomy TL;DR at a pinned revision. |

One assessment skill is intentional. Audit, recursion, variety, escalation, topology, token cost, and TL;DR are conditional parts of the same evidence chain rather than independent entrypoints.

## Profile tracking

The skill packages a generated `references/profile/PROFILE.md` snapshot for portability. The source remains [`vsm-harness-profile/PROFILE.md`](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md).

```bash
python scripts/sync_profile.py
python scripts/sync_profile.py --check
python scripts/validate_skills.py
```

CI checks the profile repository owned by the same GitHub organization and rejects drift. Do not edit the generated snapshot by hand.

## Consumers

[vsm-harness-index](https://github.com/opensiro/vsm-harness-index) uses `assess-vsm-harness` to reconstruct categorical fingerprints. The index owns `data/catalog.psv` and generated presentation; the skill owns the evidence and classification procedure.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The generated profile snapshot at `skills/assess-vsm-harness/references/profile/PROFILE.md` is licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt), matching its source repository.
