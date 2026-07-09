#!/usr/bin/env python3
"""Generate reviewable 26111 / 26121 Camera FL draft tables.

The draft is intentionally distribution-friendly rather than final:
- preserve current Bitable rows where available;
- add algorithm source rows and active Tree/KB integration candidates;
- keep unresolved support as TBD so PM/SE/QA can fill it in the shared table.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "knowledge" / "_output"
REQ = OUT / "lark_26111_requirements"
DRAFT = OUT / "fl_draft_26111_26121"

CURRENT = OUT / "current-fl-records-26111-26121.json"
KB = OUT / "kb-functions-algorithms.json"
CANDIDATES = REQ / "tree-kb-integration-candidates.v1.json"
ALGO_MD = ROOT / "knowledge" / "reference" / "algorithm-fl-source-26111-26121.md"

PROJECTS = {
    "26111": {
        "table": "26111",
        "cameras": ["Main", "UW", "Front"],
        "note": "Phone 5a Base; HP5 200MP main, IMX355 UW, OV32D front, no tele.",
    },
    "26121": {
        "table": "26121",
        "cameras": ["Main", "UW", "Tele", "Front"],
        "note": "Phone 5a Pro; reuses 25111 Pro IMX896 + IMX355 + JN5 + KD1.",
    },
}

MODE_ALIASES = {
    "拍照": "照片",
    "Photo": "照片",
    "Portrait": "人像",
    "Action": "运动",
    "录像": "视频",
    "Video": "视频",
    "Night": "夜景",
    "Slowmo": "慢动作",
    "Slow motion": "慢动作",
    "Pano": "全景",
    "Pro": "专业",
    "Expert": "专业",
    "Dual View Video": "前后双录",
    "Timelapse": "延时摄影",
    "延时": "延时摄影",
    "高像素": "高像素",
    "全部拍摄模式": "通用",
}

ALL_MODES = ["照片", "人像", "运动", "视频", "夜景", "慢动作", "全景", "专业", "前后双录", "高像素", "延时摄影"]

FINAL_COLUMNS = [
    "模式",
    "一级分类",
    "二级分类",
    "名称",
    "说明",
    "Main",
    "UW",
    "Tele",
    "Front",
    "不支持原因",
    "状态",
    "确认负责人",
    "验证方法",
    "来源",
    "备注",
]

LEVEL1_DISPLAY = {
    "通用功能": "通用功能 / Common",
    "Preset": "预设 / Preset",
    "Settings": "设置 / Settings",
    "Widget": "小组件 / Widget",
    "功能": "功能 / Feature",
    "基础算法": "基础算法 / Base Algorithm",
}

MODE_DISPLAY = {
    "通用": "通用 / Common",
    "照片": "照片 / Photo",
    "人像": "人像 / Portrait",
    "运动": "运动 / Action",
    "视频": "视频 / Video",
    "夜景": "夜景 / Night",
    "慢动作": "慢动作 / Slow Motion",
    "全景": "全景 / Panorama",
    "专业": "专业 / Expert",
    "前后双录": "前后双录 / Dual View Video",
    "高像素": "高像素 / High Resolution",
    "延时摄影": "延时摄影 / Timelapse",
}

LEVEL2_DISPLAY = {
    "Preview": "预览框 / Preview",
    "预览框": "预览框 / Preview",
    "AE/AF": "AE/AF",
    "Zoom": "变焦 / Zoom",
    "Toolbar": "工具栏 / Toolbar",
    "Top Toolbar": "工具栏 / Toolbar",
    "Mode Switch": "模式栏 / Mode Switch",
    "Preset": "预设 / Preset",
    "Settings": "设置 / Settings",
    "General settings": "通用设置 / General Settings",
    "Photo settings": "照片设置 / Photo Settings",
    "Video settings": "视频设置 / Video Settings",
    "Help & Support": "帮助与反馈 / Help & Support",
    "Widget": "小组件 / Widget",
    "Video Specs": "视频规格 / Video Specs",
    "Slow Motion Specs": "慢动作规格 / Slow Motion Specs",
    "左侧暂态开关": "左侧暂态开关 / Left Transient Switch",
    "右侧暂态开关": "右侧暂态开关 / Right Transient Switch",
    "系统": "系统 / System",
    "实时算法": "实时算法 / Realtime Algorithm",
    "后处理算法": "后处理算法 / Post-processing Algorithm",
}


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " / ".join(str(v) for v in value)
    return str(value)


def normalize_mode(mode: str) -> str:
    mode = mode.strip()
    return MODE_ALIASES.get(mode, mode)


def split_modes(scope: str) -> list[str]:
    scope = as_text(scope).strip()
    if not scope:
        return ["通用"]
    scope = scope.replace("、", " / ").replace(",", " / ")
    if scope in {"通用", "全部拍摄模式"}:
        return ["通用"]
    parts = [normalize_mode(part.strip()) for part in scope.split("/") if part.strip()]
    return parts or ["通用"]


def normalize_level1(value: str) -> str:
    value = as_text(value).strip()
    if value in {"底层算法", "算法", "基础算法"}:
        return "基础算法"
    if value in {"通用", "通用功能", "公共功能", "Common"}:
        return "通用功能"
    if value in {"预设", "Preset", "预设 / Preset"}:
        return "Preset"
    if value in {"设置", "Setting", "Settings", "设置 / Setting", "设置 / Settings"}:
        return "Settings"
    if value in {"小组件", "Widget", "小组件 / Widget"}:
        return "Widget"
    if value in {"交互功能", "功能", ""}:
        return "功能"
    return value


SETTING_GROUP_BY_NAME = {
    "Preset": "General settings",
    "Save location": "General settings",
    "Shutter sound": "General settings",
    "Mirror front camera": "General settings",
    "Level": "General settings",
    "Auto Tone": "Photo settings",
    "Watermark settings": "Photo settings",
    "Tap to take a photo": "Photo settings",
    "QR code scanner": "Photo settings",
    "Press and hold shutter": "Photo settings",
    "Ultra XDR": "Photo settings",
    "Video encoding": "Video settings",
    "Power saving recording": "Video settings",
    "Auto FPS": "Video settings",
    "视频防抖开关": "Video settings",
    "锁定白平衡": "Video settings",
    "锁定镜头": "Video settings",
    "Tips and feedback": "Help & Support",
}

SETTINGS_LEVEL2 = {"General settings", "Photo settings", "Video settings", "Help & Support"}
COMMON_LEVEL1 = {"通用功能", "Preset", "Settings", "Widget"}
PRUNED_NAMES = {"普通场景检测", "运动检测"}


def normalize_level2(value: str) -> str:
    value = as_text(value).strip()
    aliases = {
        "General": "General settings",
        "General setting": "General settings",
        "General settings": "General settings",
        "通用设置": "General settings",
        "通用设置 / General Settings": "General settings",
        "Photo": "Photo settings",
        "Photo setting": "Photo settings",
        "Photo settings": "Photo settings",
        "照片设置": "Photo settings",
        "照片设置 / Photo setting": "Photo settings",
        "照片设置 / Photo Settings": "Photo settings",
        "Video": "Video settings",
        "Video setting": "Video settings",
        "Video settings": "Video settings",
        "视频设置": "Video settings",
        "视频设置 / Video setting": "Video settings",
        "视频设置 / Video Settings": "Video settings",
        "Help": "Help & Support",
        "Help & Support": "Help & Support",
        "帮助与反馈": "Help & Support",
        "帮助与反馈 / Help & Support": "Help & Support",
        "设置 / Settings": "Settings",
        "设置 / Setting": "Settings",
        "预设 / Preset": "Preset",
        "小组件 / Widget": "Widget",
    }
    return aliases.get(value, value)


def settings_level2_for_name(name: str, fallback: str = "Settings") -> str:
    fallback = normalize_level2(fallback)
    if fallback in SETTINGS_LEVEL2:
        return fallback
    return SETTING_GROUP_BY_NAME.get(name, "General settings")


def common_level1_for_level2(level2: str) -> str:
    level2 = normalize_level2(level2)
    if level2 == "Preset":
        return "Preset"
    if level2 == "Widget":
        return "Widget"
    if level2 == "Settings" or level2 in SETTINGS_LEVEL2:
        return "Settings"
    return ""


def clean_legacy_text(value: str) -> str:
    value = as_text(value)
    value = value.replace("Hyper Zoom", "AI Zoom")
    value = value.replace("Top Toolbar", "Toolbar")
    value = value.replace("AIGC SR / AI Zoom", "AI Zoom / AIGC SR")
    value = value.replace("EIS / PZS", "Photo EIS / PZL")
    value = value.replace("4x以上支持", "高倍变焦支持门槛按项目配置确认")
    value = value.replace("虹软AI场景识别算法", "AI 场景检测算法")
    return value


def row_search_text(row: dict[str, str]) -> str:
    searchable_fields = ["模式", "一级分类", "二级分类", "名称", "说明", "验证方法", "备注"]
    return " ".join(as_text(row.get(field)) for field in searchable_fields)


def normalize_legacy_name(row: dict[str, str]) -> None:
    name = row.get("名称", "")
    mode = normalize_mode(row.get("模式", ""))
    if re.search(r"TouchAE|TouchAF|FaceAE|FaceAF|CAF|PDAF|AE&AF|EV\+\-", name, re.I):
        row["名称"] = "自动对焦-自动曝光"
        if not row.get("说明"):
            row["说明"] = "包含自动对焦、自动曝光、点按对焦/测光、人脸对焦/测光、长按锁定和曝光补偿等预览基础能力。"
    elif name in {"AI场景检测", "AI 场景检测"}:
        row["名称"] = "ASD / AI场景检测"
        if not row.get("说明"):
            row["说明"] = "ASD（AI Scene Detection）通过 AI 模型识别绿植、舞台、天空等语义场景，并驱动对应调试策略。"
    elif name in {"SAT", "SAT平滑镜头切换"}:
        row["名称"] = "SAT / 平滑镜头切换"
    elif name in {"FRT / 人脸清晰度增强", "FRT"}:
        row["名称"] = "人脸清晰度增强"
    elif name in {"镜头畸变矫正", "光学畸变矫正/光学畸变校正"}:
        row["名称"] = "光学畸变矫正"
    elif name in {"EIS / PZS", "Photo EIS / PZS"}:
        row["名称"] = "Photo EIS / PZL"
    elif name == "EIS":
        row["名称"] = "Video EIS" if mode in {"视频", "慢动作", "延时摄影", "前后双录"} else "Photo EIS / PZL"
    elif "数码变焦" in name:
        row["名称"] = "变焦"
    elif name == "SR（Zoom）":
        row["名称"] = "SR / Super Resolution"
    elif name in {"AI极夜", "极夜"}:
        row["名称"] = "极夜"
    elif name == "Ultra HDR":
        row["名称"] = "Ultra XDR"
    elif name in {"remosaic单帧", "Remosaic 单帧"}:
        row["名称"] = "Remosaic"
    elif name == "多帧降噪（低ISO）":
        row["名称"] = "多帧降噪"
    elif re.search(r"3s.*10s.*倒计时|倒计时", name):
        row["名称"] = "Timer"
    elif any(term in name for term in ["滤镜强度", "自定义滤镜", "选择一种滤镜"]) or ("滤镜" in name and "场景检测" in name):
        row["名称"] = "Filter"
    elif len([term for term in ["光韵", "映迹", "琥珀", "菲林", "黑白", "负片"] if term in name]) >= 3:
        row["名称"] = "Filter"
    elif all(term in name for term in ["曝光", "对比度", "饱和度", "色温", "颗粒"]):
        row["名称"] = "Tuning"
    elif "50MP" in name and "输出" in name:
        row["名称"] = "Quality"
    elif name in {"Auto HDR", "HDR关"}:
        row["名称"] = "HDR"
    elif name == "Auto tone":
        row["名称"] = "Auto Tone"
    elif name == "EV" or re.search(r"-2.*\+2.*曝光", name):
        row["名称"] = "Exposure"
    elif "网格线" in name:
        row["名称"] = "Grid"
    elif "拍照比例" in name or ("16:9" in name and "1:1" in name):
        row["名称"] = "Ratio"
    elif name == "封面帧支持HDR":
        row["名称"] = "Motion Photo cover HDR"
    elif "无效信息截取" in name:
        row["名称"] = "动态照片 - 无效信息截取"
        if not row.get("说明"):
            row["说明"] = "Motion Photo 动态照片子能力：拍摄时自动截掉按下快门前后明显无效的过渡片段，减少误触、抬手或收手造成的无效动态内容。"
    elif any(term in name for term in ["屏幕补光", "补光 (torchMode)", "Glyph灯"]) or name == "补光":
        row["名称"] = "Flash"


def normalize_legacy_classification(row: dict[str, str]) -> None:
    """Map old FL categories into the current Tree/KB classification."""
    level2 = row.get("二级分类", "")
    name = row.get("名称", "")
    text = f"{level2} {name}"
    algo_realtime = [
        "ASD / AI场景检测",
        "脏污检测",
        "人脸检测",
        "SAT",
        "OIS",
        "EIS",
        "Video EIS",
        "Photo EIS",
        "TouchAE",
        "CAF",
        "PDAF",
        "MFNR",
        "HDR",
    ]
    algo_post = ["FRT", "夜景", "美颜", "畸变矫正", "Remosaic", "SR", "超分", "XDR"]
    if row.get("名称") == "自动对焦-自动曝光":
        row["一级分类"] = "功能"
        row["二级分类"] = "AE/AF"
    elif row.get("名称") == "Auto Tone":
        row["一级分类"] = "Settings"
        row["二级分类"] = "Photo settings"
    elif row.get("名称") in {"Exposure", "Filter", "Flash", "Grid", "HDR", "Motion Photo cover HDR", "Quality", "Ratio", "Timer", "Tuning", "动态照片 - 无效信息截取"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "Toolbar"
    elif level2 in {"底层通用", "底层"}:
        if "数码变焦" in name:
            row["一级分类"] = "功能"
            row["二级分类"] = "Zoom"
        elif any(term in text for term in algo_realtime):
            row["一级分类"] = "基础算法"
            row["二级分类"] = "实时算法"
        elif any(term in text for term in algo_post):
            row["一级分类"] = "基础算法"
            row["二级分类"] = "后处理算法"
        else:
            row["一级分类"] = "基础算法"
            row["二级分类"] = "实时算法"
    elif level2 in {"通用模块"}:
        if row.get("名称") == "自动对焦-自动曝光":
            row["一级分类"] = "功能"
            row["二级分类"] = "AE/AF"
        elif any(term in name for term in ["变焦", "SAT"]):
            row["一级分类"] = "功能"
            row["二级分类"] = "Zoom"
        elif any(term in name for term in ["人脸检测", "普通场景检测", "AI场景检测", "脏污检测"]):
            row["一级分类"] = "功能"
            row["二级分类"] = "预览框"
        elif any(term in name for term in ["极夜", "夜景", "多帧降噪", "Remosaic", "SR", "Ultra XDR", "美颜"]):
            row["一级分类"] = "基础算法"
            row["二级分类"] = "后处理算法"
        elif any(term in name for term in ["Glyph", "补光", "录影灯", "Rec. light", "色彩模式", "比例", "4K", "1080P", "屏幕补光"]):
            row["一级分类"] = "功能"
            row["二级分类"] = "Toolbar"
        else:
            row["一级分类"] = "功能"
            row["二级分类"] = "Toolbar"
    elif level2 in {"滤镜", "闪光灯", "HDR", "动态照片", "倒计时", "Glyph灯", "风格", "高像素", "曝光调节", "网格线", "比例", "水印", "连拍", "色彩模式", "Top Toolbar"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "Toolbar"
    elif level2 in {"畸变矫正", "FRT", "夜景"}:
        row["一级分类"] = "基础算法"
        row["二级分类"] = "后处理算法"
    elif level2 in {"AI Zoom"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "右侧暂态开关"
    elif level2 in {"变焦"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "Zoom"
    elif normalize_level2(level2) in {"Preset", "Settings", "Widget"} | SETTINGS_LEVEL2:
        common_level1 = common_level1_for_level2(level2)
        if common_level1:
            row["一级分类"] = common_level1
            row["二级分类"] = settings_level2_for_name(row.get("名称", ""), level2) if common_level1 == "Settings" else normalize_level2(level2)
    elif level2 in {"EV/ISO/WB/Shutter/Focus"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "Toolbar"
    elif level2 in {"美颜", "单摄虚化"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "Mode Switch"
    elif level2 in {"无交互息屏"}:
        row["一级分类"] = "功能"
        row["二级分类"] = "系统"
    level1 = normalize_level1(row.get("一级分类", ""))
    level2 = normalize_level2(row.get("二级分类", ""))
    name = row.get("名称", "")
    if level1 == "通用功能" and level2 in {"Preset", "Settings", "Widget"} | SETTINGS_LEVEL2:
        level1 = common_level1_for_level2(level2) or level1
    if name in SETTING_GROUP_BY_NAME and level1 in {"通用功能", "功能", "Settings"} and name != "Preset":
        level1 = "Settings"
        level2 = settings_level2_for_name(name, level2)
    if level1 in COMMON_LEVEL1 or level2 in {"Preset", "Widget"} | SETTINGS_LEVEL2:
        row["一级分类"] = level1
        row["二级分类"] = settings_level2_for_name(name, level2) if level1 == "Settings" else level2
        row["模式"] = "通用"


def default_verification(row: dict[str, str]) -> str:
    level1 = row.get("一级分类", "")
    level2 = row.get("二级分类", "")
    name = row.get("名称", "")
    if level2 == "AE/AF":
        return "在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。"
    if level2 == "Zoom":
        return "在对应模式点击默认变焦点并拖动变焦条，确认倍率范围、镜头切换、画质和稳定性符合项目规格。"
    if level2 == "预览框":
        return "在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。"
    if level2 == "Toolbar":
        return "在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。"
    if level1 == "Settings" or level2 == "Settings" or level2 in SETTINGS_LEVEL2:
        return "进入 Camera Settings 修改该项，返回对应模式后确认设置生效、持久化和默认值符合规格。"
    if level2 == "Mode Switch":
        return "滑动模式栏进入对应模式，确认入口展示、默认状态、退出恢复和拍摄/录制流程符合规格。"
    if level2 in {"左侧暂态开关", "右侧暂态开关"}:
        return "在满足触发条件的场景确认暂态开关出现；切换开关后确认预览、拍摄和状态恢复符合规格。"
    if level1 == "基础算法" and level2 == "后处理算法":
        return "按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。"
    if level1 == "基础算法":
        return "按项目算法规格在对应镜头、倍率、分辨率或帧率下测试，确认预览/录制稳定和效果符合规格。"
    return f"按项目 FL 规格确认 `{name}` 的入口、支持范围、默认值和结果表现。"


def repair_legacy_current_row(row: dict[str, str], project: str, source: str) -> None:
    if source != "current-fl-records-26111-26121.json":
        return
    validation = row.get("验证方法", "").strip()
    weak_validation = validation in {"", "✓", "✗"}
    if validation in {"", "✓", "✗"}:
        row["验证方法"] = default_verification(row)
        row["状态"] = "待确认"
    if row.get("二级分类") == "AE/AF":
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = "TBD"
    elif weak_validation and (row.get("二级分类") in {"预览框", "Zoom"} or row.get("一级分类") == "基础算法"):
        for cam in PROJECTS[project]["cameras"]:
            if row.get(cam) in {"", "✓", "✗"}:
                row[cam] = "TBD"
    if row.get("名称") == "AI Zoom":
        row["验证方法"] = "在 30x 以上场景确认 AI Zoom 暂态开关是否出现；点击后拍摄高细节目标，检查成片清晰度和生成伪影。"
        row["状态"] = "待确认"
        for cam in PROJECTS[project]["cameras"]:
            if project == "26121" and cam == "Tele":
                row[cam] = "TBD"
            else:
                row[cam] = "✗"
    elif row.get("名称") == "EIS":
        row["验证方法"] = "根据项目防抖规格，在对应镜头、倍率或视频规格下手持移动测试，确认预览/成片稳定和视角裁切。"
        row["状态"] = "待确认"
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = "TBD"


def owner_for(row: dict[str, str]) -> str:
    text = f"{row.get('一级分类','')} {row.get('二级分类','')} {row.get('名称','')}"
    if row.get("一级分类") == "基础算法" or any(term in text for term in ["算法", "HDR", "EIS", "OIS", "SAT", "ISZ", "Remosaic", "SR", "FRT", "人脸", "场景检测"]):
        return "影像 SE"
    if any(term in text for term in ["Tuning", "滤镜", "Style", "Photo Style", "Preset", "风格", "调色"]):
        return "PM / Tuning"
    if any(term in text for term in ["Settings", "setting", "设置", "编码", "Auto FPS", "Lock"]):
        return "PM / QA"
    return "PM / QA / SE"


def status_for(row: dict[str, str]) -> str:
    text = json.dumps(row, ensure_ascii=False)
    if "Pending" in text:
        return "Pending"
    if "TBD" in text or "待确认" in text or "[TBD]" in text:
        return "待确认"
    return as_text(row.get("状态")) or "待确认"


def row_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (
        as_text(row.get("模式")),
        normalize_level1(row.get("一级分类", "")),
        normalize_level2(row.get("二级分类", "")),
        as_text(row.get("名称")),
    )


def should_prune_row(row: dict[str, str]) -> bool:
    return as_text(row.get("名称")) in PRUNED_NAMES


def normalize_row(row: dict, project: str, source: str) -> dict[str, str]:
    out = {col: "" for col in FINAL_COLUMNS}
    for col in ["模式", "一级分类", "二级分类", "名称", "说明", "状态", "验证方法", "备注"]:
        out[col] = clean_legacy_text(row.get(col))
    if not out["验证方法"]:
        out["验证方法"] = clean_legacy_text(row.get("验证"))
    out["模式"] = normalize_mode(out["模式"])
    out["一级分类"] = normalize_level1(out["一级分类"])
    out["二级分类"] = normalize_level2(out["二级分类"])
    normalize_legacy_name(out)
    normalize_legacy_classification(out)
    out["来源"] = source
    for cam in PROJECTS[project]["cameras"]:
        out[cam] = as_text(row.get(cam)) or as_text(row.get(f"{project} {cam}"))
    for cam in {"Main", "UW", "Tele", "Front"} - set(PROJECTS[project]["cameras"]):
        out[cam] = ""
    out["确认负责人"] = as_text(row.get("确认负责人")) or owner_for(out)
    out["状态"] = status_for(out)
    repair_legacy_current_row(out, project, source)
    return out


def merge_row(rows: dict[tuple[str, str, str, str], dict[str, str]], row: dict[str, str], prefer_new: bool = False) -> None:
    key = row_key(row)
    if key not in rows:
        rows[key] = row
        return
    current = rows[key]
    for field in FINAL_COLUMNS:
        if field in {"Main", "UW", "Tele", "Front"}:
            if prefer_new or not current.get(field) or current.get(field) in {"TBD", "[TBD]"}:
                current[field] = row.get(field, current.get(field, ""))
        elif prefer_new and row.get(field):
            current[field] = row[field]
        elif not current.get(field) and row.get(field):
            current[field] = row[field]
    if row.get("来源") and row["来源"] not in current.get("来源", ""):
        current["来源"] = (current.get("来源", "") + "; " + row["来源"]).strip("; ")
    if row.get("备注") and row["备注"] not in current.get("备注", ""):
        current["备注"] = (current.get("备注", "") + " | " + row["备注"]).strip(" |")
    current["状态"] = "待确认" if "待确认" in {current.get("状态"), row.get("状态")} else current.get("状态", row.get("状态", ""))


def apply_canonical_support_overrides(row: dict[str, str], project: str) -> None:
    """Keep merged rows aligned with canonical camera-scope rules."""
    name = row.get("名称", "")
    cameras = PROJECTS[project]["cameras"]
    if name == "SAT / 平滑镜头切换":
        for cam in cameras:
            row[cam] = "✗" if cam == "Front" else "✓"
    elif name == "前后双录后置镜头选择":
        for cam in cameras:
            row[cam] = "✗" if cam == "Front" else "✓"


def parse_markdown_table(md: str, heading: str) -> list[dict[str, str]]:
    idx = md.find(heading)
    if idx == -1:
        return []
    tail = md[idx:]
    lines = tail.splitlines()
    table_lines: list[str] = []
    in_table = False
    for line in lines:
        if line.startswith("|"):
            table_lines.append(line)
            in_table = True
        elif in_table:
            break
    if len(table_lines) < 3:
        return []
    headers = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    rows = []
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def support_from_algo(algo: dict[str, str], project: str, cam: str) -> str:
    value = algo.get(f"{project} {cam}", "")
    if value == "[TBD]":
        return "TBD"
    return value or "✗"


def add_algorithm_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    md = ALGO_MD.read_text(encoding="utf-8")
    for item in parse_markdown_table(md, "## Algorithm Rows For FL"):
        for mode in split_modes(item["模式"]):
            row = {col: "" for col in FINAL_COLUMNS}
            row.update(
                {
                    "模式": mode,
                    "一级分类": "基础算法",
                    "二级分类": item["二级分类"],
                    "名称": clean_legacy_text(item["名称"]),
                    "说明": clean_legacy_text(item["说明"]),
                    "状态": "待确认" if "TBD" in json.dumps(item, ensure_ascii=False) else "待确认",
                    "确认负责人": "影像 SE",
                    "验证方法": clean_legacy_text(item["验证方法"]),
                    "来源": "algorithm-fl-source-26111-26121.md",
                    "备注": "算法来源行，需 SE 按项目实测确认。",
                }
            )
            for cam in PROJECTS[project]["cameras"]:
                row[cam] = support_from_algo(item, project, cam)
            merge_row(rows, row)


def heuristic_support(row: dict[str, str], project: str, cam: str) -> str:
    text = row_search_text(row)
    name = row.get("名称", "")
    mode = row.get("模式", "")
    if cam not in PROJECTS[project]["cameras"]:
        return ""
    if row.get("一级分类") in COMMON_LEVEL1 or row.get("二级分类") in {"Settings", "Preset", "Widget", "Mode Switch"} | SETTINGS_LEVEL2 or mode == "通用":
        return "✓"
    if name == "SAT / 平滑镜头切换":
        return "✗" if cam == "Front" else "✓"
    if name == "Video EIS":
        return "✓"
    if "前置" in text or "front" in text.lower():
        return "✓" if cam == "Front" else "✗"
    if mode == "高像素" or any(term in name for term in ["Remosaic", "高像素", "200MP", "50MP"]):
        if project == "26111":
            return "✓" if cam == "Main" else "✗"
        return "✓" if cam in {"Main", "Tele"} else "✗"
    if any(term in text for term in ["长焦", "Tele", "AI Zoom", "AIGC SR"]):
        return "✓" if project == "26121" and cam == "Tele" else "✗"
    return "TBD"


def add_kb_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    for item in json.loads(KB.read_text(encoding="utf-8")):
        for mode in split_modes(item["模式"]):
            level1 = normalize_level1(item["一级分类"])
            level2 = normalize_level2("Toolbar" if item["二级分类"] == "Top Toolbar" else item["二级分类"])
            if level1 == "通用功能":
                level1 = common_level1_for_level2(level2) or level1
            row = {col: "" for col in FINAL_COLUMNS}
            row.update(
                {
                    "模式": mode,
                    "一级分类": level1,
                    "二级分类": settings_level2_for_name(item["名称"], level2) if level1 == "Settings" else level2,
                    "名称": item["名称"],
                    "说明": item["说明"],
                    "状态": "待确认",
                    "确认负责人": owner_for(item),
                    "验证方法": item["验证方法"],
                    "来源": "kb-functions-algorithms.json",
                    "备注": "由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。",
                }
            )
            for cam in PROJECTS[project]["cameras"]:
                row[cam] = heuristic_support(row, project, cam)
            merge_row(rows, row)


VIDEO_SPEC_SUPPORT = {
    "26111": {
        "1080P 30FPS": {"Main": "✓", "UW": "✓", "Front": "✓"},
        "1080P 60FPS": {"Main": "✗", "UW": "✗", "Front": "✗"},
        "4K 30FPS": {"Main": "✗", "UW": "TBD", "Front": "✓"},
        "4K 60FPS": {"Main": "✗", "UW": "✗", "Front": "✗"},
        "1080P 30FPS HLG": {"Main": "✓", "UW": "✓", "Front": "TBD"},
        "1080P 60FPS HLG": {"Main": "✗", "UW": "✗", "Front": "✗"},
        "4K 30FPS HLG": {"Main": "✗", "UW": "TBD", "Front": "TBD"},
        "4K 60FPS HLG": {"Main": "✗", "UW": "✗", "Front": "✗"},
    },
    "26121": {
        "1080P 30FPS": {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✓"},
        "1080P 60FPS": {"Main": "✓", "UW": "TBD", "Tele": "✓", "Front": "✗"},
        "4K 30FPS": {"Main": "✓", "UW": "TBD", "Tele": "✓", "Front": "✓"},
        "4K 60FPS": {"Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✗"},
        "1080P 30FPS HLG": {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "TBD"},
        "1080P 60FPS HLG": {"Main": "✓", "UW": "TBD", "Tele": "✓", "Front": "✗"},
        "4K 30FPS HLG": {"Main": "✓", "UW": "TBD", "Tele": "✓", "Front": "TBD"},
        "4K 60FPS HLG": {"Main": "TBD", "UW": "✗", "Tele": "TBD", "Front": "✗"},
    },
}


VIDEO_SPEC_DESCRIPTIONS = {
    "1080P 30FPS": "视频基础规格。普通视频模式下 1080P 30fps 录制能力，每个摄像头独立确认。",
    "1080P 60FPS": "视频高帧率规格。普通视频模式下 1080P 60fps 录制能力，每个摄像头独立确认。",
    "4K 30FPS": "视频 4K 30fps 规格。前置 4K 视频需求落在该行，不再单独保留“前置 4K 视频”行。",
    "4K 60FPS": "视频 4K 60fps 规格。P0 当前仅标注 26121 Pro 主摄&长焦 4K60。",
    "1080P 30FPS HLG": "视频 HLG/HDR 规格。普通视频模式下 1080P 30fps HLG 录制能力，每个摄像头独立确认。",
    "1080P 60FPS HLG": "视频 HLG/HDR 规格。普通视频模式下 1080P 60fps HLG 录制能力，每个摄像头独立确认。",
    "4K 30FPS HLG": "视频 HLG/HDR 规格。普通视频模式下 4K 30fps HLG 录制能力，每个摄像头独立确认。",
    "4K 60FPS HLG": "视频 HLG/HDR 规格。普通视频模式下 4K 60fps HLG 录制能力，每个摄像头独立确认。",
}


SLOW_MOTION_SPEC_SUPPORT = {
    "26111": {
        "1080P 30FPS": {"Main": "TBD", "UW": "TBD", "Front": "TBD"},
        "1080P 120FPS": {"Main": "TBD", "UW": "TBD", "Front": "TBD"},
        "1080P 240FPS": {"Main": "TBD", "UW": "TBD", "Front": "TBD"},
        "720P 120FPS": {"Main": "TBD", "UW": "TBD", "Front": "TBD"},
        "720P 240FPS": {"Main": "TBD", "UW": "TBD", "Front": "TBD"},
        "720P 480FPS": {"Main": "TBD", "UW": "TBD", "Front": "TBD"},
    },
    "26121": {
        "1080P 30FPS": {"Main": "TBD", "UW": "TBD", "Tele": "TBD", "Front": "TBD"},
        "1080P 120FPS": {"Main": "TBD", "UW": "TBD", "Tele": "TBD", "Front": "TBD"},
        "1080P 240FPS": {"Main": "TBD", "UW": "TBD", "Tele": "TBD", "Front": "TBD"},
        "720P 120FPS": {"Main": "TBD", "UW": "TBD", "Tele": "TBD", "Front": "TBD"},
        "720P 240FPS": {"Main": "TBD", "UW": "TBD", "Tele": "TBD", "Front": "TBD"},
        "720P 480FPS": {"Main": "TBD", "UW": "TBD", "Tele": "TBD", "Front": "TBD"},
    },
}


HIGH_RES_OPTION_SUPPORT = {
    "26111": {
        "50MP": {"Main": "✓", "UW": "✗", "Front": "✗"},
        "200MP": {"Main": "✓", "UW": "✗", "Front": "✗"},
        "200MP Ultra": {"Main": "✓", "UW": "✗", "Front": "✗"},
    },
    "26121": {
        "50MP": {"Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✗"},
        "50MP Ultra": {"Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✗"},
    },
}


def add_video_spec_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    for spec, supports in VIDEO_SPEC_SUPPORT[project].items():
        row = {col: "" for col in FINAL_COLUMNS}
        row.update(
            {
                "模式": "视频",
                "一级分类": "功能",
                "二级分类": "Video Specs",
                "名称": spec,
                "说明": VIDEO_SPEC_DESCRIPTIONS[spec],
                "状态": "待确认",
                "确认负责人": "PM / SE / QA",
                "验证方法": f"切到视频模式，分别选择 {spec}，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。",
                "来源": "generated-video-spec-matrix",
                "备注": "初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。",
            }
        )
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = supports.get(cam, "✗")
        merge_row(rows, row, prefer_new=True)


def add_slow_motion_spec_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    for spec, supports in SLOW_MOTION_SPEC_SUPPORT[project].items():
        row = {col: "" for col in FINAL_COLUMNS}
        row.update(
            {
                "模式": "慢动作",
                "一级分类": "功能",
                "二级分类": "Slow Motion Specs",
                "名称": spec,
                "说明": f"慢动作模式录制规格：{spec}。慢动作模式支持本身已确认，具体规格按摄像头独立打勾/打叉。",
                "状态": "待确认",
                "确认负责人": "PM / SE / QA",
                "验证方法": f"切到慢动作模式，选择 {spec}，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。",
                "来源": "generated-slow-motion-spec-matrix",
                "备注": "按 PM 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/QA 填写最终支持列。",
            }
        )
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = supports.get(cam, "✗")
        merge_row(rows, row, prefer_new=True)


def add_high_res_option_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    for option, supports in HIGH_RES_OPTION_SUPPORT[project].items():
        is_ultra = "Ultra" in option
        desc = (
            f"高像素模式输出选项：{option}。"
            "高像素链路使用 remosaic；Ultra 选项在 remosaic 后叠加 RAW HDR 以提升清晰度和画质。"
            if is_ultra
            else f"高像素模式输出选项：{option}。该选项使用 remosaic 高像素输出链路。"
        )
        row = {col: "" for col in FINAL_COLUMNS}
        row.update(
            {
                "模式": "高像素",
                "一级分类": "功能",
                "二级分类": "Mode Switch",
                "名称": option,
                "说明": desc,
                "状态": "待确认",
                "确认负责人": "PM / SE / QA",
                "验证方法": f"进入高像素模式选择 {option}，逐个支持摄像头拍摄并确认入口、分辨率、处理耗时、RAW HDR/Ultra 标记和成片画质。",
                "来源": "generated-high-res-options",
                "备注": "按 PM 口径：26111 支持 50MP / 200MP / 200MP Ultra；26121 支持 50MP / 50MP Ultra。",
            }
        )
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = supports.get(cam, "✗")
        merge_row(rows, row, prefer_new=True)


def add_video_toolbar_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    definitions = [
        {
            "名称": "Filter",
            "说明": "视频模式滤镜能力。摄像头列表示该摄像头在视频模式存在可用滤镜链路；前置 4K PRD 明确 4K 前置当前不支持 Filter/Tuning，因为仅 1080P pipeline 支持。",
            "验证方法": "视频模式选择滤镜后录制 1080P30/1080P60/4K30/4K60 样片，确认预览、成片滤镜、规格互斥和降级提示。",
        },
        {
            "名称": "Style",
            "说明": "视频模式风格能力，用于记录视频是否支持类似 Filter/Tuning/Style 的风格化效果。摄像头列表示视频模式存在可用风格链路；4K/60fps 互斥需按规格进一步确认。",
            "验证方法": "视频模式选择风格或调色效果后录制，确认入口、预览、成片、Preset 保存关系，以及 4K/60fps 互斥策略。",
        },
    ]
    for item in definitions:
        row = {col: "" for col in FINAL_COLUMNS}
        row.update(
            {
                "模式": "视频",
                "一级分类": "功能",
                "二级分类": "Toolbar",
                "名称": item["名称"],
                "说明": item["说明"],
                "状态": "待确认",
                "确认负责人": "PM / SE / QA",
                "验证方法": item["验证方法"],
                "来源": "generated-video-toolbar-rules",
                "备注": "由前置 4K 互斥表、VSS 说明和 PM 反馈补齐；具体规格互斥需继续确认。",
            }
        )
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = "✓"
        merge_row(rows, row, prefer_new=False)


def add_dual_view_v2_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    supports_rear_choice = {
        "26111": {"Main": "✓", "UW": "✓", "Front": "✗"},
        "26121": {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✗"},
    }[project]
    definitions = [
        {
            "模式": "前后双录",
            "一级分类": "功能",
            "二级分类": "预览框",
            "名称": "前后双录后置镜头选择",
            "说明": "前后双录预览中的后置镜头选择入口。26111 支持主摄/超广角；26121 Pro 支持主摄/超广角/长焦。",
            "验证方法": "进入前后双录，在预览中切换后置镜头，确认可选镜头、预览布局、录制结果和切换状态符合规格。",
            "supports": supports_rear_choice,
        },
        {
            "模式": "前后双录",
            "一级分类": "功能",
            "二级分类": "预览框",
            "名称": "前后双录主副互换 / 小窗大小",
            "说明": "前后双录预览交互能力，支持主副画面互换和 PiP 小窗大小调整。",
            "验证方法": "进入前后双录，切换主副画面并调整小窗大小，录制后确认画面布局和文件结果一致。",
            "supports": {cam: "✓" for cam in PROJECTS[project]["cameras"]},
        },
        {
            "模式": "通用",
            "一级分类": "Settings",
            "二级分类": "Video settings",
            "名称": "前后双录分开保存",
            "说明": "视频设置项。控制前后双录结果按合并文件或前后路分开保存。",
            "验证方法": "进入 Settings > Video 切换前后双录分开保存，录制前后双录样片并确认文件数量、命名、音画同步和相册展示。",
            "supports": {cam: "✓" for cam in PROJECTS[project]["cameras"]},
        },
    ]
    for item in definitions:
        row = {col: "" for col in FINAL_COLUMNS}
        row.update(
            {
                "模式": item["模式"],
                "一级分类": item["一级分类"],
                "二级分类": item["二级分类"],
                "名称": item["名称"],
                "说明": item["说明"],
                "状态": "待确认",
                "确认负责人": "PM / SE / QA",
                "验证方法": item["验证方法"],
                "来源": "generated-dual-view-v2-rules",
                "备注": "由 PM 口径拆分前后双录 v2：后置镜头选择归预览；split-save 归 Settings；Pro tele、Filter/Tuning 支持。",
            }
        )
        for cam in PROJECTS[project]["cameras"]:
            row[cam] = item["supports"].get(cam, "✗")
        merge_row(rows, row, prefer_new=True)


def add_log_video_row(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    row = {col: "" for col in FINAL_COLUMNS}
    row.update(
        {
            "模式": "视频",
            "一级分类": "功能",
            "二级分类": "Toolbar",
            "名称": "Log 视频",
            "说明": "视频 Toolbar 中的 Log 拍摄功能，用于以 Log 曲线录制视频；需在说明/规格中写清支持的分辨率、帧率、镜头和编码范围。",
            "状态": "待确认",
            "确认负责人": "PM / SE / QA",
            "验证方法": "在视频 Toolbar 开启 Log，按支持规格录制样片，确认入口、编码/位深、颜色曲线、LUT 还原、相册识别和不支持规格的置灰/提示。",
            "来源": "generated-log-video-toolbar-rule",
            "备注": "按 PM 口径：Log 放在视频 Toolbar；支持规格范围仍需根据项目 PRD/平台能力补齐。",
        }
    )
    for cam in PROJECTS[project]["cameras"]:
        if project == "26121" and cam in {"Main", "Tele"}:
            row[cam] = "TBD"
        else:
            row[cam] = "✗"
    merge_row(rows, row, prefer_new=True)


def candidate_modes(item: dict[str, str]) -> list[str]:
    req = item["requirement"]
    label = item.get("proposed_tree_label", "")
    if "前置自动小广角" in req:
        return ["照片"]
    if "镜头脏污" in req:
        return ["照片", "人像"]
    if "专业模式" in req:
        return ["专业"]
    if "AI Preset" in req:
        return ["通用"]
    if "200MP" in req or "高像素" in req:
        return ["高像素"]
    if any(term in req for term in ["视频", "EIS", "H.265", "锁定白平衡", "锁定镜头", "前置 4K", "VSS", "Log"]):
        if "前后双录" in req:
            return ["前后双录"]
        return ["视频"]
    if "前后双录" in req:
        return ["前后双录"]
    if "人像" in req or "美颜" in req:
        return ["人像"]
    if "SAT" in req:
        return ["照片", "视频", "夜景", "延时摄影"]
    if "Tuning" in req or "照片风格" in req:
        return ["照片", "人像", "夜景", "专业", "高像素"]
    if "运动场景引导" in req:
        return ["照片"]
    if "Tips" in req:
        return ["通用"]
    if "二维码" in req or "识别框" in req:
        return ["照片"]
    if "ISZ" in req:
        return ["视频"]
    if "相机设计" in req:
        return ["通用"]
    if "Mode Switch" in label:
        return ["通用"]
    return ["通用"]


def candidate_level2(label: str) -> str:
    if "Settings" in label or "设置" in label:
        if "Video" in label or "视频" in label:
            return "Video settings"
        if "Photo" in label or "照片" in label:
            return "Photo settings"
        if "Help" in label or "Support" in label or "Tips" in label or "反馈" in label:
            return "Help & Support"
        return "General settings"
    for part in ["预览框", "AE/AF", "Zoom", "Toolbar", "Top Toolbar", "Mode Switch", "Preset", "Widget", "左侧暂态开关", "右侧暂态开关"]:
        if part in label:
            return "Toolbar" if part == "Top Toolbar" else part
    return "预览框" if "AI Preset" in label else "Toolbar"


def candidate_support(item: dict[str, str], project: str, cam: str, mode: str) -> str:
    text = json.dumps(item, ensure_ascii=False)
    req = item["requirement"]
    if cam not in PROJECTS[project]["cameras"]:
        return ""
    if item.get("dispute_level") == "high":
        if "200MP" in req and project == "26121":
            return "✗"
        return "TBD"
    if item.get("kb_name") == "Photo Style" or "照片风格" in req:
        return "✗" if cam == "Front" else "✓"
    if "前置自动小广角" in req:
        return "✓" if cam == "Front" else "✗"
    if "前置 4K" in req:
        return "✓" if cam == "Front" else "✗"
    if "镜头脏污" in req:
        return "✓" if cam in {"Main", "Front"} else "TBD"
    if "200MP" in req:
        return "✓" if project == "26111" and cam == "Main" else "✗"
    if "高像素" in req:
        return "✓" if (project == "26111" and cam == "Main") or (project == "26121" and cam in {"Main", "Tele"}) else "✗"
    if "人像" in req or "美颜" in req:
        return "✓" if cam in {"Main", "Tele", "Front"} else "✗"
    if "长焦" in text:
        return "✓" if project == "26121" and cam == "Tele" else "✗"
    if "4K 60" in text or "Video HDR" in text:
        return "✓" if project == "26121" and cam in {"Main", "Tele"} else "✗"
    if "AI Zoom" in text:
        return "✓" if project == "26121" and cam == "Tele" else "✗"
    return "TBD" if item.get("dispute_level") == "medium" else "✓"


def add_candidate_rows(project: str, rows: dict[tuple[str, str, str, str], dict[str, str]]) -> None:
    for item in json.loads(CANDIDATES.read_text(encoding="utf-8")):
        if item.get("requirement") == "前置 4K 视频":
            continue
        if item.get("candidate_id") in {"REQ26111-KB-009", "REQ26111-KB-021", "REQ26111-KB-029"}:
            continue
        if item.get("candidate_id") == "REQ26111-KB-007":
            # Tuning Palette is an update to the existing Tuning capability.
            # Do not create a separate "Style / Tuning Palette / Palette-Parameters"
            # row; it duplicates Photo Style and Tuning in the final FL.
            for row in rows.values():
                if row.get("名称") != "Tuning":
                    continue
                row["说明"] = (
                    "Tuning / Tuning Palette 调色能力：包含 Palette Mode、Parameter Mode、Strength "
                    "与 7 参数精调。当前 PRD 明确 Filter 与 Tuning 暂不合并；"
                    "Style / Filter+Tuning 只作为后续方向，不单独生成 FL 行。"
                )
                row["验证方法"] = (
                    "打开 Tuning，分别验证 Palette Mode、Parameter Mode、Strength、7 参数调节、"
                    "Reset、Preset 保存/恢复，以及与 Filter、Photo Style 的叠加顺序。"
                )
                row["确认负责人"] = "PM / Tuning"
                if item.get("notes") and item["notes"] not in row.get("备注", ""):
                    row["备注"] = (row.get("备注", "") + " | " + clean_legacy_text(item["notes"])).strip(" |")
                if "tree-kb-integration-candidates.v1.json" not in row.get("来源", ""):
                    row["来源"] = (row.get("来源", "") + "; tree-kb-integration-candidates.v1.json").strip("; ")
            continue
        for mode in candidate_modes(item):
            level2 = candidate_level2(item.get("proposed_tree_label", ""))
            level1 = common_level1_for_level2(level2) or "功能"
            normalized_mode = "通用" if level1 in COMMON_LEVEL1 else mode
            description = clean_legacy_text(item.get("fl_impact", ""))
            verification = clean_legacy_text(item.get("manual_review_question", ""))
            note = clean_legacy_text(f"{item['candidate_id']} | {item.get('proposed_tree_action')} | dispute={item.get('dispute_level')} | {item.get('notes','')}")
            if item.get("kb_name") == "Tips and feedback":
                description = "Camera Settings 中的帮助与反馈入口，跳转系统 Tips and feedback；Camera 内不自建反馈表单。"
                verification = "进入 Camera Settings 点击 Tips and feedback，确认跳转系统帮助/反馈入口，并能返回 Camera。"
                note = f"{item['candidate_id']} | Help & Support group added in Common Settings taxonomy."
            elif item.get("kb_name") == "Video encoding":
                verification = "切换 H.264/H.265 后分别录制普通视频、慢动作、延时摄影和前后双录样片，确认文件编码、默认 H.265 策略、HLG 强制 H.265 以及异常提示符合规格。"
            elif item.get("kb_name") == "视频防抖开关":
                verification = "进入 Settings > Video 切换视频防抖开关，在支持 EIS 的视频规格下录制并确认防抖开关生效；在不支持规格下确认置灰或隐藏策略。"
            elif item.get("kb_name") == "锁定白平衡":
                verification = "开启锁定白平衡后在不同色温光源间移动录制，确认白平衡保持起始状态；关闭后确认 WB 正常收敛。"
            elif item.get("kb_name") == "锁定镜头":
                verification = "开启锁定镜头后开始录制，跨镜头倍率点变焦，确认不发生物理镜头切换且录制不中断。"
            row = {col: "" for col in FINAL_COLUMNS}
            row.update(
                {
                    "模式": normalized_mode,
                    "一级分类": level1,
                    "二级分类": level2,
                    "名称": item.get("kb_name") or item["requirement"],
                    "说明": description,
                    "状态": "待确认" if item.get("dispute_level") in {"medium", "high"} else "待确认",
                    "确认负责人": "PM / SE" if item.get("dispute_level") in {"medium", "high"} else "PM / QA",
                    "验证方法": verification,
                    "来源": "tree-kb-integration-candidates.v1.json",
                    "备注": note,
                }
            )
            for cam in PROJECTS[project]["cameras"]:
                row[cam] = candidate_support(item, project, cam, normalized_mode)
            merge_row(rows, row, prefer_new=True)


def unsupported_reason(row: dict[str, str], project: str, cam: str) -> str:
    name = row.get("名称", "")
    mode = row.get("模式", "")
    level2 = row.get("二级分类", "")
    text = row_search_text(row)
    if row.get(cam) != "✗":
        return ""

    if name == "动态照片 - 无效信息截取":
        if mode != "照片":
            return "该子能力属于 Motion Photo 动态照片拍照链路，当前模式不支持动态照片。"
        return "当前基线 FL 未覆盖该摄像头的 Motion Photo 无效片段裁剪链路，需 PM/SE 确认是否纳入。"
    if name == "Photo Style" and cam == "Front":
        return "Photo Style PRD 当前范围为后置自然/鲜明风格，前置风格未纳入本期。"

    if mode == "视频" and level2 == "Video Specs":
        if project == "26111":
            if name.startswith("1080P 60FPS"):
                return "26111 Base 项目配置标注无 1080P60。"
            if name.startswith("4K 30FPS"):
                if cam == "Main":
                    return "26111 Base 项目配置标注无通用 4K；当前仅前置 4K PRD 明确进入评估。"
                return "当前 4K30 未确认支持该摄像头。"
            if name.startswith("4K 60FPS"):
                return "26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。"
        if project == "26121":
            if name.startswith("1080P 60FPS") and cam == "Front":
                return "前置 4K PRD 互斥表明确 60fps 不支持。"
            if name.startswith("4K 60FPS"):
                if cam == "UW":
                    return "P0 仅标注 Pro 主摄&长焦 4K60，未覆盖超广角。"
                if cam == "Front":
                    return "前置 4K PRD 互斥表明确 4K 锁定 30fps。"
        if "HLG" in name:
            return "当前项目资料未标注该摄像头支持此 HLG/HDR 视频规格。"
        return "当前项目资料未标注该摄像头支持此视频规格。"

    if mode == "慢动作" and level2 == "Slow Motion Specs":
        return "当前项目资料未标注该摄像头支持此慢动作规格。"

    if "前置" in text or "front" in text.lower():
        return "该功能限定前置摄像头。"
    if any(term in name for term in ["AI Zoom", "AIGC SR"]) or "长焦" in text:
        return "依赖长焦/高倍率链路，该摄像头不在支持范围。"
    if mode == "高像素" or any(term in name for term in ["200MP", "50MP", "Remosaic", "高像素"]):
        return "依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。"
    if cam == "Front" and any(term in name for term in ["Flash", "Glyph", "Glyph Mirror"]):
        return "前置无后置闪光灯/Glyph 硬件链路。"
    if cam == "UW" and any(term in name for term in ["OIS", "AI Zoom"]):
        return "超广角无对应 OIS/长焦高倍链路。"
    return "按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。"


def finalize_row(row: dict[str, str], project: str) -> dict[str, str]:
    cameras = PROJECTS[project]["cameras"]
    reasons = []
    for cam in cameras:
        reason = unsupported_reason(row, project, cam)
        if reason:
            reasons.append(f"{cam}: {reason}")
    row["不支持原因"] = "；".join(reasons)
    values = [row.get(cam, "") for cam in cameras]
    if values and all(value in {"✓", "✗"} for value in values):
        row["状态"] = "已确认"
    elif any(value == "TBD" for value in values):
        row["状态"] = "待确认"
    return row


def sorted_rows(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    mode_order = {m: i for i, m in enumerate(ALL_MODES + ["通用"])}
    capture_level_order = {"功能": 0, "基础算法": 1, "Preset": 2, "Settings": 3, "Widget": 4, "通用功能": 5}
    common_level_order = {"Preset": 0, "Settings": 1, "Widget": 2, "功能": 3, "基础算法": 4, "通用功能": 5}
    level2_order = {
        "Preset": 0,
        "General settings": 10,
        "Photo settings": 11,
        "Video settings": 12,
        "Help & Support": 13,
        "Widget": 20,
    }

    def level_sort(row: dict[str, str]) -> int:
        if row.get("模式") == "通用":
            return common_level_order.get(row.get("一级分类", ""), 9)
        return capture_level_order.get(row.get("一级分类", ""), 9)

    return sorted(
        rows,
        key=lambda r: (
            mode_order.get(r.get("模式", ""), 99),
            level_sort(r),
            level2_order.get(r.get("二级分类", ""), 99),
            r.get("二级分类", ""),
            r.get("名称", ""),
        ),
    )


def display_row(row: dict[str, str]) -> dict[str, str]:
    rendered = dict(row)
    level1 = row.get("一级分类", "")
    level2 = normalize_level2(row.get("二级分类", ""))
    mode = row.get("模式", "")
    rendered["模式"] = MODE_DISPLAY.get(mode, mode)
    rendered["一级分类"] = LEVEL1_DISPLAY.get(level1, level1)
    rendered["二级分类"] = LEVEL2_DISPLAY.get(level2, level2)
    return rendered


def display_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [display_row(row) for row in rows]


def write_csv(path: Path, rows: list[dict[str, str]], project: str) -> None:
    hidden_columns = {"来源", "备注"}
    columns = [c for c in FINAL_COLUMNS if (c not in {"Tele"} or "Tele" in PROJECTS[project]["cameras"]) and c not in hidden_columns]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({col: row.get(col, "") for col in columns})


def write_markdown(path: Path, rows: list[dict[str, str]], project: str) -> None:
    columns = [c for c in ["模式", "一级分类", "二级分类", "名称", *PROJECTS[project]["cameras"], "不支持原因", "状态", "确认负责人", "验证方法"]]
    lines = [f"# {project} Camera FL Draft", "", f"> {PROJECTS[project]['note']}", "", f"Rows: {len(rows)}", ""]
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("|" + "|".join(["---"] * len(columns)) + "|")
    for row in rows:
        vals = [str(row.get(c, "")).replace("\n", " ").replace("|", "/") for c in columns]
        lines.append("| " + " | ".join(vals) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def audit(project_rows: dict[str, list[dict[str, str]]]) -> str:
    lines = ["# 26111 / 26121 FL Draft Audit", ""]
    lines.append("This is a distribution draft, not final acceptance sign-off.")
    lines.append("")
    for project, rows in project_rows.items():
        lines.append(f"## {project}")
        lines.append("")
        status_counts = Counter(r.get("状态", "") for r in rows)
        mode_counts = Counter(r.get("模式", "") for r in rows)
        tbd_rows = [r for r in rows if "TBD" in json.dumps(r, ensure_ascii=False) or r.get("状态") == "待确认"]
        dupes = [key for key, count in Counter(row_key(r) for r in rows).items() if count > 1]
        lines.append(f"- Rows: {len(rows)}")
        lines.append(f"- Status: {dict(status_counts)}")
        lines.append(f"- Modes: {dict(mode_counts)}")
        lines.append(f"- Rows needing fill/review: {len(tbd_rows)}")
        lines.append(f"- Duplicate keys: {len(dupes)}")
        lines.append("")
        if tbd_rows:
            lines.append("### Review Queue")
            lines.append("")
            lines.append("| 模式 | 一级分类 | 二级分类 | 名称 | owner | reason |")
            lines.append("|---|---|---|---|---|---|")
            for r in tbd_rows[:120]:
                reason = r.get("备注", "") or r.get("验证方法", "")
                reason = reason.replace("|", "/")
                lines.append(f"| {r.get('模式','')} | {r.get('一级分类','')} | {r.get('二级分类','')} | {r.get('名称','')} | {r.get('确认负责人','')} | {reason[:160]} |")
            if len(tbd_rows) > 120:
                lines.append(f"| ... | ... | ... | ... | ... | {len(tbd_rows) - 120} more rows omitted |")
            lines.append("")
    return "\n".join(lines) + "\n"


def hardware_rows() -> list[dict[str, str]]:
    return [
        {"项目代号": "26111", "机型": "Base", "相机位置": "主摄", "Sensor 型号": "HP5", "分辨率": "200MP", "OIS": "NO", "备注": "SM7635; 200MP high-pixel risk/TBD"},
        {"项目代号": "26111", "机型": "Base", "相机位置": "超广角", "Sensor 型号": "IMX355", "分辨率": "8MP", "OIS": "NO", "备注": "FF"},
        {"项目代号": "26111", "机型": "Base", "相机位置": "前置", "Sensor 型号": "OV32D", "分辨率": "32MP", "OIS": "NO", "备注": "front auto-wide depends on orientation"},
        {"项目代号": "26121", "机型": "Pro", "相机位置": "主摄", "Sensor 型号": "IMX896", "分辨率": "50MP", "OIS": "YES", "备注": "same as 25111 Pro"},
        {"项目代号": "26121", "机型": "Pro", "相机位置": "超广角", "Sensor 型号": "IMX355", "分辨率": "8MP", "OIS": "NO", "备注": "same as 25111 Pro"},
        {"项目代号": "26121", "机型": "Pro", "相机位置": "长焦", "Sensor 型号": "JN5", "分辨率": "50MP", "OIS": "YES", "备注": "3.5x; same as 25111 Pro"},
        {"项目代号": "26121", "机型": "Pro", "相机位置": "前置", "Sensor 型号": "KD1", "分辨率": "32MP", "OIS": "NO", "备注": "same as 25111 Pro"},
    ]


def main() -> None:
    DRAFT.mkdir(parents=True, exist_ok=True)
    current = json.loads(CURRENT.read_text(encoding="utf-8"))
    project_rows: dict[str, list[dict[str, str]]] = {}
    for project in PROJECTS:
        merged: dict[tuple[str, str, str, str], dict[str, str]] = {}
        for item in current.get(project, []):
            merge_row(merged, normalize_row(item, project, "current-fl-records-26111-26121.json"))
        add_algorithm_rows(project, merged)
        add_kb_rows(project, merged)
        add_candidate_rows(project, merged)
        add_video_spec_rows(project, merged)
        add_slow_motion_spec_rows(project, merged)
        add_high_res_option_rows(project, merged)
        add_video_toolbar_rows(project, merged)
        add_dual_view_v2_rows(project, merged)
        add_log_video_row(project, merged)
        for key in list(merged):
            if should_prune_row(merged[key]):
                del merged[key]
        for row in merged.values():
            apply_canonical_support_overrides(row, project)
        rows = sorted_rows(finalize_row(row, project) for row in merged.values())
        project_rows[project] = rows
        rendered_rows = display_rows(rows)
        (DRAFT / f"{project}_fl_draft.v0.2.json").write_text(json.dumps(rendered_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_csv(DRAFT / f"{project}_fl_draft.v0.2.csv", rendered_rows, project)
        write_markdown(DRAFT / f"{project}_fl_draft.v0.2.md", rendered_rows, project)

    hw = hardware_rows()
    (DRAFT / "hardware_config.v0.2.json").write_text(json.dumps(hw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (DRAFT / "hardware_config.v0.2.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["项目代号", "机型", "相机位置", "Sensor 型号", "分辨率", "OIS", "备注"])
        writer.writeheader()
        writer.writerows(hw)

    (DRAFT / "fl-generation-audit.v0.2.md").write_text(audit(project_rows), encoding="utf-8")
    manifest = {
        "version": "v0.2",
        "meaning": "Distribution draft for PM/SE/QA fill-in, not final sign-off.",
        "base_link": "https://nothing-tech.sg.larksuite.com/wiki/RbYFwco6qiFiywklWSKlL3WcgMg?table=tblmjUrlAEUhegjG&view=vew2pV2f4a",
        "tables": {
            project: {
                "rows": len(rows),
                "json": f"{project}_fl_draft.v0.2.json",
                "csv": f"{project}_fl_draft.v0.2.csv",
                "markdown": f"{project}_fl_draft.v0.2.md",
            }
            for project, rows in project_rows.items()
        },
        "hardware": {"rows": len(hw), "json": "hardware_config.v0.2.json", "csv": "hardware_config.v0.2.csv"},
    }
    (DRAFT / "manifest.v0.2.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
