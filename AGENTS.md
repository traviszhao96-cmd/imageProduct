# Image Product Agent Instructions

## Project-local skills

Treat valid skill folders under `skills/` as available project skills even when they are absent from the global Codex skill inventory. When a task matches one, read its `SKILL.md` completely before acting.

- Camera KB、知识库、KB 表格、Feature Tree、KB v7 schema、KB visualizer 或 KB → FL 投影：use `skills/knowledge-base-manage/SKILL.md`.
- Project Feature List、线上 FL、多维表格支持矩阵或模块评审：use `skills/feature-list-writer/SKILL.md`; use `lark-base` for live Base operations.
- Requirement List generation or standardized requirement Base creation: use `skills/requirement-list-creator/SKILL.md`.
- Camera/Gallery PRD authoring: use `skills/image-feature-prd-writer/SKILL.md`.

If a project-local skill conflicts with a globally installed tool skill, use the project-local skill for product policy and the global skill for tool execution.

## KB source-of-truth rules

- KB is the canonical capability manual; FL is a downstream project acceptance matrix.
- Tree is generated from KB `节点 ID / 父节点 ID`; never maintain a second manual Tree.
- Edit KB definitions in `scripts/build_kb_functions_algorithms.py` and follow `knowledge/reference/kb-functions-algorithms-schema.md`.
- Do not hand-edit generated KB JSON, `knowledge/feature-tree.md`, or `outputs/kb-visualizer/data.js`.
- Regenerate with `python3 scripts/build_kb_functions_algorithms.py`, then `python3 scripts/build_kb_visualizer.py`.
- Treat the approved requirement list as formal input for new/changed functions. Use code and device/sensor evidence to determine implementation and hardware bounds.
- A current-project node enters FL when it is a new functional requirement, creates a project/mode/camera/spec/entry difference, or needs an independent acceptance conclusion.

## Working rules

- Preserve unrelated user changes in a dirty worktree.
- Use minimal edits and verify generated artifacts after changing source definitions.
- Do not guess camera support, unsupported reasons, or review conclusions.
- For online writes, read back affected rows before reporting completion.
