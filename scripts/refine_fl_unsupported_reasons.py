#!/usr/bin/env python3
"""Replace inherited FL unsupported templates with causal dependency reasons."""

from __future__ import annotations

import json
import re
from pathlib import Path


CAMERAS = ("Main", "UW", "Tele", "Front")
BAD_REASON = re.compile(
    r"按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。|"
    r"当前基线 FL 未覆盖该摄像头.*|"
    r"依赖长焦/高倍率链路，该摄像头不在支持范围。"
)
PHOTO_CAMERA_INDEPENDENT = {"Exposure", "Grid", "More settings", "Ratio", "Watermark", "Timer"}
NIGHT_TOOLBAR_EXCLUDED = {
    "Grid", "Motion Photo cover HDR", "Ratio", "Watermark", "动态照片-视频支持录制声音",
    "支持跳转保存到 预设（方案待定）", "长按快门连拍 / Press and Hold Burst", "风格 / Style",
}


def split_reason(value: str) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    for part in str(value or "").split("；"):
        part = part.strip()
        if not part:
            continue
        if ":" in part:
            camera, reason = part.split(":", 1)
            result.append((camera.strip(), reason.strip()))
        else:
            result.append(("", part))
    return result


def causal_reason(row: dict, camera: str, high_res_cameras: set[str]) -> str | None:
    name = str(row.get("名称") or "")
    mode = str(row.get("模式") or "")

    if mode == "照片 / Photo" and name in PHOTO_CAMERA_INDEPENDENT:
        return None
    if name == "SAT / 平滑镜头切换" and camera == "Front":
        return "SAT 依赖同一方向的多颗物理摄像头、镜头标定和融合切换链路；前置仅有单颗摄像头，不存在前置镜头间切换，因此不适用。"
    if name == "Quality":
        if camera in high_res_cameras:
            return None
        return (
            "Quality 像素档位切换依赖摄像头提供对应的高像素 Sensor 输出模式，以及 Remosaic/高像素成像输出链路；"
            "该摄像头未开放 20MP、50MP 或 200MP 等高像素档位，因此不支持 Quality 切换。"
        )
    if name == "LDC / 光学畸变矫正":
        return "LDC 依赖镜头存在需要校正的显著光学畸变，并具备对应标定参数和实时矫正链路；该摄像头不需要或未配置该矫正链路，因此不启用 LDC。"
    if name == "人脸畸变矫正":
        return "人脸畸变矫正依赖大视场角镜头的边缘人脸形变场景、人脸关键点和局部几何校正链路；该摄像头未配置对应的边缘人脸矫正链路，因此不启用。"
    if name == "Photo EIS":
        return "Photo EIS 依赖该摄像头进入项目定义的高倍率拍照范围，并具备陀螺仪数据、画面裁切空间和 EIS 链路；该摄像头没有对应高倍率触发范围，因此不启用。"
    if name in {"人像模式 Consistent Zoom", "人像 HDR"} and camera == "UW":
        return "人像模式不开放超广角作为可选择或输出摄像头；该能力依赖人像模式的有效输出镜头，因此 UW 不适用。"
    if name == "Log 视频":
        return "Log 录制依赖该摄像头接入 Log 曲线处理、对应位深/编码和指定分辨率帧率的视频链路；当前摄像头未接入该 Log 规格链路，因此不支持。"
    if name == "1080P@ 120fps":
        return "1080P 120fps 依赖 Sensor 高帧率读出、ISP 带宽和 120fps 录制编码链路；当前摄像头未开放该高帧率规格，因此不支持。"
    if name == "4K" and mode == "延时摄影 / Timelapse":
        return "延时摄影 4K 依赖该摄像头的 4K 采集、延时合成和 4K 编码链路；当前摄像头未开放该模式的 4K 输出链路，因此不支持。"
    if name == "Flash":
        return "该模式的补光依赖摄像头可使用的 LED/Torch 或屏幕补光硬件，并需要录制/拍摄链路开放同步控制；当前组合未开放对应补光链路，因此不支持。"
    if name in {"动态照片 - 无效信息截取", "动态照片-视频支持录制声音", "Motion Photo cover HDR"}:
        return "该子能力依赖当前摄像头完整接入 Motion Photo 的视频片段采集、处理和封装链路；当前摄像头未接入对应子链路，因此不支持。"
    if name == "运动抓拍" and camera == "Front":
        return "运动抓拍依赖后置摄像头的运动检测、快速曝光和多帧成像链路；当前前置链路未接入该运动抓拍算法，因此不支持。"
    if name == "Remosaic":
        return "Remosaic 依赖多像素合一 Sensor 的高像素读出模式及对应 ISP/软件重排链路；当前模式或摄像头不进入高像素输出链路，因此不启用。"
    if name == "极夜":
        return "极夜依赖极低照检测、长曝光多帧合成和对应平台算法配置；当前摄像头未接入极夜分支，因此不支持。"
    if mode == "高像素 / High Resolution" and camera not in high_res_cameras:
        return "该能力依赖当前摄像头能够进入高像素模式并提供对应高像素输出链路；该摄像头没有可用的高像素模式输出，因此在此模式下不适用。"
    if mode == "慢动作 / Slow Motion":
        return "该能力依赖当前摄像头接入慢动作高帧率采集、预览和编码链路；当前摄像头未开放慢动作规格链路，因此在该模式下不支持。"
    if mode == "夜景 / Night" and name in NIGHT_TOOLBAR_EXCLUDED:
        return f"{name} 依赖夜景模式提供对应工具栏入口及处理链路；当前夜景模式未配置该入口/链路，因此不支持。"
    if name in {"AI Zoom", "AIGC SR", "超分 / Super Resolution（SR）", "HDSR", "Hex Zoom"}:
        return "该能力依赖长焦或高倍率成像输入，并需要达到项目定义的触发倍率；该摄像头没有对应高倍率输出链路，无法进入触发区间，因此不支持。"
    return "TBD：现有资料只有不支持结论，尚未说明缺失的具体硬件、算法或模式依赖；需主责确认依赖缺口后再判定。"


