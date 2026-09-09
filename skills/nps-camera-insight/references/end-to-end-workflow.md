# End-to-end workflow and confirmed evidence

## Ownership

| Stage | Owner | Output |
|---|---|---|
| Typeform/NPS response | NPS/product | `refid` plus score, response time, and other survey attributes |
| `refid → deviceId` | NPS Push System / ContactLedger | 16-character Android ID |
| `deviceId → items.aid` | Data query side | matching telemetry device |
| Camera behavior analysis | Camera data owner | aggregated cohort metrics |

Encryption protects the NPS service request and response. It is not a conversion algorithm. `refid` and `deviceId` are values stored in the same ContactLedger relationship; they cannot be derived locally by MD5, removing UUID hyphens, truncating, or padding.

## Confirmed state

As of 2026-09-09, the India NPS Push System exposes a working **Ref IDs** lookup in **Survey Recipients**. A known sample returned one `Found` result and the same 16-character deviceId previously matched in Athena.

The known device matched:

- project/model: SuperContra / A009P;
- language and OS: `en`, OS `4.1`;
- device configuration: white, 8 GB RAM, 128 GB storage;
- expected software builds;
- 1,493 telemetry events during 2026-08-14 through 2026-08-21;
- 38 `NTCamera` events in that validation window.

This confirms the full chain `refid → deviceId → items.aid → NTCamera`.

## Existing artifacts

- Lark document: `https://nothing-tech.sg.larksuite.com/docx/OcnvdTj2coRFiIx8M3dlWSBfgce`
- Historical validation summary: `outputs/athena_results/nps_refid_validation/2026-08-31-aid-validation-summary.csv`
- Earlier single-device implementation: `skills/camera-data-insight/scripts/nps_camera_query.py`

The Lark document may describe an earlier implementation state. Prefer this skill's dated confirmed state when they conflict, and update shared documentation only when the user asks.

## Completion criteria

An analysis is end-to-end complete only when:

1. the input refids are tied to actual survey responses;
2. NPS lookup produces real deviceIds rather than a generic success status;
3. the mapping coverage and unmatched rows are reported;
4. Athena matches deviceIds through `items.aid`;
5. the requested Camera behavior is aggregated against the intended NPS cohort.
