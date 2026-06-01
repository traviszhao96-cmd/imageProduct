#!/usr/bin/env python3
"""Generate an interactive HTML world bubble map from a local SQLite DB."""

from __future__ import annotations

import argparse
import html
import json
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
    # Manual SVG-space fallback for tiny regions without a standalone path in the base map.
    "Hong Kong": (678.0, 478.0),
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
            elif upper in {"S", "Q"}:
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


def project(lon: float, lat: float, viewbox: tuple[float, float, float, float]) -> tuple[float, float]:
    min_x, min_y, width, height = viewbox
    x = min_x + ((lon + 180.0) / 360.0) * width
    y = min_y + ((90.0 - lat) / 180.0) * height
    return x, y


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

    for country, point in FALLBACK_POINTS.items():
        centers[country] = point

    return centers


def build_html(base_svg_path: Path, rows: list[tuple[str, int]], output_path: Path) -> None:
    svg_text = base_svg_path.read_text(encoding="utf-8")
    viewbox, inner_svg = parse_svg(svg_text)
    min_x, min_y, width, height = viewbox
    centers = svg_country_centers(base_svg_path, viewbox)
    max_count = max(count for _, count in rows)

    def radius(count: int) -> float:
        return 4.0 + (math.sqrt(count) / math.sqrt(max_count)) * 28.0

    bubbles = []
    bubble_data = []
    for country, count in rows:
        if country not in centers:
            continue
        x, y = centers[country]
        r = radius(count)
        bubble_id = f"bubble-{len(bubble_data)}"
        bubbles.append(
            f'<circle id="{bubble_id}" class="bubble" cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" '
            f'data-country="{html.escape(country, quote=True)}" data-count="{count}" />'
        )
        bubble_data.append({"id": bubble_id, "country": country, "count": count})

    rows_html = "\n".join(
        f"<tr><td>{idx + 1}</td><td>{html.escape(country)}</td><td>{count:,}</td></tr>"
        for idx, (country, count) in enumerate(rows[:20])
    )

    html_text = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Photo Frequency World Bubble Map</title>
  <style>
    :root {{
      --bg: #f4f7fb;
      --card: rgba(255,255,255,0.92);
      --text: #14212b;
      --muted: #5f7382;
      --bubble: rgba(214, 39, 40, 0.38);
      --bubble-stroke: #991b1b;
      --bubble-hover: rgba(214, 39, 40, 0.62);
      --land: #dfe7dc;
      --land-stroke: #aab7a3;
      --accent: #c62828;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background:
        radial-gradient(circle at top left, #e8f2fa 0%, transparent 28%),
        radial-gradient(circle at top right, #fdeeee 0%, transparent 24%),
        linear-gradient(180deg, #f8fbfd 0%, #eef3f7 100%);
      color: var(--text);
    }}
    .page {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 28px 24px 36px;
    }}
    .header {{
      margin-bottom: 18px;
    }}
    .title {{
      margin: 0;
      font-size: 32px;
      line-height: 1.1;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}
    .subtitle {{
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 15px;
    }}
    .layout {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 320px;
      gap: 18px;
      align-items: start;
    }}
    .map-card, .side-card {{
      background: var(--card);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(20, 33, 43, 0.08);
      border-radius: 20px;
      box-shadow: 0 18px 40px rgba(32, 54, 74, 0.08);
    }}
    .map-card {{
      padding: 18px 18px 10px;
      position: relative;
      overflow: hidden;
    }}
    .map-wrap {{
      position: relative;
      width: 100%;
    }}
    svg {{
      display: block;
      width: 100%;
      height: auto;
    }}
    .world-map path {{
      fill: var(--land);
      stroke: var(--land-stroke);
      stroke-width: 1.1;
      transition: fill 120ms ease;
    }}
    .world-map path:hover {{
      fill: #d4dfcf;
    }}
    .bubble {{
      fill: var(--bubble);
      stroke: var(--bubble-stroke);
      stroke-width: 1.3;
      cursor: pointer;
      transition: fill 120ms ease, transform 120ms ease;
      transform-origin: center;
    }}
    .bubble:hover {{
      fill: var(--bubble-hover);
      transform: scale(1.03);
    }}
    .tooltip {{
      position: fixed;
      pointer-events: none;
      padding: 10px 12px;
      background: rgba(20, 33, 43, 0.94);
      color: #fff;
      border-radius: 12px;
      font-size: 13px;
      line-height: 1.4;
      box-shadow: 0 10px 24px rgba(0,0,0,0.18);
      opacity: 0;
      transform: translate(10px, 10px);
      transition: opacity 80ms ease;
      z-index: 20;
      min-width: 180px;
    }}
    .tooltip strong {{
      display: block;
      margin-bottom: 2px;
      font-size: 14px;
    }}
    .legend {{
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 6px 2px;
      color: var(--muted);
      font-size: 13px;
    }}
    .legend-dot {{
      width: 14px;
      height: 14px;
      border-radius: 999px;
      background: rgba(214, 39, 40, 0.5);
      border: 1px solid #991b1b;
      flex: 0 0 auto;
    }}
    .side-card {{
      padding: 16px 16px 12px;
    }}
    .side-title {{
      margin: 0 0 10px;
      font-size: 18px;
      font-weight: 700;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      padding: 8px 6px;
      border-bottom: 1px solid rgba(20, 33, 43, 0.08);
      text-align: left;
    }}
    th {{
      color: var(--muted);
      font-weight: 600;
    }}
    td:last-child, th:last-child {{
      text-align: right;
    }}
    .footnote {{
      margin-top: 10px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.5;
    }}
    @media (max-width: 1100px) {{
      .layout {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="header">
      <h1 class="title">不同国家/地区拍摄频率世界地图</h1>
      <p class="subtitle">悬停红色气泡可查看国家/地区与拍摄频率。气泡半径按拍摄量缩放。</p>
    </div>
    <div class="layout">
      <section class="map-card">
        <div class="map-wrap">
          <svg viewBox="{min_x - 16:.3f} {min_y - 16:.3f} {width + 32:.3f} {height + 32:.3f}" aria-label="Photo frequency world bubble map">
            <g class="world-map">
              {inner_svg}
            </g>
            <g class="bubble-layer">
              {''.join(bubbles)}
            </g>
          </svg>
        </div>
        <div class="legend">
          <span class="legend-dot"></span>
          <span>气泡越大，表示该国家/地区照片拍摄量越高。</span>
        </div>
      </section>
      <aside class="side-card">
        <h2 class="side-title">Top Markets</h2>
        <table>
          <thead>
            <tr><th>#</th><th>Country / Region</th><th>Photo Count</th></tr>
          </thead>
          <tbody>
            {rows_html}
          </tbody>
        </table>
        <div class="footnote">
          数据源：本地 SQLite `photo_events_parsed`。<br/>
          底图：GitHub `flekschas/simple-world-map`。
        </div>
      </aside>
    </div>
  </div>
  <div id="tooltip" class="tooltip"></div>
  <script>
    const tooltip = document.getElementById('tooltip');
    const bubbles = document.querySelectorAll('.bubble');
    const fmt = new Intl.NumberFormat('en-US');

    function showTooltip(event) {{
      const country = event.target.dataset.country;
      const count = Number(event.target.dataset.count || 0);
      tooltip.innerHTML = `<strong>${{country}}</strong>Photo Count: ${{fmt.format(count)}}`;
      tooltip.style.opacity = '1';
      moveTooltip(event);
    }}

    function moveTooltip(event) {{
      tooltip.style.left = `${{event.clientX + 14}}px`;
      tooltip.style.top = `${{event.clientY + 14}}px`;
    }}

    function hideTooltip() {{
      tooltip.style.opacity = '0';
    }}

    bubbles.forEach((bubble) => {{
      bubble.addEventListener('mouseenter', showTooltip);
      bubble.addEventListener('mousemove', moveTooltip);
      bubble.addEventListener('mouseleave', hideTooltip);
    }});
  </script>
</body>
</html>
"""
    output_path.write_text(html_text, encoding="utf-8")


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
    build_html(base_svg_path, rows, output_path)


if __name__ == "__main__":
    main()
