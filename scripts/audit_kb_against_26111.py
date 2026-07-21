#!/usr/bin/env python3
"""Audit canonical KB coverage and rule consistency against reviewed 26111 FL."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB_PATH = ROOT / "knowledge" / "_output" / "kb-functions-algorithms.json"
FL_PATH = ROOT / "outputs" / "feature-list-table" / "data" / "26111.json"
REPORT = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121" / "kb-vs-26111-audit-2026-07-21.md"


SPEC_FAMILY_BY_MODE = {
    "视频": "视频规格 / Video Specs",
    "慢动作": "慢动作规格 / Slow Motion Specs",
    "延时摄影": "延时摄影规格 / Timelapse Specs",
    "高像素": "高像素输出规格 / High Resolution Specs",
}
SPEC_NAME = re.compile(r"^(?:720P|1080P|4K|50MP|200MP)(?:\s|@|$)", re.I)


def project_mode(row: dict) -> str:
    return str(row.get("模式") or "").split(" / ", 1)[0]


def main() -> None:
    kb = json.loads(KB_PATH.read_text(encoding="utf-8"))
    fl = json.loads(FL_PATH.read_text(encoding="utf-8"))
    kb_by_name = {str(row.get("名称") or ""): row for row in kb}
    fl_names = {str(row.get("名称") or "") for row in fl if row.get("名称")}

    direct_missing = sorted(fl_names - set(kb_by_name))
    spec_rows: dict[str, list[str]] = {family: [] for family in SPEC_FAMILY_BY_MODE.values()}
    missing_nodes: list[str] = []
    for name in direct_missing:
        modes = {project_mode(row) for row in fl if row.get("名称") == name}
        families = {SPEC_FAMILY_BY_MODE[mode] for mode in modes if mode in SPEC_FAMILY_BY_MODE}
        if SPEC_NAME.match(name) and len(families) == 1:
            spec_rows[next(iter(families))].append(name)
        else:
            missing_nodes.append(name)

    mode_scope_drift = []
    for row in fl:
        name = str(row.get("名称") or "")
        kb_row = kb_by_name.get(name)
        if not kb_row:
            continue
        mode = project_mode(row)
        kb_modes = str(kb_row.get("模式") or "")
        if mode != "通用" and mode not in kb_modes:
            mode_scope_drift.append((mode, name, kb_modes))

    portrait_uw_conflicts = [
        row for row in fl
        if project_mode(row) == "人像" and row.get("UW") == "✓"
    ]
    confirmed_but_unresolved = [
        row for row in fl
        if row.get("状态") == "已确认"
        and re.search(r"仍需确认|待确认|需确认.*(?:方案|范围|焦段|量产)", str(row.get("不支持原因") or ""))
    ]
    unsupported_without_reason = [
        row for row in fl
        if "✗" in [row.get(camera) for camera in ("Main", "UW", "Front")]
        and not str(row.get("不支持原因") or "").strip()
    ]
    empty_verification = [row for row in fl if not str(row.get("验证方法") or "").strip()]
    hex_zoom = next((row for row in fl if row.get("名称") == "Hex Zoom"), None)

    lines = [
        "# KB vs 26111 Audit",
        "",
        "- Date: 2026-07-21",
        f"- Canonical KB rows: {len(kb)}",
        f"- Reviewed 26111 FL rows: {len(fl)}",
        f"- FL names without an exact KB node: {len(direct_missing)}",
        f"- Non-spec FL names without an exact KB node: {len(missing_nodes)}",
        f"- KB mode-scope drift: {len(mode_scope_drift)}",
        f"- Portrait rows with UW=✓: {len(portrait_uw_conflicts)}",
        f"- Confirmed rows that still say unresolved: {len(confirmed_but_unresolved)}",
        f"- Rows with ✗ but no unsupported reason: {len(unsupported_without_reason)}",
        f"- Rows with empty verification: {len(empty_verification)}",
        "",
        "## Critical Conflicts",
        "",
        "### Portrait UW Semantics",
        "",
        "HAL defines Portrait UW as an internal depth-assist input, not a user-selectable/output camera. These FL rows currently use UW=✓ and must be clarified before the result can become a KB rule:",
        "",
    ]
    lines.extend(f"- {row['名称']}: Main={row.get('Main')} / UW={row.get('UW')} / Front={row.get('Front')}" for row in portrait_uw_conflicts)
    lines.extend(["", "### Confirmed But Still Unresolved", ""])
    lines.extend(f"- {row['模式']} | {row['名称']}: {row.get('不支持原因')}" for row in confirmed_but_unresolved)
    if hex_zoom and "ISZ" in str(hex_zoom.get("不支持原因") or ""):
        lines.extend([
            "",
            "### Hex Zoom Reason Mismatch",
            "",
            "- Hex Zoom is explicitly not ISZ, but its UW/Front unsupported reason says those cameras do not provide ISZ. The reason should instead point to the missing HP5 hex/4x4 RAW input and external remosaic path.",
        ])

    lines.extend(["", "## KB Coverage", "", "### Missing Canonical Nodes", ""])
    lines.extend(f"- {name}" for name in missing_nodes)
    lines.extend(["", "### Concrete Spec Rows Requiring Family Rules", ""])
    for family, names in spec_rows.items():
        state = "present" if family in kb_by_name else "MISSING"
        lines.append(f"- {family} [{state}]: {', '.join(names) if names else 'None'}")

    lines.extend(["", "## Mode Scope Drift", ""])
    if mode_scope_drift:
        lines.extend(f"- {mode} | {name}: KB modes = {kb_modes}" for mode, name, kb_modes in mode_scope_drift)
    else:
        lines.append("- None after the Grid scope update.")

    lines.extend(["", "## FL Quality Issues Affecting KB Intake", "", "### Unsupported Without Cause", ""])
    lines.extend(f"- {row['模式']} | {row['名称']}" for row in unsupported_without_reason)
    lines.extend(["", "### Empty Verification", ""])
    lines.extend(f"- {row['模式']} | {row['名称']}" for row in empty_verification)

    lines.extend([
        "",
        "## Intake Decision",
        "",
        "- Accepted into KB: Grid mode scope, default/memory behavior, and the Portrait UW output-vs-depth distinction.",
        "- No KB meaning change required: Tuning confirmations that only changed 26111 support/status for MFNR, face distortion correction, Super Night, Extreme Night, Motion Capture, and Video Night.",
        "- Blocked from KB intake: Portrait UW=✓ rows, AIGC SR confirmed/unresolved conflict, Hex Zoom unsupported reason, and rows lacking causal reasons or verification.",
        "- Added reusable family nodes for Video Specs, Slow Motion Specs, Timelapse Specs, and High Resolution Specs; next resolve the non-spec missing-node list instead of hardcoding those rows only in the FL generator.",
    ])

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT)


if __name__ == "__main__":
    main()
