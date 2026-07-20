#!/usr/bin/env python3
"""Sync the latest 26111 review into local FL/KB artifacts for 26121 review."""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from snapshot_lark_fl import load_project  # noqa: E402
from sync_lark_fl_review_20260715 import FIELDS, transform  # noqa: E402


FRONTEND = ROOT / "outputs" / "feature-list-table" / "data"
FINAL = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121"
SNAPSHOTS = ROOT / "knowledge" / "_output" / "lark_base_snapshots"
KB_FILES = [
    ROOT / "knowledge" / "_output" / "kb-functions-algorithms.v6.json",
    ROOT / "knowledge" / "_output" / "kb-functions-algorithms.json",
]
AUDIT = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121" / "26111-to-26121-sync-audit-2026-07-20.md"


def key(row: dict) -> tuple[str, str]:
    return str(row.get("模式") or ""), str(row.get("名称") or "")


def camera_reason(camera: str, reason: str) -> str:
    return f"{camera}: {reason}"


def clean_reasons(row: dict, cameras: list[str]) -> None:
    reasons = str(row.get("不支持原因") or "")
    kept = []
    for part in (piece.strip() for piece in reasons.split("；")):
        if not part:
            continue
        prefix = part.split(":", 1)[0]
        if prefix in cameras and row.get(prefix) == "✓":
            continue
        kept.append(part)
    row["不支持原因"] = "；".join(dict.fromkeys(kept))


def set_support(row: dict, values: dict[str, str], reason: str = "") -> None:
    existing_parts = []
    for part in (piece.strip() for piece in str(row.get("不支持原因") or "").split("；")):
        if not part:
            continue
        prefix = part.split(":", 1)[0]
        if prefix not in values:
            existing_parts.append(part)
    for camera, value in values.items():
        row[camera] = value
    row["不支持原因"] = "；".join(dict.fromkeys(existing_parts))
    if reason:
        additions = [camera_reason(camera, reason) for camera, value in values.items() if value == "✗"]
        row["不支持原因"] = "；".join(dict.fromkeys(filter(None, [row["不支持原因"], *additions])))


def row_template(mode: str, second: str, name: str, description: str, validation: str) -> dict:
    return {
        "模式": mode,
        "一级分类": "功能 / Feature",
        "二级分类": second,
        "名称": name,
        "说明": description,
        "Main": "✓",
        "UW": "✓",
        "Tele": "✓",
        "Front": "✗",
        "不支持原因": "Front: 专业模式不开放前置摄像头，因此该功能在 Front 不适用。",
        "状态": "待确认",
        "确认负责人": ["Product"],
        "验证方法": validation,
    }


def upsert(rows: list[dict], item: dict) -> None:
    for index, row in enumerate(rows):
        if key(row) == key(item):
            rows[index] = item
            return
    rows.append(item)


def remove_semantic_duplicates(rows: list[dict]) -> list[dict]:
    result = []
    for row in rows:
        level = str(row.get("一级分类") or "")
        name = str(row.get("名称") or "")
        if name == "SAT / 平滑镜头切换" and level == "功能 / Feature":
            continue
        if name == "ASD / AI场景检测" and level == "功能 / Feature":
            continue
        if name == "变焦" and level == "算法 / Algorithm":
            continue
        result.append(row)
    return result


