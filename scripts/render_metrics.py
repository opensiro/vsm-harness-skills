#!/usr/bin/env python3
"""Render repository-owned public metrics for VSM Harness Skills."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_ROW_RE = re.compile(r"^\|\s*\[([^\]]+)\]\([^)]+\)\s*\|")


def parse_skill_ids(text: str) -> list[str]:
    in_section = False
    found_section = False
    identities: list[str] = []
    for line in text.splitlines():
        if line.strip() == "## Skill catalog":
            in_section = True
            found_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        match = SKILL_ROW_RE.match(line)
        if match:
            identities.append(match.group(1).strip())
    if not found_section:
        raise ValueError("README.md must contain a Skill catalog section")
    if len(identities) != len(set(identities)):
        raise ValueError("duplicate skill identity in README skill catalog")
    return identities


def compute_core_metrics(
    repo: Path, *, allow_missing_version: bool = False
) -> dict[str, object]:
    version_path = repo / "skills" / "assess-vsm-harness" / "VERSION"
    if version_path.is_file():
        version: str | None = version_path.read_text(encoding="utf-8").strip()
        if not version:
            raise ValueError("Methodology VERSION must not be empty")
    elif allow_missing_version:
        version = None
    else:
        raise ValueError("Methodology VERSION is required for current metrics generation")

    identities = parse_skill_ids((repo / "README.md").read_text(encoding="utf-8"))
    return {
        "methodology_version": version,
        "skill_catalog_entries": len(identities),
        "skill_ids": identities,
    }


def render(repo: Path) -> str:
    return json.dumps(
        {"schema_version": 1, **compute_core_metrics(repo)},
        indent=2,
        ensure_ascii=False,
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--stdout-core-json", action="store_true")
    args = parser.parse_args()

    repo = (args.source_root or Path(__file__).resolve().parents[1]).resolve()
    if args.stdout_core_json:
        print(
            json.dumps(
                compute_core_metrics(repo, allow_missing_version=True),
                sort_keys=True,
            )
        )
        return 0

    output = repo / "data" / "metrics.json"
    rendered = render(repo)
    if args.check:
        current = output.read_text(encoding="utf-8") if output.exists() else ""
        if current != rendered:
            raise SystemExit(
                "stale generated metric file: data/metrics.json; "
                "run python scripts/render_metrics.py"
            )
        print("Skills metrics are current")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
