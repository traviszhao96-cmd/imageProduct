# Feature List Layout And Common Feature Rules

> Source: Travis verbal clarification, 2026-07-07.
> Purpose: guide canonical KB maintenance and 26111/26121 Feature List expansion.

## Functional Bar Layout

From top to bottom, the Camera functional areas are:

1. Top Toolbar / toolbar drawer
2. Zoom bar
3. Left and right transient switches
4. Mode bar
5. Shutter area
6. Preset area
7. Settings

The shutter area includes:

- Shutter button
- Gallery thumbnail
- Front/rear camera flip button

These shutter-area controls should **not** be expanded into Feature List rows because every camera includes them by default and they are not currently differentiated by project/camera. Only create an FL row for a shutter-area item when a project adds a clearly differentiated behavior.

## KB Versus Final FL

Use two layers:

- KB/manual layer: one row per unique function, with `模式` as a mode scope such as `全部拍摄模式` or `照片 / 人像 / 视频`.
- Final FL layer: expand the KB mode scope into one row per real project mode, then fill project/camera support columns with `✓` or `✗`.

Do not use `通用` as a mode value by default. If a function applies to all modes, write `全部拍摄模式` in KB and expand it to actual modes in final FL.

## Preset

Preset is a bottom independent functional area.

KB classification:

| Field | Value |
|---|---|
| 模式 | 全部拍摄模式 |
| 一级分类 | 功能 |
| 二级分类 | Preset |

Preset applies across modes. In final FL, expand it to the project modes when the FL needs to show per-mode support differences, unless the Bitable design explicitly creates a separate non-mode common-feature table.

## Settings

Settings are common features.

KB classification:

| Field | Value |
|---|---|
| 模式 | 全部拍摄模式 or a concrete mode scope |
| 一级分类 | 功能 |
| 二级分类 | Settings |

### General Settings

General includes:

| Setting | Meaning |
|---|---|
| Preset | Preset-related setting entry |
| Save location | Storage location setting |
| Shutter sound | Camera shutter sound setting |
| Mirror front camera | Front camera mirror setting |
| Level | Level / horizon guide setting |

### Photo Settings

Photo includes settings that can influence still-photo results, including portrait and other still photo modes.

| Setting | Meaning |
|---|---|
| Watermark | Photo watermark settings |
| Auto Tone | Photo tone processing setting |
| Tap to take a photo | Tap preview to trigger capture |
| QR code scanner | QR code scanner setting |
| Press and hold shutter | Long-press shutter behavior, such as burst or quick video |
| Ultra XDR | Ultra HDR / XDR photo display/output setting |

### Video Settings

Video includes:

| Setting | Meaning |
|---|---|
| Video encoding | User can choose H.264 or H.265 |
| Power saving recording | When enabled, Camera saves power by turning off the preview screen while the device is stationary |
| Auto FPS | User can choose Off, Auto 30 FPS, or Auto 30 & 60 FPS |

Known PRD references:

- Video H.265: `knowledge/reference/26111-prd-links.md` → `视频H265`
- Power saving recording: PRD exists; link needs to be attached when found
- Auto FPS: PRD exists; link needs to be attached when found
