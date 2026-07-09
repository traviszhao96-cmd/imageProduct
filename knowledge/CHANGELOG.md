# Knowledge Base Changelog

> 记录 `knowledge/` 目录下所有文件的修改历史。

---

## 2026-07-09

### 修改

- **`feature-tree.md`** — 与 `requirement-list-creator` skill 对齐确认，交互区节点无变更。Skill 中新增同步机制（每次操作前 hash tree，不一致则更新 Bitable 选项）。
- **`devices/26111.yaml`** — 从硬件规格表补充完整传感器参数（OV32D、HP5→S5KHP5SP05、OV08J10；OIS 从 NO→YES）

### 新增

- **`CHANGELOG.md`** (本文件)

---

## 2026-07-08

### 重大更新

- **`feature-tree.md`** — 业务树作为 RL 模块映射的权威来源。确认 71 个合法模块路径，排除快门区域。
- **`devices/26111.yaml`** — 从规格表纠正：主摄有 OIS (HFC66B5003+DW9828N)，UW 是 OV08J10 非 IMX355。
- **`devices/project-mapping.yaml`** — 新增 26111/26121 映射。
- **`reference/26111-prd-links.md`** — 新增，Camera 5.1-26111 wiki 目录下 23 份 PRD 索引。
- **`reference/algorithm-fl-source-26111-26121.md`** — FL 算法项来源映射。
- **`reference/feature-list-layout-common-rules.md`** — FL 布局通用规则。
- **`reference/photo-top-toolbar-rules.md`** — 照片顶部工具栏规则。
- **`reference/kb-functions-algorithms-schema.md`** — KB 功能-算法 schema 定义。
- **`reference/video/dual-recording.md`** — 双摄同录参考。
- **`reference/action.md`** — Action/Motion 模式参考。
- **`reference/photo.md`** — 照片模式参考更新。
- **`reference/INDEX.md`** — 索引更新。

### 生成产物 (`_output/`)

- **`fl_draft_26111_26121/`** — 26111/26121 FL 草稿、最终版、硬件配置、审计报告。
- **`lark_26111_requirements/`** — Camera 5.1-26111 wiki 目录全部 35 个节点的 docx/md/raw 导出。
- **`lark_base_snapshots/`** — 26121 Lark Bitable 快照。
- **`kb-functions-algorithms.v2.json`** ~ **`v6.json`** — KB 功能-算法映射迭代。
- **`kb-functions-algorithms.v6.audit.md`** — v6 审计报告。
- **`tree-kb-integration-candidates.v1.json`** — 业务树-KB 集成候选。

---

## 格式约定

- 日期格式：`YYYY-MM-DD`
- 分组：`重大更新`、`修改`、`新增`、`删除`、`生成产物`
- `_output/` 和 `_raw/` 下的生成物在「生成产物」中汇总，不逐条列
