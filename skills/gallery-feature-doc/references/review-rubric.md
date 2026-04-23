# Review Rubric

Use this rubric when reviewing a Gallery software feature PRD.

## Development Review

Check whether the document clearly defines:

- feature entry and exit conditions
- page or layer state after entering the feature
- interaction sequence and toolbar behavior
- object model and editable attributes
- save, cancel, undo, and redo behavior
- selection, focus, and editing-state transitions
- unsupported or deferred behaviors
- event tracking requirements

Common review comments:

- `需明确 Text 输入完成后的默认选中态，否则编辑态切换容易产生实现分歧。`
- `需明确保存后是否覆盖原图，否则存储链路和恢复策略无法收敛。`
- `需明确多文本对象的层级与选中优先级，否则拖拽与删除逻辑容易冲突。`

## Testing Review

Check whether the document supports:

- clear acceptance criteria
- coverage of normal flow and abnormal flow
- coverage of repeated entry and repeated editing
- compatibility across image ratios and orientations
- validation of undo, redo, cancel, and save paths
- validation of edge cases such as empty text, max count, overlap, or off-canvas movement

Common review comments:

- `需补充空文本直接保存是否允许，否则无法定义通过标准。`
- `需补充多比例图片下工具栏和画布区域的适配要求，否则兼容性测试范围不清晰。`
- `需补充最大输入长度和超限提示，否则边界测试无法覆盖。`
