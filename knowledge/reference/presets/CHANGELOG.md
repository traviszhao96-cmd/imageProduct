# Default Preset — Change Log

> 12 presets across Nothing/CMF phones
> Bitable: https://nothing-tech.sg.larksuite.com/wiki/DZuBw5vdciCoHykr5ixlTo1RgKd?table=tblOqjh4vBfGct0j

---

## 2026-06-15

### Data migration
- 从 `Default preset v3.2.xlsx` (65MB, 6 sheets) 迁移至 Lark 多维表格
- 10 张封面图从 xlsx 提取 → 1080×1440 JPEG → Drive API 上传为附件
- 删除 Shutter Speed 字段

### Cricket & Sports
- **Focal Length**: 25131 24mm → **28mm**（主摄就是 28mm）
- **Tuning**: `Contrast +12 | Saturation +10 | Warmth -7 | Tint +5 | Sharpen +5 | Grain 0 | Vignette +5` → **Vignette +15**
- Cricket 与 Sports 数据同步，仅 Watermark/备注 按地区区分

### Fill rules established
- 空值分类: **不涉及** / **无** / **None** / **Original**
- Author: 无 → "无"
- Filter: 无 → "Original"
- Portrait Effect / Bokeh: 非 Portrait → "不涉及"

### Skill created
- `skills/default-preset-manage/SKILL.md`
- 本地 snapshot: `references/default-preset-bitable-v1.json`
