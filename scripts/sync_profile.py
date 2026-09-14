#!/usr/bin/env python3
"""Sync the authoritative VSM profile into the portable assessment skill."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HEADER = "<!-- Generated from vsm-harness-profile; do not edit here. -->\n\n"


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile-dir", type=Path, default=repo.parent / "vsm-harness-profile")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = args.profile_dir.resolve() / "PROFILE.md"
    target = repo / "skills" / "assess-vsm-harness" / "references" / "profile" / "PROFILE.md"
    if not source.is_file():
        print(f"missing profile source: {source}", file=sys.stderr)
        return 1
    expected = HEADER + source.read_text(encoding="utf-8")
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            print(f"stale profile snapshot: {target}", file=sys.stderr)
            return 1
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(expected, encoding="utf-8")
        print(f"Synced profile into {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
