# 26111 / 26121 Feature List First Review

> Meeting: 2026-07-15 14:17-14:54
> Source: `/Users/travis.zhao/Downloads/26111 & 26121 Feature list 第一轮评审.txt`
> Status: first-round framework review; not a final FL freeze review

## 1. Confirmed Positioning

Feature List is a shared project capability and acceptance matrix, not a requirement list. It must let Product, APP, SE, SQA and IQA answer:

> In this project, mode and physical camera, is this function or algorithm supported, and what is its effective range?

The FL keeps explicit per-mode and per-camera support rows. The KB maintains canonical names and explanations. Detailed frame timing, algorithm decision thresholds and pipeline composition belong in the reviewed software design, with the FL retaining the support result and the range needed for acceptance.

## 2. Decisions Applied After The Meeting

| Topic | Decision |
|---|---|
| First-round status | Reset every non-Pending row to `待确认`; existing support marks remain candidate values, not frozen conclusions. |
| Unsupported reason | Clear AI-generated reasons. Reviewers must supply the real project reason when confirming an unsupported camera. |
| Responsibility fields | Separate one named `主责确认人` from multi-select `评审角色`. Function rows route to Product/APP/SQA; algorithm and hardware-boundary rows route to HAL SE and relevant algorithm roles; effect rows route to Effect Product/Tuning SE/IQA. |
| Capture timing | Remove PZL/capture-strategy rows from KB and FL. Keep capture timing, frame count and ZSL/post-trigger strategy only in software design. |
| Optical distortion | Canonical name is `LDC / 光学畸变矫正`; confirm UW preview and capture paths separately in the supporting design. |
| RAW HDR | Canonical FL name is `RAW HDR`; remove supplier-specific `TF HDR` from the standard name. |
| HDSR | Keep as an FL algorithm row, but SE must fill its effective camera and focal-range trigger. |
| Algorithm composition | FL indicates whether an algorithm can be used in a mode/camera. Detailed stacking, ordering, mutual exclusion and decision thresholds stay in software design. |
| Function/algorithm naming | User controls must include interaction semantics, such as `HDR 开关` and `AI Zoom 开关`; underlying algorithms keep reviewed algorithm names so Product/APP functions are not confused with SE-owned algorithm capabilities. |

## 3. Review Responsibilities

| Scope | Primary decision owner | Review / acceptance participants |
|---|---|---|
| User-visible function, interaction and requirement scope | Named Product owner | APP, SQA |
| Hardware, HAL, realtime algorithm, post-processing algorithm and supported range | Named HAL SE owner | Algorithm/Tuning owners, IQA |
| Software behavior acceptance | SQA | Product, APP |
| Image/video effect acceptance | IQA | SE, Tuning |

Reviewers must check both the existence of the row and its mode, camera, specification and focal-range boundary. A check mark without the effective range is incomplete for focal-dependent algorithms such as HDSR, ISZ, EIS or SR.

## 4. Open Structural Decisions

The meeting raised these proposals but did not freeze a schema change:

1. Add a `核心能力 / Core` or priority field so reviewers can filter high-pixel, Action capture, HDR, Super Night and other project highlights.
2. Populate the approved owner map so every row can resolve to one named `主责确认人`; keep `评审角色` as a separate multi-select participant list.
3. Publish the algorithm decision/strategy table and pipeline composition from the software design as a linked companion artifact.
4. Ask algorithm owners to review the KB algorithm inventory for missing capabilities and inconsistent historical names.

## 5. Next Review Gate

A row can return to `已确认` only after the named accountable person checks its support cells, fills meaningful unsupported reasons, confirms the applicable mode/camera/specification/focal range, and ensures the verification method can prove the boundary. After human edits, AI must audit duplicates, mechanical descriptions, missing reasons, invalid status, ownership ambiguity, and KB/FL drift before the next published version.

## 6. Current Quality Audit

The deterministic audit was run against the local FL synchronized from the reviewed Base. Reports:

- `knowledge/_output/fl_draft_26111_26121/26111_quality_audit_2026-07-15.json`
- `knowledge/_output/fl_draft_26111_26121/26121_quality_audit_2026-07-15.json`

| Project | Owner placeholders | Short descriptions | Empty unsupported reasons | Duplicate mode/name rows | Status/TBD conflicts |
|---|---:|---:|---:|---:|---:|
| 26111 | 239 | 24 | 0 | 6 groups | 0 |
| 26121 | 245 | 22 | 0 | 7 groups | 0 |

Duplicate groups are concentrated in SAT, Zoom, ASD, and one 26121 Night Watermark group. Owner placeholders currently contain roles rather than names; they must be migrated after the approved person/scope list is supplied. Short descriptions require semantic review rather than blind length expansion: rewrite only when the capability meaning and scope are supported by evidence, otherwise ask the named accountable person. Generic baseline-derived unsupported reasons were removed: evidence-backed rows now state the dependency and missing capability; unsupported marks without a provable cause were reverted to `TBD / 待确认`.
