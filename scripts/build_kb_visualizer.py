#!/usr/bin/env python3
"""Build file:// compatible data for the local KB visualizer."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "knowledge/_output/kb-functions-algorithms.json"
OUTPUT = ROOT / "outputs/kb-visualizer/data.js"


def main() -> None:
    rows = json.loads(SOURCE.read_text(encoding="utf-8"))
    payload = {
        "generatedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source": str(SOURCE.relative_to(ROOT)),
        "rows": rows,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "window.KB_PAYLOAD = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
