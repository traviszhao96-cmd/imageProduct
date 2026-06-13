# Knowledge Base — Roadmap

## P0 — 补数据缺口

- [ ] **"24M" SoC 确认** — 23114 CMF 1、24121 CMF 2 Pro、24121T 3a Lite 的 SoC 列是 "24M"，需确认是否占位符还是真实芯片代号
- [ ] **25131 Phone (4b) camera spec** — 目前仅主摄 JN1+GC08A8+GC16B3C 从 JSON 补的，待确认完整
- [ ] **25141 Phone (4a) Lite camera spec** — 完全空白
- [ ] **25151 CMF Phone 3 camera spec** — 完全空白
- [ ] **26111 Phone (5a) SoC + 屏幕** — 目前 TBD

## P1 — 补 Sensor Datasheet

已有（4个）：JN1、GC08A、IMX896、OS08A10

缺失清单：

- [ ] OV51A    — 26111 主摄
- [ ] KN1      — 26111 Pro 3.9x 潜望长焦
- [ ] OV05H    — 23112 Phone (3) 主摄
- [ ] GNJ      — 24111 Pro Phone (3a) Pro 主摄
- [ ] OV50D    — 24121 CMF 2 Pro 超广角
- [ ] IMX355   — 多机型超广角
- [ ] IMX882   — 24111 Pro 长焦 / 23114 主摄
- [ ] KD1      — 前置
- [ ] GC16B3C  — 25131 前置
- [ ] OV32D    — 26111 前置
- [ ] SC202    — 23114 凑数
- [ ] GC02M1   — 24121T 凑数
- [ ] IMX766   — 20111 主摄
- [ ] IMX890   — 22111 主摄
- [ ] GN9      — 多机型主摄

→ 格式化规范: `knowledge/devices/sensors/{model}.yaml`，含 `capability_summary`（4k_30fps/60fps, 1080p_60fps/120fps/240fps, hdr_photo, hdr_video, pdaf, ois）

## P2 — 更新 Feature Matrix

- [ ] 补充 Phone (3a) 的功能矩阵 → `features/rear-camera.json` / `front-camera.json`
- [ ] 补充 Phone (4a)/(4a) Pro 的功能矩阵
- [ ] 补充 Phone (5a) 的功能矩阵（参考 26111 feature list）
- [ ] 对照 `feature-tree.md` 检查功能覆盖完整性

## P3 — 补齐 PRD 归档

`reference/_raw/prd/` 现有: 4.1、5.0

- [ ] Phone (3a) / (3a) Pro PRD (24111)
- [ ] Phone (3) PRD (23112)
- [ ] Phone (4a) / (4a) Pro PRD (25111)
- [ ] Phone (5a) 初始 PRD (26111)
- [ ] 如有飞书链接，整理为 `knowledge/reference/` 下对应 feature group 文档

## P4 — 工具增强

- [ ] `generate.py` 扩展：支持 YAML→markdown 查表
- [ ] `scripts/validate-knowledge.sh` — 自动校验 device YAML × feature JSON 一致性
- [ ] CI/auto-check: push 时自动跑 `generate.py` 更新 `_output/`
