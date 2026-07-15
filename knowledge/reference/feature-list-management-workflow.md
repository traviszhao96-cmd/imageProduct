# Camera Feature List Management Workflow

> Date: 2026-07-14
> Current release: 26111 / 26121 Camera Feature List v1.0
> Purpose: define what FL management is, how a project FL is produced, and the completion criteria for organization, confirmation, and acceptance.

## 1. What FL Management Is

Feature List is the project's final Camera capability and acceptance checklist. It answers a concrete question:

> For this project, mode, physical camera, and specification, is this function or algorithm supported?

FL is an output, not the canonical source of product taxonomy or function meaning. Its repeated mode rows and camera support columns are intentionally verbose because Product, SQA, and IQA need an explicit acceptance matrix.

FL management is therefore not just maintaining a Base table. It is a small product-management system that continuously turns requirements, knowledge, hardware, and project decisions into an auditable project checklist.

The managed layers are:

| Layer | Responsibility |
|---|---|
| Project requirements / PRDs | Define new behavior, scope changes, and project decisions |
| Unified KB | Maintain the unique taxonomy, hierarchy, meaning, judgement basis, dependencies, and verification method of each function or algorithm |
| Feature Tree view | Generated from KB classification and parent relations for navigation and audit; not maintained separately |
| Hardware / project config | Maintain physical cameras, sensor/platform limits, inherited capability, and project switches |
| Project FL | Expand the maintained inputs into mode-by-camera `✓ / ✗ / TBD` acceptance rows |
| Change log | Record version, time, scope, old value, new value, and modifier |

## 2. End-To-End Workflow

```text
PRD / HAL / algorithm design / baseline FL / project feedback
                            |
                            v
                  Extract project changes
                            |
                            v
              Map each change to existing KB nodes
                            |
              +-------------+-------------+
              |                           |
       Existing capability          Truly new capability
       Update existing node         Add one new KB node
              |                           |
              +-------------+-------------+
                            |
                 Human review of integration
                            |
                            v
             AI audit: duplicate, conflict, missing evidence
                            |
                            v
       Expand KB with hardware/config into project FL draft
                            |
                            v
          AI audit: missing rows, bad support marks, drift
                            |
                            v
       Product / HAL SE / Tuning SE resolve disputed and high-risk items
                            |
                            v
             Publish versioned Base + change record
                            |
                            v
                    SQA / IQA acceptance
```

Today's 26111 / 26121 work followed this path: consolidate PRDs, algorithm documents and HAL design into local knowledge; correct KB taxonomy, terminology and ownership; generate separate project FLs; review and edit the table; run consistency checks; write the final data back to Base; then distribute an SE checklist for remaining confirmation.

## 3. Requirements For A Project FL

### Structure

- 26111 and 26121 are separate project tables under one versioned Base.
- Each real Camera mode has a filtered view. Views are grouped by mode, not by first-level category.
- `模式`、`一级分类`、`二级分类` use bilingual values.
- First-level categories are only `功能 / Feature`、`算法 / Algorithm`、`通用 / Common`.
- `通用 / Common` is placed at the bottom and contains Settings, Preset, and Widget as second-level areas. They are not repeated under capture modes.
- A KB capability is expanded into one row per relevant project mode when the mode needs an independent acceptance result.
- Unsupported capabilities remain visible as `✗`; they are not deleted merely to shorten the table.

### Content

Every FL row must contain enough information for another person to judge and test it:

- A unique, canonical feature or algorithm name.
- A useful description of what the capability is and its applicable range.
- An independent `✓ / ✗ / TBD` judgement for every physical camera in the project.
- A concrete reason for each meaningful `✗`.
- Hardware, platform, mode, focal-range, specification, trigger, performance, power, and mutual-exclusion dependencies when applicable.
- A verification method that describes how to prove the judgement, not merely a PRD name or check mark.
- One named `主责确认人` per row, resolved from the approved person-to-scope map.
- Multi-select `评审角色`: `Product`、`APP`、`HAL SE`、`Tuning SE`、`SQA`、or `IQA`.
- A status consistent with the support columns: any unresolved `TBD` means `待确认`.

### Ownership

- `Product`: requirement scope, user-visible function, interaction, and product decision.
- `HAL SE`: hardware, HAL, pipeline, algorithm, integration feasibility, specification boundary, and project support judgement.
- `Tuning SE`: image tuning scope, tuning parameters, and tuning delivery judgement.
- `SQA`: software function, interaction, state, compatibility, and specification acceptance execution.
- `IQA`: image/video quality and algorithm-effect acceptance execution.

