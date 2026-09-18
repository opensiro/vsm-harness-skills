from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if old not in text:
        raise SystemExit(f"{path}: expected text not found: {old!r}")
    write(path, text.replace(old, new, 1))


write("skills/assess-vsm-harness/VERSION", "0.3.4\n")

for path in (
    "skills/assess-vsm-harness/SKILL.md",
    "skills/assess-vsm-harness/references/autonomy-states.md",
    "skills/assess-vsm-harness/references/assessment-format.md",
    "SYNTHESIS.md",
):
    replace_once(path, "**Methodology version:** 0.3.3", "**Methodology version:** 0.3.4")

for path in (
    "skills/assess-vsm-harness/SKILL.md",
    "skills/assess-vsm-harness/references/assessment-format.md",
):
    text = read(path)
    text = text.replace(
        "generated_assessment_procedure_version: 0.3.3",
        "generated_assessment_procedure_version: 0.3.4",
    )
    text = text.replace(
        "assessment_procedure_version: 0.3.3",
        "assessment_procedure_version: 0.3.4",
    )
    write(path, text)

versioning = read("VERSIONING.md")
if "Methodology: 0.3.3" not in versioning:
    raise SystemExit("VERSIONING.md: current Methodology marker missing")
versioning = versioning.replace("Methodology: 0.3.3", "Methodology: 0.3.4", 1)
release_marker = "\n## Release tracking\n"
note = """
Methodology `0.3.4` is a patch-level validator correction over `0.3.3`. It fixes the structural completion oracle so `S3*` headings are parsed as `S3*` rather than being consumed by the `S3` heading matcher. The assessment format, VSM mappings, ownership states, evidence thresholds, ranking projection, bundled Profile `0.2.2`, and `0.3.3` reproducibility requirements are unchanged. `0.3.4`'s checker also accepts `0.3.3` artifacts because the structural contract is identical; current assessments should still record the current Methodology version when newly produced or revalidated.
"""
if release_marker not in versioning:
    raise SystemExit("VERSIONING.md: Release tracking marker missing")
versioning = versioning.replace(release_marker, "\n" + note + release_marker, 1)
write("VERSIONING.md", versioning)

changelog_path = "skills/assess-vsm-harness/CHANGELOG.md"
changelog = read(changelog_path)
entry = """## 0.3.4 — 2026-09-18

- fix `scripts/check_assessment_contract.py` so `## S3*` is parsed as the complementary-audit section rather than as a second `S3` section;
- replace the word-boundary section matcher with an explicit heading-boundary lookahead that works for the non-word `*` suffix;
- add a regression test covering all six function headings and distinct `S3` / `S3*` keys;
- allow the corrected oracle to validate `0.3.3` artifacts because `0.3.4` changes validator implementation only, not the `0.3.3` structural assessment contract;
- preserve Profile `0.2.2`, autonomy notation, evidence requirements and ranking semantics unchanged.

"""
if "## 0.3.4 —" in changelog:
    raise SystemExit("CHANGELOG already contains 0.3.4")
if changelog.startswith("# Changelog\n\n"):
    changelog = changelog.replace("# Changelog\n\n", "# Changelog\n\n" + entry, 1)
else:
    raise SystemExit("unexpected changelog header")
write(changelog_path, changelog)

checker_path = "scripts/check_assessment_contract.py"
checker = read(checker_path)
checker = checker.replace(
    '"""Check Methodology 0.3.3 assessment artifact structural completeness."""',
    '"""Check Methodology 0.3.3/0.3.4 assessment artifact structural completeness."""',
    1,
)
old_match = 'matches=list(re.finditer(r"^## (S1|S2|S3|S3\\*|S4|S5)\\b.*$",text,re.MULTILINE)); out={}; rev={v:k for k,v in FUNCTIONS}'
new_match = 'matches=list(re.finditer(r"^## (S3\\*|S1|S2|S3|S4|S5)(?=\\s|$).*$",text,re.MULTILINE)); out={}; rev={v:k for k,v in FUNCTIONS}'
if old_match not in checker:
    raise SystemExit("checker section regex changed unexpectedly")
checker = checker.replace(old_match, new_match, 1)
old_gate = '''    if fm.get("assessment_procedure_version") != "0.3.3":\n        print(f"{path}: skipped (current Methodology {fm.get('assessment_procedure_version','unknown')}, not 0.3.3)"); return []'''
new_gate = '''    supported = {"0.3.3", "0.3.4"}\n    if fm.get("assessment_procedure_version") not in supported:\n        print(f"{path}: skipped (Methodology {fm.get('assessment_procedure_version','unknown')} not supported by this completion oracle)"); return []'''
if old_gate not in checker:
    raise SystemExit("checker version gate changed unexpectedly")
checker = checker.replace(old_gate, new_gate, 1)
write(checker_path, checker)

test_path = "tests/test_methodology_contract.py"
test = read(test_path)
test = test.replace("from pathlib import Path\nimport unittest\n", "from pathlib import Path\nimport importlib.util\nimport unittest\n", 1)
test = test.replace('self.assertEqual(version, "0.3.3")', 'self.assertEqual(version, "0.3.4")', 1)
marker = "    def test_release_tracking_is_persistent_and_changelog_driven(self):\n"
regression = '''    def test_034_oracle_parses_s3star_separately(self):\n        checker_path = ROOT / "scripts" / "check_assessment_contract.py"\n        spec = importlib.util.spec_from_file_location("assessment_contract_checker", checker_path)\n        self.assertIsNotNone(spec)\n        checker = importlib.util.module_from_spec(spec)\n        assert spec.loader is not None\n        spec.loader.exec_module(checker)\n        text = "\\n".join((\n            "## S1 — Operations",\n            "## S2 — Coordination",\n            "## S3 — Inside-and-now control",\n            "## S3* — Complementary audit",\n            "## S4 — Outside-and-then intelligence",\n            "## S5 — Policy and identity",\n        ))\n        self.assertEqual(\n            set(checker.sections(text)),\n            {"s1", "s2", "s3", "s3_star", "s4", "s5"},\n        )\n\n'''
if marker not in test:
    raise SystemExit("tests: release-tracking marker missing")
test = test.replace(marker, regression + marker, 1)
write(test_path, test)
