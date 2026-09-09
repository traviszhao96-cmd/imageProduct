#!/usr/bin/env python3
"""Join respondent-level NPS rows with device mapping and remove direct PII."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


PII_HEADERS = {"firstname", "lastname", "email", "token"}


def normalize_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def find_column(headers: list[str], candidates: set[str]) -> str:
    for header in headers:
        if normalize_header(header) in candidates:
            return header
    raise ValueError(f"找不到字段：{', '.join(sorted(candidates))}")


def nps_cohort(value: str) -> str:
    try:
        score = int(float(value.strip()))
    except (TypeError, ValueError):
        return "invalid_or_missing"
    if score >= 9:
        return "promoter"
    if score >= 7:
        return "passive"
    if score >= 0:
        return "detractor"
    return "invalid_or_missing"


def main() -> int:
    parser = argparse.ArgumentParser(description="生成 NPS + deviceId 分析交接 CSV")
    parser.add_argument("--responses-csv", type=Path, required=True)
    parser.add_argument("--mapping-csv", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--quality-json", type=Path, required=True)
    args = parser.parse_args()

    with args.mapping_csv.expanduser().open("r", encoding="utf-8-sig", newline="") as handle:
        mapping_rows = list(csv.DictReader(handle))
    mapping = {row["refid"].lower(): row for row in mapping_rows}

    with args.responses_csv.expanduser().open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("问卷 CSV 没有表头")
        headers = list(reader.fieldnames)
        refid_col = find_column(headers, {"refid", "ledgerid"})
        nps_col = find_column(headers, {"howlikelyareyoutorecommendphone4btoyourfriendsandfamilyfrom0to10"})
        kept_headers = [h for h in headers if normalize_header(h) not in PII_HEADERS]
        source_rows = list(reader)

    refid_counts = Counter((row.get(refid_col) or "").strip().lower() for row in source_rows)
    output_headers = [
        "device_id",
        "device_id_raw",
        "mapping_status",
        "nps_cohort",
        "duplicate_refid_count",
    ] + kept_headers
    output_rows: list[dict[str, str | int]] = []
    for row in source_rows:
        refid = (row.get(refid_col) or "").strip().lower()
        match = mapping.get(refid, {})
        output_row: dict[str, str | int] = {
            "device_id": match.get("device_id", ""),
            "device_id_raw": match.get("device_id_raw", ""),
            "mapping_status": match.get("mapping_status", "not_queried"),
            "nps_cohort": nps_cohort(row.get(nps_col, "")),
            "duplicate_refid_count": refid_counts.get(refid, 0),
        }
        output_row.update({header: row.get(header, "") for header in kept_headers})
        output_rows.append(output_row)

    output = args.output_csv.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_headers)
        writer.writeheader()
        writer.writerows(output_rows)

    status_counts = Counter(str(row["mapping_status"]) for row in output_rows)
    cohort_counts = Counter(str(row["nps_cohort"]) for row in output_rows)
    quality = {
        "source_rows": len(source_rows),
        "unique_refids": len([value for value in refid_counts if value]),
        "duplicate_refid_groups": sum(count > 1 for count in refid_counts.values()),
        "duplicate_extra_rows": sum(max(0, count - 1) for count in refid_counts.values()),
        "mapping_status_rows": dict(status_counts),
        "unique_mapped_device_ids": len(
            {str(row["device_id"]) for row in output_rows if row["device_id"]}
        ),
        "short_hex_device_id_rows": sum(
            str(row["mapping_status"]) == "device_id_invalid" for row in output_rows
        ),
        "nps_cohort_rows": dict(cohort_counts),
        "removed_direct_pii_columns": ["First name", "Last name", "Email", "Token"],
        "notes": [
            "Rows are preserved; repeated refids are flagged rather than silently removed.",
            "device_id_raw preserves noncanonical 13–15 digit hex values; do not pad or query them as items.aid without validation.",
            "device_id is respondent-level sensitive data. Keep the handoff local and access-controlled.",
        ],
    }
    quality_path = args.quality_json.expanduser().resolve()
    quality_path.parent.mkdir(parents=True, exist_ok=True)
    quality_path.write_text(json.dumps(quality, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"交接 CSV：{output}")
    print(f"质量摘要：{quality_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
