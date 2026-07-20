#!/usr/bin/env python3
"""Audit algorithm definitions and project FL mode expansion."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge" / "_output" / "kb-functions-algorithms.json"
FL_DIR = ROOT / "outputs" / "feature-list-table" / "data"
REPORT = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121" / "algorithm-expansion-audit-2026-07-20.md"

MODE_LABELS = {
    "照片": "照片 / Photo",
    "人像": "人像 / Portrait",
    "视频": "视频 / Video",
    "夜景": "夜景 / Night",
    "慢动作": "慢动作 / Slow Motion",
    "延时摄影": "延时摄影 / Timelapse",
    "专业": "专业 / Expert",
    "高像素": "高像素 / High Resolution",
}


def expected_modes(scope: str) -> set[str]:
    return {label for token, label in MODE_LABELS.items() if token in scope}


def main() -> None:
    kb_rows = json.loads(KB.read_text(encoding="utf-8"))
    definitions = {
        row["名称"]: expected_modes(row["模式"])
        for row in kb_rows
        if row["一级分类"] == "算法 / Algorithm"
    }
    lines = [
        "# Algorithm Expansion Audit",
        "",
        f"- KB algorithm definitions: {len(definitions)}",
        "- Rule: KB defines the mode universe; project FL keeps the same algorithm identity and varies support by camera/project.",
        "- Exception: Hex Zoom is a 26111 HP5-specific path and is not expanded into 26121.",
    ]

    for project in ("26111", "26121"):
        rows = json.loads((FL_DIR / f"{project}.json").read_text(encoding="utf-8"))
        algorithms = [row for row in rows if row["一级分类"] == "算法 / Algorithm"]
        by_name: dict[str, set[str]] = {}
        for row in algorithms:
            by_name.setdefault(row["名称"], set()).add(row["模式"])

        missing = []
        extra = []
        for name, modes in definitions.items():
            if project == "26121" and name == "Hex Zoom":
                continue
            for mode in sorted(modes - by_name.get(name, set())):
                missing.append((mode, name))
        for name, modes in by_name.items():
            if name not in definitions:
                extra.extend((mode, name) for mode in sorted(modes))
            else:
                extra.extend((mode, name) for mode in sorted(modes - definitions[name]))

        all_unsupported = [
            row for row in algorithms
            if all(row.get(camera) in ("", "✗") for camera in ("Main", "UW", "Tele", "Front"))
        ]
        status = Counter(row["状态"] for row in algorithms)
        owners = Counter(tuple(row["确认负责人"]) for row in algorithms)
        lines.extend([
            "",
            f"## {project}",
            "",
            f"- Algorithm rows: {len(algorithms)}",
            f"- Unique algorithms: {len(by_name)}",
            f"- Status: {dict(status)}",
            f"- Owners: {dict(owners)}",
            f"- Missing KB expansions: {len(missing)}",
            f"- Unexpected expansions: {len(extra)}",
            f"- All-camera unsupported candidates requiring SE review: {len(all_unsupported)}",
        ])
        if missing:
            lines.extend(["", "### Missing", "", *[f"- {mode} / {name}" for mode, name in missing]])
        if extra:
            lines.extend(["", "### Unexpected", "", *[f"- {mode} / {name}" for mode, name in extra]])
        if all_unsupported:
            lines.extend(["", "### All-camera Unsupported", ""])
            lines.extend(
                f"- {row['模式']} / {row['名称']}: {row.get('不支持原因') or '缺少原因'}"
                for row in all_unsupported
            )

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT)


if __name__ == "__main__":
    main()
