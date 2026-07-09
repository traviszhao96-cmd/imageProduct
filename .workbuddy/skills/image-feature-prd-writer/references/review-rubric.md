# Review Rubric

Use this rubric for the initial requirement review after drafting or when the user asks for review only.

## Development Review

### Shared (Camera + Gallery)

- Objective: whether the expected outcome is specific enough to implement
- Scope: whether feature boundaries are explicit
- Dependency: whether hardware, algorithm, platform, and cross-team inputs are named
- Schedule risk: whether milestones depend on unstable inputs
- Rollback strategy: whether downgrade or feature-off behavior exists

### Camera-Specific

- Interface impact: whether upstream and downstream modules are identified
- Resource impact: whether performance, memory, storage, and power costs are mentioned
- Observability: whether logs, metrics, or debug hooks are needed
- **Memory rules: whether the feature's persistence behavior is defined across all 9 standard scenarios** (switch mode, switch camera, gallery, settings, kill 5min in/out, Home 5min in/out, secure camera). If a feature modifies user state, every scenario must have an explicit answer.
- **Mutual exclusion: whether all conflicting features are listed with resolution behavior** (disable self, disable other, coexistence with algorithm bypass, etc.) and whether basic/pro differences are noted.

Common findings:
- Requirement goal is present, but implementation boundary is missing
- Hardware dependency is implied, not confirmed
- No downgrade strategy when algorithm or tuning is not ready
- `功能未定义切换模式后的记忆行为，开发和测试无法确定预期状态。`
- `未列出与 HDR/夜景/闪光灯的互斥关系，可能引入未预期的功能冲突。`

### Gallery-Specific

- Feature entry and exit conditions
- Page or layer state after entering the feature
- Interaction sequence and toolbar behavior
- Object model and editable attributes
- Save, cancel, undo, and redo behavior
- Selection, focus, and editing-state transitions

Common findings:
- `需明确 Text 输入完成后的默认选中态，否则编辑态切换容易产生实现分歧。`
- `需明确保存后是否覆盖原图，否则存储链路和恢复策略无法收敛。`

## Testing Review

### Shared

- Acceptance criteria: observable and testable pass conditions
- Abnormal flow: interruption, low battery, temperature, storage full, permission denial
- Regression impact: whether related modes or pipelines are listed

### Camera-Specific

- Test objects: mode, scene, device matrix, version matrix
- Environment dependency: lab, field, darkroom, ISP package, calibration state
- Compatibility coverage: region, SKU, memory variant, thermal state
- Objective evidence: sample rules, logs, metrics, screenshots, or EXIF signals

Common findings:
- Acceptance language is subjective and cannot support pass/fail judgment
- Scene coverage insufficient for low light, backlight, motion, and zoom transitions
- Regression scope does not mention adjacent functions such as portrait, video, or gallery

### Gallery-Specific

- Coverage of repeated entry and repeated editing
- Compatibility across image ratios and orientations
- Validation of undo, redo, cancel, and save paths
- Edge cases: empty text, max count, overlap, off-canvas movement

Common findings:
- `需补充空文本直接保存是否允许，否则无法定义通过标准。`
- `需补充最大输入长度和超限提示，否则边界测试无法覆盖。`

## Risk Grading

- High: may block implementation or release
- Medium: may cause rework, unstable scope, or low test efficiency
- Low: wording or completeness issue with limited downstream impact

## Review Output Style

- Keep each finding to one or two sentences
- State the issue first, then the impact
- If possible, propose the minimum extra information needed to close the issue
