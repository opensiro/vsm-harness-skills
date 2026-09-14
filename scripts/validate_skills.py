#!/usr/bin/env python3
"""Validate the small repository-level Agent Skills contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    failures: list[str] = []
    skills = sorted((repo / "skills").glob("*/SKILL.md"))
    if not skills:
        failures.append("no skills found")
    for path in skills:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append(f"{path}: missing frontmatter")
            continue
        try:
            frontmatter = text.split("---\n", 2)[1]
        except IndexError:
            failures.append(f"{path}: malformed frontmatter")
            continue
        values = {}
        for line in frontmatter.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                values[key.strip()] = value.strip()
        name = values.get("name", "")
        if name != path.parent.name or not NAME.fullmatch(name):
            failures.append(f"{path}: name must match kebab-case directory")
        if not values.get("description"):
            failures.append(f"{path}: missing description")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Validated {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
