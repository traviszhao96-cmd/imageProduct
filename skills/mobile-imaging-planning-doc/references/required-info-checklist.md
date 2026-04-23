# Required Info Checklist

Use this checklist before drafting a mobile imaging planning document.

## Product Context

- Product name or project code
- Target market or target region
- Target launch window
- Product stage: concept, pre-study, planning, implementation, or release refinement
- Related hardware platform, if already fixed

## User and Scenario

- Core user group
- Core use scenario
- Current pain point or opportunity
- Competing baseline or internal baseline
- Expected user-visible improvement

## Scope Definition

- Feature name
- In-scope capabilities
- Explicit out-of-scope items
- Trigger conditions or entry path
- Configuration options or control strategy

## Technical Dependencies

- Sensor, lens, flash, or other hardware dependency
- ISP, NPU, SoC, or memory/performance dependency
- Camera framework or Android version dependency
- Algorithm maturity or model availability
- Cross-team dependency: camera, tuning, framework, gallery, cloud, OTA, legal

## Quality and Metrics

- Success metric or KPI
- Image quality target
- Performance target: capture latency, preview fluency, processing time
- Stability target
- Compatibility boundary

## Delivery and Validation

- Milestone plan
- Owner or responsible team
- Test entry and exit criteria
- Risks and fallback plan
- Whether grayscale, pilot, or regional rollout is needed

## Clarification Prompt Pattern

When critical fields are missing, ask like this:

```markdown
以下信息缺失，当前无法可靠定稿，请先补充：

1. 产品与版本信息
- 机型/项目代号：
- 上市时间或版本窗口：

2. 功能范围
- 功能边界：
- 明确不做的内容：

3. 技术依赖
- 依赖的硬件/算法/平台条件：
- 是否涉及跨团队支持：

4. 验收与风险
- 成功指标：
- 已知风险或兜底方案：
```