def update_26121(rows: list[dict], online_26111: list[dict]) -> tuple[list[dict], list[str]]:
    changes: list[str] = []
    by_key = {key(row): row for row in rows}

    # A completed 26111 review still leaves these items pending; carry that review need to 26121.
    pending_names = {key(row) for row in online_26111 if row.get("状态") == "待确认"}
    for item_key in pending_names:
        if item_key in by_key:
            by_key[item_key]["状态"] = "待确认"

    front_supported = {
        ("照片 / Photo", name) for name in {
            "Exposure", "Grid", "More settings", "Ratio", "Timer", "Watermark",
            "HDR 开关 / HDR Switch", "风格 / Style", "动态照片 - 无效信息截取",
            "动态照片-视频支持录制声音", "长时间无交互息屏以节约电量",
        }
    } | {
        ("人像 / Portrait", name) for name in {
            "Exposure", "Grid", "More settings", "Ratio", "Timer", "Watermark",
            "HDR 开关 / HDR Switch", "风格 / Style",
        }
    } | {("夜景 / Night", "Exposure")}
    for item_key in front_supported:
        row = by_key.get(item_key)
        if row:
            set_support(row, {"Front": "✓"})
            row["状态"] = "待确认"
    changes.append("前置能力：照片/人像/夜景中的工具栏、风格和动态照片子能力按 26111 结论开放，26121 标记待确认。")

    # ASD is an algorithm capability, not a generic preview feature in every mode.
    for row in rows:
        if row.get("名称") != "ASD / AI场景检测":
            continue
        if row.get("模式") == "照片 / Photo":
            set_support(row, {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✗"}, "ASD 当前仅在照片模式后置链路开放，前置不接入该语义场景策略。")
        else:
            set_support(row, {"Main": "✗", "UW": "✗", "Tele": "✗", "Front": "✗"}, "ASD 当前仅在照片模式后置链路开放，该模式不接入 ASD。")
        row["状态"] = "待确认"
    changes.append("ASD：仅照片模式后置摄像头支持，其他模式及前置不支持。")

    row = by_key.get(("照片 / Photo", "前置自动小广角"))
    if row:
        set_support(row, {"Main": "✗", "UW": "✗", "Tele": "✗", "Front": "✗"}, "26111/26121 前置原生 FOV 不满足小广角切换收益，当前项目取消该功能。")
        row["不支持原因"] = "26111/26121 前置原生 FOV 不满足小广角切换收益，当前项目取消该功能。"
        row["说明"] = "依据设备方向自动切换前置宽视角的候选能力；26111 与 26121 因前置原生 FOV 不满足收益要求，当前项目均不支持。"
        row["状态"] = "已确认"
    changes.append("前置自动小广角：26111/26121 均取消，原因是前置原生 FOV 不满足收益要求。")

    row = by_key.get(("照片 / Photo", "Quality"))
    if row:
        set_support(row, {"Main": "✗", "UW": "✗", "Tele": "✗", "Front": "✗"}, "项目提供独立高像素模式，照片模式不再保留 Quality 像素档位入口。")
        row["不支持原因"] = "项目提供独立高像素模式，照片模式不再保留 Quality 像素档位入口。"
        row["说明"] = "照片模式中的像素档位入口；当项目提供独立高像素模式时取消该入口，高像素输出能力统一在高像素模式验收。"
        row["状态"] = "待确认"
    changes.append("Quality：有独立高像素模式时从照片工具栏移除。")

    row = by_key.get(("照片 / Photo", "Flash"))
    if row:
        set_support(row, {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✓"})
        row["说明"] = "照片工具栏补光入口。后置摄像头使用 LED Flash/Torch；前置无物理闪光灯时使用屏幕或环形补光，并可提供 Auto。"
        row["不支持原因"] = ""
        row["状态"] = "待确认"
    changes.append("照片 Flash：后置使用 LED/Torch，前置使用屏幕或环形补光。")

    for name in ("AE / 自动曝光", "人脸检测", "变焦"):
        row = by_key.get(("专业 / Expert", name))
        if row:
            set_support(row, {"Front": "✗"}, "专业模式不开放前置摄像头，该能力在 Front 不适用。")
            row["状态"] = "待确认"
    action_zoom = by_key.get(("运动 / Action", "变焦"))
    if action_zoom:
        set_support(action_zoom, {"Front": "✗"}, "运动模式不开放前置摄像头，该能力在 Front 不适用。")
        action_zoom["状态"] = "待确认"

    portrait_zoom = by_key.get(("人像 / Portrait", "人像模式 Consistent Zoom"))
    if portrait_zoom:
        portrait_zoom["说明"] = "后摄人像模式支持连续变焦；具体 UI 变焦点和连续变焦范围跟随项目 UI Spec，光圈与虚化效果随焦段联动。"
        portrait_zoom["状态"] = "待确认"

    for name in ("AE / 自动曝光", "人脸检测", "变焦"):
        row = by_key.get(("高像素 / High Resolution", name))
        if row:
            row["不支持原因"] = (
                "UW: 高像素模式依赖摄像头提供 50MP 及以上 Sensor 输出与 Remosaic 链路，UW 不满足项目配置；"
                "Front: 高像素模式不开放前置摄像头。"
            )
            row["状态"] = "待确认"
    high_flash = by_key.get(("高像素 / High Resolution", "Flash"))
    if high_flash:
        set_support(high_flash, {"Main": "TBD", "UW": "✗", "Tele": "TBD", "Front": "✗"}, "高像素补光依赖对应摄像头的高像素输出链路与 Flash 同步策略，需逐摄像头确认。")
        high_flash["状态"] = "待确认"

    # Dual View Video is a Video feature, not a standalone camera mode.
    dual_names = {"前后双录主副互换 / 小窗大小", "前后双录后置镜头选择", "Video EIS"}
    moved = []
    kept = []
    for row in rows:
        if row.get("模式") == "前后双录 / Dual View Video":
            if row.get("名称") in dual_names:
                row["模式"] = "视频 / Video"
                row["二级分类"] = "前后同录 / Dual Video" if row.get("名称") != "Video EIS" else "实时算法 / Realtime Algorithm"
                row["状态"] = "待确认"
                moved.append(row)
            continue
        kept.append(row)
    rows = kept
    existing_keys = {key(row) for row in rows}
    for row in moved:
        if key(row) in existing_keys:
            existing = next(item for item in rows if key(item) == key(row))
            existing["状态"] = "待确认"
            continue
        rows.append(row)
        existing_keys.add(key(row))
    upsert(rows, {
        "模式": "视频 / Video", "一级分类": "功能 / Feature", "二级分类": "前后同录 / Dual Video",
        "名称": "前后双录", "说明": "视频模式中的前后同录功能入口，同时采集前置和一个后置摄像头；不再作为模式栏中的独立模式。",
        "Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✓", "不支持原因": "", "状态": "待确认",
        "确认负责人": ["Product"], "验证方法": "从视频模式进入前后同录，确认入口、前后画面组合、录制文件、音画同步和退出后的状态恢复。",
    })
    changes.append("前后双录：从独立模式迁移为视频模式下的功能，并迁移主副互换、后置镜头选择和 Video EIS。")

    # Preserve the parameter-range row; the 26111 edit overwrote it with Peaking.
    rows = [row for row in rows if row.get("名称") != "Expert Mode 2.0"]
    for item in (
        row_template("专业 / Expert", "工具栏 / Toolbar", "峰值对焦", "在手动对焦时高亮显示处于焦内的高反差边缘，辅助用户判断清晰区域。", "切换手动对焦并移动焦点，确认峰值颜色、阈值、预览延迟和开关状态符合规格。"),
        row_template("专业 / Expert", "工具栏 / Toolbar", "直方图", "在专业模式预览中显示实时亮度分布，辅助判断欠曝、高光溢出和整体曝光。", "在低调、高调和正常曝光场景检查直方图形态、刷新率、开关和旋转布局。"),
        row_template("专业 / Expert", "工具栏 / Toolbar", "间隔快门", "按用户设置的间隔与张数连续拍摄静态照片，用于延时过程或固定节奏连拍。", "设置不同间隔和张数拍摄，确认触发节奏、计数、停止、锁屏/来电异常和文件完整性。"),
    ):
        upsert(rows, item)
    changes.append("专业模式：移除聚合的 Expert Mode 2.0 行，保留参数极值范围，并新增峰值对焦、直方图、间隔快门。")

    snapshot = by_key.get(("视频 / Video", "录制中拍照 / Video Snapshot"))
    if snapshot:
        snapshot["名称"] = "录像中拍照"
        snapshot["二级分类"] = "录制中拍照 / Capture While Recording"
        snapshot["说明"] = "视频录制过程中从当前视频帧完成常规截帧拍照，不中断主视频录制；需确认输出分辨率、FOV、色彩和支持规格。"
        snapshot["状态"] = "待确认"
    changes.append("录像中拍照：按 26111 最新表改为常规视频截帧；与旧 KB 的独立拍照流定义存在冲突，保留待确认。")

    order = {name: index for index, name in enumerate([
        "照片 / Photo", "人像 / Portrait", "运动 / Action", "视频 / Video", "夜景 / Night",
        "慢动作 / Slow Motion", "延时摄影 / Timelapse", "全景 / Panorama", "专业 / Expert",
        "高像素 / High Resolution", "通用 / Common",
    ])}
    rows.sort(key=lambda item: (order.get(str(item.get("模式")), 99), str(item.get("一级分类")), str(item.get("二级分类")), str(item.get("名称"))))
    deduplicated = []
    seen = set()
    for row in rows:
        exact_key = (row.get("模式"), row.get("一级分类"), row.get("二级分类"), row.get("名称"))
        if exact_key in seen:
            continue
        seen.add(exact_key)
        deduplicated.append(row)
    return remove_semantic_duplicates(deduplicated), changes


def update_kb(rows: list[dict]) -> list[dict]:
    by_name = {str(row.get("名称")): row for row in rows}
    mode_bar = by_name.get("模式栏")
    if mode_bar:
        mode_bar["说明"] = "相机默认进入照片模式；模式栏按项目展示人像、运动、视频、夜景、慢动作、延时摄影、全景、专业等模式。前后双录属于视频模式内的功能，不作为独立模式栏入口。"

    asd = by_name.get("ASD / AI场景检测")
    if asd:
        asd["模式"] = "照片（后置）"
        asd["判断依据"] = "当前规则仅在照片模式后置摄像头接入 ASD；其他模式和前置默认不支持。后续项目扩大范围时必须由算法链路和项目 FL 单独确认。"
        asd["验证方法"] = "使用绿植、舞台、天空等 ASD 场景集逐个后置摄像头验证识别与策略；同时确认前置和其他模式不会误触发。"

    quality = by_name.get("Quality")
    if quality:
        quality["说明"] = "照片工具栏中的像素档位入口。项目若提供独立高像素模式，则照片模式取消 Quality 入口，高像素输出统一在高像素模式验收。"
        quality["判断依据"] = "先判断项目是否有独立高像素模式；有则照片模式不展开 Quality。没有时再按 Sensor 输出、Remosaic/ISZ、内存与耗时判断可选档位。"

    flash = by_name.get("Flash")
    if flash:
        flash["说明"] = "工具栏补光入口。照片后置使用 LED Flash/Torch；前置无物理闪光灯时使用屏幕或环形补光并可提供 Auto。夜景是否开放补光需独立判断，不能继承照片模式结论。"

    for name in ("Timer", "HDR 开关 / HDR Switch", "Exposure", "Grid", "Ratio", "Watermark", "More settings"):
        item = by_name.get(name)
        if item:
            item["模式"] = "照片 / 人像 / 夜景（按项目配置）"
            rule = "当前项目确认支持前置时，Front 不得因摄像头位置被默认排除。"
            if rule not in str(item.get("判断依据") or ""):
                item["判断依据"] = (str(item.get("判断依据") or "").rstrip() + " " + rule).strip()

    for name in ("动态照片 - 无效信息截取", "动态照片-视频支持录制声音"):
        item = by_name.get(name)
        if item:
            rule = "前置是否支持由 Motion Photo 子链路决定，不得仅因前置摄像头而默认判为不支持。"
            if rule not in str(item.get("判断依据") or ""):
                item["判断依据"] = (str(item.get("判断依据") or "").rstrip() + " " + rule).strip()

    by_name = {str(row.get("名称")): row for row in rows}
    if "前置自动小广角" not in by_name:
        rows.append({
            "模式": "照片（前置）", "一级分类": "功能 / Feature", "二级分类": "变焦 / Zoom", "名称": "前置自动小广角",
            "说明": "根据设备方向在前置原生与宽视角间自动切换的候选能力。26111/26121 因前置原生 FOV 不满足收益要求，当前项目取消。",
            "判断依据": "依赖前置 Sensor 原生 FOV、可用宽视角裁切点和陀螺仪/方向事件；只有宽视角收益成立时才在项目 FL 展开。",
            "依赖": "依赖前置 FOV、裁切输出、陀螺仪/方向事件和变焦状态管理。",
            "验证方法": "横竖屏切换并手动变焦，确认自动切换、暂停和恢复；26111/26121 确认入口不出现。",
            "来源项目": "26111 / 26121", "备注": "当前两个项目不支持。",
        })

    additions = [
        ("峰值对焦", "手动对焦时高亮焦内高反差边缘，辅助判断清晰区域。", "依赖手动对焦、边缘检测、预览叠加和阈值/颜色配置。"),
        ("直方图", "在专业模式预览中显示实时亮度分布，辅助判断欠曝与高光溢出。", "依赖预览亮度统计、直方图渲染与刷新性能。"),
        ("间隔快门", "按设置的间隔与张数连续拍摄静态照片。", "依赖定时调度、连续拍照、计数、存储与异常恢复。"),
    ]
    existing = {str(row.get("名称")) for row in rows}
    for name, description, dependency in additions:
        if name not in existing:
            rows.append({
                "模式": "专业", "一级分类": "功能 / Feature", "二级分类": "工具栏 / Toolbar", "名称": name,
                "说明": description, "判断依据": f"专业模式产品规格明确提供{name}时展开独立 FL 行。", "依赖": dependency,
                "验证方法": f"在专业模式逐摄像头验证{name}入口、状态、实时反馈和拍摄结果。", "来源项目": "26111 / 26121", "备注": "",
            })

    existing = {str(row.get("名称")) for row in rows}
    if "前后双录" not in existing:
        rows.append({
            "模式": "视频", "一级分类": "功能 / Feature", "二级分类": "前后同录 / Dual Video", "名称": "前后双录",
            "说明": "视频模式中的前后同录功能，同时采集前置和一个后置摄像头；不作为模式栏中的独立模式。",
            "判断依据": "项目视频模式提供前后同录入口时，在视频模式下展开功能及其子能力。",
            "依赖": "依赖前后摄并发、双路预览/编码、布局、音画同步、功耗和后置镜头选择。",
            "验证方法": "从视频模式进入前后同录，验证画面组合、主副切换、后置镜头选择、录制输出和状态恢复。",
            "来源项目": "26111 / 26121", "备注": "",
        })

    snapshot = next((row for row in rows if row.get("名称") == "录制中拍照 / Video Snapshot"), None)
    if snapshot:
        snapshot["说明"] = "视频录制过程中不中断主视频地输出静态照片。实现可为当前视频帧截取或独立拍照流，必须按项目明确；26111 最新 FL 当前写为常规截帧。"
        snapshot["判断依据"] = "确认项目采用视频截帧还是独立拍照流，并逐摄像头、分辨率、帧率、SDR/HDR、风格和防抖状态定义支持范围。"
        snapshot["备注"] = "26111 最新 FL 与旧 KB 的独立拍照流定义存在冲突，需在 26121 评审时确认。"
    return rows


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            rendered = {field: row.get(field, "") for field in FIELDS}
            owners = rendered.get("确认负责人")
            if isinstance(owners, list):
                rendered["确认负责人"] = " / ".join(str(owner) for owner in owners)
            writer.writerow(rendered)


def main() -> None:
    previous = json.loads((SNAPSHOTS / "26111_lark_review_2026-07-15.json").read_text(encoding="utf-8"))
    online_raw = load_project("26111")
    online_26111 = remove_semantic_duplicates(transform("26111", online_raw))
    local_26121 = json.loads((FRONTEND / "26121.json").read_text(encoding="utf-8"))
    updated_26121, transfer_notes = update_26121(local_26121, online_26111)

    write_json(FRONTEND / "26111.json", online_26111)
    write_json(FRONTEND / "26121.json", updated_26121)
    write_json(FINAL / "26111_fl_final.json", online_26111)
    write_json(FINAL / "26121_fl_final.json", updated_26121)
    write_csv(FINAL / "26111_fl_final.csv", online_26111)
    write_csv(FINAL / "26121_fl_final.csv", updated_26121)
    inline = "window.FL_INLINE_DATA = " + json.dumps({"26111": online_26111, "26121": updated_26121}, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (FRONTEND / "inline-data.js").write_text(inline, encoding="utf-8")

    write_json(SNAPSHOTS / "26111_lark_review_2026-07-20.json", online_raw)
    for path in KB_FILES:
        write_json(path, update_kb(json.loads(path.read_text(encoding="utf-8"))))

    old = {row["_record_id"]: row for row in previous}
    new = {row["_record_id"]: row for row in online_raw}
    tracked = ["模式", "一级分类", "二级分类", "名称", "说明", "Main", "UW", "Front", "不支持原因", "状态", "确认负责人", "验证方法"]
    changed = []
    changed_fields = Counter()
    for record_id in old.keys() & new.keys():
        diff = {field: [old[record_id].get(field), new[record_id].get(field)] for field in tracked if old[record_id].get(field) != new[record_id].get(field)}
        if diff:
            changed.append((record_id, new[record_id], diff))
            changed_fields.update(diff.keys())

    status_26111 = Counter(str(row.get("状态")) for row in online_raw)
    status_26121 = Counter(str(row.get("状态")) for row in updated_26121)
    report = [
        "# 26111 第一轮评审同步到 26121（本地）",
        "",
        "## 差异概览",
        "",
        f"- 26111 当前线上记录：{len(online_raw)} 条；相对 2026-07-15 快照新增 {len(new.keys() - old.keys())} 条、删除 {len(old.keys() - new.keys())} 条。",
        f"- 发生字段变化的既有记录：{len(changed)} 条，共 {sum(changed_fields.values())} 个单元格。",
        f"- 线上 26111 状态：已确认 {status_26111['已确认']}，待确认 {status_26111['待确认']}。",
        f"- 本地 26121 更新后：{len(updated_26121)} 条；已确认 {status_26121['已确认']}，待确认 {status_26121['待确认']}。",
        "- 本轮只更新本地 JSON、HTML 数据和 KB；没有写回线上 26121。",
        "",
        "## 涉及 KB 的规则",
        "",
        *[f"- {note}" for note in transfer_notes],
        "",
        "## AI 审计发现",
        "",
        "- 26111 将“各项专业模式参数极值范围”原记录直接改成“峰值对焦”，会丢失 ISO、AWB、快门、EV 和 Focus 范围验收。本地 26121 保留参数范围行，并单独新增峰值对焦。",
        "- 26111 最新“录像中拍照”定义为常规视频截帧，与 KB 之前的独立拍照流定义冲突；26121 已按最新表展示，但保持待确认。",
        "- 前后双录已从独立模式迁移到视频功能，但线上 26111 仍遗留一条“前后双录模式 / Video EIS”；本地 26121 已一并迁入视频，避免继续保留空模式。",
        "- 用户说明评审已完成，但线上状态字段仍有待确认项；本地保留这些待确认信号，不擅自改为已确认。",
        "",
        "## 下午重点确认",
        "",
        "- 26121 的 Tele 是否支持高像素模式 Flash，以及具体依赖。",
        "- 录像中拍照采用视频截帧还是独立拍照流。",
        "- ASD 是否确定只支持照片模式后置，且功能行与算法行是否需要合并。",
        "- 前后双录迁入视频后，Video EIS、后置镜头选择和主副画面交互的归属是否完整。",
        "- 专业模式峰值对焦、直方图、间隔快门及参数极值范围是否逐项完整。",
        "",
        "## 变化字段统计",
        "",
        *[f"- {field}: {count}" for field, count in changed_fields.most_common()],
    ]
    AUDIT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"26111 online -> HTML: {len(online_26111)}")
    print(f"26121 local -> HTML: {len(updated_26121)}")
    print(f"audit: {AUDIT}")


if __name__ == "__main__":
    main()
