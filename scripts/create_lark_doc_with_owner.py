#!/usr/bin/env python3
"""Create a Lark docx and grant the target user full access.

This script uses the current OpenClaw Feishu app credentials from
~/.openclaw/openclaw.json and grants a stable owner/editor identity for
newly-created documents.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import requests


OPENCLAW_CONFIG = Path.home() / ".openclaw" / "openclaw.json"
LARK_BASE_URL = "https://open.larksuite.com"


def load_app_credentials() -> tuple[str, str]:
    config = json.loads(OPENCLAW_CONFIG.read_text(encoding="utf-8"))
    account = config["channels"]["feishu"]["accounts"]["main"]
    return account["appId"], account["appSecret"]


def get_tenant_token(app_id: str, app_secret: str) -> str:
    response = requests.post(
        f"{LARK_BASE_URL}/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise RuntimeError(payload)
    return payload["tenant_access_token"]


def create_doc(token: str, title: str) -> str:
    response = requests.post(
        f"{LARK_BASE_URL}/open-apis/docx/v1/documents",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={"title": title},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise RuntimeError(payload)
    return payload["data"]["document"]["document_id"]


def grant_full_access(token: str, doc_token: str, email: str) -> dict:
    response = requests.post(
        f"{LARK_BASE_URL}/open-apis/drive/v1/permissions/{doc_token}/members?type=docx",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={"member_type": "email", "member_id": email, "perm": "full_access"},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise RuntimeError(payload)
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a Lark docx and grant a target email full access."
    )
    parser.add_argument("--title", required=True, help="New document title.")
    parser.add_argument(
        "--email",
        default="travis.zhao@nothing.tech",
        help="Target collaborator email. Defaults to travis.zhao@nothing.tech.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    app_id, app_secret = load_app_credentials()
    token = get_tenant_token(app_id, app_secret)
    doc_token = create_doc(token, args.title)
    grant_full_access(token, doc_token, args.email)
    result = {
        "document_id": doc_token,
        "url": f"https://nothing-tech.sg.larksuite.com/docx/{doc_token}",
        "full_access_email": args.email,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
