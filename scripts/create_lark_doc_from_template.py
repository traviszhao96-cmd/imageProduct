#!/usr/bin/env python3
"""Create a Lark doc from a local Markdown template and populate it safely."""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any

import requests


OPENCLAW_CONFIG = Path.home() / ".openclaw" / "openclaw.json"
LARK_BASE_URL = "https://open.larksuite.com"
DEFAULT_OWNER_EMAIL = "travis.zhao@nothing.tech"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = PROJECT_ROOT / "Camera-PRD-Template.md"
REQUEST_TIMEOUT = 30


def load_app_credentials() -> tuple[str, str]:
    config = json.loads(OPENCLAW_CONFIG.read_text(encoding="utf-8"))
    account = config["channels"]["feishu"]["accounts"]["main"]
    return account["appId"], account["appSecret"]


def get_tenant_token(app_id: str, app_secret: str) -> str:
    response = requests.post(
        f"{LARK_BASE_URL}/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise RuntimeError(payload)
    return payload["tenant_access_token"]


def api_request(
    method: str,
    path: str,
    token: str,
    *,
    payload: dict[str, Any] | None = None,
    max_retries: int = 5,
) -> dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8",
    }
    url = f"{LARK_BASE_URL}{path}"
    for attempt in range(max_retries):
        response = requests.request(
            method,
            url,
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        if response.status_code == 429:
            time.sleep(min(2**attempt, 8))
            continue
        response.raise_for_status()
        body = response.json()
        if body.get("code") == 0:
            return body
        message = f"{body.get('code')}: {body.get('msg')}"
        if (
            "too many requests" in message.lower()
            or body.get("code") in {99991663, 230020}
        ) and attempt + 1 < max_retries:
            time.sleep(min(2**attempt, 8))
            continue
        raise RuntimeError(body)
    raise RuntimeError(f"Failed after retries: {path}")


def create_doc(token: str, title: str) -> str:
    payload = api_request(
        "POST",
        "/open-apis/docx/v1/documents",
        token,
        payload={"title": title},
    )
    return payload["data"]["document"]["document_id"]


def grant_full_access(token: str, doc_token: str, email: str) -> None:
    api_request(
        "POST",
        f"/open-apis/drive/v1/permissions/{doc_token}/members?type=docx",
        token,
        payload={"member_type": "email", "member_id": email, "perm": "full_access"},
    )


def normalize_tables(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            rows = [row.strip("|").split("|") for row in table_lines]
            rows = [[cell.strip() for cell in row] for row in rows]
            if rows:
                header = rows[0]
                out.append(f"表格字段：{' / '.join(header)}")
                for row in rows[2:]:
                    if any(cell for cell in row):
                        out.append(f"- {' | '.join(row)}")
                if len(rows) <= 2:
                    out.append("- 待补充")
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out).strip() + "\n"


def apply_replacements(markdown: str, replacements: dict[str, str]) -> str:
    result = markdown
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}", value)
        result = result.replace(f"[[{key}]]", value)
    return result


def split_markdown(markdown: str, max_chars: int = 3500) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    in_fence = False
    for line in markdown.splitlines():
        if re.match(r"^(`{3,}|~{3,})", line):
            in_fence = not in_fence
        line_len = len(line) + 1
        is_heading = bool(re.match(r"^#{1,2}\s", line))
        if current and (current_len + line_len > max_chars or (is_heading and not in_fence)):
            chunks.append("\n".join(current).strip())
            current = []
            current_len = 0
        current.append(line)
        current_len += line_len
    if current:
        chunks.append("\n".join(current).strip())
    return [chunk for chunk in chunks if chunk]


def convert_markdown(token: str, markdown: str) -> dict[str, Any]:
    return api_request(
        "POST",
        "/open-apis/docx/v1/documents/blocks/convert",
        token,
        payload={"content_type": "markdown", "content": markdown},
    )["data"]


