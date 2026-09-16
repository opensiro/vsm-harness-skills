#!/usr/bin/env python3
"""Validate repository-level Agent Skills and release-version consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
PROCEDURE_VERSION = re.compile(r"^\*\*Procedure version:\*\*\s+([^\s]+)\s*$", re.MULTILINE)
BUNDLED_PROFILE_VERSION = re.compile(
    r"bundled Profile for this procedure is \*\*v([^*]+)\*\*"
)
GENERATED_PROFILE_HEADER = re.compile(
    r"^<!-- Generated from opensiro/vsm-harness-profile v([^\s]+)\. -->$", re.MULTILINE
)
PROFILE_BLOB_HEADER = re.compile(
    r"^<!-- Source PROFILE\.md blob: ([0-9a-f]{40}) -->$", re.MULTILINE
)
PROFILE_BODY_VERSION = re.compile(r"^\*\*Version:\*\*\s+([^\s]+)\s*$", re.MULTILINE)


def read(path: Path, failures: list[str]) -> str:
    if not path.is_file():
        failures.append(f"{path}: missing required file")
        return ""
    return path.read_text(encoding="utf-8")


def require_procedure_version(path: Path, expected: str, failures: list[str]) -> None:
    text = read(path, failures)
    if not text:
        return
    match = PROCEDURE_VERSION.search(text)
    if not match:
        failures.append(f"{path}: missing Procedure version marker")
    elif match.group(1) != expected:
        failures.append(
            f"{path}: Procedure version {match.group(1)} differs from VERSION {expected}"
        )


def require_literal(path: Path, text: str, literal: str, failures: list[str]) -> None:
    if literal not in text:
        failures.append(f"{path}: missing expected version marker {literal!r}")


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

        version_path = path.parent / "VERSION"
        version = read(version_path, failures).strip()
        if not version:
            continue
        if not SEMVER.fullmatch(version):
            failures.append(f"{version_path}: invalid semantic version {version!r}")
            continue

        # Procedure-facing documents must identify the current procedure release,
        # even when a patch intentionally leaves the underlying autonomy semantics unchanged.
        require_procedure_version(path, version, failures)
        assessment_format = path.parent / "references" / "assessment-format.md"
        autonomy_states = path.parent / "references" / "autonomy-states.md"
        require_procedure_version(assessment_format, version, failures)
        require_procedure_version(autonomy_states, version, failures)

        changelog = path.parent / "CHANGELOG.md"
        changelog_text = read(changelog, failures)
        if changelog_text and f"## {version} " not in changelog_text:
            failures.append(f"{changelog}: missing current release heading for {version}")

        bundled_match = BUNDLED_PROFILE_VERSION.search(text)
        if not bundled_match:
            failures.append(f"{path}: missing bundled Profile version declaration")
            continue
        profile_version = bundled_match.group(1)
        if not SEMVER.fullmatch(profile_version):
            failures.append(f"{path}: invalid bundled Profile version {profile_version!r}")
            continue

        snapshot = path.parent / "references" / "profile" / "PROFILE.md"
        snapshot_text = read(snapshot, failures)
        if snapshot_text:
            header_match = GENERATED_PROFILE_HEADER.search(snapshot_text)
            body_match = PROFILE_BODY_VERSION.search(snapshot_text)
            if not header_match:
                failures.append(f"{snapshot}: missing generated Profile version header")
            elif header_match.group(1) != profile_version:
                failures.append(
                    f"{snapshot}: generated header v{header_match.group(1)} differs from SKILL bundled v{profile_version}"
                )
            if not PROFILE_BLOB_HEADER.search(snapshot_text):
                failures.append(f"{snapshot}: missing immutable source PROFILE.md blob header")
            if not body_match:
                failures.append(f"{snapshot}: missing Profile body Version marker")
            elif body_match.group(1) != profile_version:
                failures.append(
                    f"{snapshot}: body version {body_match.group(1)} differs from bundled v{profile_version}"
                )

        # Generation examples are part of the procedure contract and should track
        # the current procedure plus its bundled normative Profile.
        require_literal(
            path,
            text,
            f"generated_profile_version: {profile_version}",
            failures,
        )
        require_literal(
            path,
            text,
            f"generated_assessment_procedure_version: {version}",
            failures,
        )
        assessment_text = read(assessment_format, failures)
        if assessment_text:
            for key, expected in (
                ("generated_profile_version", profile_version),
                ("generated_assessment_procedure_version", version),
                ("profile_version", profile_version),
                ("assessment_procedure_version", version),
            ):
                require_literal(
                    assessment_format,
                    assessment_text,
                    f"{key}: {expected}",
                    failures,
                )

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Validated {len(skills)} skills and release-version consistency")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
