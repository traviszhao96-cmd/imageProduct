#!/usr/bin/env python3
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def build_adf_text(text: str) -> dict:
    paragraphs = []
    for block in text.split("\n\n"):
        lines = block.splitlines() or [""]
        content = []
        for index, line in enumerate(lines):
            if line:
                content.append({"type": "text", "text": line})
            if index < len(lines) - 1:
                content.append({"type": "hardBreak"})
        paragraphs.append({"type": "paragraph", "content": content or [{"type": "text", "text": ""}]})
    return {"type": "doc", "version": 1, "content": paragraphs or [{"type": "paragraph", "content": []}]}


class JiraClient:
    def __init__(self) -> None:
        self.base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        self.token = os.environ.get("JIRA_TOKEN", "")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.auth_mode = os.environ.get("JIRA_AUTH_MODE", "").strip().lower()

        if not self.base_url:
            raise SystemExit("Missing JIRA_BASE_URL")
        if not self.token:
            raise SystemExit("Missing JIRA_TOKEN")

        if not self.auth_mode:
            self.auth_mode = "basic" if self.email else "bearer"

        if self.auth_mode not in {"basic", "bearer"}:
            raise SystemExit("JIRA_AUTH_MODE must be 'basic' or 'bearer'")
        if self.auth_mode == "basic" and not self.email:
            raise SystemExit("JIRA_EMAIL is required when JIRA_AUTH_MODE=basic")

    def _headers(self) -> dict:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if self.auth_mode == "basic":
            raw = f"{self.email}:{self.token}".encode("utf-8")
            headers["Authorization"] = "Basic " + base64.b64encode(raw).decode("ascii")
        else:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def request(self, method: str, path: str, payload: dict | None = None) -> dict:
        url = self.base_url + path
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, method=method, headers=self._headers())
        try:
            with urllib.request.urlopen(req) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                parsed = {"error": raw}
            raise SystemExit(
                json.dumps(
                    {
                        "status": exc.code,
                        "path": path,
                        "response": parsed,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )

    def get_issue(self, issue_key: str) -> dict:
        fields = ",".join(["summary", "description", "status", "assignee", "issuetype", "project", "updated"])
        return self.request("GET", f"/rest/api/3/issue/{urllib.parse.quote(issue_key)}?fields={fields}")

    def create_issue(self, project: str, issue_type: str, summary: str, description: str, extra_fields: dict) -> dict:
        fields = {
            "project": {"key": project},
            "issuetype": {"name": issue_type},
            "summary": summary,
        }
        if description:
            fields["description"] = build_adf_text(description)
        fields.update(extra_fields)
        return self.request("POST", "/rest/api/3/issue", {"fields": fields})

    def update_issue(self, issue_key: str, summary: str | None, description: str | None, extra_fields: dict) -> dict:
        fields = dict(extra_fields)
        if summary is not None:
            fields["summary"] = summary
        if description is not None:
            fields["description"] = build_adf_text(description)
        return self.request("PUT", f"/rest/api/3/issue/{urllib.parse.quote(issue_key)}", {"fields": fields})

    def add_comment(self, issue_key: str, body: str) -> dict:
        payload = {"body": build_adf_text(body)}
        return self.request("POST", f"/rest/api/3/issue/{urllib.parse.quote(issue_key)}/comment", payload)

    def assign_issue(self, issue_key: str, account_id: str) -> dict:
        payload = {"accountId": account_id}
        return self.request("PUT", f"/rest/api/3/issue/{urllib.parse.quote(issue_key)}/assignee", payload)

    def list_transitions(self, issue_key: str) -> dict:
        return self.request("GET", f"/rest/api/3/issue/{urllib.parse.quote(issue_key)}/transitions")

    def transition_issue(self, issue_key: str, transition_id: str) -> dict:
        payload = {"transition": {"id": transition_id}}
        return self.request("POST", f"/rest/api/3/issue/{urllib.parse.quote(issue_key)}/transitions", payload)

    def search(self, jql: str, limit: int) -> dict:
        payload = {
            "jql": jql,
            "maxResults": limit,
            "fields": ["summary", "status", "assignee", "issuetype", "updated"],
        }
        return self.request("POST", "/rest/api/3/search/jql", payload)


def parse_extra_fields(raw_json: str | None) -> dict:
    if not raw_json:
        return {}
    try:
        parsed = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON for --fields-json: {exc}") from exc
    if not isinstance(parsed, dict):
        raise SystemExit("--fields-json must decode to a JSON object")
    return parsed


def cmd_get(client: JiraClient, args: argparse.Namespace) -> int:
    print(json.dumps(client.get_issue(args.issue), ensure_ascii=False, indent=2))
    return 0


def cmd_create(client: JiraClient, args: argparse.Namespace) -> int:
    result = client.create_issue(
        project=args.project,
        issue_type=args.issue_type,
        summary=args.summary,
        description=args.description or "",
        extra_fields=parse_extra_fields(args.fields_json),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_update(client: JiraClient, args: argparse.Namespace) -> int:
    if args.summary is None and args.description is None and not args.fields_json:
        raise SystemExit("update requires at least one of --summary, --description, or --fields-json")
    result = client.update_issue(
        issue_key=args.issue,
        summary=args.summary,
        description=args.description,
        extra_fields=parse_extra_fields(args.fields_json),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_comment(client: JiraClient, args: argparse.Namespace) -> int:
    print(json.dumps(client.add_comment(args.issue, args.body), ensure_ascii=False, indent=2))
    return 0


def cmd_assign(client: JiraClient, args: argparse.Namespace) -> int:
    print(json.dumps(client.assign_issue(args.issue, args.account_id), ensure_ascii=False, indent=2))
    return 0


def cmd_transitions(client: JiraClient, args: argparse.Namespace) -> int:
    print(json.dumps(client.list_transitions(args.issue), ensure_ascii=False, indent=2))
    return 0


def cmd_transition(client: JiraClient, args: argparse.Namespace) -> int:
    print(json.dumps(client.transition_issue(args.issue, args.transition_id), ensure_ascii=False, indent=2))
    return 0


def cmd_search(client: JiraClient, args: argparse.Namespace) -> int:
    print(json.dumps(client.search(args.jql, args.limit), ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Minimal Jira REST API CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    get_parser = subparsers.add_parser("get", help="Get an issue")
    get_parser.add_argument("--issue", required=True, help="Issue key, for example IMGP-123")
    get_parser.set_defaults(func=cmd_get)

    create_parser = subparsers.add_parser("create", help="Create an issue")
    create_parser.add_argument("--project", required=True, help="Project key")
    create_parser.add_argument("--issue-type", required=True, help="Issue type name")
    create_parser.add_argument("--summary", required=True, help="Issue summary")
    create_parser.add_argument("--description", help="Plain text description")
    create_parser.add_argument("--fields-json", help="Extra fields as JSON object")
    create_parser.set_defaults(func=cmd_create)

    update_parser = subparsers.add_parser("update", help="Update an issue")
    update_parser.add_argument("--issue", required=True, help="Issue key")
    update_parser.add_argument("--summary", help="New summary")
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument("--fields-json", help="Extra fields as JSON object")
    update_parser.set_defaults(func=cmd_update)

    comment_parser = subparsers.add_parser("comment", help="Add a comment")
    comment_parser.add_argument("--issue", required=True, help="Issue key")
    comment_parser.add_argument("--body", required=True, help="Comment body")
    comment_parser.set_defaults(func=cmd_comment)

    assign_parser = subparsers.add_parser("assign", help="Assign an issue")
    assign_parser.add_argument("--issue", required=True, help="Issue key")
    assign_parser.add_argument("--account-id", required=True, help="Jira accountId")
    assign_parser.set_defaults(func=cmd_assign)

    transitions_parser = subparsers.add_parser("transitions", help="List available transitions")
    transitions_parser.add_argument("--issue", required=True, help="Issue key")
    transitions_parser.set_defaults(func=cmd_transitions)

    transition_parser = subparsers.add_parser("transition", help="Move an issue to another state")
    transition_parser.add_argument("--issue", required=True, help="Issue key")
    transition_parser.add_argument("--transition-id", required=True, help="Transition id")
    transition_parser.set_defaults(func=cmd_transition)

    search_parser = subparsers.add_parser("search", help="Search issues with JQL")
    search_parser.add_argument("--jql", required=True, help="JQL string")
    search_parser.add_argument("--limit", type=int, default=20, help="Max results")
    search_parser.set_defaults(func=cmd_search)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    client = JiraClient()
    return args.func(client, args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        eprint("Interrupted")
        raise SystemExit(130)
