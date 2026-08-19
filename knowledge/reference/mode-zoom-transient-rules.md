# Camera Mode / Zoom Bar / Transient Switch Rules

> Source: Travis verbal clarification, 2026-07-07.
> Online PRD sources checked 2026-07-15: `Camera 5.0-变焦圆盘 Zoom dial` (revision 624), `Camera 4.0 交互&视觉体验优化汇总` (revision 1200), `Camera 5.1-前置自动小广角` (revision 12), and mode-specific PRDs.
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

1. Start from the project's actual camera selection and configured capture paths. Do not copy another project's UI points merely because the product tier or mode name is similar.
2. Cover every hardware optical zoom point exposed by the selected cameras.
3. If a selected camera supports **In-Sensor Zoom (ISZ)**, also expose its configured ISZ point.
4. If the project configures another recommended quality path, such as **Hex Zoom**, it may also be exposed as a UI point even though it is not a separate physical lens or ISZ point.
5. A default zoom point must represent a real project capture path, not a decorative UI stop.

Project selection baselines:

| Project | Camera-selection-derived rear Photo UI points | Meaning |
|---|---|---|
| 26111 | 0.6x / 1x / 2x / 4x | 0.6x UW; 1x Main; 2x Main 200MP ISZ; 4x Main Hex Zoom. The project has no Tele camera. |
| 26121 | 0.6x / 1x / 2x / 3.5x | Follows the 25111 Pro camera selection/configuration; 3.5x is the Tele entry. |

These are project-level candidate points. Each mode must still filter them by its own confirmed pipeline. For example, Video must not inherit Photo ISZ or Hex Zoom when the video pipeline does not support those paths.

For the 26111 HP5 Main sensor, the sensor documentation separately defines 200MP software remosaic, 50MP four-pixel summation followed by hardware remosaic, and 12.5MP eight-pixel summation plus two-average binning. These sensor output operations are capability evidence, not UI-zoom evidence. The 2x UI point is classified as ISZ because the 26111 HAL explicitly defines the 2x ISZ path; the 4x UI point is classified as Hex Zoom because the HAL defines hex/4x4 RAW plus external software remosaic. Do not rename 4x as ISZ or Tele.

Default zoom points are mode-specific. A Photo-mode ISZ point must not be copied into Video, Slow Motion, or another mode unless that mode has its own confirmed ISZ path. For 26111 and 26121, Video does not support ISZ because switching the ISZ setting causes visible effect jumps and increases power consumption; the Photo ISZ conclusion cannot be used as Video FL evidence.

Example: 25131 has an ultrawide camera and a main camera. The main camera supports ISZ and can output 12MP at 2x. Therefore its configured default zoom points are:

| Zoom point | Meaning |
|---|---|
| 0.6x | Ultrawide hardware point |
| 1x | Main camera hardware point |
| 2x | Main camera ISZ point |

### Zoom Dial Point Types

Do not treat every point shown on the Zoom dial as a default UI zoom point. The online Zoom dial PRD defines four different point types:

| Point type | Display and behavior |
|---|---|
| Optical / ISZ zoom point | Hardware quality peak. Permanently shows ratio, tick and equivalent focal length; supports highlight and snapping. |
| Integer marker | Used mainly at 10x and above. Permanently shows ratio and tick, but no equivalent focal length and no snapping. |
| Quick zoom point | Intermediate common focal length shown as a dot. Equivalent focal length appears when the dial reaches the point; supports snapping. |
| Other scale | Reference tick only. The PRD suggests one tick per 5x, adjustable by visual density. |

`UI zoom point` and `Quick zoom point` must remain separate fields in project zoom specifications:

- UI zoom points come from exposed optical points and confirmed ISZ points.
- Quick zoom points are optional intermediate focal lengths configured by mode and project.
- Clicking a UI focal button to switch focal length is an interaction on the UI point; it does not make that point a Quick zoom point.
- A mode without explicit quick-point configuration should not inherit another mode's points automatically.

Quick Zoom points are ratio-led, not label-led. Define the point from the configured Zoom-dial ratio and the calibrated equivalent focal length of the physical camera that supplies the point, then derive the integer `mm` label used by the UI. The rounded project label (for example `24mm` for Main) is a display value and must not be used to reverse-calculate the ratio. This is why a Quick Zoom point must be maintained as a mapping such as `ratio · displayed focal length · source camera`, not as a free-standing traditional photography focal length.

Online baseline examples:

