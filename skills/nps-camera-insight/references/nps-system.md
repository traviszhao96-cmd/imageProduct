# NPS Push System refid lookup

## Entry point

India system:

```text
http://push-server-india.s3-website.ap-south-1.amazonaws.com/login
```

Do not store its credentials in this skill. Obtain them from the user or an approved secret store at runtime.

## UI procedure

1. Open the login page in the available browser.
2. Before transmitting credentials, follow the active browser/computer-use confirmation policy.
3. After login, open **Survey Recipients**.
4. Select query method **Ref IDs**.
5. Enter newline-separated refids. The UI accepts up to 500 entries per query.
6. Choose **Query ref IDs**.
7. Verify the result summary and rows.
8. Export the mapping using **Export Device ID CSV** or the equivalent visible export action.

## Batch script

For a local CSV containing a `refid` column, use `scripts/nps_refid_lookup.py`. It calls the same authenticated lookup endpoint used by the UI, preserves not-found rows, validates response ordering, and writes `refid,device_id,mapping_status`.

Supply the username and password only at runtime through `NPS_USERNAME` / `NPS_PASSWORD` or the password prompt. Never add credentials to the script, shell history, output file, Skill, or Git.

Keep any returned non-empty value that fails the 16-character rule in `device_id_raw` and mark it `device_id_invalid`. In particular, do not silently left-pad shorter hexadecimal values without upstream or Athena evidence.

The Ref IDs mode states that campaign, survey, model, completion, and date filters do not apply.

## Result interpretation

Expected visible columns:

| Column | Meaning |
|---|---|
| Ref ID | NPS/Typeform UUID |
| Device ID | 16-character Android ID |
| Status | Lookup result such as `Found` |

Validate each returned deviceId with the regular expression `^[0-9a-fA-F]{16}$`.

`Found` only confirms a sending/contact record exists. It does not mean the user completed the survey. Join with the original response export to obtain completion, NPS score, comment, response time, campaign, and survey attributes.

## Quality report

Always record:

- input refid count;
- syntactically valid UUID count;
- found and not-found counts;
- unique deviceId count;
- duplicate refids;
- multiple refids mapping to the same deviceId.

Preserve not-found rows for upstream investigation.

## Security note

The current site uses HTTP rather than HTTPS. Before wider or routine use, recommend HTTPS/TLS and rotation of any password previously posted in chat. Do not echo credentials in commentary, logs, screenshots, local files, or packaged output.
