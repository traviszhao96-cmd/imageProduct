#!/usr/bin/env python3
"""Generate the Camera Feature Tree from canonical KB node relations."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge" / "_output" / "kb-functions-algorithms.v7.json"
OUT = ROOT / "knowledge" / "feature-tree.md"


def node_label(node: dict[str, str]) -> str:
    if node["节点类型"] == "目录":
        return f"{node['名称']}  `{node['节点 ID']}`"
    projection = node["FL 投影"]
    dimensions = node.get("FL 展开维度") or "无"
    return (
        f"{node['名称']}  `{node['节点 ID']}`"
        f" 〔{node['节点类型']}｜FL: {projection}｜维度: {dimensions}〕"
    )


def render_branch(
    node_id: str,
    by_id: dict[str, dict[str, str]],
    children: dict[str, list[str]],
    prefix: str = "",
) -> list[str]:
    lines: list[str] = []
    child_ids = children.get(node_id, [])
    for index, child_id in enumerate(child_ids):
        is_last = index == len(child_ids) - 1
        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + node_label(by_id[child_id]))
        next_prefix = prefix + ("    " if is_last else "│   ")
        lines.extend(render_branch(child_id, by_id, children, next_prefix))
    return lines


def main() -> None:
    rows = json.loads(KB.read_text(encoding="utf-8"))
    by_id = {row["节点 ID"]: row for row in rows}
    children: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if row.get("父节点 ID"):
            children[row["父节点 ID"]].append(row["节点 ID"])

    projection_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        projection_counts[row["FL 投影"]] += 1

    lines = [
        "# Camera Feature Tree",
        "",
        "<!-- GENERATED FILE: DO NOT EDIT. Edit the canonical KB builder instead. -->",
        "",
        "> 本文件由 `scripts/build_feature_tree.py` 从 canonical KB 的 `节点 ID / 父节点 ID` 生成。",
        "> Tree 不是独立数据源，禁止手工维护；节点解释、代码绑定、门控和 FL 展开条件以 KB 为准。",
        "",
        "## FL 投影语义",
        "",
        "- `不进入 FL`：目录或纯知识节点。",
        "- `父节点汇总`：FL 默认只保留父能力一行，子能力留在 KB 中解释。",
        "- `随父节点`：不独立成行，除非它改变父能力的验收结论。",
        "- `独立行`：默认形成一条 FL 验收行。",
        "- `条件展开`：只有项目、模式、摄像头或规格差异会改变支持/验收结论时展开。",
        "- `规格展开`：按明确的摄像头 × 分辨率/帧率/像素档等规格笛卡尔积生成候选行。",
        "",
        "核心原则：**KB 可以细，FL 只展开会产生关键项目或摄像头差异的节点。**",
        "",
        "## 统计",
        "",
        f"- KB 节点总数：{len(rows)}",
        f"- 知识/能力节点：{len(rows) - projection_counts['不进入 FL']}",
        f"- 目录节点：{projection_counts['不进入 FL']}",
        f"- 独立行：{projection_counts['独立行']}",
        f"- 条件展开：{projection_counts['条件展开']}",
        f"- 规格展开：{projection_counts['规格展开']}",
        f"- 父节点汇总/随父节点：{projection_counts['父节点汇总'] + projection_counts['随父节点']}",
        "",
        "## 业务树",
        "",
        "```text",
        node_label(by_id["kb.root"]),
        *render_branch("kb.root", by_id, children),
        "```",
        "",
        "## 生成与审计",
        "",
        "```bash",
        "python3 scripts/build_kb_functions_algorithms.py",
        "```",
        "",
        "生成后检查 `knowledge/_output/kb-functions-algorithms.v7.audit.md`；任何孤儿父节点、重复节点 ID 或无效 FL 投影都必须为 0。",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({len(rows)} nodes)")


if __name__ == "__main__":
    main()
