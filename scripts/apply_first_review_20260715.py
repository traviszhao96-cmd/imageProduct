#!/usr/bin/env python3
"""Apply the 2026-07-15 first-review baseline to the local project FLs."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "knowledge" / "_output" / "fl_draft_26111_26121"
FRONTEND_DIR = ROOT / "outputs" / "feature-list-table" / "data"
PROJECTS = ("26111", "26121")


def apply_review(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    reviewed: list[dict[str, str]] = []
    for original in rows:
        row = dict(original)
        name = str(row.get("名称", "")).strip()

        # Capture timing belongs in the software design, not the FL support matrix.
        if name == "PZL":
            continue

        category = str(row.get("一级分类", ""))
        row["确认负责人"] = "SE" if category.startswith("算法") else "Product"
        if row.get("状态") != "Pending":
            row["状态"] = "待确认"
        row["不支持原因"] = ""

        if name in {"光学畸变矫正", "LDC / 光学畸变矫正"}:
            row["名称"] = "LDC / 光学畸变矫正"
            row["二级分类"] = "实时算法 / Realtime Algorithm"
            row["说明"] = (
                "Lens Distortion Correction。依据镜头标定参数矫正整幅画面的桶形、枕形等几何畸变，"
                "主要用于超广角等大视场角镜头；预览和成片链路都需要确认是否接入 LDC。"
                "该能力通常伴随裁切和视场角变化，不等同于人脸畸变矫正。"
            )
            row["验证方法"] = (
                "使用网格、建筑直线和边缘目标分别检查预览与成片；确认 UW 的 LDC 是否生效，"
                "并记录裁切、视场角、边缘拉伸和分辨率损失。"
            )

        if name in {"Raw HDR / TF HDR", "RAW HDR / TF HDR", "TF HDR", "Raw HDR"}:
            row["名称"] = "RAW HDR"
            row["二级分类"] = "后处理算法 / Post-processing Algorithm"
            row["说明"] = (
                "RAW 域多帧 HDR 算法，通过不同曝光帧的对齐与融合提升动态范围并控制高光和暗部。"
                "TF 仅是特定供应商方案称呼，不作为 FL 标准名称；具体触发阈值、摄像头、倍率和模式范围由 SE 确认。"
            )

        if name == "HDSR":
            row["说明"] = (
                "HDR 与 SR 的组合成像链路：在 SR 倍率范围内且 HDR 场景检测成立时触发，"
                "用于同时提升高倍清晰度和动态范围。必须按项目确认生效摄像头、起止倍率、场景阈值及与普通 SR/HDR 的切换关系。"
            )
            row["验证方法"] = (
                "覆盖各摄像头与连续变焦范围，在普通和高动态场景结合算法 tag 确认 HDSR 的触发起止倍率、"
                "退出条件、成片动态范围、清晰度和切换一致性。"
            )

        reviewed.append(row)
    return reviewed


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError(f"No rows for {path}")
    fieldnames = list(rows[0])
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    payload: dict[str, list[dict[str, str]]] = {}
    for project in PROJECTS:
        final_json = FINAL_DIR / f"{project}_fl_final.json"
        rows = json.loads(final_json.read_text(encoding="utf-8"))
        rows = apply_review(rows)

        final_json.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_csv(FINAL_DIR / f"{project}_fl_final.csv", rows)
        (FRONTEND_DIR / f"{project}.json").write_text(
            json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        payload[project] = rows

    inline = "window.FL_INLINE_DATA = " + json.dumps(
        payload, ensure_ascii=False, separators=(",", ":")
    ) + ";\n"
    (FRONTEND_DIR / "inline-data.js").write_text(inline, encoding="utf-8")

    for project, rows in payload.items():
        print(f"{project}: {len(rows)} rows; all non-Pending rows reset to 待确认")


if __name__ == "__main__":
    main()
