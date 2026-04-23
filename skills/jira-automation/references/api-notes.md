# Jira API Notes

## Environment

Required:

- `JIRA_BASE_URL`
- `JIRA_TOKEN`

Optional:

- `JIRA_AUTH_MODE=bearer|basic`
- `JIRA_EMAIL`

Examples:

```bash
export JIRA_BASE_URL="https://your-domain.atlassian.net"
export JIRA_EMAIL="name@example.com"
export JIRA_TOKEN="your-api-token"
export JIRA_AUTH_MODE="basic"
```

or:

```bash
export JIRA_BASE_URL="https://jira.company.com"
export JIRA_TOKEN="your-personal-access-token"
export JIRA_AUTH_MODE="bearer"
```

## Endpoints Used

- `GET /rest/api/3/issue/{issueKey}`
- `POST /rest/api/3/issue`
- `PUT /rest/api/3/issue/{issueKey}`
- `POST /rest/api/3/issue/{issueKey}/comment`
- `PUT /rest/api/3/issue/{issueKey}/assignee`
- `GET /rest/api/3/issue/{issueKey}/transitions`
- `POST /rest/api/3/issue/{issueKey}/transitions`
- `POST /rest/api/3/search/jql`

## Common Shapes

Create payload:

```json
{
  "fields": {
    "project": { "key": "IMGP" },
    "issuetype": { "name": "Task" },
    "summary": "Add Gallery edit telemetry audit",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            { "type": "text", "text": "Need a first-pass telemetry gap review." }
          ]
        }
      ]
    }
  }
}
```

Assign payload:

```json
{
  "accountId": "5b10a2844c20165700ede21g"
}
```

Transition payload:

```json
{
  "transition": {
    "id": "31"
  }
}
```

Search payload:

```json
{
  "jql": "project = IMGP ORDER BY updated DESC",
  "maxResults": 20,
  "fields": ["summary", "status", "assignee", "issuetype", "updated"]
}
```

## Common Failure Cases

- `401` or `403`: wrong auth mode, invalid token, or missing permission
- `400` on create: project uses required custom fields
- `404`: wrong issue key or insufficient visibility
- assignment fails: account id is required for this Jira setup

When create fails because of field validation, read the error body and retry with explicit custom fields instead of inventing defaults.
