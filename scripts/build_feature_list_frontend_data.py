#!/usr/bin/env python3
"""Build the file:// fallback bundle for the local Feature List frontend."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "outputs" / "feature-list-table" / "data"
OUTPUT = DATA_DIR / "inline-data.js"


def main() -> None:
    payload = {
        project: json.loads((DATA_DIR / f"{project}.json").read_text(encoding="utf-8"))
        for project in ("26111", "26121")
    }
    content = "window.FL_INLINE_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
