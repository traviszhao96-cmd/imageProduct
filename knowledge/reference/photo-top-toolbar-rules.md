# Photo Toolbar Rules

> Source: Travis verbal clarification, 2026-07-07.
> Purpose: define Photo-mode Toolbar rows for 26111/26121 Feature List regeneration.

## Scope

This document describes the **Photo / 照片** mode Toolbar. Photo and Video are the most complete toolbar modes; other modes usually remove or disable part of this set.

Feature List classification for these rows:

| Field | Value |
|---|---|
| 模式 | 照片 / Photo |
| 一级分类 | 功能 / Feature |
| 二级分类 | 工具栏 / Toolbar |

## Photo Toolbar Items

Photo mode includes:

| Item | Meaning / options |
|---|---|
| Flash | Rear flash supports Off, On, Torch. Front camera has no physical flash and uses screen fill; front flash can expose Auto. Some older / Glyph-capable devices can expose Glyph as a fill-light mode when the required Glyph hardware exists. |
| Timer | Off, 3s, 10s. |
| HDR | Only Auto and Off in current projects. No forced On. HDR Auto and Off can map to different algorithm paths by project. Typical future/default rule: Off uses MFNR, Auto uses RAW HDR / HDR path when triggered. Some projects may use RAW HDR even when Off. |
| Exposure | Global photo exposure adjustment. Range: -2 to +2 EV, with 0.3 EV step. |
| Filter | Built-in filters plus user-imported filters. Do not enumerate all filter names in FL; reference the current filter management document instead. |
| Tuning | Manual tuning capability. Includes Tuning Palette / Palette Mode / Parameter Mode / Strength / seven-parameter adjustment. Do not create a separate `Style / Tuning Palette / Palette-Parameters` FL row. |
| Photo Style | Natural / Vivid ISP style switch. This is a distinct user-facing style preset from manual Tuning. Keep it as `Photo Style` when the project exposes the Natural/Vivid entry. |
| Motion Photo | Dynamic photo. Support scope differs by project/camera; describe differences in notes. `Motion Photo cover HDR` and `动态照片 - 无效信息截取` may be split into separate rows when inherited FLs or QA acceptance need explicit validation. |
| Quality | Output pixel-count selection. Current common values: 20MP and 50MP; projects with 200MP add 200MP. Decide options based on In-Sensor Zoom and camera output mode. |
| Grid | On / Off. |
| Ratio | 1:1, 4:3, 16:9, Full. If current camera is in 50MP/max-pixel output, ratio switching is not supported because max-pixel output cannot crop to alternate aspect ratios. |
| Watermark | Tap toggles On / Off. Long press jumps to Settings > Photo > Watermark for detailed configuration. |
| More settings | Opens Camera Settings. |
| Glyph Mirror | Optional. Uses a large rear Glyph LED rectangle to preview framing so users can take selfies with rear cameras. Supported only on projects with the required large Glyph hardware; e.g. 25111 Pro supports it, 25111 does not. |

## Notes For FL Generation

- Keep one row per user-facing toolbar item unless a sub-capability is large enough to test independently.
- Do not expand every filter name into FL rows. Link to the filter management reference.
- Do not generate `Style / Tuning Palette / Palette-Parameters` as an independent FL row. Treat Tuning Palette PRDs as updates to the existing `Tuning` row, unless PM confirms a new user-facing `Style` entry that replaces existing Filter/Tuning UI.
- Keep `Photo Style` separate from `Tuning`: `Photo Style` is Natural/Vivid ISP style, while `Tuning` is manual parameter / palette adjustment.
- Do not expand every Motion Photo implementation detail by default.
- `Motion Photo cover HDR` may be an independent row because support differs by project/camera.
- `动态照片 - 无效信息截取` may be an independent row when the baseline FL already tracks it or QA needs to validate invalid clip trimming separately.
- `Watermark` appears as a Photo Toolbar shortcut, while detailed watermark configuration belongs to `模式=通用 / Common`, `一级分类=通用功能 / Common`, `二级分类=设置 / Settings`.
- `More settings` is a toolbar entry to Settings; the settings themselves stay under `模式=通用 / Common`.

## Reference Links

- Filter management: `knowledge/reference/filter.md`
- Tuning / Preset 2.0: `knowledge/reference/tuning.md`
- Watermark references: `knowledge/reference/watermark/`
