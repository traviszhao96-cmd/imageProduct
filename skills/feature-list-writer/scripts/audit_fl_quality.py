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
    "作为新功能进入 FL",
    "不进入 Camera FL",
    "继承原项目",
    "沿用原项目",
    "follow 原项目",
)
INVALID_UNSUPPORTED_REASON = re.compile(
    r"按当前项目硬件、PRD 或基线 FL|当前基线 FL 未覆盖|该摄像头不在支持范围|"
    r"(?:继承|沿用|follow).*(?:所以|因此)?.*不支持|(?:基线|原项目).*(?:标记|填写|为).*不支持",
    re.I,
)
GENERIC_UNSUPPORTED_REASON = re.compile(
    r"^(?:(?:Main|UW|Tele|Front)[:：]\s*)?(?:该|此|本)?(?:功能|项目|摄像头|模式)?"
    r"(?:不支持|不适用|不开放|已取消|不做|不在范围)[。.]?$",
    re.I,
)
ROOT_CAUSE_MARKERS = (
    "依赖", "需要", "要求", "受限", "由于", "缺少", "缺失", "未提供", "未开放", "不开放",
    "没有", "不具备", "仅支持", "只支持", "硬件", "sensor", "pipeline", "平台", "规格",
    "分辨率", "帧率", "像素", "编码", "功耗", "性能", "内存", "模式不", "链路",
)
CONSEQUENCE_MARKERS = (
    "因此", "所以", "导致", "无法", "不能", "不可", "不支持", "不适用", "不提供", "不显示", "不开放",
)
STATEFUL_CONTROL = re.compile(r"开关|设置|On\s*/\s*Off|开启|关闭|切换选项", re.I)
DEFAULT_MARKERS = ("默认", "初始", "首次")
MEMORY_MARKERS = ("记忆", "保持上次", "持久化", "重置", "恢复默认", "5min", "5 min", "杀进程", "Home", "安全相机")
VAGUE_VALUE_PHRASES = ("提升体验", "满足需求", "支持该能力", "提升画质", "效果更好")
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


def has_repeated_sentence(value: str) -> bool:
    sentences = [re.sub(r"\s+", "", part) for part in re.split(r"[。！？!?；;]+", value) if part.strip()]
    return len(sentences) != len(set(sentences))


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
            if GENERIC_DESCRIPTION.match(description):
                add(issues, index, row, "DESCRIPTION_VACUOUS", "high", "说明言之无物：只有支持/配置/来源结论，没有解释功能或算法")
            if any(phrase in description for phrase in MECHANICAL_PHRASES):
                add(issues, index, row, "DESCRIPTION_MECHANICAL", "medium", "说明包含机械模板句，需要语义复核")
            if sum(phrase in description for phrase in VAGUE_VALUE_PHRASES) >= 2:
                add(issues, index, row, "DESCRIPTION_VAGUE_VALUE", "high", "说明堆叠抽象价值词，但没有提供足够的行为、结果或边界信息")
            if has_repeated_sentence(description):
                add(issues, index, row, "DESCRIPTION_REPETITIVE", "medium", "说明存在重复句，字数增加但没有增加有效信息")
            if re.search(r"\b26(?:111|121)\b.*(?:支持|不支持)", description):
                add(issues, index, row, "DESCRIPTION_SUPPORT_NARRATION", "medium", "说明写了项目支持结论，应改为能力定义与范围")
            if level1 in {"功能 / Feature", "通用 / Common"} and STATEFUL_CONTROL.search(f"{name} {description}"):
                if not any(marker in description for marker in DEFAULT_MARKERS):
                    add(issues, index, row, "DESCRIPTION_DEFAULT_UNKNOWN", "medium", "有状态功能未说明默认值或状态持久化；未知时应形成主责确认问题")
                if "入口" not in description and not any(marker.lower() in description.lower() for marker in MEMORY_MARKERS):
                    add(issues, index, row, "DESCRIPTION_MEMORY_UNKNOWN", "medium", "有状态功能未说明关键记忆或重置规则；应参考九场景基线并确认项目差异")
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
        elif unsupported_reason and GENERIC_UNSUPPORTED_REASON.match(unsupported_reason):
            add(issues, index, row, "UNSUPPORTED_REASON_VACUOUS", "high", "不支持原因只是重复不支持结论，没有解释根因")
        elif unsupported_reason and any(value == "✗" for value in support):
            lowered_reason = unsupported_reason.lower()
            if not any(marker.lower() in lowered_reason for marker in ROOT_CAUSE_MARKERS):
                add(issues, index, row, "UNSUPPORTED_REASON_CAUSE_MISSING", "medium", "不支持原因未指出具体依赖或项目限制")
            if not any(marker.lower() in lowered_reason for marker in CONSEQUENCE_MARKERS):
                add(issues, index, row, "UNSUPPORTED_REASON_CONSEQUENCE_MISSING", "medium", "不支持原因未说明依赖缺口如何导致该功能不可用")

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
