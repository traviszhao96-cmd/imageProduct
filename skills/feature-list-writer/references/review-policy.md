# FL Review Policy

## 1. Boundary

Feature List is a project capability and acceptance matrix. A row belongs in FL when the team needs an independent conclusion for whether a named function or algorithm is supported in a project mode, physical camera, specification, or focal range.

Keep in FL:

- User-visible functions, entries, modes, settings, and concrete recording/output specifications.
- Algorithms that need an explicit per-mode/per-camera support conclusion.
- Effective focal range or specification when it is required to interpret `✓` or execute acceptance.
- A concise dependency or constraint that explains the support boundary.

Keep outside FL:

- Frame timing, frame count, ZSL/post-trigger capture strategy, thresholds, tuning decision tables, and detailed algorithm parameters.
- Pipeline order, stacking, mutual exclusion, and all scene-by-scene combinations.
- Internal optimization work that does not create a distinct capability or acceptance conclusion.
- Requirement history, source-project narration, implementation task lists, and detailed PRD prose.

Detailed design belongs in reviewed HAL/algorithm/software design. KB owns the canonical name, meaning, judgement basis, dependencies, and verification method. FL links the capability to the project acceptance result; it does not replace either source.

Boundary test: if a reviewer can answer the row with one project support conclusion plus a meaningful range, keep it. If the answer requires a decision tree, pipeline diagram, frame sequence, or threshold table, put those details in software design and keep only the resulting capability/range in FL.

## 2. Responsibility Model

Use two separate fields:

- `主责确认人`: exactly one approved person name. This person resolves the row and is accountable for `已确认`.
- `评审角色`: one or more roles that must review or execute acceptance.

Default routing:

| Row scope | Default accountable role | Review roles |
|---|---|---|
| Pure function, setting, entry, interaction, or product scope | Product | Product, APP, SQA |
| APP implementation behavior with no product-scope dispute | APP | Product, APP, SQA |
| Hardware, HAL, pipeline feasibility, algorithm support, camera/spec/focal boundary | HAL SE | HAL SE, relevant algorithm owner, SQA or IQA |
| Tuning parameters, image style, or effect-delivery boundary | Tuning SE | Effect Product, Tuning SE, IQA |
| Software acceptance conclusion itself is disputed | SQA | Product, APP, SQA |
| Image/video effect acceptance conclusion itself is disputed | IQA | Effect Product, Tuning SE, IQA |

Product visibility does not make Product the owner of an algorithm row. SQA/IQA normally execute acceptance and become accountable only when the unresolved decision belongs to testing.

When an owner list is supplied, create `references/owner-map.yaml` with this shape:

```yaml
people:
  - name: Full Name
    roles: [Product]
    scopes: [Toolbar, Settings]
  - name: Full Name
    roles: [HAL SE]
    scopes: [Realtime Algorithm, Post-processing Algorithm, Video Specs]
```

Select the person whose role and scope best match the row. If no unique match exists, leave `主责确认人` empty, set the row to `待确认`, and emit `OWNER_AMBIGUOUS`; never invent a name. If several people match, prefer the narrowest scope, then project-specific assignment. Do not round-robin accountability.

## 3. Description Quality Gate

A good `说明` lets a reviewer understand why the capability exists and what changes for the user without opening its source document. It must answer the relevant questions below; it is not a prose expansion exercise.

For a user-visible function, setting, entry, or control:

1. **Purpose / benefit:** what user problem it solves or what value it provides.
2. **Behavior:** how it is triggered or operated, and what options or states exist.
3. **Result impact:** what changes in preview, capture, output, saved state, or subsequent behavior when it is enabled, disabled, or changed.
4. **Default and memory:** default state/value, whether the state is remembered or reset, and the important reset boundary when the function has a state or option. Do not invent a default or memory policy for stateless actions.
5. **Scope:** applicable mode, camera, specification, focal range, or prerequisite when it changes the acceptance conclusion.

For an algorithm:

1. **Problem / benefit:** the imaging problem it addresses and the intended result.
2. **Trigger and scope:** the scene, mode, camera, specification, or focal range in which it takes effect.
3. **Observable impact:** the expected image/video change and any important tradeoff that affects acceptance.
4. **Dependency / variable:** the hardware, platform, upstream detection, input, or project boundary that determines whether it is available.

Not every row needs separate sentences for every item. Include only applicable information, but do not omit a known default, enable/disable impact, or memory/reset rule for a stateful control. Do not put source provenance, inheritance history, support conclusions, FL process narration, or test steps in place of the explanation.

Memory rules use `knowledge/reference/memory-mutex.json` as the structured baseline. It contains 45 stateful features and nine standard scenarios: switching mode, switching front/rear camera, entering Gallery, entering Settings, process kill within five minutes, Home within five minutes, process kill after five minutes, Home after five minutes, and Secure Camera. The source baseline is `Camera 互斥记忆默认值列表 v2.0.xlsx` for 25111 MP1.5; target projects must confirm deltas rather than inherit it silently.

