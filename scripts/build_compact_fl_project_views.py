#!/usr/bin/env python3
"""Build compact 26111/26121 review views from the latest confirmed project data."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "outputs" / "feature-list-table" / "data"
LATEST_26121 = ROOT / "knowledge" / "_output" / "lark_base_snapshots" / "26121_lark_latest_2026-07-20.json"
REPORT = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121" / "compact-view-audit-2026-07-20.md"
FINAL_DIR = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121"

FIELDS = (
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
)

ALGORITHM_DESCRIPTIONS = {
    "AIGC SR": "面向高倍率变焦的 AI 细节重建能力，通过模型恢复或生成传统超分难以保留的纹理；它不同于常规多帧 SR。核心验收范围是实际生效摄像头、起止倍率、生成错误、文字真实性、性能和功耗。",
    "HDSR": "HDR 与 Super Resolution 的组合成像链路，在高动态且需要超分增强的场景同时改善动态范围和高倍率细节；需确认实际生效摄像头、焦段，以及与普通 HDR、SR 的切换边界。",
    "Hex Zoom": "26111 主摄 4x 高倍率成像路径，使用 HP5 hex/4x4 RAW 输入并由外部软件完成 remosaic 和细节重建；它不是 ISZ，也不是长焦摄像头。",
    "RAW HDR": "在 RAW 域对多帧不同曝光图像进行对齐与融合，扩展动态范围并保留高光、暗部和颜色信息。FL 只确认模式、摄像头和输出规格是否接入该链路，具体亮度阈值与帧策略属于软件设计。",
    "CFR / 紫边去除": "检测并抑制高反差边缘附近由镜头色散产生的紫边或彩边，尽量保持真实边缘颜色与细节；需按模式、摄像头和 HDR/非 HDR 链路确认生效范围。",
    "Video EIS": "视频电子防抖通过陀螺仪运动信息、画面裁切和逐帧几何补偿降低录制抖动，在项目支持的视频规格和倍率范围内持续生效；需确认与 OIS、变焦、HDR 和高帧率规格的兼容范围。",
    "运动抓拍": "针对运动主体和手持运动场景进行运动检测，并联动曝光、取帧、HDR 与多帧融合策略，提高高速场景的成片清晰度和成功率；需确认触发场景、摄像头范围及运动伪影。",
    "视频夜景": "视频录制中的低照增强与时域降噪能力，在控制噪声的同时维持曝光、颜色、运动连续性和实时帧率；需确认支持的摄像头、分辨率、帧率、倍率及功耗温升。",
    "超级夜景": "低照拍摄中的多帧长短曝光融合链路，用于提升暗部可见度、控制高光并降低噪声；夜景模式直接使用，照片模式可由自动夜景判断触发。FL 只确认模式和摄像头范围，帧数与 ZSL/NZSL 策略属于软件设计。",
}


def load_rows(path: Path) -> list[dict]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    normalized = []
    for row in rows:
        item = {field: row.get(field, "") for field in FIELDS}
        for field, value in item.items():
            if isinstance(value, list) and len(value) == 1 and field != "确认负责人":
                item[field] = value[0]
        owner = item["确认负责人"]
        if isinstance(owner, str):
            item["确认负责人"] = [owner] if owner else []
        normalized.append(item)
    return normalized


def append_reason(row: dict, reason: str) -> None:
    current = row.get("不支持原因", "").strip()
    if reason not in current:
        row["不支持原因"] = f"{current}；{reason}".strip("；")


def apply_camera_scope(rows: list[dict], project: str) -> None:
    for row in rows:
        if project == "26111":
            row["Tele"] = ""
        if row["模式"] == "人像 / Portrait" and row["UW"] != "✗":
            row["UW"] = "✗"
            append_reason(row, "UW: 人像模式不开放超广角摄像头，该功能在 UW 不适用。")
        if row["模式"] == "高像素 / High Resolution":
            for camera in ("UW", "Front"):
                if row[camera] != "✗":
                    row[camera] = "✗"
                    append_reason(row, f"{camera}: 该摄像头不提供本项目高像素模式所需的高像素输出链路。")
        if row["名称"] == "各项专业模式参数极值范围":
            row["确认负责人"] = ["HAL SE"]
            row["状态"] = "待确认"


def normalize_algorithm_rows(rows: list[dict], project: str) -> list[dict]:
    super_night = next(
        (row for row in rows if row["模式"] == "夜景 / Night" and row["名称"] == "超级夜景"),
        None,
    )
    tf_super_night = next(
        (row for row in rows if row["模式"] == "夜景 / Night" and row["名称"] == "TF SN / Super Night"),
        None,
    )
    if super_night and tf_super_night:
        for camera in ("Main", "UW", "Tele", "Front"):
            if tf_super_night[camera] not in ("", "TBD"):
                super_night[camera] = tf_super_night[camera]

    rows = [
        row for row in rows
        if row["名称"] not in {"SAT / 平滑镜头切换", "HLG / HDR 规格", "TF SN / Super Night"}
    ]
    for row in rows:
        name = row["名称"]
        if name in ALGORITHM_DESCRIPTIONS:
            row["说明"] = ALGORITHM_DESCRIPTIONS[name]
        if name in {"LDC / 光学畸变矫正", "CFR / 紫边去除"}:
            row["一级分类"] = "算法 / Algorithm"
            row["二级分类"] = "后处理算法 / Post-processing Algorithm"
        if name == "Ultra HDR":
            row["一级分类"] = "功能 / Feature"
            row["二级分类"] = "系统 / System"
        if name == "AIGC SR":
            row["Main"] = "TBD" if project == "26111" else "✗"
            row["UW"] = "✗"
            row["Tele"] = "" if project == "26111" else "TBD"
            row["Front"] = "✗"
            row["状态"] = "待确认"
            row["不支持原因"] = "AIGC 高倍率链路仍需确认算法方案、实际生效焦段、内存、性能和量产范围。"
        if name == "ISZ / In Sensor Zoom" and row["模式"] == "照片 / Photo" and project == "26111":
            row["Main"] = "✓"
            row["UW"] = "✗"
            row["Tele"] = ""
            row["Front"] = "✗"

    existing = {key(row) for row in rows}
    missing = (
        ("人像 / Portrait", "多帧降噪 / MFNR"),
        ("人像 / Portrait", "人脸畸变矫正"),
    )
    for mode, name in missing:
        if (mode, name) in existing:
            continue
        source = next((row for row in rows if row["名称"] == name), None)
        if not source:
            continue
        row = dict(source)
        row["模式"] = mode
        row["Main"] = "TBD"
        row["UW"] = "✗"
        row["Tele"] = "" if project == "26111" else "TBD"
        row["Front"] = "TBD"
        row["不支持原因"] = "UW: 人像模式不开放超广角摄像头，该算法在 UW 不适用。"
        row["状态"] = "待确认"
        row["确认负责人"] = ["HAL SE"]
        rows.append(row)
    return rows


def apply_product_confirmations(rows: list[dict], project: str) -> None:
    if project != "26111":
        return
    confirmed = {
        ("照片 / Photo", "前后翻转 / Front-Rear Camera Switch"),
        ("人像 / Portrait", "前后翻转 / Front-Rear Camera Switch"),
        ("视频 / Video", "前后翻转 / Front-Rear Camera Switch"),
        ("夜景 / Night", "前后翻转 / Front-Rear Camera Switch"),
        ("视频 / Video", "录制中拍摄动态照片 / Motion Photo While Recording"),
        ("通用 / Common", "快速模式切换 / Quick Mode Switch"),
    }
    for row in rows:
        if key(row) not in confirmed:
            continue
        row["状态"] = "已确认"
        row["确认负责人"] = ["Product"]
        if row["名称"] == "录制中拍摄动态照片 / Motion Photo While Recording":
            row["Main"] = "✓"
            row["UW"] = "✓"
            row["Front"] = "✓"
            row["不支持原因"] = ""


def is_all_unsupported(row: dict, project: str) -> bool:
    cameras = ("Main", "UW", "Front") if project == "26111" else ("Main", "UW", "Tele", "Front")
    return row["状态"] == "已确认" and all(row[camera] == "✗" for camera in cameras)


def is_mode_level_noise(row: dict, project: str) -> bool:
    if not is_all_unsupported(row, project):
        return False
    mode, name = row["模式"], row["名称"]
    if "脏污检测" in name and mode not in {"照片 / Photo", "人像 / Portrait"}:
        return True
    if mode == "夜景 / Night" and name in {
        "Flash",
        "Motion Photo cover HDR",
        "动态照片 - 无效信息截取",
        "动态照片-视频支持录制声音",
        "长按快门连拍 / Press and Hold Burst",
    }:
        return True
    if mode == "慢动作 / Slow Motion" and name == "Flash":
        return True
    if mode == "照片 / Photo" and name in {"Quality", "前置自动小广角"}:
        return True
    return False


def key(row: dict) -> tuple[str, str]:
    return row["模式"], row["名称"]


def align_structure(
    rows_26111: list[dict], rows_26121: list[dict]
) -> tuple[list[dict], list[dict], list[str]]:
    notes = []
    rows_26121 = [
        row for row in rows_26121
        if not (row["模式"] == "夜景 / Night" and row["名称"] == "变焦 / Zoom")
    ]
    notes.append("删除 26121 夜景模式重复的‘变焦 / Zoom’，保留规范名称‘变焦’。")

    rows_26111 = [
        row for row in rows_26111
        if not (row["模式"] == "前后双录 / Dual View Video" and row["名称"] == "Video EIS")
    ]
    notes.append("删除 26111 独立前后双录模式下的重复 Video EIS；前后双录能力归入视频模式。")

    for row in rows_26111:
        if row["名称"] == "长时间无交互息屏以节约电量":
            row["模式"] = "通用 / Common"
            row["不支持原因"] = ""
    notes.append("将 26111 长时间无交互息屏移动到通用，与 26121 对齐。")

    existing_26111 = {key(row) for row in rows_26111}
    additions = {
        ("专业 / Expert", "各项专业模式参数极值范围"),
        ("照片 / Photo", "人脸畸变矫正"),
    }
    for source in rows_26121:
        if key(source) not in additions or key(source) in existing_26111:
            continue
        row = dict(source)
        row["Main"] = "TBD"
        row["UW"] = "TBD"
        row["Tele"] = ""
        row["Front"] = "TBD" if row["模式"] == "照片 / Photo" else "✗"
        row["状态"] = "待确认"
        row["不支持原因"] = "" if row["Front"] == "TBD" else "Front: 专业模式不开放前置摄像头。"
        rows_26111.append(row)
        notes.append(f"26111 补齐待确认行：{row['模式']} / {row['名称']}。")
    return rows_26111, rows_26121, notes


def main() -> None:
    rows_26111 = load_rows(FRONTEND / "26111.json")
    rows_26121 = load_rows(LATEST_26121)
    rows_26111, rows_26121, notes = align_structure(rows_26111, rows_26121)
    rows_26111 = normalize_algorithm_rows(rows_26111, "26111")
    rows_26121 = normalize_algorithm_rows(rows_26121, "26121")
    notes.extend([
        "SAT 合并到变焦能力，不再保留独立算法行。",
        "删除 HLG/HDR 汇总算法行，由逐规格视频行表达支持范围。",
        "TF SN / Super Night 合并到规范名称‘超级夜景’。",
        "补齐人像模式 MFNR 与人脸畸变矫正算法行。",
    ])
    apply_camera_scope(rows_26111, "26111")
    apply_camera_scope(rows_26121, "26121")
    apply_product_confirmations(rows_26111, "26111")
    apply_product_confirmations(rows_26121, "26121")

    removed: dict[str, list[dict]] = {"26111": [], "26121": []}
    compact: dict[str, list[dict]] = {}
    for project, rows in (("26111", rows_26111), ("26121", rows_26121)):
        removed[project] = [row for row in rows if is_mode_level_noise(row, project)]
        compact[project] = [row for row in rows if not is_mode_level_noise(row, project)]
        (FRONTEND / f"{project}.json").write_text(
            json.dumps(compact[project], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (FINAL_DIR / f"{project}_fl_final.json").write_text(
            json.dumps(compact[project], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        with (FINAL_DIR / f"{project}_fl_final.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            for row in compact[project]:
                rendered = dict(row)
                rendered["确认负责人"] = " / ".join(rendered["确认负责人"])
                writer.writerow(rendered)

    inline = "window.FL_INLINE_DATA = " + json.dumps(compact, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (FRONTEND / "inline-data.js").write_text(inline, encoding="utf-8")

    keys_26111 = {key(row) for row in compact["26111"]}
    keys_26121 = {key(row) for row in compact["26121"]}
    report = [
        "# 26111 / 26121 Compact FL View Audit",
        "",
        "## Result",
        "",
        f"- 26111: {len(rows_26111)} -> {len(compact['26111'])} rows",
        f"- 26121: {len(rows_26121)} -> {len(compact['26121'])} rows",
        "- Complete online snapshots remain unchanged; this script only builds compact local review views.",
        "",
        "## Structural Alignment",
        "",
        *[f"- {note}" for note in notes],
    ]
    for project in ("26111", "26121"):
        report.extend(["", f"## Hidden In {project}", ""])
        report.extend(f"- {row['模式']} / {row['名称']}" for row in removed[project])
    report.extend(["", "## Remaining Project-only Rows", "", "### 26111", ""])
    report.extend(f"- {mode} / {name}" for mode, name in sorted(keys_26111 - keys_26121))
    report.extend(["", "### 26121", ""])
    report.extend(f"- {mode} / {name}" for mode, name in sorted(keys_26121 - keys_26111))
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"26111={len(compact['26111'])}, 26121={len(compact['26121'])}, report={REPORT}")


if __name__ == "__main__":
    main()
