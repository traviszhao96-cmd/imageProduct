# Review Rubric

Use this rubric for the initial requirement review after drafting or when the user asks for review only.

## Development Review

Check whether the document clearly defines:

- Objective: whether the expected outcome is specific enough to implement
- Scope: whether feature boundaries are explicit
- Dependency: whether hardware, algorithm, platform, and cross-team inputs are named
- Interface impact: whether upstream and downstream modules are identified
- Resource impact: whether performance, memory, storage, and power costs are mentioned
- Schedule risk: whether milestones depend on unstable inputs
- Rollback strategy: whether downgrade or feature-off behavior exists
- Observability: whether logs, metrics, or debug hooks are needed

Typical findings:

- Requirement goal is present, but implementation boundary is missing.
- Hardware dependency is implied, not confirmed.
- KPI exists, but measurement path is absent.
- There is no downgrade strategy when algorithm or tuning is not ready.

## Test Review

Check whether the document clearly defines:

- Acceptance criteria: observable and testable pass conditions
- Test objects: mode, scene, device matrix, version matrix
- Environment dependency: lab, field, darkroom, ISP package, cloud model, calibration state
- Compatibility coverage: region, SKU, memory variant, thermal state, accessory state
- Abnormal flow: interruption, low battery, temperature, storage full, permission denial
- Regression impact: whether related modes or pipelines are listed
- Objective evidence: sample rules, logs, metrics, screenshots, or EXIF signals

Typical findings:

- Acceptance language is subjective and cannot support pass/fail judgment.
- Scene coverage is not enough for low light, backlight, motion, and zoom transitions.
- Regression scope does not mention adjacent functions such as portrait, video, or gallery.
- No objective output signal is defined for algorithm enablement or fallback.

## Risk Grading

Use lightweight grading:

- High: may block implementation or release
- Medium: may cause rework, unstable scope, or low test efficiency
- Low: wording or completeness issue with limited downstream impact

## Review Output Style

- Keep each finding to one or two sentences.
- State the issue first, then the impact.
- If possible, propose the minimum extra information needed to close the issue.
