# Required Info Checklist

Use this checklist before drafting a Gallery software feature document.

## 1. Basic Feature Definition

- Feature name
- Feature type
  Examples: `Text`, `Draw`, `Markup`, `Sticker`, `Filter adjustment`
- Is it a new feature, an enhancement, or a redesign
- Applicable module
  Examples: edit page, photo viewer, album detail page

## 2. User Value

- What user problem does it solve
- In which scenario will it be used
- What is the expected user benefit
- Is there any benchmark product or reference behavior

## 3. Entry and Main Flow

- Where the user enters the feature
- What the first visible state is
- What the main toolbar or panel contains
- What the user can do step by step
- What the top-level actions are
  Examples: `Cancel`, `Undo`, `Redo`, `Save`

## 4. Editable Objects and Properties

- What object is being edited
  Examples: text box, stroke, shape, sticker
- Which properties can be changed
  Examples: color, size, opacity, font, alignment, position
- Which properties are global and which are object-level
- Whether editing selections can be re-entered later

## 5. State and Persistence

- What happens on save
- What happens on cancel
- Whether undo and redo are supported
- Whether edits overwrite the original or create a new image
- Whether restoration or non-destructive behavior exists

## 6. Scope Boundary

- What is in scope
- What is explicitly out of scope
- Any unsupported file types, entry paths, or image states
- Any known limits
  Examples: max object count, no GIF support, no video support

## 7. Layout and Compatibility

- Which image ratios or orientations must be supported
- Whether dark mode and light mode matter
- Whether foldable, tablet, or large-image cases matter
- Any performance expectation

## 8. Analytics and Metrics

- Entry event
- Tool usage events
- Save or cancel events
- Error or limit events

## Follow-up Prompt Style

If information is missing, ask grouped questions like:

- `请补充入口路径、主流程和顶部操作，否则交互链路无法写清楚。`
- `请补充 Text 功能支持哪些属性调整，否则功能范围和测试点会过于模糊。`
- `请补充保存策略和撤销恢复规则，否则开发和测试无法确认最终行为。`
