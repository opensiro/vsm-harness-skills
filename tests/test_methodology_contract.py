from pathlib import Path
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
        self.assertIn("**S1:** `P` is not published.", text)
        self.assertIn("**S2:** `P` is not published.", text)
        self.assertIn("**S3:** `P`, `A(P)`, and `C(P)` are permitted", text)
        self.assertIn("**S3*:** parent-mode notation is not published in the `0.3.x` line", text)
        self.assertIn("**S4:** `P`, `A(P)`, and `C(P)` are permitted", text)
        self.assertIn("**S5:** parent governance is the canonical `P` case", text)
        self.assertIn("This boundary is methodological, not ontological.", text)

    def test_parent_modes_are_not_described_as_a_maturity_ladder(self):
        text = self.text("skills/assess-vsm-harness/references/autonomy-states.md")
        self.assertIn("not maturity levels", text)
        self.assertIn("multi-mode capability notation", text)
        self.assertNotIn("— < C < P < A", text)

    def test_assessment_format_only_documents_parent_modes_for_s3_s4_s5(self):
        text = self.text("skills/assess-vsm-harness/references/assessment-format.md")
        self.assertIn("valid only for S3, S4, and S5", text)
        self.assertIn("S1 and S2 do not publish `P`", text)
        self.assertIn("S3* does not publish the parent modifier in `0.3.x`", text)
        self.assertIn("S5 is the canonical parent-governed case", text)
        for function in ("S3", "S4", "S5"):
            self.assertIn(f"For `{function}=P`", text)
            self.assertIn(f"`{function}=A(P)`", text)
            self.assertIn(f"`{function}=C(P)`", text)

    def test_synthesis_keeps_parent_mode_unweighted(self):
        text = self.text("SYNTHESIS.md")
        self.assertIn("A(P)   → base A, parent yes", text)
        self.assertIn("C(P)   → base C, parent yes", text)
        self.assertIn("parent-mode presence", text)
        self.assertIn("never converted to fractional weights", text)

    def test_skill_explicitly_rejects_parent_publication_for_s1_s2_s3star(self):
        text = self.text("skills/assess-vsm-harness/SKILL.md")
        self.assertIn(
            "Methodology `0.3.x` does not apply `(P)` or standalone `P` to S1, S2, or S3*.",
            text,
        )
        self.assertIn("**S1:** no `P` publication state.", text)
        self.assertIn("**S2:** no `P` publication state.", text)
        self.assertIn("**S3*:** no parent-mode modifier in the `0.3.x` line.", text)
        self.assertIn("**S3:** parent mode is an explicit supervisory/current-control exception.", text)
        self.assertIn("**S4:** parent mode is an explicit adaptation exception.", text)
        self.assertIn("**S5:** parent governance is the canonical `P` case", text)


if __name__ == "__main__":
    unittest.main()
