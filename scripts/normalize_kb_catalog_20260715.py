#!/usr/bin/env python3
"""Normalize the KB catalog to Feature / Algorithm / Common taxonomy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge" / "_output" / "kb-functions-algorithms.v6.json"
STYLE_NAMES = {
    "Filter", "Tuning", "风格 / Style", "风格-滤镜 / Style-Filter",
    "风格-调色 / Style-Tuning", "风格-调色盘 / Style-Tuning Palette",
}


def normalize(rows: list[dict]) -> list[dict]:
    normalized: list[dict] = []
    style_index = None
    for row in rows:
        name = str(row.get("名称") or "").strip()
        if name == "PZL" or row.get("二级分类") in {"取帧策略", "取帧策略 / Frame Capture Strategy"}:
            continue
        if name in STYLE_NAMES:
            if style_index is None:
                style_index = len(normalized)
            continue

        item = dict(row)
        mode = str(item.get("模式") or "")
        level1 = str(item.get("一级分类") or "")
        level2 = str(item.get("二级分类") or "")
        if level2 in {"Mode Switch", "模式栏 / Mode Switch", "前后翻转 / Camera Switch"}:
            item["一级分类"] = "功能 / Feature"
        elif mode == "通用" or level1 in {"Settings", "Preset", "Widget", "通用 / Common"}:
            item["一级分类"] = "通用 / Common"
        elif "算法" in level1 or "Algorithm" in level1:
            item["一级分类"] = "算法 / Algorithm"
        else:
            item["一级分类"] = "功能 / Feature"

        if item.get("二级分类") == "自然质感人像 / Natural Texture Portrait":
            item["二级分类"] = "后处理算法 / Post-processing Algorithm"
        if name == "美颜升级 / Beauty Upgrade":
            item["名称"] = "美颜算法 / Beauty Algorithm"
        if item.get("名称") == "FRT / 人像清晰度提升":
            item["说明"] = (
                "独立的人脸清晰度增强后处理算法。FRT（Face Restoration Technology）在人脸检测成立时恢复和增强人脸细节，"
                "重点改善人脸区域清晰度；它不是美颜参数或肤质修饰功能。"
            )
        if item.get("名称") == "美颜算法 / Beauty Algorithm":
            item["说明"] = (
                "独立的美颜后处理算法，仅用于照片和人像模式的前置摄像头。能力包括磨皮、美白、亮眼、胡须保护、匀肤、"
                "肤色分层、性别分层、年龄分层和脸型流畅等参数与效果处理；目标是在保留真实肤色、纹理、毛发和个人特征的前提下提升自然度。"
            )
        if item.get("二级分类") == "Toolbar":
            item["二级分类"] = "工具栏 / Toolbar"
        if item.get("二级分类") == "实时算法":
            item["二级分类"] = "实时算法 / Realtime Algorithm"
        if item.get("二级分类") == "后处理算法":
            item["二级分类"] = "后处理算法 / Post-processing Algorithm"
        normalized.append(item)

    style = {
        "模式": "照片 / 人像 / 运动 / 视频 / 夜景 / 专业 / 前后双录 / 高像素",
        "一级分类": "功能 / Feature",
        "二级分类": "工具栏 / Toolbar",
        "名称": "风格 / Style",
        "说明": "相机工具栏中的统一风格入口，包含滤镜与调色两类子能力；调色内部再分调色盘模式和参数模式。强度是滤镜与调色盘共用的统一控制值，同时缩放当前滤镜效果和调色盘映射参数的整体贡献；参数模式中的 7 个独立参数直接写入最终值，不受统一强度二次缩放。调色盘模式只包含调色盘和统一强度，不提供复古滑杆；颗粒与暗角保留为参数模式中的独立调节项。滤镜使用预览框内的横向画廊切换：适当缩小有效预览范围并增加遮罩，用户滑动画廊切换滤镜，圆点反馈当前位置。在 KB 和 FL 中只维护一条风格功能，不把子能力拆成独立功能行。视频风格/LUT 处理链路当前仅支持普通 SDR 1080P30；其他模式和摄像头范围按项目配置确认。",
        "判断依据": "项目需求或 Style PRD 明确定义统一风格入口，且当前模式至少支持 Filter 或 Tuning 中的一项时，FL 展开一条风格功能；子能力范围、摄像头和规格限制写入该行说明及支持状态。",
        "依赖": "依赖工具栏入口、预览框缩放与遮罩、横向滤镜画廊、圆点状态反馈、滤镜/LUT、调色、滤镜与调色盘共用的统一强度、预设保存恢复，以及各模式的处理链路和规格限制。",
        "验证方法": "打开风格入口，验证滤镜画廊横向滑动、选中卡片、滤镜名称、统一强度、圆点位置和实时预览一致；调整统一强度时，确认当前滤镜效果和调色盘映射参数按相同比例变化。再验证调色盘模式仅显示调色盘和统一强度、不出现复古滑杆，参数模式中的 7 个独立参数不受统一强度二次缩放，颗粒与暗角只能在参数模式中独立调节，并验证重置、预设保存恢复、互斥或叠加关系及摄像头范围。视频确认仅普通 SDR 1080P30 可用。",
        "来源项目": "Style PRD；25111 / 25131",
        "备注": "Style PRD：Pwe0wwnytilR3nkh3QjlyvwNgVh。待确认最终信息架构、默认落点、Filter/Tuning 效果互斥或叠加顺序，以及旧项目入口与 Preset 数据迁移策略。",
    }
    normalized.insert(style_index if style_index is not None else len(normalized), style)
    return normalized


def main() -> None:
    rows = json.loads(KB.read_text(encoding="utf-8"))
    normalized = normalize(rows)
    KB.write_text(json.dumps(normalized, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"KB: {len(rows)} -> {len(normalized)} rows")


if __name__ == "__main__":
    main()
