from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "assess-vsm-harness"


class MethodologyContractTests(unittest.TestCase):
    def text(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_version_surfaces_match_methodology_version(self):
        version = (SKILL / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(version, "0.3.1")
        for relative in (
            "skills/assess-vsm-harness/SKILL.md",
            "skills/assess-vsm-harness/references/autonomy-states.md",
            "skills/assess-vsm-harness/references/assessment-format.md",
            "SYNTHESIS.md",
        ):
            self.assertIn(f"**Methodology version:** {version}", self.text(relative), relative)
        self.assertIn(f"Methodology: {version}", self.text("VERSIONING.md"))
        self.assertIn(f"## {version} —", self.text("skills/assess-vsm-harness/CHANGELOG.md"))

    def test_parent_mode_publication_boundary_is_explicit(self):
        text = self.text("skills/assess-vsm-harness/references/autonomy-states.md")
        self.assertIn("**S3, S4, or S5 only.**", text)
        self.assertIn("S1 and S2 remain agent-harness operational/coordination states", text)
        self.assertIn("Methodology does not publish `P`, `A(P)`, or `C(P)` for S1 or S2", text)
        self.assertIn("S5 is the canonical parent-governed case", text)
        self.assertIn("S3 and S4 are explicit parent-assisted exceptions", text)
        self.assertIn("S3* remains outside the parent-mode publication notation in the 0.3.x line", text)

    def test_parent_modes_are_not_described_as_a_maturity_ladder(self):
        text = self.text("skills/assess-vsm-harness/references/autonomy-states.md")
        self.assertIn("not maturity levels", text)
        self.assertIn("multi-mode capability notation", text)
        self.assertNotIn("— < C < P < A", text)

    def test_assessment_format_only_documents_parent_modes_for_s3_s4_s5(self):
        text = self.text("skills/assess-vsm-harness/references/assessment-format.md")
        self.assertIn("valid only for S3, S4, and S5", text)
        self.assertIn("does not publish `(P)` or standalone `P` for S1, S2, or S3*", text)
        for function in ("S3", "S4", "S5"):
            self.assertRegex(text, rf"For `{function}=P`|For `{function}=P`,|For `{function}=P`.*`{function}=A\(P\)`")

    def test_synthesis_keeps_parent_mode_unweighted(self):
        text = self.text("SYNTHESIS.md")
        self.assertIn("A(P)   → base A, parent yes", text)
        self.assertIn("C(P)   → base C, parent yes", text)
        self.assertIn("parent-mode presence", text)
        self.assertIn("never converted to fractional weights", text)

    def test_no_parent_publication_shortcut_is_added_for_s1_s2_s3star(self):
        text = self.text("skills/assess-vsm-harness/SKILL.md")
        forbidden = (
            "S1=P",
            "S2=P",
            "S3*=P",
            "S1=A(P)",
            "S2=A(P)",
            "S3*=A(P)",
            "S1=C(P)",
            "S2=C(P)",
            "S3*=C(P)",
        )
        for token in forbidden:
            self.assertNotIn(token, text, token)


if __name__ == "__main__":
    unittest.main()
