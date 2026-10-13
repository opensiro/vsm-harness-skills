# Positive-evidence calibration — frozen comparison sample (2026-10-13)

**Purpose:** Reproduce cohort selection and source provenance behind R1–R10, not certify 23 independently reassessed harnesses or estimate population error.

**Frozen Index cut:** [`main@80fc101edd018461ab3b14a5b707af6977cda275`](https://github.com/opensiro/vsm-harness-index/tree/80fc101edd018461ab3b14a5b707af6977cda275), last admission 2026-10-12. The recent cohort is the 20 most recent distinct *canonical admissions*, in merged-admission-PR order at this cut (not proposed assessment PRs or directory order). A separate targeted workbook cohort contains 12 distinct systems, 9 overlapping the recent cohort, and thus 23 in union. This comparison was context-exposed/non-blind.

## Most recent 20 canonical admissions

| Order | Harness and accepted assessment at frozen Index cut | Admission PR | Pinned upstream `review_ref` | Original Methodology |
| ---: | --- | --- | --- | --- |
| 1 | [AtomCode](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/atomcode.md) | [#1515](https://github.com/opensiro/vsm-harness-index/pull/1515) | `152b2cc132dda9b177c3a030e21cfacd95494ea3` | `0.3.7` |
| 2 | [KairoCode](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/kairocode.md) | [#1513](https://github.com/opensiro/vsm-harness-index/pull/1513) | `018c74035de1354f69a92eda626ddbb210fbebcc` | `0.3.7` |
| 3 | [CXAgent](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/cxagent.md) | [#1511](https://github.com/opensiro/vsm-harness-index/pull/1511) | `e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1` | `0.3.7` |
| 4 | [Xoder](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/xoder.md) | [#1509](https://github.com/opensiro/vsm-harness-index/pull/1509) | `5a13d1cd4471cf95bb89befe2ac7634d93a610a7` | `0.3.7` |
| 5 | [Orchestra](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/orchestra.md) | [#1508](https://github.com/opensiro/vsm-harness-index/pull/1508) | `72d48a93210c3cf12da91f7e693a4a6aae0e40f2` | `0.3.7` |
| 6 | [Agent Harness](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/agent-harness.md) | [#1505](https://github.com/opensiro/vsm-harness-index/pull/1505) | `0c30ff12476898543246912a3d49d653ae86b874` | `0.3.7` |
| 7 | [Agent-OS (kai-linux)](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/kai-linux-agent-os.md) | [#1503](https://github.com/opensiro/vsm-harness-index/pull/1503) | `d7330ebc5e117f06df1fdf23118af8da2c327507` | `0.3.7` |
| 8 | [Capstan](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/capstan.md) | [#1501](https://github.com/opensiro/vsm-harness-index/pull/1501) | `60f284fc94ce96d05e72b52d2ffe55b4096b0177` | `0.3.7` |
| 9 | [Agent OS (earthwalker17)](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/earthwalker17-agent-os.md) | [#1500](https://github.com/opensiro/vsm-harness-index/pull/1500) | `59833d3f436bd1fd842860af2aa1c081d4b20363` | `0.3.7` |
| 10 | [mini-swe-agent](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/mini-swe-agent.md) | [#1497](https://github.com/opensiro/vsm-harness-index/pull/1497) | `04d809ceab9df28f9adaed044884180159172930` | `0.3.7` |
| 11 | [Open SWE](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/open-swe.md) | [#1494](https://github.com/opensiro/vsm-harness-index/pull/1494) | `d0e0fe3ef76f2d84f49ac222f5274be6e60eb7b5` | `0.3.7` |
| 12 | [DeepCode](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/deepcode.md) | [#1492](https://github.com/opensiro/vsm-harness-index/pull/1492) | `2b223c13fd36a574157751e3812c1cdebd8921c6` | `0.3.7` |
| 13 | [Devika](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/devika.md) | [#1490](https://github.com/opensiro/vsm-harness-index/pull/1490) | `80bb343cbe4a4e5f5a0ba08d2524920139baceb6` | `0.3.7` |
| 14 | [Claw Code](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/claw-code.md) | [#1488](https://github.com/opensiro/vsm-harness-index/pull/1488) | `08106b0c3771ef5b4a5aa176acccd460e88b7325` | `0.3.6` |
| 15 | [Swarms](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/swarms.md) | [#1487](https://github.com/opensiro/vsm-harness-index/pull/1487) | `3009364a7e44dc3e55fec238b56b3a4fa6949a05` | `0.3.7` |
| 16 | [ZCode](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/zcode.md) | [#1485](https://github.com/opensiro/vsm-harness-index/pull/1485) | `872ad960de7ec172591f7e1952f7849229f94521` | `0.3.7` |
| 17 | [Grok Build](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/grok-build.md) | [#1483](https://github.com/opensiro/vsm-harness-index/pull/1483) | `4247f661689354b831191f11eeeac8424993fe3d` | `0.3.7` |
| 18 | [AgentScope 2.0](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/agentscope-2-0.md) | [#1481](https://github.com/opensiro/vsm-harness-index/pull/1481) | `5ff52f877de12d66a30d55af279dd4f42b1590f3` | `0.3.7` |
| 19 | [ShelraCode](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/shelracode.md) | [#1479](https://github.com/opensiro/vsm-harness-index/pull/1479) | `45f87d1f7f71d5f6bba07405167893fa74d7c2a4` | `0.3.7` |
| 20 | [OpenHuman](https://github.com/opensiro/vsm-harness-index/blob/80fc101edd018461ab3b14a5b707af6977cda275/assessments/openhuman.md) | [#1478](https://github.com/opensiro/vsm-harness-index/pull/1478) | `eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d` | `0.3.7` |

## R1–R10 targeted cohort (12 distinct systems)

| Harness id | Contrast cases | Within recent-20? |
| --- | --- | --- |
| `atomcode` | R1/R6 | yes |
| `openhuman` | R2 | yes |
| `swarms` | R3 | yes |
| `suisuicode` | R4/R9 | no |
| `rum` | R5/R9 | no |
| `bb` | R6 | no |
| `kairocode` | R7 | yes |
| `capstan` | R7/R8 | yes |
| `xoder` | R8 | yes |
| `claw-code` | R9 | yes |
| `mini-swe-agent` | R10 | yes |
| `agentscope-2-0` | R10 | yes |

Targeted-only cases are SuisuiCode, Rum and bb. bb's sampled Index artifact was **proposed**, not canonically admitted. Original historical frozen source revision and Methodology for the targeted systems are in the R1–R10 guide; unresolved reviewer disputes are not gold labels.

## Limits of inference

- These links substantiate a historical cohort and frozen review refs, **not** the correctness of its assessment vectors.
- The illustrative sample is nonrandom and intentionally enriched with debated examples; no empirical rate of systematic misclassification follows.
- The research did not carry out 23 fresh blind or whole-harness provider-backed evaluations; a pin and a documentation test do not prove the semantics of every claim.
- No source re-pin, Index vector change, automatic reassessment, threshold change or frozen research-protocol amendment is authorized by this manifest.
