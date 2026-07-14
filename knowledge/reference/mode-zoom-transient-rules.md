# Camera Mode / Zoom Bar / Transient Switch Rules

> Source: Travis verbal clarification, 2026-07-07.
> Purpose: help AI understand current Feature List rows without inventing extra FL categories.

## Scope

This document explains product meaning and support-judgement rules for:

- Mode switch / mode bar
- Zoom bar default zoom points
- Left and right transient switches

Do not use this document to introduce new Feature List top-level categories. Current FL rows should still use the fields already present in the Feature List table: `模式`, `一级分类`, `二级分类`, `名称`, `说明`, camera support columns, `状态`, `验证方法`.

## Mode Bar

The default camera mode is **Photo / 照片**.

Other mode-bar modes include:

| English | Chinese | Notes |
|---|---|---|
| Photo | 照片 | Default mode |
| Portrait | 人像 | Portrait / bokeh mode |
| Action | 运动 | Sports/action capture mode |
| Video | 视频 | Normal video recording |
| Night | 夜景 | Dedicated night mode |
| Slowmo | 慢动作 | High-frame-rate slow-motion video |
| Time Lapse | 延时摄影 | Time-lapse capture |
| Pano | 全景 | Panorama capture |
| Expert | 专业 | Manual exposure, ISO, shutter, WB, focus, RAW where supported |
| Dual View Video | 前后双录 | Front and rear camera simultaneous recording |

Use the mode list above as the current Feature List expansion baseline.

## Zoom Bar

The zoom bar sits above the mode bar. It contains default zoom points.

Default zoom-point rules:

1. Cover every hardware optical zoom point exposed by the device cameras.
2. If a camera supports **In-Sensor Zoom (ISZ)**, also expose the supported ISZ zoom point.
3. A default zoom point should represent a real capture path, not just a decorative UI stop.

Default zoom points are mode-specific. A Photo-mode ISZ point must not be copied into Video, Slow Motion, or another mode unless that mode has its own confirmed ISZ path. For 26111 and 26121, Video does not support ISZ because switching the ISZ setting causes visible effect jumps and increases power consumption; the Photo ISZ conclusion cannot be used as Video FL evidence.

Example: 25131 has an ultrawide camera and a main camera. The main camera supports ISZ and can output 12MP at 2x. Therefore the default zoom points are:

| Zoom point | Meaning |
|---|---|
| 0.6x | Ultrawide hardware point |
| 1x | Main camera hardware point |
| 2x | Main camera ISZ point |

## Transient Switches

Transient switches are independent interaction areas. They are spatially placed on the left and right sides of the zoom bar, but they are **not** children of Zoom / 变焦.

Use these Feature List classifications for transient-switch rows:

| Side | Feature List `二级分类` | Typical features |
|---|---|---|
| Left | 左侧暂态开关 | Macro Control / 自动微距控制 |
| Right | 右侧暂态开关 | Night switch / 夜景开关, AI Zoom switch, Text Mode / 文本模式 |

## Left Transient Switch

The left transient-switch area is reserved for **Macro Control / 自动微距控制**.

Meaning:

- A transient switch is a temporary control shown only when its trigger condition is met.
- It is not a persistent toolbar item.
- The user can tap it to temporarily disable or cancel the suggested behavior.

Macro Control dependency:

- The device must support **fallback**.
- Fallback means that when the main camera or tele camera cannot focus, the camera can switch to another camera with a shorter minimum focus distance to complete focus.
- If fallback is not supported, Macro Control should not appear.

Feature List judgement:

- Mark Macro Control as supported only when fallback is supported and the mode exposes this transient switch behavior.
- If the camera hardware or project policy does not support fallback, mark it unsupported even if the UI area exists.

## Right Transient Switches

The right transient-switch area is reserved for:

1. Night transient switch
2. AI Zoom transient switch
3. Text Mode transient switch

### Night Transient Switch

Trigger:

- Ambient light is dark enough that night capture is expected to perform better than normal photo capture.
- The camera detects that the night algorithm should be entered.

Behavior:

- The Night switch appears only when the condition is met.
- If the user does not manually turn it off, tapping shutter in Photo mode will capture through the Super Night algorithm path.

Feature List judgement:

- The row should depend on night-scene detection and Super Night algorithm support.
- It should be treated as a Photo-mode transient control, not the same thing as dedicated Night mode.

### AI Zoom Transient Switch

Trigger:

- Zoom ratio is greater than 30x.
- The device has 30x+ zoom capability.
- Platform capability is high enough, at least SM7750-class.
- The project supports AI super zoom / AISR / AI SR algorithm.

Behavior:

- AI Zoom uses AI generation / super-resolution to improve clarity in high-zoom tele capture.
- It appears in the right transient-switch area when the trigger condition is met.

Feature List judgement:

- Mark as supported only when the device has the tele/high-zoom path, platform capability, and AISR/AI Zoom algorithm.
- For devices without 30x+ zoom capability or without SM7750-class platform support, mark unsupported.

### Text Mode Transient Switch

Trigger:

- The preview detects text in the frame.

Behavior:

- The Text Mode switch appears only when text is detected.
- After the user taps it, Camera frames the text boundary in the image, corrects the text perspective so it is horizontally and vertically aligned, and enhances text clarity/readability.

Feature List judgement:

- The row should depend on text detection, text boundary detection, perspective correction, and text enhancement support.
- It should be treated as a right transient-switch control, not as a fixed mode-bar mode.
