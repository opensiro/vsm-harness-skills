#!/usr/bin/env python3
"""Sync the authoritative VSM profile into the portable assessment skill."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


def git_blob_sha(data: bytes) -> str:
    """Return the Git blob object id for exact source-content provenance."""
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def generated_header(version: str, source_blob: str) -> str:
    return (
        f"<!-- Generated from opensiro/vsm-harness-profile v{version}. -->\n"
        f"<!-- Source PROFILE.md blob: {source_blob} -->\n"
        "<!-- Do not edit here. -->\n\n"
    )


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile-dir", type=Path, default=repo.parent / "vsm-harness-profile")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    profile_dir = args.profile_dir.resolve()
    source = profile_dir / "PROFILE.md"
    version_file = profile_dir / "VERSION"
    target = repo / "skills" / "assess-vsm-harness" / "references" / "profile" / "PROFILE.md"

    if not source.is_file():
        print(f"missing profile source: {source}", file=sys.stderr)
        return 1
    if not version_file.is_file():
        print(f"missing profile version: {version_file}", file=sys.stderr)
        return 1

    version = version_file.read_text(encoding="utf-8").strip()
    if not version:
        print(f"empty profile version: {version_file}", file=sys.stderr)
        return 1

    source_bytes = source.read_bytes()
    source_text = source_bytes.decode("utf-8")
    source_blob = git_blob_sha(source_bytes)
    expected = generated_header(version, source_blob) + source_text

    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            print(
                f"stale profile snapshot: {target} "
                f"(expected v{version}, source blob {source_blob})",
                file=sys.stderr,
            )
            return 1
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(expected, encoding="utf-8")
        print(f"Synced Profile v{version} ({source_blob}) into {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
