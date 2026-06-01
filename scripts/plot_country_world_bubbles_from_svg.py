#!/usr/bin/env python3
"""Overlay country bubble markers on a GitHub-sourced SVG world map."""

from __future__ import annotations

import argparse
import math
import re
import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path


TOP_COUNTRIES_SQL = """
SELECT country, COUNT(*) AS photo_count
FROM photo_events_parsed
WHERE country IS NOT NULL AND TRIM(country) <> ''
GROUP BY 1
ORDER BY 2 DESC
LIMIT ?
"""


COUNTRY_TO_SVG_ID = {
    "India": "in",
    "Australia": "au",
    "Bangladesh": "bd",
    "Nepal": "np",
    "Thailand": "th",
    "Germany": "de",
    "United Kingdom of Great Britain and Northern Ireland": "gb",
    "United States of America": "us",
    "Philippines": "ph",
    "France": "fr",
    "United Arab Emirates": "ae",
    "Mexico": "mx",
    "Italy": "it",
    "Japan": "jp",
    "Spain": "es",
    "Saudi Arabia": "sa",
    "Malaysia": "my",
    "Netherlands": "nl",
    "Poland": "pl",
    "New Zealand": "nz",
    "Singapore": "sg",
    "Switzerland": "ch",
    "Viet Nam": "vn",
    "Taiwan, Province of China": "tw",
    "Ireland": "ie",
    "Czechia": "cz",
    "Austria": "at",
    "Belgium": "be",
    "Greece": "gr",
    "Hong Kong": None,
}


FALLBACK_POINTS = {
    # For tiny or missing regions that do not have a useful country path in the SVG.
    "Hong Kong": (114.17, 22.32),
}


def fetch_rows(db_path: Path, top_n: int) -> list[tuple[str, int]]:
    with sqlite3.connect(db_path) as conn:
        return conn.execute(TOP_COUNTRIES_SQL, (top_n,)).fetchall()


def parse_svg(svg_text: str) -> tuple[tuple[float, float, float, float], str]:
    viewbox_match = re.search(r'viewBox="([^"]+)"', svg_text)
    if not viewbox_match:
        raise ValueError("viewBox not found in base SVG")
    min_x, min_y, width, height = map(float, viewbox_match.group(1).split())
    inner = re.sub(r"^<svg[^>]*>", "", svg_text)
    inner = re.sub(r"</svg>\s*$", "", inner)
    return (min_x, min_y, width, height), inner


def project(lon: float, lat: float, viewbox: tuple[float, float, float, float]) -> tuple[float, float]:
    min_x, min_y, width, height = viewbox
    # This base map is close enough to cylindrical for a linear overlay to work visually.
    x = min_x + ((lon + 180.0) / 360.0) * width
    y = min_y + ((90.0 - lat) / 180.0) * height
    return x, y


def tokenize_path(d: str) -> list[str]:
    return re.findall(r"[A-Za-z]|[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?", d)


def update_bbox(bbox: list[float], x: float, y: float) -> None:
    bbox[0] = min(bbox[0], x)
    bbox[1] = min(bbox[1], y)
    bbox[2] = max(bbox[2], x)
    bbox[3] = max(bbox[3], y)


def path_bbox(d: str) -> tuple[float, float, float, float] | None:
    tokens = tokenize_path(d)
    if not tokens:
        return None

    param_counts = {
        "M": 2, "L": 2, "T": 2,
        "H": 1, "V": 1,
        "S": 4, "Q": 4,
        "C": 6,
        "A": 7,
        "Z": 0,
    }

    idx = 0
    cmd = None
    x = y = 0.0
    start_x = start_y = 0.0
    bbox = [float("inf"), float("inf"), float("-inf"), float("-inf")]

    while idx < len(tokens):
        token = tokens[idx]
        if re.fullmatch(r"[A-Za-z]", token):
            cmd = token
            idx += 1
            if cmd in "Zz":
                x, y = start_x, start_y
                update_bbox(bbox, x, y)
                continue
        if cmd is None:
            break

        upper = cmd.upper()
        count = param_counts.get(upper)
        if count is None or count == 0:
            continue

        while idx + count <= len(tokens):
            if re.fullmatch(r"[A-Za-z]", tokens[idx]):
                break
            vals = [float(tokens[idx + i]) for i in range(count)]
            idx += count

            if upper == "M":
                if cmd.islower():
                    x += vals[0]
                    y += vals[1]
                else:
                    x, y = vals[0], vals[1]
                start_x, start_y = x, y
                update_bbox(bbox, x, y)
                cmd = "l" if cmd.islower() else "L"
                upper = cmd.upper()
                count = param_counts[upper]
            elif upper == "L":
                if cmd.islower():
                    x += vals[0]
                    y += vals[1]
                else:
                    x, y = vals[0], vals[1]
                update_bbox(bbox, x, y)
            elif upper == "H":
                x = x + vals[0] if cmd.islower() else vals[0]
                update_bbox(bbox, x, y)
            elif upper == "V":
                y = y + vals[0] if cmd.islower() else vals[0]
                update_bbox(bbox, x, y)
            elif upper == "C":
                points = []
                if cmd.islower():
                    points = [
                        (x + vals[0], y + vals[1]),
                        (x + vals[2], y + vals[3]),
                        (x + vals[4], y + vals[5]),
                    ]
                else:
                    points = [
                        (vals[0], vals[1]),
                        (vals[2], vals[3]),
                        (vals[4], vals[5]),
                    ]
                for px, py in points:
                    update_bbox(bbox, px, py)
                x, y = points[-1]
            elif upper == "S" or upper == "Q":
                points = []
                if cmd.islower():
                    points = [
                        (x + vals[0], y + vals[1]),
                        (x + vals[2], y + vals[3]),
                    ]
                else:
                    points = [
                        (vals[0], vals[1]),
                        (vals[2], vals[3]),
                    ]
                for px, py in points:
                    update_bbox(bbox, px, py)
                x, y = points[-1]
            elif upper == "T":
                if cmd.islower():
                    x += vals[0]
                    y += vals[1]
                else:
                    x, y = vals[0], vals[1]
                update_bbox(bbox, x, y)
            elif upper == "A":
                if cmd.islower():
                    x += vals[5]
                    y += vals[6]
                else:
                    x, y = vals[5], vals[6]
                update_bbox(bbox, x, y)

    if bbox[0] == float("inf"):
        return None
    return bbox[0], bbox[1], bbox[2], bbox[3]


