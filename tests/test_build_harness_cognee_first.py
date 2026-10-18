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
        # Read the canonical release line dynamically: this experimental skill
        # must not block a future general Methodology release.
        general_version = (GENERAL / "VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(general_version, r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
        general_skill = (GENERAL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f"**Methodology version:** {general_version}", general_skill)

    def test_gate_and_evidence_contract_is_explicit(self):
        text = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        for requirement in (
            "Gate 1", "Gate 2", "C1", "C2", "C3", "C4",
            "process_status", "build_status", "evaluation_level",
            "model_quality_claim", "verification_level",
            "A successful Cognee-first construction trace does not depend on running",
            "not a release of the canonical",
            "references/run-contract.md",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text)

    def test_gameplay_or_model_run_not_mandatory(self):
        skill = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        contract = (BUILD / "references/run-contract.md").read_text(encoding="utf-8")
        self.assertIn("not a mandatory C4 gate", skill)
        self.assertIn("acceptable final states", contract)
        self.assertIn("source-to-code mapping", skill)

    def test_preimport_c1_and_real_connector_contract(self):
        skill = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        run_contract = (BUILD / "references/run-contract.md").read_text(encoding="utf-8")
        trace = (BUILD / "references/decision-trace.md").read_text(encoding="utf-8")
        for text in (skill, run_contract, trace):
            with self.subTest(document=text.splitlines()[0]):
                self.assertIn("connector import", text)
                self.assertIn("native Cognee", text)
                self.assertIn("C1", text)
        self.assertIn("before the first Cognee import", skill)
        self.assertIn("pinned OpenSiro Cognee connector", skill)
        self.assertIn("direct-SDK-only import", run_contract)
        self.assertIn("first connector import/index build", trace)

    def test_no_adaptation_still_requires_constructed_harness(self):
        skill = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        contract = (BUILD / "references/run-contract.md").read_text(encoding="utf-8")
        trace = (BUILD / "references/decision-trace.md").read_text(encoding="utf-8")
        self.assertIn("NO_ADAPTATION still requires a produced", skill)
        self.assertIn("no constructed harness", contract)
        self.assertIn("NO_ADAPTATION versus no built harness", trace)

    def test_discovery_contribution_is_explicit_and_bounded(self):
        skill = (BUILD / "SKILL.md").read_text(encoding="utf-8")
        contract = (BUILD / "references/run-contract.md").read_text(encoding="utf-8")
        trace = (BUILD / "references/decision-trace.md").read_text(encoding="utf-8")
        for text in (skill, contract, trace):
            with self.subTest(document=text.splitlines()[0]):
                for value in ("discovery_contribution", "DIRECT", "CORROBORATIVE",
                              "NONE", "INDETERMINATE"):
                    self.assertIn(value, text)
        self.assertIn("Only DIRECT", skill)
        self.assertIn("positive Cognee architecture-discovery result", trace)

    def test_documents_have_no_dangling_relative_links(self):
        for path in sorted(BUILD.rglob("*.md")):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "#")):
                    continue
                with self.subTest(path=str(path), target=target):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).is_file())


if __name__ == "__main__":
    unittest.main()
