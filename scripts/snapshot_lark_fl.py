#!/usr/bin/env python3
"""Convert paged lark-cli Base record-list output into auditable row snapshots."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "knowledge" / "_output" / "lark_base_snapshots"
PROJECTS = ("26111", "26121")


def scalar(value):
    if isinstance(value, list) and len(value) == 1:
        return value[0]
    return value


def load_project(project: str) -> list[dict]:
    records: list[dict] = []
    for offset in (0, 200):
        path = Path(f"/tmp/lark-{project}-{offset}.json")
        envelope = json.loads(path.read_text(encoding="utf-8"))
        payload = envelope["data"]
        fields = payload["fields"]
        for record_id, values in zip(payload["record_id_list"], payload["data"], strict=True):
            row = {field: scalar(value) for field, value in zip(fields, values, strict=True)}
            row["_record_id"] = record_id
            records.append(row)
    return records


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for project in PROJECTS:
        rows = load_project(project)
        target = OUTPUT / f"{project}_lark_review_2026-07-15.json"
        target.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{project}: {len(rows)} records -> {target}")


if __name__ == "__main__":
    main()
