#!/usr/bin/env python3
"""Build a normalization payload for a Lark document workflow.

This script does not call the Lark API or any model directly.
It packages the workspace rules, template, and source content into a stable JSON
contract that a separate service, such as the Cam Pulse Lark app backend, can send
to a model endpoint.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RULES = WORKSPACE_ROOT / "knowledge" / "doc_normalization_rules.md"
DEFAULT_PRD_TEMPLATE = WORKSPACE_ROOT / "templates" / "prd_normalization_template.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def build_instruction(mode: str, doc_type: str) -> str:
    return (
        "You are a document normalizer for internal product documents. "
        f"Current mode: {mode}. "
        f"Document type: {doc_type}. "
        "Preserve facts, do not invent missing information, and mark unknown required fields as 待确认. "
        "Return JSON with keys issues, normalized_markdown, and change_summary."
    )


def build_payload(
    source_text: str,
    mode: str,
    doc_type: str,
    source_title: str | None,
    source_url: str | None,
) -> dict[str, Any]:
    template_path = DEFAULT_PRD_TEMPLATE if doc_type == "prd" else None
    return {
        "mode": mode,
        "doc_type": doc_type,
        "source": {
            "title": source_title or "Untitled document",
            "url": source_url,
            "content": source_text,
        },
        "rules_markdown": read_text(DEFAULT_RULES),
        "template_markdown": read_text(template_path) if template_path else None,
        "instruction": build_instruction(mode, doc_type),
        "expected_output_schema": {
            "issues": [
                {
                    "severity": "high|medium|low",
                    "title": "short label",
                    "detail": "what should be fixed or confirmed",
                }
            ],
            "normalized_markdown": "full rewritten draft",
            "change_summary": [
                "short bullet describing major normalization changes"
            ],
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a JSON payload for the Lark document normalization flow."
    )
    parser.add_argument(
        "--input-file",
        required=True,
        help="Local markdown or text file exported from Lark.",
    )
    parser.add_argument(
        "--mode",
        default="suggest",
        choices=["diagnose", "suggest", "apply"],
        help="Normalization mode. Default is suggest.",
    )
    parser.add_argument(
        "--doc-type",
        default="prd",
        help="Document type identifier. Default is prd.",
    )
    parser.add_argument(
        "--source-title",
        default=None,
        help="Optional original document title.",
    )
    parser.add_argument(
        "--source-url",
        default=None,
        help="Optional original Lark document URL.",
    )
    parser.add_argument(
        "--output-file",
        default=None,
        help="Optional path to write the JSON payload.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_file).expanduser().resolve()
    payload = build_payload(
        source_text=read_text(input_path),
        mode=args.mode,
        doc_type=args.doc_type,
        source_title=args.source_title,
        source_url=args.source_url,
    )

    serialized = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output_file:
        output_path = Path(args.output_file).expanduser().resolve()
        output_path.write_text(serialized + "\n", encoding="utf-8")
    else:
        print(serialized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
