"""Regression tests for the independently versioned experimental build skill."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "skills" / "build-harness-cognee-first"
GENERAL = ROOT / "skills" / "assess-vsm-harness"


class ExperimentalBuildSkillTests(unittest.TestCase):
    def test_explicit_experimental_identity_and_independent_version(self):
        text = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        version = (BUILD / "VERSION").read_text(encoding="utf-8").strip()
        self.assertIn("name: build-harness-cognee-first", text.split("---", 2)[1])
        self.assertIn("status: experimental", text.split("---", 2)[1])
        self.assertEqual(version, "0.1.0")
        self.assertIn(f"**Skill version:** {version}", text)
        self.assertNotIn("**Methodology version:**", text)
        self.assertEqual((GENERAL / "VERSION").read_text().strip(), "0.3.8")

    def test_gate_and_evidence_contract_is_explicit(self):
        text = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        for requirement in (
            "Gate 1", "Gate 2", "C1", "C2", "C3", "C4",
            "process_status", "build_status", "evaluation_level",
            "model_quality_claim", "not a release of the canonical",
            "references/run-contract.md",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text)

    def test_documents_have_no_dangling_relative_links(self):
        for path in sorted(BUILD.rglob("*.md")):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "#")):
                    continue
                with self.subTest(path=str(path), target=target):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).is_file())


if __name__ == "__main__":
    unittest.main()
