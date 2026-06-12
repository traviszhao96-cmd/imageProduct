#!/usr/bin/env python3
"""Write Markdown into an existing Lark docx while preserving native tables."""

from __future__ import annotations

import argparse
import json
import re
import time
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


def extract_token_from_url(source_url: str) -> tuple[str, str]:
    path = urlparse(source_url).path
    wiki_match = re.search(r"/wiki/([A-Za-z0-9]+)", path)
    if wiki_match:
        return "wiki", wiki_match.group(1)
    doc_match = re.search(r"/docx/([A-Za-z0-9]+)", path)
    if doc_match:
        return "docx", doc_match.group(1)
    raise ValueError(f"Unsupported Lark URL: {source_url}")


def api_request(
    method: str,
    path: str,
    token: str,
    *,
    payload: dict[str, Any] | None = None,
    params: dict[str, Any] | None = None,
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
            params=params,
            timeout=REQUEST_TIMEOUT,
        )
        if response.status_code == 429:
            time.sleep(min(2**attempt, 8))
            continue
        response.raise_for_status()
        body = response.json()
        if body.get("code") == 0:
            return body
        if attempt + 1 < max_retries and body.get("code") in {99991663, 230020}:
            time.sleep(min(2**attempt, 8))
            continue
        raise RuntimeError({"path": path, "payload": payload, "response": body})
    raise RuntimeError(f"Failed after retries: {path}")


def resolve_document_id(token: str, *, document_id: str | None, source_url: str | None) -> str:
    if document_id:
        return document_id
    assert source_url is not None
    source_type, source_token = extract_token_from_url(source_url)
    if source_type == "docx":
        return source_token
    payload = api_request(
        "GET",
        "/open-apis/wiki/v2/spaces/get_node",
        token,
        params={"token": source_token},
    )
    node = payload["data"]["node"]
    if node.get("obj_type") != "docx":
        raise RuntimeError(f"Wiki node is not docx: {node.get('obj_type')}")
    return node["obj_token"]


def split_sections(markdown: str) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    lines = markdown.splitlines()
    current_text: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("|"):
            if current_text and any(item.strip() for item in current_text):
                sections.append({"type": "markdown", "content": "\n".join(current_text).strip()})
                current_text = []
            table_lines = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            sections.append({"type": "table", "rows": parse_table(table_lines)})
            continue
        current_text.append(line)
        i += 1
    if current_text and any(item.strip() for item in current_text):
        sections.append({"type": "markdown", "content": "\n".join(current_text).strip()})
    return sections


def parse_table(table_lines: list[str]) -> list[list[str]]:
    rows = [[cell.strip() for cell in row.strip("|").split("|")] for row in table_lines]
    if len(rows) >= 2 and all(re.fullmatch(r"[-:\s]+", cell or "-") for cell in rows[1]):
        rows.pop(1)
    width = max((len(row) for row in rows), default=0)
    return [row + [""] * (width - len(row)) for row in rows]


def split_markdown_chunks(markdown: str, max_chars: int = 2800) -> list[str]:
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


def clear_document(token: str, document_id: str) -> int:
    removed = 0
    while True:
        response = api_request(
            "GET",
            f"/open-apis/docx/v1/documents/{document_id}/blocks/{document_id}/children",
            token,
            params={"page_size": 100},
        )
        items = response.get("data", {}).get("items", [])
        if not items:
            return removed
        api_request(
            "DELETE",
            f"/open-apis/docx/v1/documents/{document_id}/blocks/{document_id}/children/batch_delete",
            token,
            payload={"start_index": 0, "end_index": len(items)},
        )
        removed += len(items)
        time.sleep(0.2)


def write_markdown_chunk(token: str, document_id: str, markdown: str) -> int:
    converted = api_request(
        "POST",
        "/open-apis/docx/v1/documents/blocks/convert",
        token,
        payload={"content_type": "markdown", "content": markdown},
    )["data"]
    api_request(
        "POST",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{document_id}/descendant",
        token,
        payload={
            "children_id": converted.get("first_level_block_ids", []),
            "descendants": converted.get("blocks", []),
            "index": -1,
        },
    )
    return len(converted.get("blocks", []))


def create_table(token: str, document_id: str, values: list[list[str]]) -> str:
    row_size = len(values)
    column_size = max((len(row) for row in values), default=0)
    response = api_request(
        "POST",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{document_id}/children",
        token,
        payload={
            "children": [
                {
                    "block_type": 31,
                    "table": {"property": {"row_size": row_size, "column_size": column_size}},
                }
            ]
        },
    )
    for child in response.get("data", {}).get("children", []):
        if child.get("block_type") == 31 and child.get("block_id"):
            return child["block_id"]
    raise RuntimeError("Failed to create table block")


