#!/usr/bin/env python3
"""Validate a vsm-assessment/v1 artifact and upsert comparison CSV tables."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "vsm-assessment/v1"
HARNESS_FIELDS = [
    "assessment_id", "harness_id", "project_name", "repository", "ref",
    "generated_at", "rubric_version", "assessment_mode", "ai_native_class",
    "verdict", "recommended_topology", "maturity_stage", "harness_kind",
    "execution_model", "state_mode", "tool_mode", "human_gate",
    "audit_independence", "vsm_tldr",
]
METRIC_FIELDS = [
    "assessment_id", "harness_id", "project_name", "ref", "generated_at",
    "rubric_version", "ai_native_class", "verdict", "recommended_topology",
    "harness_kind", "execution_model", "state_mode", "tool_mode",
    "metric_id", "metric_group", "vsm_function", "axis", "scenario", "workload_id", "value",
    "max_value", "unit", "status", "confidence", "evidence_level",
    "availability",
]


def require_mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    return value


def require_text(mapping: dict[str, Any], key: str, scope: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{scope}.{key} must be a non-empty string")
    return value.strip()


def load_artifact(path: Path) -> dict[str, Any]:
    data = require_mapping(json.loads(path.read_text(encoding="utf-8")), "artifact")
    if data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"schema_version must be {SCHEMA_VERSION!r}")

    require_text(data, "assessment_id", "artifact")
    require_text(data, "generated_at", "artifact")
    snapshot = require_mapping(data.get("snapshot"), "snapshot")
    harness = require_mapping(data.get("harness"), "harness")
    summary = require_mapping(data.get("summary"), "summary")
    for key in ("project_name", "repository", "ref", "assessment_mode", "rubric_version"):
        require_text(snapshot, key, "snapshot")
    for key in ("harness_id", "harness_kind", "execution_model"):
        require_text(harness, key, "harness")
    for key in ("ai_native_class", "verdict", "recommended_topology", "maturity_stage", "vsm_tldr"):
        require_text(summary, key, "summary")

    metrics = data.get("metrics")
    if not isinstance(metrics, list):
        raise ValueError("metrics must be an array")
    seen: set[tuple[str, str, str]] = set()
    for index, metric in enumerate(metrics):
        metric = require_mapping(metric, f"metrics[{index}]")
        metric_id = require_text(metric, "metric_id", f"metrics[{index}]")
        metric_key = (metric_id, str(metric.get("scenario", "")), str(metric.get("workload_id", "")))
        if metric_key in seen:
            raise ValueError(f"duplicate metric key: {metric_key}")
        seen.add(metric_key)
        for key in ("metric_group", "axis", "unit", "status", "confidence", "evidence_level", "availability"):
            require_text(metric, key, f"metrics[{index}]")
        if metric.get("availability") not in {"available", "unknown"}:
            raise ValueError(f"{metric_id}: availability must be available or unknown")
        if metric.get("availability") == "unknown" and metric.get("value") is not None:
            raise ValueError(f"{metric_id}: unknown metric value must be null")
    return data


def scalar(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def base_row(data: dict[str, Any]) -> dict[str, Any]:
    snapshot, harness, summary = data["snapshot"], data["harness"], data["summary"]
    return {
        "assessment_id": data["assessment_id"], "harness_id": harness["harness_id"],
        "project_name": snapshot["project_name"], "repository": snapshot["repository"],
        "ref": snapshot["ref"], "generated_at": data["generated_at"],
        "rubric_version": snapshot["rubric_version"], "assessment_mode": snapshot["assessment_mode"],
        "ai_native_class": summary["ai_native_class"], "verdict": summary["verdict"],
        "recommended_topology": summary["recommended_topology"], "maturity_stage": summary["maturity_stage"],
        "harness_kind": harness["harness_kind"], "execution_model": harness["execution_model"],
        "state_mode": harness.get("state_mode", "unknown"), "tool_mode": harness.get("tool_mode", "unknown"),
        "human_gate": harness.get("human_gate", "unknown"),
        "audit_independence": harness.get("audit_independence", "unknown"),
        "vsm_tldr": summary["vsm_tldr"],
    }


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows({key: scalar(row.get(key)) for key in fields} for row in rows)


def upsert(data: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    assessment_id, base = data["assessment_id"], base_row(data)
    harness_path = output_dir / "harnesses.csv"
    harness_rows = [row for row in read_rows(harness_path) if row.get("assessment_id") != assessment_id]
    harness_rows.append(base)
    harness_rows.sort(key=lambda row: (str(row.get("harness_id", "")), str(row.get("generated_at", "")), str(row.get("assessment_id", ""))))
    write_rows(harness_path, HARNESS_FIELDS, harness_rows)

    metric_path = output_dir / "harness-metrics.csv"
    metric_rows = [row for row in read_rows(metric_path) if row.get("assessment_id") != assessment_id]
    metric_rows.extend({**base, **metric} for metric in data["metrics"])
    metric_rows.sort(key=lambda row: (str(row.get("harness_id", "")), str(row.get("metric_id", "")), str(row.get("assessment_id", ""))))
    write_rows(metric_path, METRIC_FIELDS, metric_rows)
    return harness_path, metric_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    artifact = args.artifact.resolve()
    data = load_artifact(artifact)
    harness_path, metric_path = upsert(data, (args.output_dir or artifact.parents[2]).resolve())
    print(harness_path)
    print(metric_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
