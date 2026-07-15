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

A good `说明` lets a reviewer understand the row without opening its source document. It must answer:

1. What is the function or algorithm?
2. What user-visible behavior or imaging problem does it address?
3. Where does it apply: mode, camera, focal range, specification, or trigger?
4. What boundary or variable still needs project confirmation?

Not every row needs four separate sentences, but all relevant information must be present. Do not put source provenance, support conclusions, or test steps in place of the explanation.

Reject descriptions such as:

- `支持该功能。`
- `在对应模式生效。`
- `按项目配置。`
- `26111 支持，26121 不支持。`
- `来自基线 FL。`
- `打开入口，确认选项、状态保持。`

Unsupported reasons must use a causal chain: `required dependency -> missing/limited project capability -> unsupported consequence`. Never use `按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围` as a reason. A baseline mark is evidence to investigate, not the cause. Example: `Quality depends on a high-pixel Sensor output mode and its Remosaic/output pipeline; this camera does not expose a supported high-pixel output, so Quality switching is unavailable.` If the missing dependency cannot be established, change the support cell to `TBD`, keep the row pending, and ask the accountable person.

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

Verdicts:

- `PASS`: score >= 8, no dimension is 0, no evidence conflict.
- `NEEDS_REWRITE`: meaning is known but wording is generic, mechanical, duplicated, or misplaced.
- `NEEDS_OWNER_INPUT`: support, range, reason, or accountable person cannot be resolved from approved evidence.
- `BOUNDARY_VIOLATION`: row is detailed design/optimization rather than an independently accepted capability.

The Agent may propose a rewrite only from existing evidence. It must not invent a focal range, specification, trigger, unsupported reason, or person. It must group the same KB capability across modes and flag inconsistent descriptions instead of rewriting each row independently.

Output a review queue with: project, mode, feature name, issue code, verdict, current text, evidence used, proposed text or exact owner question, and severity. Humans review critical conflicts and disputed rows; AI can directly apply low-risk wording normalization after preserving meaning.
