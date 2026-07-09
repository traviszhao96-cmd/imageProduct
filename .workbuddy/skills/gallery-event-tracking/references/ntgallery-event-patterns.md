# NTGallery Event Patterns

Source workbook:

- `/Users/travis.zhao/Downloads/NTGallery App Event Tracking Spec 2026 v1.0 (1).xlsx`

## Sheets

- `Manage`
- `Edit`
- `Settings`

## Common Columns

Bitable 列名与 PRD 列名映射：

| Bitable 列 | PRD 列 | 含义 |
| --- | --- | --- |
| `event` | `event_name` | 事件名 |
| `label` | `key` | 参数名 |
| `label_note` | `key_description` | 参数的中文说明 |
| `value` | `parameter_value` | 参数可选值 |
| `value_note` / `操作场景说明` | `说明` | 触发场景/备注 |

## Edit Sheet Pattern

### Entry and click events

`edit_action`

Examples:

| parameter_name | parameter_value |
| --- | --- |
| `enter_module` | `adjust / crop / erase / filter / watermark / trim / audio / slow_mo` |
| `adjust_click` | specific adjust item |
| `erase_click` | specific erase item |
| `crop_click` | specific crop item |
| `watermark_click` | specific watermark item |
| `UUID` | session identifier |

### Save-time settlement events

Examples:

| event_name | parameter_name | parameter_value |
| --- | --- | --- |
| `edit_adjust` | changed parameter names | final numeric values |
| `edit_adjust` | `UUID` | `xxxx` |
| `edit_crop` | `ratio / rotate_slider / rotate_90 / flip / vertical / horizontal` | final applied values |
| `edit_crop` | `UUID` | `xxxx` |

## Recommendation For New Edit Features

For a new edit feature like `Text` or `Draw`:

1. Add `edit_action` with `enter_module`.
2. Add `UUID`.
3. Add one save-time event such as `edit_text` or `edit_draw`.
4. Put only final effective parameters into the save-time event.
5. Add process events only when product analysis truly depends on them.