def refine(rows: list[dict]) -> tuple[list[dict], dict[str, int]]:
    stats = {"rewritten": 0, "promoted_supported": 0, "reverted_tbd": 0}
    high_res_cameras = {
        camera
        for row in rows
        if row.get("模式") == "高像素 / High Resolution" and re.search(r"(?:50|200)MP", str(row.get("名称") or ""))
        for camera in CAMERAS
        if row.get(camera) == "✓"
    }
    for row in rows:
        rendered: list[tuple[str, str]] = []
        seen: set[tuple[str, str]] = set()
        for camera, reason in split_reason(row.get("不支持原因", "")):
            if camera in CAMERAS and BAD_REASON.search(reason):
                replacement = causal_reason(row, camera, high_res_cameras)
                if replacement is None:
                    row[camera] = "✓"
                    stats["promoted_supported"] += 1
                    continue
                if replacement.startswith("TBD："):
                    row[camera] = "TBD"
                    row["状态"] = "待确认"
                    stats["reverted_tbd"] += 1
                else:
                    stats["rewritten"] += 1
                reason = replacement
            pair = (camera, reason)
            if pair not in seen:
                rendered.append(pair)
                seen.add(pair)
        covered = {camera for camera, _ in rendered if camera in CAMERAS}
        for camera in CAMERAS:
            if row.get(camera) != "✗" or camera in covered:
                continue
            replacement = causal_reason(row, camera, high_res_cameras)
            if replacement is None:
                row[camera] = "✓"
                stats["promoted_supported"] += 1
                continue
            if replacement.startswith("TBD："):
                row[camera] = "TBD"
                row["状态"] = "待确认"
                stats["reverted_tbd"] += 1
            else:
                stats["rewritten"] += 1
            rendered.append((camera, replacement))
        row["不支持原因"] = "；".join(f"{camera}: {reason}" if camera else reason for camera, reason in rendered)
        if any(row.get(camera) == "TBD" for camera in CAMERAS):
            row["状态"] = "待确认"
    return rows, stats


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.input.read_text(encoding="utf-8"))
    rows, stats = refine(rows)
    output = args.output or args.input
    output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
