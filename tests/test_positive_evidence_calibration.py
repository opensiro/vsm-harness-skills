"""Documentation-regression checks for proposed, non-normative positive calibration.

These validate link/fixture integrity only, not VSM semantics or canonical grades.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "skills/assess-vsm-harness/references/positive-evidence-calibration.md"
SKILL = ROOT / "skills/assess-vsm-harness/SKILL.md"
SAMPLE = ROOT / "skills/assess-vsm-harness/references/positive-evidence-sample-2026-10-13.md"


class PositiveEvidenceCalibrationTests(unittest.TestCase):
    def test_skill_links_informative_guide(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("[positive-evidence-calibration.md](references/positive-evidence-calibration.md)", text)

    def test_ten_distinct_non_gold_contrast_cases(self):
        guide = GUIDE.read_text(encoding="utf-8")
        ids = re.findall(r"^### (R\d+) — ", guide, flags=re.MULTILINE)
        self.assertEqual(ids, [f"R{i}" for i in range(1, 11)])
        sections = re.split(r"^### R\d+ — ", guide, flags=re.MULTILINE)[1:]
        self.assertEqual(len(sections), 10)
        for section in sections:
            self.assertIn("**Expected evidence decision:**", section)
            self.assertIn("**Counter-check:**", section)
        self.assertIn("not a", guide.lower())
        self.assertIn("not accepted state labels or gold grading fixtures", guide)

    def test_frozen_sample_manifest_is_reproducible(self):
        sample = SAMPLE.read_text(encoding="utf-8")
        recent = sample.split("## Most recent 20 canonical admissions", 1)[1].split("## R1–R10 targeted cohort", 1)[0]
        targeted = sample.split("## R1–R10 targeted cohort", 1)[1].split("## Limits of inference", 1)[0]
        rows = [line for line in recent.splitlines() if line.startswith("| ") and "/assessments/" in line]
        self.assertEqual(len(rows), 20)
        self.assertEqual([int(line.split("|")[1].strip()) for line in rows], list(range(1, 21)))
        ids = re.findall(r"/assessments/([a-z0-9-]+)\.md", "\n".join(rows))
        self.assertEqual(len(set(ids)), 20)
        targets = re.findall(r"^\| `([a-z0-9-]+)` \| R", targeted, flags=re.MULTILINE)
        self.assertEqual(len(set(targets)), 12)
        self.assertEqual(len(set(ids) | set(targets)), 23)
        self.assertIn("80fc101edd018461ab3b14a5b707af6977cda275", sample)
        for line in rows:
            self.assertRegex(line, r"`[0-9a-f]{40}`")

    def test_contrast_wiring_anchors_are_specific(self):
        guide = GUIDE.read_text(encoding="utf-8")
        for path in ("src/kairocode/cli.py", "src/kairocode/tui/app.py",
                     "src/kairocode/team/tools/__init__.py",
                     "src/xoder_coding/data/skills/create-xoder-extension/SKILL.md",
                     "src/xoder_coding/extensions/runtime.py"):
            self.assertIn(path, guide)
        self.assertIn("user's reason or authorization", guide)
        self.assertIn("agent's discretionary choice", guide)

    def test_immutable_upstream_sources_are_embedded(self):
        guide = GUIDE.read_text(encoding="utf-8")
        expected = {
            "AtomCode": "152b2cc132dda9b177c3a030e21cfacd95494ea3",
            "OpenHuman": "eb4fdc0f4f4a036d8ab7c12bd52f16128e4a6b5d",
            "Swarms": "3009364a7e44dc3e55fec238b56b3a4fa6949a05",
            "SuisuiCode": "c9017b0613b22151325a5904a521aefe4c62abbc",
            "Rum": "9c00bdb35f2a55959d6e56bd0d27b9573aac6fdd",
            "bb": "c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf",
            "KairoCode": "018c74035de1354f69a92eda626ddbb210fbebcc",
            "Capstan": "60f284fc94ce96d05e72b52d2ffe55b4096b0177",
            "Xoder": "5a13d1cd4471cf95bb89befe2ac7634d93a610a7",
            "Claw Code": "08106b0c3771ef5b4a5aa176acccd460e88b7325",
            "mini-swe-agent": "04d809ceab9df28f9adaed044884180159172930",
            "AgentScope": "5ff52f877de12d66a30d55af279dd4f42b1590f3",
        }
        for name, sha in expected.items():
            with self.subTest(harness=name):
                self.assertIn(sha, guide)
                self.assertRegex(sha, r"^[0-9a-f]{40}$")

    def test_no_canonical_adjudication_claim(self):
        guide = GUIDE.read_text(encoding="utf-8")
        for phrase in (
            "informative positive-evidence calibration",
            "not an executable semantic oracle",
            "proposed",
            "Profile `0.2.4`",
            "Methodology `0.3.7`",
            "not automatically first-party S3*",
        ):
            self.assertIn(phrase, guide)


if __name__ == "__main__":
    unittest.main()