def bbox_center(bbox: tuple[float, float, float, float]) -> tuple[float, float]:
    min_x, min_y, max_x, max_y = bbox
    return (min_x + max_x) / 2.0, (min_y + max_y) / 2.0


def svg_country_centers(base_svg_path: Path, viewbox: tuple[float, float, float, float]) -> dict[str, tuple[float, float]]:
    tree = ET.parse(base_svg_path)
    root = tree.getroot()
    centers: dict[str, tuple[float, float]] = {}
    ns = {"svg": "http://www.w3.org/2000/svg"}

    for country, svg_id in COUNTRY_TO_SVG_ID.items():
        if not svg_id:
            continue
        elem = root.find(f".//*[@id='{svg_id}']")
        if elem is None:
            continue

        bboxes = []
        tag = elem.tag.rsplit("}", 1)[-1]
        if tag == "path":
            d = elem.attrib.get("d")
            if d:
                bbox = path_bbox(d)
                if bbox:
                    bboxes.append(bbox)
        elif tag == "g":
            mainland = None
            for child in elem.findall(".//svg:path", ns):
                classes = child.attrib.get("class", "")
                if "mainland" in classes.split():
                    mainland = child
                    break
            target_paths = [mainland] if mainland is not None else elem.findall(".//svg:path", ns)
            for child in target_paths:
                if child is None:
                    continue
                d = child.attrib.get("d")
                if not d:
                    continue
                bbox = path_bbox(d)
                if bbox:
                    bboxes.append(bbox)

        if bboxes:
            min_x = min(b[0] for b in bboxes)
            min_y = min(b[1] for b in bboxes)
            max_x = max(b[2] for b in bboxes)
            max_y = max(b[3] for b in bboxes)
            centers[country] = bbox_center((min_x, min_y, max_x, max_y))

    for country, lonlat in FALLBACK_POINTS.items():
        centers[country] = project(lonlat[0], lonlat[1], viewbox)

    return centers


def build_svg(base_svg_path: Path, rows: list[tuple[str, int]], output_path: Path) -> None:
    svg_text = base_svg_path.read_text(encoding="utf-8")
    viewbox, inner_svg = parse_svg(svg_text)
    min_x, min_y, width, height = viewbox
    country_centers = svg_country_centers(base_svg_path, viewbox)

    max_count = max(count for _, count in rows)

    def radius(count: int) -> float:
        return 4.0 + (math.sqrt(count) / math.sqrt(max_count)) * 26.0

    bubble_parts = []
    label_parts = []
    for idx, (country, count) in enumerate(rows):
        if country not in country_centers:
            continue
        x, y = country_centers[country]
        r = radius(count)
        bubble_parts.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="#d62728" fill-opacity="0.38" stroke="#a31c1c" stroke-width="1.3"/>'
        )
        bubble_parts.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.8" fill="#8c1111"/>'
        )

        if idx < 10:
            label_parts.append(
                f'<text x="{min_x + width - 6}" y="{min_y + 24 + idx * 17}" text-anchor="end" font-size="12" fill="#333">{idx + 1}. {country}: {count:,}</text>'
            )

    title_y = min_y - 18
    subtitle_y = min_y - 2
    legend_y = min_y + height + 26
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width + 80:.0f}" height="{height + 90:.0f}" viewBox="{min_x - 20:.3f} {min_y - 35:.3f} {width + 40:.3f} {height + 70:.3f}">
  <rect x="{min_x - 20:.2f}" y="{min_y - 35:.2f}" width="{width + 40:.2f}" height="{height + 70:.2f}" fill="#ffffff"/>
  <text x="{min_x + width / 2:.2f}" y="{title_y:.2f}" text-anchor="middle" font-size="26" font-weight="700" fill="#111">Photo Frequency World Bubble Map</text>
  <text x="{min_x + width / 2:.2f}" y="{subtitle_y:.2f}" text-anchor="middle" font-size="14" fill="#555">GitHub base map: flekschas/simple-world-map, bubbles scaled by photo count</text>
  <g opacity="0.95">
    {inner_svg}
  </g>
  <g>
    {''.join(bubble_parts)}
  </g>
  <g>
    {''.join(label_parts)}
  </g>
  <text x="{min_x:.2f}" y="{legend_y:.2f}" font-size="12" fill="#444">Red bubble radius = photo capture volume</text>
</svg>
"""
    output_path.write_text(svg, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--base-svg", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--top-countries", type=int, default=20)
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()
    base_svg_path = Path(args.base_svg).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = fetch_rows(db_path, args.top_countries)
    build_svg(base_svg_path, rows, output_path)


if __name__ == "__main__":
    main()
