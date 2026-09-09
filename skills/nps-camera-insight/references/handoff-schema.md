# Respondent-level handoff

Use this format when another agent will analyze Camera telemetry for an NPS cohort.

## Deliverables

1. Mapping CSV: `refid`, validated `device_id`, preserved `device_id_raw`, and `mapping_status`.
2. Analysis handoff CSV: original analytical survey fields plus `device_id`, `device_id_raw`, `mapping_status`, `nps_cohort`, and `duplicate_refid_count`.
3. Quality JSON: row counts, mapping coverage, duplicate counts, cohort counts, and removed direct-PII fields.

Create the mapping with `scripts/nps_refid_lookup.py`, then create the analysis handoff with `scripts/prepare_nps_handoff.py`.

## Required privacy treatment

- Remove `First name`, `Last name`, `Email`, and `Token` from the agent handoff.
- Preserve `refid` only when the next step needs traceability back to the NPS system.
- Keep 13–15 digit hexadecimal lookup values in `device_id_raw` with `mapping_status=device_id_invalid`. Do not infer missing leading zeroes or query them as `items.aid` until the NPS/data owner confirms the representation.
- Treat `device_id`, `refid`, free-text answers, and respondent attributes as access-controlled respondent-level data.
- Store respondent-level files under ignored local output paths. Do not package them inside the skill and do not commit them to Git.
- Publish only cohort-level findings unless the user explicitly requests authorized respondent-level investigation.

## Duplicate handling

Do not silently deduplicate during handoff. Add `duplicate_refid_count` and report duplicate groups in the quality summary. The analysis owner must apply the survey's approved deduplication rule before calculating NPS or respondent counts.

## Agent prompt

The next agent should be told:

```text
Use device_id only to join Athena items.aid. First report mapping and telemetry coverage. Apply the approved NPS duplicate rule before respondent-level counts. Analyze and publish cohort-level Camera behavior; do not expose per-device activity or direct identifiers.
```
