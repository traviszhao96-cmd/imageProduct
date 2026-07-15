#!/usr/bin/env python3
"""Audit Camera FL JSON/CSV structure and description quality."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


CAMERAS = ("Main", "UW", "Tele", "Front")
VALID_LEVEL1 = {"功能 / Feature", "算法 / Algorithm", "通用 / Common"}
VALID_ROLES = {"Product", "APP", "HAL SE", "Tuning SE", "SQA", "IQA"}
GENERIC_DESCRIPTION = re.compile(
    r"^(支持(该|此)?功能|在对应模式(下)?生效|按项目配置|功能项|待确认|来自.*(?:FL|PRD)|—|-)[。.]?$",
    re.I,
)
MECHANICAL_PHRASES = (
    "入口、选项、状态保持",
    "按当前项目硬件、PRD 或基线 FL",
    "当前基线 FL 未覆盖",
    "在对应模式打开",
)
INVALID_UNSUPPORTED_REASON = re.compile(
    r"按当前项目硬件、PRD 或基线 FL|当前基线 FL 未覆盖|该摄像头不在支持范围",
    re.I,
)
BOUNDARY_TERMS = ("取帧策略", "PZL", "帧数配置", "pipeline 排序", "算法叠加顺序")


def text(value) -> str:
    if isinstance(value, list):
        return " / ".join(str(item).strip() for item in value if str(item).strip())
    return str(value or "").strip()


def read_rows(path: Path) -> list[dict]:
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        payload = payload.get("rows", payload.get("records", payload))
    if not isinstance(payload, list):
        raise ValueError("Expected a JSON array, or an object containing rows/records")
    return payload


def add(issues: list[dict], index: int, row: dict, code: str, severity: str, message: str) -> None:
    issues.append({
        "row": index + 1,
        "mode": text(row.get("模式")),
        "name": text(row.get("名称")),
        "code": code,
        "severity": severity,
        "message": message,
    })


def owner_name(row: dict) -> str:
    return text(row.get("主责确认人") or row.get("确认负责人"))


def audit(rows: list[dict]) -> list[dict]:
    issues: list[dict] = []
    seen: Counter[tuple[str, str]] = Counter()
    for index, row in enumerate(rows):
        mode, name = text(row.get("模式")), text(row.get("名称"))
        description = text(row.get("说明"))
        verification = text(row.get("验证方法"))
        level1 = text(row.get("一级分类"))
        seen[(mode, name)] += 1

        if not name:
            add(issues, index, row, "NAME_EMPTY", "critical", "名称为空")
        if level1 not in VALID_LEVEL1:
            add(issues, index, row, "LEVEL1_INVALID", "critical", f"一级分类不是三类标准值: {level1 or '空'}")
        if not description:
            add(issues, index, row, "DESCRIPTION_EMPTY", "critical", "说明为空")
        else:
            compact = re.sub(r"\s+", "", description)
            if len(compact) < 20:
                add(issues, index, row, "DESCRIPTION_TOO_SHORT", "high", "说明过短，无法独立解释能力和范围")
            if GENERIC_DESCRIPTION.match(description):
                add(issues, index, row, "DESCRIPTION_GENERIC", "high", "说明只有支持/配置结论，没有解释功能或算法")
            if any(phrase in description for phrase in MECHANICAL_PHRASES):
                add(issues, index, row, "DESCRIPTION_MECHANICAL", "medium", "说明包含机械模板句，需要语义复核")
            if re.search(r"\b26(?:111|121)\b.*(?:支持|不支持)", description):
                add(issues, index, row, "DESCRIPTION_SUPPORT_NARRATION", "medium", "说明写了项目支持结论，应改为能力定义与范围")
        if not verification:
            add(issues, index, row, "VERIFICATION_EMPTY", "high", "验证方法为空")

        support = [text(row.get(camera)) for camera in CAMERAS if camera in row]
        if any(value == "TBD" for value in support) and text(row.get("状态")) == "已确认":
            add(issues, index, row, "STATUS_TBD_CONFLICT", "critical", "存在 TBD 但状态为已确认")
        unsupported_reason = text(row.get("不支持原因"))
        if any(value == "✗" for value in support) and not unsupported_reason:
            add(issues, index, row, "UNSUPPORTED_REASON_EMPTY", "high", "存在不支持摄像头但不支持原因为空")
        if INVALID_UNSUPPORTED_REASON.search(unsupported_reason):
            add(issues, index, row, "UNSUPPORTED_REASON_NON_CAUSAL", "high", "不支持原因只有来源/范围结论，没有说明依赖缺口和因果关系")

        owner = owner_name(row)
        if not owner:
            add(issues, index, row, "OWNER_EMPTY", "critical", "主责确认人为空")
        elif owner in VALID_ROLES or "/" in owner:
            add(issues, index, row, "OWNER_IS_ROLE", "high", "主责确认人应为一个具体姓名，不应是角色或组合值")

        combined = f"{name} {description}"
        if any(term.lower() in combined.lower() for term in BOUNDARY_TERMS):
            add(issues, index, row, "BOUNDARY_REVIEW", "high", "可能属于软件设计细节，需执行 FL 边界判断")

    duplicates = {key for key, count in seen.items() if count > 1 and all(key)}
    for index, row in enumerate(rows):
        key = (text(row.get("模式")), text(row.get("名称")))
        if key in duplicates:
            add(issues, index, row, "DUPLICATE_MODE_NAME", "critical", "同一模式存在重复名称")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--fail-on", choices=("critical", "high", "medium"), default="critical")
    args = parser.parse_args()

    rows = read_rows(args.input)
    issues = audit(rows)
    counts = Counter(issue["severity"] for issue in issues)
    payload = {"input": str(args.input), "rows": len(rows), "issues": issues, "summary": dict(counts)}
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    rank = {"medium": 1, "high": 2, "critical": 3}
    threshold = rank[args.fail_on]
    raise SystemExit(1 if any(rank[issue["severity"]] >= threshold for issue in issues) else 0)


if __name__ == "__main__":
    main()
