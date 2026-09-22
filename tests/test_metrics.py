import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_metrics.py"
SPEC = importlib.util.spec_from_file_location("render_metrics", SCRIPT)
metrics = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(metrics)


class MetricsTests(unittest.TestCase):
    def test_generated_metrics_match_repository(self):
        repo = Path(__file__).resolve().parents[1]
        expected = {"schema_version": 1, **metrics.compute_core_metrics(repo)}
        actual = json.loads((repo / "data" / "metrics.json").read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)

    def test_duplicate_skill_identity_fails(self):
        text = """# X
## Skill catalog
| Skill | Purpose |
| --- | --- |
| [alpha](a) | A |
| [alpha](b) | B |
## Other
"""
        with self.assertRaises(ValueError):
            metrics.parse_skill_ids(text)

    def test_core_query_is_source_root_scoped_and_write_free(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            version = repo / "skills" / "assess-vsm-harness" / "VERSION"
            version.parent.mkdir(parents=True)
            version.write_text("9.9.9\n", encoding="utf-8")
            (repo / "README.md").write_text(
                "# X\n\n## Skill catalog\n\n| Skill | Purpose |\n| --- | --- |\n"
                "| [alpha](a) | A |\n| [beta](b) | B |\n",
                encoding="utf-8",
            )
            result = metrics.compute_core_metrics(repo, allow_missing_version=True)
            self.assertEqual(result["methodology_version"], "9.9.9")
            self.assertEqual(result["skill_catalog_entries"], 2)
            self.assertEqual(result["skill_ids"], ["alpha", "beta"])
            self.assertFalse((repo / "data" / "metrics.json").exists())

    def test_historical_query_preserves_count_before_version_instrumentation(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "README.md").write_text(
                "# X\n\n## Skill catalog\n\n| Skill | Purpose |\n| --- | --- |\n"
                "| [alpha](a) | A |\n",
                encoding="utf-8",
            )
            result = metrics.compute_core_metrics(repo, allow_missing_version=True)
            self.assertIsNone(result["methodology_version"])
            self.assertEqual(result["skill_catalog_entries"], 1)
            with self.assertRaises(ValueError):
                metrics.compute_core_metrics(repo)


if __name__ == "__main__":
    unittest.main()