FL descriptions should summarize only the default and the meaningful memory/reset behavior, for example: `默认关闭；切换模式和摄像头时保持，退出超过 5 分钟或进入安全相机后恢复默认。` The full nine-scenario matrix remains in KB/reference data and the verification plan. Do not paste all nine columns into every FL row.

Description quality has no minimum character count. A short definition is acceptable when it precisely identifies the capability and its relevant scope; reject a description because it is empty, generic, mechanical, circular, or substitutes a support/source conclusion for meaning, not because it is short.

Editing rule: every sentence must change the reader's understanding of purpose, behavior, result, default/memory, scope, or dependency. Remove repeated wording and sentences that only say the row exists, needs review, comes from another project, or belongs in FL. More words do not increase quality.

Reject descriptions such as:

- `支持该功能。`
- `在对应模式生效。`
- `按项目配置。`
- `26111 支持，26121 不支持。`
- `来自基线 FL。`
- `打开入口，确认选项、状态保持。`

Unsupported reasons must use a causal chain: `required dependency -> missing/limited project capability -> unsupported consequence`. Never use `按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围` as a reason. A baseline mark is evidence to investigate, not the cause. Example: `Quality depends on a high-pixel Sensor output mode and its Remosaic/output pipeline; this camera does not expose a supported high-pixel output, so Quality switching is unavailable.` If the missing dependency cannot be established, change the support cell to `TBD`, keep the row pending, and ask the accountable person.

An unsupported reason must contain three facts:

1. **Required condition:** the concrete hardware, mode, pipeline, platform, specification, product scope, or upstream capability needed.
2. **Project fact:** what this camera/project actually lacks or limits.
3. **Consequence:** why that missing condition makes this feature unavailable in this exact row.

Acceptable: `Quality requires a 50MP-or-higher Sensor output and the matching high-pixel processing path. The UW Sensor only exposes an 8MP output, so the Photo toolbar cannot provide a high-pixel Quality option.`

Reject: `26121 follows the previous project, so it is unsupported.` / `The baseline FL marks it unsupported.` / `This camera is outside the support range.` / `The project does not support it.` These are conclusions or provenance, not causes. If only the conclusion is known, use `TBD`, record the exact missing question, and do not manufacture a causal sentence.

Function descriptions should identify the entry/trigger, behavior/options, and output or state effect. Algorithm descriptions should identify the problem solved, trigger scene, effective mode/camera/focal/spec range, and important dependency or project variable.

Function controls and algorithm capabilities must not share an ambiguous canonical name. Name user controls with their interaction role, such as `HDR 开关 / HDR Switch` or `AI Zoom 开关 / AI Zoom Switch`; keep the underlying algorithm as `RAW HDR`, `Video HDR 算法`, `AIGC SR`, or another reviewed algorithm name. Flag a feature row named only `HDR`, `AI Zoom`, or another algorithm term as `NEEDS_REWRITE`.

## 4. Review Agent

Run deterministic audit first:

```bash
python3 skills/feature-list-writer/scripts/audit_fl_quality.py path/to/fl.json --output audit.json
```

Then review only flagged rows and high-risk rows (algorithm, video/high-resolution specs, focal-dependent capability, all `TBD`, and recently edited rows).

For each reviewed row, score five dimensions from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Identity | unclear/generic | named but ambiguous | canonical and unambiguous |
| Meaning | support statement only | partial behavior | explains capability/problem and result |
| Scope | missing | mode/camera only | relevant mode/camera/spec/focal/trigger boundary |
| Evidence consistency | conflicts or invented | weak/inherited only | consistent with approved evidence or explicitly TBD |
| Testability | cannot derive acceptance | partial | verification can prove the stated boundary |

For stateful feature rows, `Meaning=2` additionally requires the known enable/disable or option impact, default state, and meaningful memory/reset behavior. For algorithm rows, `Meaning=2` requires the problem solved and observable result; naming an algorithm or saying it improves quality is insufficient. Length is never scored directly.

Verdicts:

- `PASS`: score >= 8, no dimension is 0, no evidence conflict.
- `NEEDS_REWRITE`: meaning is known but wording is generic, mechanical, duplicated, or misplaced.
- `NEEDS_OWNER_INPUT`: support, range, reason, or accountable person cannot be resolved from approved evidence.
- `BOUNDARY_VIOLATION`: row is detailed design/optimization rather than an independently accepted capability.

The Agent may propose a rewrite only from existing evidence. It must not invent a focal range, specification, trigger, unsupported reason, or person. It must group the same KB capability across modes and flag inconsistent descriptions instead of rewriting each row independently.

Output a review queue with: project, mode, feature name, issue code, verdict, current text, evidence used, proposed text or exact owner question, and severity. Humans review critical conflicts and disputed rows; AI can directly apply low-risk wording normalization after preserving meaning.
