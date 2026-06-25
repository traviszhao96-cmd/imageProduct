# Feature To Field Mapping

Use this reference when turning product-language requests into analytics fields.

## 1. Filter usage

Product request:

- 滤镜使用
- 原图 / 官方有名称滤镜 / 自制滤镜

Primary field:

- `filter`

Business interpretation:

- Raw image:
  - `filter = 0`
  - or empty / null if the export uses blank for not applied
- Official named filter:
  - `filter` is not `0`
  - and the value belongs to the official filter list from `Nothing Filter 3.1 for Camera_Gallery.xlsx`
- DIY filter:
  - `filter` is not `0`
  - and the value is not in the official filter list

Official filter list:

- `Stretch`
- `Chrome`
- `Analog`
- `Amber`
- `Natural`
- `Retro`
- `Tone`
- `CC Film`
- `Warm`
- `Cold`
- `Texture`
- `B&W Film`
- `Noir`
- `Negative`
- `Lenticular`
- `Silver`

Observed raw aliases:

- `cc` should be treated as `CC Film`
- `b&w` should be treated as `B&W Film`
- raw values are usually lowercase short names such as `stretch`, `chrome`, `analog`, `amber`
- numeric values such as `101`, `102` should currently be treated as DIY / custom unless product gives an official mapping table

Recommended output:

- One pie / donut chart with:
  - raw image percentage
  - official filter percentage
  - DIY filter percentage
- Optional:
  - top official filters
  - top DIY filter names

Important note:

- This is different from `preset`.
- Do not map “滤镜使用” to `preset` unless the user explicitly means preset.

## 2. Tuning usage

Product request:

- tuning 功能使用
- 调色
- 具体调节参数

Primary fields:

- `tuning_apply`
- `tuning_contrast`
- `tuning_saturation`
- `tuning_warmth`
- `tuning_tint`
- `tuning_shapen`
- `tuning_grain`
- `tuning_vignette`

Business interpretation:

- `tuning_apply`
  - `0` = not applied
  - `1` = applied
- `tuning_contrast`
  - range `-10.0 ~ +10.0`
- `tuning_saturation`
  - range `-10.0 ~ +10.0`
- `tuning_warmth`
  - range `-10.0 ~ +10.0`
- `tuning_tint`
  - range `-10.0 ~ +10.0`
- `tuning_shapen`
  - range `0 ~ 10.0`
- `tuning_grain`
  - range `0 ~ 10.0`
- `tuning_vignette`
  - range `0 ~ 10.0`

Recommended output:

- `tuning_apply` usage rate
- Non-zero usage rate for each parameter
- Distribution of parameter values
- Per-model comparison

Important note:

- If these fields are missing in the current shared database, say the database needs a refreshed export / rebuild before this request can be answered fully.

## 3. EV adjustment

Product request:

- EV 调节
- 曝光调节

Primary field:

- `exposure_adjust`

Business interpretation:

- `0` = not adjusted
- `1` = adjusted

Important note:

- Current definition only indicates whether the user manually adjusted exposure before shutter.
- It does not mean the actual EV numeric amount unless another field exists.

Recommended output:

- EV adjustment usage rate
- Per-model usage difference
- By-mode / by-camera penetration

## 4. Existing nearby fields that should not be mixed up

- `preset`
  - preset usage, not filter usage
- `retouching`
  - beauty intensity, not tuning
- `nightmode`
  - night scene state, not exposure adjustment

## 5. Response rule

When a user asks for one of the mapped feature points:

1. First map the product phrase to the field above.
2. Check whether the field exists in the current database schema.
3. If it exists, query directly.
4. If it does not exist, say:
   - the requested metric is clearly defined in the tracking spec
   - but the current database does not yet contain the corresponding field
   - and the export / parsing step needs to be refreshed
