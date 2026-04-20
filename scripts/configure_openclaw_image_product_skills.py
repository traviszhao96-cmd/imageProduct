#!/usr/bin/env python3
"""Sync imageProduct-related skills into an OpenClaw-only skill pack.

This keeps the Lark bot focused on imaging work instead of loading every
personal Codex skill under ~/.codex/skills.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OPENCLAW_CONFIG = Path.home() / ".openclaw" / "openclaw.json"
OPENCLAW_SKILL_PACK = Path.home() / ".openclaw" / "skills-image-product"

SHARED_SKILL_ROOT = Path.home() / ".codex" / "skills"
SHARED_SKILLS = [
    "camera-cloud-local-pipeline",
    "doc",
    "gallery-event-tracking",
    "gallery-feature-doc",
    "google-play-whats-new",
    "local-camera-analytics",
    "mobile-imaging-planning-doc",
    "nothing-camera-athena",
]

PROJECT_SKILL_ROOTS = [
    PROJECT_ROOT / "outputs" / "skills" / "aws-athena-camera-sql",
    PROJECT_ROOT / "outputs" / "skills" / "server-camera-analytics",
    PROJECT_ROOT / "outputs" / "skills" / "lark-doc-normalizer",
    PROJECT_ROOT / "outputs" / "skills" / "lark-template-doc-writer",
]


def copy_skill(src: Path, dst_root: Path) -> str:
    if not src.exists():
        raise FileNotFoundError(f"Missing skill source: {src}")
    dst = dst_root / src.name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return src.name


def sync_skill_pack() -> list[str]:
    OPENCLAW_SKILL_PACK.mkdir(parents=True, exist_ok=True)
    synced: list[str] = []
    for skill_name in SHARED_SKILLS:
        synced.append(copy_skill(SHARED_SKILL_ROOT / skill_name, OPENCLAW_SKILL_PACK))
    for src in PROJECT_SKILL_ROOTS:
        synced.append(copy_skill(src, OPENCLAW_SKILL_PACK))
    manifest = {
        "root": str(OPENCLAW_SKILL_PACK),
        "skills": sorted(synced),
    }
    (OPENCLAW_SKILL_PACK / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return sorted(synced)


def update_openclaw_config(skill_root: Path) -> None:
    config = json.loads(OPENCLAW_CONFIG.read_text(encoding="utf-8"))
    skills_cfg = config.setdefault("skills", {})
    load_cfg = skills_cfg.setdefault("load", {})
    load_cfg["extraDirs"] = [str(skill_root)]
    OPENCLAW_CONFIG.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    synced = sync_skill_pack()
    update_openclaw_config(OPENCLAW_SKILL_PACK)
    result = {
        "skill_pack_dir": str(OPENCLAW_SKILL_PACK),
        "skill_count": len(synced),
        "skills": synced,
        "openclaw_config": str(OPENCLAW_CONFIG),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
