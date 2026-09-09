# Phone (4b) Activation +7 mapping validation

Validated on 2026-09-09 against the respondent-level export named `821_nothing phone(4b) activation plus 7 results`.

## Coverage

| Metric | Result |
|---|---:|
| Response rows | 1,245 |
| Unique refids | 1,206 |
| Duplicate refid groups | 31 |
| Duplicate extra rows | 39 |
| Unique standard 16-character deviceIds | 1,134 |
| Unique noncanonical short hexadecimal values | 72 |
| Refids reported not found | 0 |

The 72 noncanonical values comprise 68 values with 15 hexadecimal characters, 3 with 14, and 1 with 13. They were preserved as `device_id_raw` and marked `device_id_invalid`. Do not infer leading zeroes without confirmation or Athena evidence.

At response-row level, duplicate refids produce 1,170 rows with a validated deviceId and 75 rows with a short raw value.

## Local handoff

The respondent-level handoff is intentionally excluded from Git and skill packages. Its expected local location is:

```text
outputs/nps_camera_handoff/2026-09-09/phone-4b-activation7-agent-handoff.csv
```

It excludes `First name`, `Last name`, `Email`, and `Token`; retains analytical survey fields, `refid`, validated `device_id`, `device_id_raw`, mapping status, NPS cohort, and duplicate count; and must remain access-controlled.

This validation covers `refid → deviceId` only. Athena Camera telemetry coverage has not yet been calculated for this full cohort.