| Mode / camera | Quick zoom points | Rule |
|---|---|---|
| Rear Photo | 1.2x / 28mm; 1.5x / 36mm | Confirmed by the Zoom dial PRD baseline. |
| 26111 Rear Video / Dual View Rear Stream | None | UI zoom points are 0.6x / 1x / 2x / 4x. Continuous zoom is 0.6x-8x. |
| 26121 Rear Video / Dual View Rear Stream | None | UI zoom points are 0.6x / 1x / 2x / 3.5x / 7x. Continuous zoom is 0.6x-20x. |
| Front camera | None | Front Auto Wide is removed from the 26111/26121 project scope. Front UI exposes only 1x on the Front camera. UI Spec focal lengths use rounded integers: 23mm on 26111 and 24mm on 26121. |
| 25111 Pro / 26121 Rear Portrait | None as extra quick dots | 1x / 2x / 3.5x are fixed UI focal entries; continuous zoom is 1x-3.5x. This Tele-derived baseline does not apply to 26111. |

Action mode is a photo-class mode and inherits Rear Photo Quick Zoom points `1.2x / 28mm` and `1.5x / 36mm`. It also uses project-specific UI zoom points and supports continuous zoom across the same displayed range. 26111 Rear Action uses `0.6x / 1x / 2x / 4x` with continuous zoom `0.6x-4x`; 26121 Rear Action uses `0.6x / 1x / 2x / 3.5x / 7x` with continuous zoom `0.6x-7x`. Preset focal-length support remains independently confirmable.

Rear Night follows Rear Photo for each project. UI zoom points, Quick Zoom points, continuous zoom range, and Preset focal-length candidates must stay aligned between the two rows; do not maintain an independent reduced Night zoom range. Front Night follows the project Front definition: Front 1x only, with no 0.8x entry or orientation-based switching.

Rear Expert also follows Rear Photo for each project. UI zoom points, Quick Zoom points, continuous zoom range, and Preset focal-length candidates must remain aligned with Rear Photo. Photo, Night, and Expert rear rows should be updated together whenever the project zoom configuration changes.

Video, Dual View, Front Video, Slow Motion, and Timelapse do not support Quick Zoom points and must write `不支持` rather than `无`, `无额外点`, or `TBD`. For Rear Video and the Dual View rear stream, 2x / 4x on 26111 and 2x / 7x on 26121 are UI zoom points, not Quick Zoom points.

Motion Photo uses the same focal-length support as Photo and is not maintained as a separate mode row in the Zoom Range Matrix. Any future Motion Photo-specific focal restriction must first be confirmed as a real project difference before a separate row is reintroduced.

26111 Rear Portrait exposes only Main 1x and Main 2x ISZ, with continuous zoom `1x-2x`. It does not support 3.5x Tele because the project has no Tele camera, and it does not support the Main-camera 4x Hex Zoom path.

### Preset Focal-Length Projection

`Preset 支持焦段` is a discrete restoration list, not another name for the continuous zoom range.

For each project/mode/position row:

1. Include the equivalent focal lengths of every confirmed `UI 变焦点` in that row.
2. Include every confirmed `快速变焦点` in that row.
3. Add only explicitly approved `扩展焦段 / Extension focal points`. An extension needs a product framing purpose, a real capture path, acceptable output quality, and a position on the configured Zoom dial. “Common photography focal length” by itself is not evidence.
4. Intersect the result with the mode's supported camera, continuous range, output specification, and restoration capability.
5. Sort from wide to tele and store one `Nmm` value per line. Do not copy a project-wide superset into a restricted mode.

The stable identity of a point is its project capture path and Zoom-dial position. The displayed `mm` is presentation metadata. UI Spec should preserve the ratio-to-focal mapping in `UI 变焦点`, `快速变焦点`, or `判断依据` whenever it is known.

Current 26121 product conclusions used by the UI Spec:

- Rear Photo-class UI points: `15mm / 24mm / 48mm / 80mm / 160mm`.
- Rear Photo-class Quick Zoom points: `28mm / 36mm`, using the calibrated Main-camera ratio mapping from the Zoom-dial baseline rather than reverse-calculation from the rounded `24mm` label.
- `100mm` is a project-approved Preset extension point where the mode's range and pipeline allow it.
- Rear Photo, Night, Expert, and Action therefore use the ordered candidate list `15 / 24 / 28 / 36 / 48 / 80 / 100 / 160mm` when their mode pipeline exposes the same UI and Quick points.
- Rear Video and Timelapse do not expose Quick Zoom points. Their confirmed Preset list is `15 / 24 / 36 / 48 / 80 / 100 / 160mm`; `36mm` and `100mm` are extensions rather than Quick Zoom points in those modes.
- Portrait, Slow Motion, Panorama, High Resolution, Front, and other restricted rows keep only their independently confirmed subset; they must not inherit the full Rear Photo list.

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
