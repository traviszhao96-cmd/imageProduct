#!/usr/bin/env python3
"""Sync the reviewed 26111 HAL ownership and reusable conclusions into 26121."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / ".codex-tmp"
DATA = ROOT / "outputs" / "feature-list-table" / "data"
FINAL = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121"
SNAPSHOTS = ROOT / "knowledge" / "_output" / "lark_base_snapshots"
FIELDS = [
    "模式", "一级分类", "二级分类", "名称", "说明", "Main", "UW", "Tele",
    "Front", "不支持原因", "状态", "确认负责人", "验证方法",
]


def scalar(value):
    if isinstance(value, list) and len(value) == 1:
        return value[0]
    return value


def read_pages(prefix: str) -> list[dict]:
    rows: list[dict] = []
    for offset in (0, 200):
        payload = json.loads((TMP / f"{prefix}-{offset}.json").read_text(encoding="utf-8"))["data"]
        for record_id, values in zip(payload["record_id_list"], payload["data"], strict=True):
            row = {field: scalar(value) for field, value in zip(payload["fields"], values, strict=True)}
            row["_record_id"] = record_id
            rows.append(row)
    return rows


def key(row: dict) -> tuple[str, str]:
    return str(row.get("模式") or ""), str(row.get("名称") or "")


def owner_list(row: dict) -> list[str]:
    owners = row.get("确认负责人") or []
    if isinstance(owners, list):
        return [str(owner) for owner in owners]
    return [str(owners)]


def normalized(row: dict, project: str) -> dict:
    result = {field: row.get(field) for field in FIELDS}
    result["模式"] = str(result["模式"] or "")
    result["一级分类"] = str(result["一级分类"] or "")
    result["二级分类"] = str(result["二级分类"] or "")
    result["名称"] = str(result["名称"] or "")
    result["说明"] = str(result["说明"] or "")
    for camera in ("Main", "UW", "Tele", "Front"):
        result[camera] = str(result[camera] or "")
    if project == "26111":
        result["Tele"] = ""
    result["不支持原因"] = str(result["不支持原因"] or "")
    result["状态"] = str(result["状态"] or "")
    result["确认负责人"] = owner_list(result)
    result["验证方法"] = str(result["验证方法"] or "")
    return result


def write_project(project: str, rows: list[dict]) -> None:
    text = json.dumps(rows, ensure_ascii=False, indent=2) + "\n"
    (DATA / f"{project}.json").write_text(text, encoding="utf-8")
    (FINAL / f"{project}_fl_final.json").write_text(text, encoding="utf-8")
    with (FINAL / f"{project}_fl_final.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            rendered = dict(row)
            rendered["确认负责人"] = " / ".join(rendered["确认负责人"])
            writer.writerow(rendered)


def set_support(row: dict, values: dict[str, str], reason: str = "") -> None:
    row.update(values)
    if reason:
        row["不支持原因"] = reason


def main() -> None:
    online_26111 = read_pages("26111-post-hal")
    online_26121 = read_pages("26121-pre-hal-sync")

    meaningful_26111 = [row for row in online_26111 if str(row.get("名称") or "").strip()]
    rows_26111 = [normalized(row, "26111") for row in meaningful_26111]
    rows_26121 = [normalized(row, "26121") for row in online_26121 if str(row.get("名称") or "").strip()]
    source_26111 = {key(row): row for row in meaningful_26111}
    target_26121 = {key(row): row for row in rows_26121}
    online_target = {key(row): row for row in online_26121}

    tuning_synced: list[tuple[str, str]] = []
    tuning_missing: list[tuple[str, str]] = []
    for item_key, source in source_26111.items():
        owners = owner_list(source)
        if "Tuning SE" not in owners:
            continue
        target = target_26121.get(item_key)
        if not target:
            tuning_missing.append(item_key)
            continue
        target["确认负责人"] = list(owners)
        target["状态"] = "待确认"
        tuning_synced.append(item_key)

    reusable_hal = {
        ("照片 / Photo", "FRT / 人像清晰度提升"),
        ("照片 / Photo", "RAW HDR"),
        ("照片 / Photo", "美颜算法 / Beauty Algorithm"),
        ("照片 / Photo", "CFR / 紫边去除"),
        ("人像 / Portrait", "FRT / 人像清晰度提升"),
        ("人像 / Portrait", "美颜算法 / Beauty Algorithm"),
        ("人像 / Portrait", "人像 HDR"),
        ("视频 / Video", "Video EIS"),
        ("夜景 / Night", "FRT / 人像清晰度提升"),
        ("夜景 / Night", "超级夜景"),
        ("慢动作 / Slow Motion", "1080P 120FPS"),
        ("高像素 / High Resolution", "FRT / 人像清晰度提升"),
    }
    hal_synced: list[tuple[str, str]] = []
    for item_key in sorted(reusable_hal):
        source = source_26111.get(item_key)
        target = target_26121.get(item_key)
        if not source or not target or source.get("状态") != "已确认":
            continue
        target["状态"] = "已确认"
        target["确认负责人"] = ["HAL SE"]
        hal_synced.append(item_key)

    portrait_beauty = target_26121[("人像 / Portrait", "美颜算法 / Beauty Algorithm")]
    set_support(
        portrait_beauty,
        {"Main": "✗", "UW": "✗", "Tele": "✗", "Front": "✓"},
        "Main/UW/Tele: 本期美颜算法升级仅接入前置人像链路，后置摄像头不在该功能范围。",
    )
    slow_120 = target_26121[("慢动作 / Slow Motion", "1080P 120FPS")]
    set_support(
        slow_120,
        {"Main": "✓", "UW": "✗", "Tele": "✗", "Front": "✗"},
        "UW/Tele/Front: 26111/26121 HAL 设计仅明确 Main/Wide 的 1080P 120FPS 慢动作通路，其他摄像头不在支持范围。",
    )

    write_project("26111", rows_26111)
    write_project("26121", rows_26121)
    inline = {
        "26111": rows_26111,
        "26121": rows_26121,
    }
    (DATA / "inline-data.js").write_text(
        "window.FL_INLINE_DATA = " + json.dumps(inline, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )

    SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    (SNAPSHOTS / "26111_lark_post_hal_review_2026-07-20.json").write_text(
        json.dumps(online_26111, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (SNAPSHOTS / "26121_lark_before_hal_sync_2026-07-20.json").write_text(
        json.dumps(online_26121, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    groups: dict[tuple[str, ...], list[str]] = {}
    for item_key in tuning_synced:
        row = target_26121[item_key]
        groups.setdefault(tuple(row["确认负责人"]), []).append(online_target[item_key]["_record_id"])
    patch_files = []
    for owners, record_ids in groups.items():
        suffix = "-".join(owner.lower().replace(" ", "-") for owner in owners)
        path = TMP / f"26121-hal-sync-owner-{suffix}.json"
        path.write_text(
            json.dumps({"record_id_list": record_ids, "patch": {"确认负责人": list(owners), "状态": "待确认"}}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        patch_files.append(path.name)

    hal_ids = [online_target[item_key]["_record_id"] for item_key in hal_synced]
    (TMP / "26121-hal-sync-confirmed.json").write_text(
        json.dumps({"record_id_list": hal_ids, "patch": {"状态": "已确认", "确认负责人": ["HAL SE"]}}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for item_key, suffix in (
        (("人像 / Portrait", "美颜算法 / Beauty Algorithm"), "portrait-beauty"),
        (("慢动作 / Slow Motion", "1080P 120FPS"), "slowmo-1080p120"),
    ):
        row = target_26121[item_key]
        patch = {field: row[field] for field in ("Main", "UW", "Tele", "Front", "不支持原因", "状态", "确认负责人")}
        (TMP / f"26121-hal-sync-{suffix}.json").write_text(
            json.dumps({"record_id_list": [online_target[item_key]["_record_id"]], "patch": patch}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    counts_26111 = Counter(row["状态"] for row in rows_26111)
    counts_26121 = Counter(row["状态"] for row in rows_26121)
    report = [
        "# 26111 HAL 评审同步到 26121",
        "",
        "- 日期：2026-07-20",
        f"- 26111 线上原始记录：{len(online_26111)}；有效 FL 行：{len(rows_26111)}；空白占位行：{len(online_26111) - len(rows_26111)}。",
        f"- 26111 状态：{dict(counts_26111)}。",
        f"- 26121 同步后状态：{dict(counts_26121)}。",
        f"- 同步 Tuning 主责：{len(tuning_synced)} 条；26111 独有未同步：{len(tuning_missing)} 条。",
        f"- 复用 HAL 结论：{len(hal_synced)} 条。",
        "",
        "## Tuning 主责同步",
        "",
    ]
    report.extend(f"- {mode} | {name}" for mode, name in tuning_synced)
    report.extend(["", "## 26111 独有 Tuning 条目", ""])
    report.extend(f"- {mode} | {name}" for mode, name in tuning_missing)
    report.extend(["", "## 可复用 HAL 结论", ""])
    report.extend(f"- {mode} | {name}" for mode, name in hal_synced)
    report.extend([
        "",
        "## 保留 26121 待确认",
        "",
        "- 视频逐规格摄像头范围：26121 平台支持 4K60，且比 26111 多 Tele，不能继承 26111 勾叉。",
        "- HDSR、SR、ISZ、Photo EIS、Video HDR：依赖 26121 Main/Tele 的 Sensor mode、焦段和算法链路。",
        "- 夜景 Remosaic/LDC/Photo EIS：26121 当前仍有 TBD，不能由 26111 无 Tele 的结论补齐。",
        "- 高像素 Remosaic/SR/Photo EIS：26121 为 Main+Tele 场景自适应链路，与 26111 HP5 单摄链路不同。",
        "- 专业参数极值：ISO 等范围必须按 26121 每颗 Sensor/HAL 性能确认。",
        "",
        "## 在线 patch",
        "",
    ])
    report.extend(f"- `{name}`" for name in [*patch_files, "26121-hal-sync-confirmed.json", "26121-hal-sync-portrait-beauty.json", "26121-hal-sync-slowmo-1080p120.json"])
    (FINAL / "26111-hal-review-sync-to-26121-2026-07-20.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"26111: {len(rows_26111)} meaningful rows; {dict(counts_26111)}")
    print(f"26121: {len(rows_26121)} rows; {dict(counts_26121)}")
    print(f"Tuning synced: {len(tuning_synced)}; missing: {tuning_missing}")
    print(f"HAL confirmed: {len(hal_synced)}")


if __name__ == "__main__":
    main()
