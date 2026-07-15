#!/usr/bin/env python3
"""Merge the latest Lark FL review records and apply the confirmed taxonomy."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from refine_fl_unsupported_reasons import refine


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = ROOT / "knowledge" / "_output" / "lark_base_snapshots"
FINAL_DIR = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121"
FRONTEND_DIR = ROOT / "outputs" / "feature-list-table" / "data"
PROJECTS = ("26111", "26121")
STYLE_NAMES = {
    "风格-滤镜 / Style-Filter",
    "风格-调色 / Style-Tuning",
    "风格-调色盘 / Style-Tuning Palette",
}
FIELDS = [
    "模式", "一级分类", "二级分类", "名称", "说明",
    "Main", "UW", "Tele", "Front", "不支持原因", "状态", "确认负责人", "验证方法",
]


def clean_scalar(value):
    if isinstance(value, list):
        return value[0] if len(value) == 1 else value
    return value if value is not None else ""


def owners(value) -> list[str]:
    values = value if isinstance(value, list) else [part.strip() for part in str(value or "").split("/")]
    result: list[str] = []
    for item in values:
        item = str(item).strip()
        if item and item not in result and item != "已确认":
            result.append(item)
    return result


def support_union(values: list[str]) -> str:
    normalized = [str(value or "").strip() for value in values]
    if "✓" in normalized:
        return "✓"
    if "TBD" in normalized:
        return "TBD"
    if "✗" in normalized:
        return "✗"
    return ""


def canonicalize(row: dict) -> dict:
    item = {field: clean_scalar(row.get(field, "")) for field in FIELDS}
    mode = str(item["模式"])
    level1 = str(item["一级分类"])
    name = str(item["名称"]).strip()

    if str(item["二级分类"]) in {"模式栏 / Mode Switch", "前后翻转 / Camera Switch"}:
        item["一级分类"] = "功能 / Feature"
    elif mode == "通用 / Common":
        item["一级分类"] = "通用 / Common"
    elif "算法" in level1 or "Algorithm" in level1:
        item["一级分类"] = "算法 / Algorithm"
    else:
        item["一级分类"] = "功能 / Feature"

    if item["二级分类"] == "自然质感人像 / Natural Texture Portrait":
        item["二级分类"] = "后处理算法 / Post-processing Algorithm"
    if name == "美颜升级 / Beauty Upgrade":
        item["名称"] = "美颜算法 / Beauty Algorithm"
    if item["名称"] == "FRT / 人像清晰度提升":
        item["说明"] = (
            "独立的人脸清晰度增强后处理算法。FRT（Face Restoration Technology）在人脸检测成立时恢复和增强人脸细节，"
            "重点改善人脸区域清晰度；它不是美颜参数或肤质修饰功能。"
        )
    if item["名称"] == "美颜算法 / Beauty Algorithm":
        item["说明"] = (
            "独立的美颜后处理算法，仅用于照片和人像模式的前置摄像头。能力包括磨皮、美白、亮眼、胡须保护、匀肤、"
            "肤色分层、性别分层、年龄分层和脸型流畅等参数与效果处理；目标是在保留真实肤色、纹理、毛发和个人特征的前提下提升自然度。"
        )
    if name in {"光学畸变矫正", "光学畸变矫正 / LDC", "光学畸变矫正 / LDC ", "LDC / 光学畸变矫正"}:
        item["名称"] = "LDC / 光学畸变矫正"
        item["二级分类"] = "实时算法 / Realtime Algorithm"
    if name in {"Raw HDR", "Raw HDR / TF HDR", "RAW HDR / TF HDR", "TF HDR"}:
        item["名称"] = "RAW HDR"
        item["二级分类"] = "后处理算法 / Post-processing Algorithm"
    if name in {"AI Zoom / AIGC SR", "AIGC SR"}:
        item["名称"] = "AIGC SR"
    if item["一级分类"] == "功能 / Feature" and name in {"AI Zoom", "AI Zoom 控制开关", "AI Zoom 开关", "AI Zoom 开关 / AI Zoom Switch"}:
        item["名称"] = "AI Zoom 开关 / AI Zoom Switch"
        item["说明"] = "右侧暂态控制开关，用于让用户启用或关闭高倍率拍摄中的 AI Zoom 增强；它是 AIGC SR/AISR 算法的交互入口，不代表算法能力本身。"
    if item["一级分类"] == "功能 / Feature" and name in {"HDR", "HDR 开关", "HDR 开关 / HDR Switch"}:
        item["名称"] = "HDR 开关 / HDR Switch"
        item["说明"] = (
            "照片工具栏中的 HDR 控制开关，提供 Auto / Off，不提供强制 On。它只描述用户控制入口，"
            "不代表 RAW HDR、Ultra HDR 或其他具体 HDR 算法；Auto/Off 对应的算法链路需按项目确认。"
        )
    if item["一级分类"] == "功能 / Feature" and name in {"自动夜景", "自动夜景开关", "自动夜景开关 / Auto Night Switch"}:
        item["名称"] = "自动夜景开关 / Auto Night Switch"
        item["说明"] = "低照且夜景算法收益成立时出现的右侧暂态控制开关；它控制是否进入 Super Night 链路，不代表超级夜景算法本身。"
    if name == "HEX Zoom":
        item["名称"] = "Hex Zoom"
    if name in {"录制中前后镜头切换", "录制中前后置切换", "录制中前后置切换 / Front-Rear Switch While Recording"}:
        item["名称"] = "录制中前后置切换 / Front-Rear Switch While Recording"
        item["二级分类"] = "前后翻转 / Camera Switch"
        item["说明"] = "视频录制过程中不中断录制地切换前置与后置摄像头。该功能属于前后翻转能力，不属于模式栏。"
        item["验证方法"] = "录制中切换前后置摄像头，确认录制不中断、时间轴连续、音画同步、预览恢复和文件输出正常。"
    if name in {"录像中拍照（VSS）", "录制中拍照", "录制中拍照 / Video Snapshot"}:
        item["名称"] = "录制中拍照 / Video Snapshot"
        item["二级分类"] = "录制中拍照 / Capture While Recording"
        item["说明"] = (
            "视频录制过程中点击拍照入口，在不中断视频录制的情况下输出一张静态照片。"
            "当前需求方向是从视频截帧升级为独立拍照流，并保持照片与视频的视场角和色彩一致。"
        )
        item["验证方法"] = (
            "逐摄像头和视频规格在录制中拍照，确认视频不中断、不丢帧，照片分辨率、FOV、色彩、"
            "时间点、保存耗时和兼容限制符合规格。"
        )

    item["确认负责人"] = owners(item["确认负责人"])
    if not item["确认负责人"]:
        item["确认负责人"] = ["HAL SE"] if item["一级分类"] == "算法 / Algorithm" else ["Product"]
    return item


def generated_interaction_rows(project: str) -> list[dict]:
    cameras = ["Main", "UW", "Front"] if project == "26111" else ["Main", "UW", "Tele", "Front"]

    def support_fields(mode: str) -> dict:
        fields = {camera: "✓" for camera in cameras}
        fields["Tele"] = fields.get("Tele", "")
        if mode == "人像 / Portrait":
            fields["UW"] = "✗"
        return fields

    rows: list[dict] = []
    for mode in ("照片 / Photo", "人像 / Portrait", "视频 / Video", "夜景 / Night"):
        rows.append({
            "模式": mode,
            "一级分类": "功能 / Feature",
            "二级分类": "前后翻转 / Camera Switch",
            "名称": "前后翻转 / Front-Rear Camera Switch",
            "说明": "拍摄或录制开始前，通过独立翻转入口在前置摄像头与后置摄像头组之间切换；它不属于模式栏，也不等同于录制中的前后置切换。",
            **support_fields(mode),
            "不支持原因": "人像模式未开放 UW 成像链路，因此人像模式的 UW 摄像头上下文不提供前后翻转。" if mode == "人像 / Portrait" else "",
            "状态": "待确认",
            "确认负责人": ["Product"],
            "验证方法": "在前置与后置预览间反复翻转，确认入口、预览恢复、默认焦段、模式参数和异常恢复符合规格。",
        })

    rows.append({
        "模式": "通用 / Common",
        "一级分类": "功能 / Feature",
        "二级分类": "模式栏 / Mode Switch",
        "名称": "快速模式切换 / Quick Mode Switch",
        "说明": "模式栏中的快速切换交互，使用户可以在项目支持的相机模式之间快速切换；需确认触发方式、覆盖模式、切换时延和状态保留规则。",
        **support_fields("通用 / Common"),
        "不支持原因": "",
        "状态": "待确认",
        "确认负责人": ["Product"],
        "验证方法": "在项目支持的相邻及非相邻模式间连续快速切换，确认响应时延、动画、预览恢复、参数状态和拍摄可用性符合规格。",
    })
    motion_photo_support = {camera: "TBD" for camera in cameras}
    motion_photo_support["Tele"] = motion_photo_support.get("Tele", "")
    rows.append({
        "模式": "视频 / Video",
        "一级分类": "功能 / Feature",
        "二级分类": "录制中拍照 / Capture While Recording",
        "名称": "录制中拍摄动态照片 / Motion Photo While Recording",
        "说明": (
            "视频录制过程中点击拍照入口，在不中断当前视频录制的情况下生成一张包含静态封面和"
            "快门前后动态片段的 Motion Photo；需确认摄像头、视频规格、SDR/HDR、声音和风格支持范围。"
        ),
        **motion_photo_support,
        "不支持原因": "",
        "状态": "待确认",
        "确认负责人": ["Product"],
        "验证方法": (
            "逐摄像头和视频规格在录制中拍摄动态照片，确认主视频连续、动态照片封面与片段时间点正确、"
            "音画同步、相册可播放，并检查掉帧、发热和不支持组合的入口限制。"
        ),
    })
    return rows


def merge_style(mode: str, rows: list[dict], project: str) -> dict:
    base = canonicalize(rows[0])
    cameras = ["Main", "UW", "Front"] if project == "26111" else ["Main", "UW", "Tele", "Front"]
    base["一级分类"] = "功能 / Feature"
    base["二级分类"] = "工具栏 / Toolbar"
    base["名称"] = "风格 / Style"
    if mode in {"视频 / Video", "前后双录 / Dual View Video"}:
        base["说明"] = (
            "工具栏中的统一风格入口，整合滤镜、调色和调色盘。视频风格/LUT pipeline 仅支持普通 SDR 1080P30；"
            "1080P60、4K30、4K60 及 HLG/HDR 视频规格不支持。摄像头列表示该摄像头在 1080P30 下是否具备风格入口。"
        )
    else:
        base["说明"] = (
            "工具栏中的统一风格入口，整合滤镜、调色和调色盘，不再拆成三个 FL 功能。"
            "具体可用子能力、Preset 保存、互斥叠加和摄像头差异由项目规格确认。"
        )
    for camera in cameras:
        base[camera] = support_union([row.get(camera, "") for row in rows])
    if project == "26111":
        base["Tele"] = ""
    base["状态"] = "已确认" if all(row.get("状态") == "已确认" for row in rows) else "待确认"
    merged_owners: list[str] = []
    for row in rows:
        for owner in owners(row.get("确认负责人")):
            if owner not in merged_owners:
                merged_owners.append(owner)
    base["确认负责人"] = merged_owners or ["Product"]
    base["不支持原因"] = "；".join(dict.fromkeys(filter(None, (str(row.get("不支持原因") or "").strip() for row in rows))))
    base["验证方法"] = (
        "打开工具栏风格入口，分别验证滤镜、调色、调色盘、强度、Reset 和 Preset 保存恢复；"
        "视频需单独确认仅 SDR 1080P30 可用，以及其他规格入口隐藏或不可用。"
    )
    return base


def transform(project: str, online: list[dict]) -> list[dict]:
    normal: list[dict] = []
    style_groups: dict[str, list[dict]] = defaultdict(list)
    for row in online:
        name = str(row.get("名称") or "").strip()
        second = str(row.get("二级分类") or "").strip()
        if name == "PZL" or second == "取帧策略 / Frame Capture Strategy":
            continue
        if name in {"前后双录", "前后双录 / Dual View Video"} and second in {"Mode Switch", "模式栏 / Mode Switch"}:
            continue
        if name in STYLE_NAMES:
            style_groups[str(row.get("模式") or "")].append(row)
            continue
        normal.append(canonicalize(row))

    normal.extend(merge_style(mode, rows, project) for mode, rows in style_groups.items())
    existing = {(str(row["模式"]), str(row["名称"])) for row in normal}
    normal.extend(
        row for row in generated_interaction_rows(project)
        if (str(row["模式"]), str(row["名称"])) not in existing
    )
    mode_order = {
        name: index for index, name in enumerate([
            "照片 / Photo", "人像 / Portrait", "运动 / Action", "视频 / Video", "夜景 / Night",
            "慢动作 / Slow Motion", "延时摄影 / Timelapse", "全景 / Panorama", "专业 / Expert",
            "前后双录 / Dual View Video", "高像素 / High Resolution", "通用 / Common",
        ])
    }
    normal.sort(key=lambda row: (mode_order.get(str(row["模式"]), 99), str(row["一级分类"]), str(row["二级分类"]), str(row["名称"])))
    return normal


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            rendered = dict(row)
            rendered["确认负责人"] = " / ".join(owners(rendered["确认负责人"]))
            writer.writerow(rendered)


def main() -> None:
    payload: dict[str, list[dict]] = {}
    for project in PROJECTS:
        source = SNAPSHOTS / f"{project}_lark_review_2026-07-15.json"
        rows = transform(project, json.loads(source.read_text(encoding="utf-8")))
        rows, reason_stats = refine(rows)
        payload[project] = rows
        (FINAL_DIR / f"{project}_fl_final.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_csv(FINAL_DIR / f"{project}_fl_final.csv", rows)
        (FRONTEND_DIR / f"{project}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{project}: {len(rows)} normalized rows; reasons={reason_stats}")

    inline = "window.FL_INLINE_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (FRONTEND_DIR / "inline-data.js").write_text(inline, encoding="utf-8")


if __name__ == "__main__":
    main()
