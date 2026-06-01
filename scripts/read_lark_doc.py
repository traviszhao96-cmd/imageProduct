#!/usr/bin/env python3
"""Read a Lark wiki/docx document through the local app credentials."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests


OPENCLAW_CONFIG = Path.home() / ".openclaw" / "openclaw.json"
LARK_BASE_URL = "https://open.larksuite.com"
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
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    response = requests.request(
        method,
        f"{LARK_BASE_URL}{path}",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise RuntimeError({"path": path, "params": params, "response": payload})
    return payload


def extract_token_from_url(source_url: str) -> tuple[str, str]:
    path = urlparse(source_url).path
    wiki_match = re.search(r"/wiki/([A-Za-z0-9]+)", path)
    if wiki_match:
        return "wiki", wiki_match.group(1)
    doc_match = re.search(r"/docx/([A-Za-z0-9]+)", path)
    if doc_match:
        return "docx", doc_match.group(1)
    raise ValueError(f"Unsupported Lark URL: {source_url}")


def resolve_document(token: str, *, source_url: str | None, document_id: str | None) -> dict[str, Any]:
    if document_id:
        metadata = api_request("GET", f"/open-apis/docx/v1/documents/{document_id}", token)
        return {
            "source_type": "docx",
            "source_token": document_id,
            "document_id": document_id,
            "title": metadata["data"]["document"]["title"],
            "wiki_node": None,
        }

    assert source_url is not None
    source_type, source_token = extract_token_from_url(source_url)
    if source_type == "docx":
        metadata = api_request("GET", f"/open-apis/docx/v1/documents/{source_token}", token)
        return {
            "source_type": "docx",
            "source_token": source_token,
            "document_id": source_token,
            "title": metadata["data"]["document"]["title"],
            "wiki_node": None,
        }

    wiki_payload = api_request(
        "GET",
        "/open-apis/wiki/v2/spaces/get_node",
        token,
        params={"token": source_token},
    )
    node = wiki_payload["data"]["node"]
    if node.get("obj_type") != "docx":
        raise RuntimeError(f"Wiki node is not docx: {node.get('obj_type')}")
    document_id = node["obj_token"]
    metadata = api_request("GET", f"/open-apis/docx/v1/documents/{document_id}", token)
    return {
        "source_type": "wiki",
        "source_token": source_token,
        "document_id": document_id,
        "title": metadata["data"]["document"]["title"],
        "wiki_node": node,
    }


def list_children(token: str, document_id: str, block_id: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    page_token: str | None = None
    while True:
        params: dict[str, Any] = {"page_size": 100}
        if page_token:
            params["page_token"] = page_token
        try:
            payload = api_request(
                "GET",
                f"/open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children",
                token,
                params=params,
            )
        except requests.HTTPError:
            return items
        data = payload.get("data", {})
        items.extend(data.get("items", []))
        if not data.get("has_more"):
            return items
        page_token = data.get("page_token")


def elements_to_text(elements: list[dict[str, Any]] | None) -> str:
    if not elements:
        return ""
    parts: list[str] = []
    for element in elements:
        text_run = element.get("text_run")
        if text_run:
            parts.append(text_run.get("content", ""))
            continue
        mention = element.get("mention_user")
        if mention:
            parts.append("@" + mention.get("name", ""))
            continue
        reminder = element.get("reminder")
        if reminder:
            parts.append(reminder.get("text", ""))
            continue
        equation = element.get("equation")
        if equation:
            parts.append(equation.get("content", ""))
            continue
        inline_file = element.get("inline_file")
        if inline_file:
            parts.append(f"[附件:{inline_file.get('file_token', '')}]")
    return "".join(parts).strip()


def render_block(block: dict[str, Any], *, token: str, document_id: str, depth: int = 0) -> list[str]:
    indent = "  " * depth
    lines: list[str] = []
    key_to_heading = {
        "heading1": "# ",
        "heading2": "## ",
        "heading3": "### ",
        "heading4": "#### ",
        "heading5": "##### ",
        "heading6": "###### ",
    }
    for key, prefix in key_to_heading.items():
        if key in block:
            text = elements_to_text(block[key].get("elements"))
            if text:
                lines.append(f"{indent}{prefix}{text}")
            return lines

    if "text" in block:
        text = elements_to_text(block["text"].get("elements"))
        if text:
            lines.append(f"{indent}{text}")
    elif "bullet" in block:
        text = elements_to_text(block["bullet"].get("elements"))
        if text:
            lines.append(f"{indent}- {text}")
    elif "ordered" in block:
        text = elements_to_text(block["ordered"].get("elements"))
        if text:
            lines.append(f"{indent}1. {text}")
    elif "quote" in block:
        text = elements_to_text(block["quote"].get("elements"))
        if text:
            lines.append(f"{indent}> {text}")
    elif "callout" in block:
        text = elements_to_text(block["callout"].get("elements"))
        if text:
            lines.append(f"{indent}> [!NOTE] {text}")
    elif "code" in block:
        text = elements_to_text(block["code"].get("elements"))
        lines.extend([f"{indent}```", f"{indent}{text}", f"{indent}```"])
    elif "todo" in block:
        text = elements_to_text(block["todo"].get("elements"))
        marker = "x" if block["todo"].get("checked") else " "
        if text:
            lines.append(f"{indent}- [{marker}] {text}")
    elif "table" in block:
        lines.append(f"{indent}[表格]")
    elif "image" in block:
        lines.append(f"{indent}[图片]")
    elif "divider" in block or block.get("block_type") == 24:
        lines.append(f"{indent}---")

    children = block.get("children") or []
    if children:
        for child in list_children(token, document_id, block["block_id"]):
            child_lines = render_block(child, token=token, document_id=document_id, depth=depth + 1)
            if child_lines:
                lines.extend(child_lines)
    return lines


def render_document(token: str, document_id: str, title: str) -> tuple[str, dict[str, int]]:
    stats: Counter[str] = Counter()
    lines = [f"# {title}", ""]
    for block in list_children(token, document_id, document_id):
        stats[str(block.get("block_type"))] += 1
        block_lines = render_block(block, token=token, document_id=document_id)
        if block_lines:
            lines.extend(block_lines)
            if block_lines[-1] != "":
                lines.append("")
    markdown = "\n".join(lines).rstrip() + "\n"
    return markdown, dict(stats)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read a Lark wiki/docx document into Markdown.")
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--source-url", help="Lark wiki/docx URL.")
    source_group.add_argument("--document-id", help="Direct Lark docx document id.")
    parser.add_argument("--output-file", help="Write rendered Markdown to file.")
    parser.add_argument("--json", action="store_true", help="Print metadata JSON instead of Markdown.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    app_id, app_secret = load_app_credentials()
    tenant_token = get_tenant_token(app_id, app_secret)
    resolved = resolve_document(
        tenant_token,
        source_url=args.source_url,
        document_id=args.document_id,
    )
    markdown, stats = render_document(tenant_token, resolved["document_id"], resolved["title"])
    payload = {
        **resolved,
        "block_type_counts": stats,
        "markdown": markdown,
    }

    if args.output_file:
        Path(args.output_file).write_text(markdown, encoding="utf-8")

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(markdown, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