def get_table_cells(token: str, document_id: str, table_block_id: str) -> list[str]:
    response = api_request(
        "GET",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{table_block_id}",
        token,
    )
    block = response.get("data", {}).get("block", {})
    cells = block.get("table", {}).get("cells", [])
    if not cells:
        raise RuntimeError("Table cell IDs unavailable")
    return cells


def clear_cell(token: str, document_id: str, cell_id: str) -> None:
    response = api_request(
        "GET",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{cell_id}/children",
        token,
        params={"page_size": 100},
    )
    items = response.get("data", {}).get("items", [])
    if not items:
        return
    api_request(
        "DELETE",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{cell_id}/children/batch_delete",
        token,
        payload={"start_index": 0, "end_index": len(items)},
    )


def write_cell(token: str, document_id: str, cell_id: str, text: str) -> None:
    # Empty cells: leave the default empty paragraph in place, no-op.
    if not text or not text.strip():
        return

    # Get the existing first child (default empty paragraph) and PATCH it.
    # DELETE + POST leaves a stale empty line because the default paragraph
    # cannot be removed; updating it in-place avoids the extra blank row.
    existing = api_request(
        "GET",
        f"/open-apis/docx/v1/documents/{document_id}/blocks/{cell_id}/children",
        token,
        params={"page_size": 50},
    )
    items = existing.get("data", {}).get("items", [])
    first_child_id = items[0]["block_id"] if items else None

    converted = api_request(
        "POST",
        "/open-apis/docx/v1/documents/blocks/convert",
        token,
        payload={"content_type": "markdown", "content": text},
    )["data"]
    source_blocks = converted.get("blocks", [])

    if first_child_id and source_blocks:
        # PATCH the first text element of the first child
        source_elements = source_blocks[0].get("text", {}).get("elements", [])
        if source_elements:
            api_request(
                "PATCH",
                f"/open-apis/docx/v1/documents/{document_id}/blocks/{first_child_id}",
                token,
                payload={"update_text_elements": {"elements": source_elements}},
            )
    elif source_blocks:
        # Fallback: no existing child, write new blocks
        for block in source_blocks:
            block.pop("parent_id", None)
        api_request(
            "POST",
            f"/open-apis/docx/v1/documents/{document_id}/blocks/{cell_id}/children",
            token,
            payload={"children": source_blocks},
        )


def write_table(token: str, document_id: str, values: list[list[str]]) -> int:
    table_block_id = create_table(token, document_id, values)
    cells = get_table_cells(token, document_id, table_block_id)
    cols = max((len(row) for row in values), default=0)
    written = 0
    for row_idx, row in enumerate(values):
        for col_idx in range(cols):
            cell_id = cells[row_idx * cols + col_idx]
            write_cell(token, document_id, cell_id, row[col_idx] if col_idx < len(row) else "")
            written += 1
            time.sleep(0.1)
    return written


def write_document(token: str, document_id: str, markdown: str) -> dict[str, int]:
    sections = split_sections(markdown)
    stats = {"markdown_blocks": 0, "table_cells": 0, "tables": 0}
    for section in sections:
        if section["type"] == "markdown":
            for chunk in split_markdown_chunks(section["content"]):
                stats["markdown_blocks"] += write_markdown_chunk(token, document_id, chunk)
                time.sleep(0.35)
        elif section["type"] == "table":
            stats["tables"] += 1
            stats["table_cells"] += write_table(token, document_id, section["rows"])
            time.sleep(0.35)
    return stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write Markdown into an existing Lark docx.")
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--document-id", help="Target docx document id.")
    source_group.add_argument("--source-url", help="Target Lark wiki/docx URL.")
    parser.add_argument("--markdown-file", required=True, help="Local Markdown source.")
    parser.add_argument(
        "--clear-first",
        action="store_true",
        help="Clear existing document root children before writing.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    app_id, app_secret = load_app_credentials()
    token = get_tenant_token(app_id, app_secret)
    document_id = resolve_document_id(token, document_id=args.document_id, source_url=args.source_url)
    markdown = Path(args.markdown_file).read_text(encoding="utf-8")
    removed = clear_document(token, document_id) if args.clear_first else 0
    stats = write_document(token, document_id, markdown)
    result = {
        "document_id": document_id,
        "url": f"https://nothing-tech.sg.larksuite.com/docx/{document_id}",
        "removed_root_children": removed,
        **stats,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
