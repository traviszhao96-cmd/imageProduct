---
name: knowledge-base-manage
description: Maintain the Nothing Camera capability knowledge base, including KB schema v7 nodes, hierarchy/Tree projection, structured descriptions, code and requirement evidence, FL projection metadata, audits, and the local KB visualizer. Use when the user asks to inspect, add, update, reorganize, validate, or visualize Camera KB/知识库/KB表格/feature tree nodes, or to judge how KB content should project into a project Feature List. Do not use as the primary workflow for editing a live project FL; use feature-list-writer plus lark-base for that.
---

# Camera Knowledge Base Manager

## Responsibility boundary

Treat the three artifacts as one pipeline with distinct roles:

- **KB** is the canonical capability manual. Keep rich explanations, hierarchy, dependencies, code bindings, lifecycle state, verification, and FL projection rules here.
- **Tree** is a generated hierarchical view of KB nodes. Never maintain a second manual Tree.
- **FL** is a downstream project acceptance matrix. It contains project/camera/spec support and review conclusions, not the canonical knowledge definition.

Use [`../feature-list-writer/SKILL.md`](../feature-list-writer/SKILL.md) for creating or maintaining project FLs. Use `lark-base` for live Base record operations. This skill owns the KB definition and the projection decision supplied to that workflow.

## Canonical sources and generated artifacts

Edit:

- `scripts/build_kb_functions_algorithms.py` — canonical node definitions, hierarchy metadata, code bindings, and FL projection attributes.
- `knowledge/reference/kb-functions-algorithms-schema.md` — schema and policy. Read it completely before changing KB structure or projection rules.
- `knowledge/devices/*.yaml` and `knowledge/devices/sensors/*.yaml` — project and hardware evidence when support boundaries depend on them.

Generate; do not hand-edit:

- `knowledge/_output/kb-functions-algorithms.json` — unversioned canonical output.
- `knowledge/_output/kb-functions-algorithms.v7.json` — current schema output.
- `knowledge/_output/kb-functions-algorithms.v6.json` — migration compatibility alias.
- `knowledge/_output/kb-functions-algorithms.v7.audit.md` — canonical audit.
- `knowledge/feature-tree.md` — Tree projected from `节点 ID / 父节点 ID`.
- `outputs/kb-visualizer/data.js` — browser payload for the local visualizer.

The visualizer entry point is `outputs/kb-visualizer/index.html`.

## Required workflow

1. Read `knowledge/reference/kb-functions-algorithms-schema.md` completely.
2. Read the relevant current nodes from `knowledge/_output/kb-functions-algorithms.v7.json` and inspect nearby parent/child nodes.
3. Gather only the evidence needed for the change:
   - current approved requirement list or PRD for product scope;
   - CameraApp code/config for implementation and entry visibility;
   - device/sensor configuration for hardware bounds;
   - current FL only for drift detection, never as the KB source of truth.
4. Decide whether to update an existing node, add a child, or add a new capability. Prefer stable identity and avoid synonym duplicates.
5. Edit `scripts/build_kb_functions_algorithms.py`. Preserve an existing `节点 ID` when renaming a node. Add an explicit ID or migration mapping when automatic identity would change.
6. Run the canonical builder:

   ```bash
   python3 scripts/build_kb_functions_algorithms.py
   ```

7. Inspect `knowledge/_output/kb-functions-algorithms.v7.audit.md`. Do not accept duplicate names/IDs, orphan parents, invalid projections, missing projection rules, invalid verification methods, or bad source-project references.
8. Rebuild the local browser payload:

   ```bash
   python3 scripts/build_kb_visualizer.py
   ```

9. Verify the affected node in both v7 JSON and `outputs/kb-visualizer/data.js`. When visual behavior changed, open `outputs/kb-visualizer/index.html` and inspect it.
10. If the change affects a live FL, hand the projection result to `feature-list-writer`; update Base only after comparing against the current requirement list and project evidence.

## Node content rules

- Keep one stable `节点 ID`; use `父节点 ID` for hierarchy.
- Treat `一级分类 / 二级分类` as FL-compatible taxonomy, not a second Tree.
- Keep KB mode scope at the maximum meaningful scope; do not duplicate KB rows for every mode or camera.
- Write `说明` to answer what the capability is, what problem it solves, user value, product goal, and its boundary. Follow the five-part requirement in the schema.
- Put implementation facts in `App 绑定 / 配置门控 / 代码基线`, not in the user-facing definition.
- Mark code-only/debug/internal capabilities accurately. Code existence alone does not prove a production entry.
- Keep project support marks out of KB. Put `✓ / ✗ / TBD` only in FL.
- Use the current or historical project that established the definition as `来源项目`; do not use a future target project as the canonical source merely because its requirement triggered the review.

## FL projection decision

Project a KB node into FL when it is in the current project scope and at least one condition is true:

1. it is a new functional requirement;
2. project, mode, camera, entry, or specification support differs;
3. it produces an independent review or acceptance conclusion.

Update an existing FL row when it can express the new requirement and verification target. Add a new row only when the existing row cannot express an independent user-facing function or acceptance result.

Use these projection values exactly:

- `不进入 FL`
- `父节点汇总`
- `随父节点`
- `独立行`
- `条件展开`
- `规格展开`

Use projection dimensions only from `项目 / 模式 / 摄像头 / 规格 / 入口`, in combinations allowed by the schema.

## Evidence and review rules

- Treat the approved requirement list as the formal scope input for new or changed functions.
- Treat KB as the capability definition and projection policy.
- Treat device/sensor/code evidence as support-boundary inputs.
- Do not infer camera support from a class name, sensor presence, or an old FL row alone.
- Do not guess unsupported reasons or final module confirmation states.
- Preserve unresolved facts as explicit `待确认` with the missing evidence named.
- Use Product/HAL/APP/Tuning review columns in FL; do not invent a single accountable owner when the project uses distributed review.

## Validation checklist

Before finishing, confirm:

- the builder exits successfully;
- v7 and unversioned canonical outputs contain the same node set;
- v6 is only a compatibility alias;
- the Tree was regenerated and has no independent manual edits;
- the audit reports zero structural errors;
- every changed non-directory node has a complete description and executable verification method;
- the visualizer payload points to v7 and contains the changed node;
- any live FL change was handled through `feature-list-writer` and read back after writing.

## Legacy paths

`knowledge/generate.py`, `knowledge/_output/features-{project}.md`, and old FL-derived audits are legacy inputs or comparison tools. Do not use them as the canonical KB v7 authoring path.
