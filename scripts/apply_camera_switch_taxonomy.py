#!/usr/bin/env python3
"""Apply the Camera Switch taxonomy to current local FL artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from sync_lark_fl_review_20260715 import FIELDS, canonicalize, generated_interaction_rows


ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121"
FRONTEND_DIR = ROOT / "outputs" / "feature-list-table" / "data"
PROJECTS = ("26111", "26121")


def transform(project: str, rows: list[dict]) -> list[dict]:
    updated = [
        canonicalize(row) for row in rows
        if not (
            str(row.get("名称") or "").strip() in {"前后双录", "前后双录 / Dual View Video"}
            and str(row.get("二级分类") or "").strip() in {"Mode Switch", "模式栏 / Mode Switch"}
        )
    ]
    existing = {(str(row["模式"]), str(row["名称"])) for row in updated}
    updated.extend(
        row for row in generated_interaction_rows(project)
        if (str(row["模式"]), str(row["名称"])) not in existing
    )
    return updated


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            rendered = dict(row)
            rendered["确认负责人"] = " / ".join(rendered.get("确认负责人") or [])
            writer.writerow(rendered)


def main() -> None:
    payload: dict[str, list[dict]] = {}
    for project in PROJECTS:
        path = FINAL_DIR / f"{project}_fl_final.json"
        rows = transform(project, json.loads(path.read_text(encoding="utf-8")))
        payload[project] = rows
        serialized = json.dumps(rows, ensure_ascii=False, indent=2) + "\n"
        path.write_text(serialized, encoding="utf-8")
        write_csv(FINAL_DIR / f"{project}_fl_final.csv", rows)
        (FRONTEND_DIR / f"{project}.json").write_text(serialized, encoding="utf-8")
        print(f"{project}: {len(rows)} rows")

    inline = "window.FL_INLINE_DATA = " + json.dumps(
        payload, ensure_ascii=False, separators=(",", ":")
    ) + ";\n"
    (FRONTEND_DIR / "inline-data.js").write_text(inline, encoding="utf-8")


if __name__ == "__main__":
    main()