Algorithm rows route to a named `HAL SE` or `Tuning SE` person according to ownership. Product visibility does not make Product the accountable person for an algorithm row. SQA and IQA are core readers and acceptance executors; they become accountable only when the unresolved decision genuinely belongs to testing. If the approved owner map cannot produce one unique person, keep the row `待确认` and raise `OWNER_AMBIGUOUS` instead of inventing a name.

## 4. Three Completion Gates

### Gate 1: FL Organization Complete

This means the FL is ready to distribute for partner review. It does **not** mean every support judgement is final.

All of the following must be true:

- Current PRDs, HAL/algorithm design, baseline FL, hardware config, and known project decisions have been included.
- Requirements have been mapped into canonical KB nodes; existing capabilities update existing nodes instead of creating duplicate rows, and the Feature Tree is generated from the same data.
- All project modes, cameras, common settings, concrete video/slow-motion/high-resolution specifications, and known unsupported differences have been expanded.
- Every row has a name, classification, description, owner, support cells, and verification method.
- Remaining uncertainty is explicitly marked `TBD / 待确认`, with a clear question and responsible role.
- AI audit has checked duplicate names, missing descriptions, status/support inconsistency, unsupported rows without reasons, and conflicts with source documents.
- Project tables, mode views, version label, and change log are published and match the local final data.

Gate 1 allows unresolved items, but it does not allow hidden uncertainty or empty checklist rows.

### Gate 2: FL Confirmation Complete

This means Product, HAL SE, and Tuning SE can freeze the capability matrix as the project's intended design.

For an individual row to be confirmed:

- Every project camera is `✓` or `✗`; no `TBD` remains.
- The support judgement has an identifiable basis: approved requirement, HAL/algorithm design, hardware/config, or explicit owner decision.
- Every `✗` has a correct reason where the distinction matters.
- Dependencies and supported mode/spec/focal range are explicit enough for testing.
- The verification method can prove the row's support boundary.
- The row has no unresolved conflict with another project document.
- The named accountable person accepts the judgement and the status is `已确认`.

For the whole FL to be confirmation-complete:

- No unresolved `TBD` remains.
- No P0/P1 missing capability or disputed support judgement remains open.
- Product has confirmed functional and interaction scope.
- HAL SE has confirmed hardware, HAL, pipeline, algorithm integration, specification, and dependency boundaries; Tuning SE has confirmed tuning-related boundaries.
- AI audit has been rerun after human changes and no critical inconsistency remains.
- The frozen version and its changes are recorded in the Base change log.

### Gate 3: FL Acceptance Complete

This is later than FL confirmation. It means implementation has been tested against the frozen FL:

- SQA has completed functional, interaction, state, compatibility, and specification verification.
- IQA has completed required image/video quality and algorithm-effect verification.
- Supported rows pass their verification methods; unsupported rows expose no unintended entry or behavior.
- Defects and deviations are closed, accepted, or reflected back into a new FL version.

Only Gate 3 means the project implementation has completed FL-based acceptance. Generating a table, publishing v1.0, or resolving all TBD items alone does not mean development and testing are complete.

## 5. AI And Human Review Boundary

AI should maintain the repetitive and auditable work:

- Read and normalize documents.
- Detect whether a requirement updates an existing capability or creates a new one.
- Expand KB mode scopes into project rows.
- Apply deterministic hardware/config rules.
- Detect duplicates, missing descriptions, invalid owners, contradictory support marks, and source drift.
- Produce a dispute list and change summary.

Humans should focus on decisions that require accountability or project judgement:

- Whether a disputed capability is in project scope.
- Whether HAL/algorithm feasibility is sufficient for mass production.
- Which specifications, cameras, and focal ranges are finally opened.
- Whether quality, performance, power, and stability risks are acceptable.

The goal is not to remove human confirmation. It is to stop spending human time maintaining repeated dead information and instead use that time on disputed, high-risk decisions.

## 6. FL And Software Design Boundary

The 2026-07-15 first review clarified the boundary between the project checklist and detailed algorithm design:

- FL records whether a capability is supported for a mode and physical camera, plus the specification or focal range needed for acceptance.
- Software design records frame timing, ZSL/post-trigger capture strategy, frame counts, decision thresholds, pipeline ordering, algorithm stacking and mutual exclusion.
- KB keeps canonical terminology and enough meaning for AI and reviewers to understand both artifacts.
- A detailed design item is not repeated as an FL row unless teams need an independent project support or acceptance conclusion for it.

For example, frame capture strategy belongs to software design and is not maintained as a KB or project FL capability row. HDSR remains in FL because the project needs an explicit support and effective-focal-range conclusion.