def normalize_child_ids(children: Any) -> list[str]:
    if isinstance(children, list):
        return [item for item in children if isinstance(item, str)]
    if isinstance(children, str):
        return [children]
    return []


def normalize_converted_blocks(
    blocks: list[dict[str, Any]], first_level_ids: list[str]
) -> list[dict[str, Any]]:
    if len(blocks) <= 1:
        return blocks
    by_id = {block["block_id"]: block for block in blocks if isinstance(block.get("block_id"), str)}
    order = {
        block["block_id"]: index
        for index, block in enumerate(blocks)
        if isinstance(block.get("block_id"), str)
    }
    child_ids = {
        child_id
        for block in blocks
        for child_id in normalize_child_ids(block.get("children"))
    }
    inferred_roots = [
        block["block_id"]
        for block in sorted(
            (
                block
                for block in blocks
                if isinstance(block.get("block_id"), str)
                and block["block_id"] not in child_ids
                and (
                    not isinstance(block.get("parent_id"), str)
                    or block["parent_id"] not in by_id
                )
            ),
            key=lambda block: order.get(block["block_id"], 0),
        )
    ]
    root_ids = [
        block_id
        for block_id in (first_level_ids or inferred_roots)
        if isinstance(block_id, str) and block_id in by_id
    ]
    ordered: list[dict[str, Any]] = []
    visited: set[str] = set()

    def visit(block_id: str) -> None:
        if block_id in visited or block_id not in by_id:
            return
        visited.add(block_id)
        block = by_id[block_id]
        ordered.append(block)
        for child_id in normalize_child_ids(block.get("children")):
            visit(child_id)

    for root_id in root_ids:
        visit(root_id)
    for block in blocks:
        block_id = block.get("block_id")
        if isinstance(block_id, str):
            visit(block_id)
        else:
            ordered.append(block)
    return ordered


def insert_block(token: str, document_id: str, block: dict[str, Any]) -> None:
    api_request(
        "POST",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{document_id}/children",
        token,
        payload={"children": [block]},
    )


def write_markdown(token: str, document_id: str, markdown: str) -> int:
    chunks = split_markdown(markdown)
    inserted = 0
    for chunk in chunks:
        converted = convert_markdown(token, chunk)
        blocks = normalize_converted_blocks(
            converted.get("blocks", []),
            converted.get("first_level_block_ids", []),
        )
        for block in blocks:
            insert_block(token, document_id, block)
            inserted += 1
    return inserted


def parse_replacements(items: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"Replacement must be KEY=VALUE, got: {item}")
        key, value = item.split("=", 1)
        result[key.strip()] = value.strip()
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a Lark docx from a local Markdown template."
    )
    parser.add_argument("--title", required=True, help="New document title.")
    parser.add_argument(
        "--template",
        default=str(DEFAULT_TEMPLATE),
        help="Markdown template path.",
    )
    parser.add_argument(
        "--owner-email",
        default=DEFAULT_OWNER_EMAIL,
        help=f"Grant full_access to this email. Default: {DEFAULT_OWNER_EMAIL}",
    )
    parser.add_argument(
        "--replace",
        action="append",
        default=[],
        help="Template replacement in KEY=VALUE form. Supports {{KEY}} and [[KEY]].",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    replacements = parse_replacements(args.replace)
    markdown = Path(args.template).read_text(encoding="utf-8")
    markdown = apply_replacements(markdown, replacements)
    markdown = normalize_tables(markdown)

    app_id, app_secret = load_app_credentials()
    token = get_tenant_token(app_id, app_secret)
    document_id = create_doc(token, args.title)
    grant_full_access(token, document_id, args.owner_email)
    block_count = write_markdown(token, document_id, markdown)

    result = {
        "document_id": document_id,
        "url": f"https://nothing-tech.sg.larksuite.com/docx/{document_id}",
        "title": args.title,
        "owner_email": args.owner_email,
        "block_count": block_count,
        "template": str(Path(args.template).resolve()),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
