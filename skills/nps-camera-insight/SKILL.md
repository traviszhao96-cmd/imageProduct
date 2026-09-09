---
name: nps-camera-insight
description: Use when the user wants to turn NPS or Typeform refids into deviceIds, join those devices to Athena camera telemetry through items.aid, validate the end-to-end mapping, or compare Camera behavior across NPS cohorts. Covers the India NPS Push System UI, batch CSV handoff, Athena queries, evidence checks, and privacy boundaries. Do not use for general Camera telemetry without an NPS/refid cohort.
---

# NPS Camera Insight

Use this skill to complete the chain:

```text
NPS response refid
→ NPS Push System / ContactLedger
→ 16-character deviceId (Android ID)
→ Athena items[key='aid'].string_value
→ NTCamera behavior
→ aggregated NPS cohort insight
```

The mapping has been verified end to end. There is no MD5, UUID normalization, or 16-to-32-character conversion.

## Route by task

- To convert one or more `refid` values, read [references/nps-system.md](references/nps-system.md).
- To create an access-controlled respondent-level file for another agent, read [references/handoff-schema.md](references/handoff-schema.md).
- For the dated Phone (4b) Activation +7 coverage and current short-ID limitation, read [references/phone-4b-activation7-validation.md](references/phone-4b-activation7-validation.md).
- To query Athena with returned deviceIds, read [references/athena-query.md](references/athena-query.md) and use [scripts/nps_camera_query.py](scripts/nps_camera_query.py).
- To prepare a Friday review or compare promoters/passives/detractors, also read [references/insight-playbook.md](references/insight-playbook.md).
- For ownership, confirmed evidence, and unresolved boundaries, read [references/end-to-end-workflow.md](references/end-to-end-workflow.md).

## Required workflow

1. Confirm the input represents real NPS response `refid` values. Preserve the original `refid` column for joining response attributes later.
2. Use the NPS Push System's **Survey Recipients → Ref IDs** query. Process at most 500 entries per batch.
3. Accept a mapping only when the UI returns `Found` and a 16-character hexadecimal `deviceId`.
4. Export the mapping CSV. Keep unmatched refids in the quality report; never silently drop them.
   For batch API lookup, use [scripts/nps_refid_lookup.py](scripts/nps_refid_lookup.py); provide credentials only at runtime.
5. Query Camera telemetry by matching the returned deviceId against Athena `items.aid`.
6. Report mapping coverage before behavioral insight: input refids, valid refids, found refids, unique deviceIds, Athena-matched devices, and NTCamera-matched devices.
7. Produce cohort-level results. Do not publish identifiable per-device behavior unless the user explicitly requests it and is authorized.

## Non-negotiable field rules

- `refid`: 36-character UUID used by the NPS survey/contact ledger.
- `deviceId`: 16-character Android ID returned by the NPS system.
- Athena match: `element_at(filter(items, x -> lower(x.key) = 'aid'), 1).string_value`.
- Do not substitute `user_pseudo_id`, `device.device_id`, `device.device_id_2`, `event_params.aid`, or `user_properties.aid`.
- `Found` means the NPS system found a sending/contact record. It does not prove that the survey was completed.

## Security and authorization

- Never store usernames, passwords, AWS keys, session tokens, or decrypted payloads in this skill, commands, reports, or archives.
- The current NPS site uses HTTP. Warn that credentials and identifiers may travel without HTTPS protection; recommend HTTPS and credential rotation before wider use.
- When browser automation must enter credentials, use credentials supplied at runtime and follow the active browser/computer-use confirmation policy immediately before submission.
- Query and export are read-only. Do not change campaigns, recipients, contact policy, or push configuration unless the user separately requests it.

## Output contract

Return or archive:

- a refid/deviceId mapping coverage summary;
- an Athena match coverage summary;
- aggregated Camera metrics by requested NPS cohort;
- the analysis time window, region, project filters, and data limitations;
- output file paths and query IDs when available.

For an agent handoff, also return a PII-minimized analysis CSV and a quality JSON created with [scripts/prepare_nps_handoff.py](scripts/prepare_nps_handoff.py). Keep both local and out of Git.

If only refids are available and the NPS system cannot be accessed, stop at a prepared refid batch and state that the database mapping cannot be computed locally.
