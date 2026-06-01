#!/usr/bin/env python3
"""Generate a simple world bubble map SVG for photo frequency by country."""

from __future__ import annotations

import argparse
import math
import sqlite3
from pathlib import Path


TOP_COUNTRIES_SQL = """
SELECT country, COUNT(*) AS photo_count
FROM photo_events_parsed
WHERE country IS NOT NULL AND TRIM(country) <> ''
GROUP BY 1
ORDER BY 2 DESC
LIMIT ?
"""


COUNTRY_POINTS = {
    "India": (78.96, 22.59),
    "Australia": (133.78, -25.27),
    "Bangladesh": (90.36, 23.69),
    "Nepal": (84.12, 28.39),
    "Thailand": (100.99, 15.87),
    "Germany": (10.45, 51.17),
    "United Kingdom of Great Britain and Northern Ireland": (-3.44, 55.38),
    "United States of America": (-98.58, 39.83),
    "Philippines": (121.77, 12.88),
    "France": (2.21, 46.23),
    "United Arab Emirates": (53.85, 23.42),
    "Mexico": (-102.55, 23.63),
    "Italy": (12.57, 41.87),
    "Japan": (138.25, 36.20),
    "Spain": (-3.75, 40.46),
    "Saudi Arabia": (45.08, 23.89),
    "Malaysia": (101.98, 4.21),
    "Netherlands": (5.29, 52.13),
    "Poland": (19.15, 51.92),
    "Hong Kong": (114.17, 22.32),
    "New Zealand": (174.89, -40.90),
    "Singapore": (103.82, 1.35),
    "Switzerland": (8.23, 46.82),
    "Viet Nam": (108.28, 14.06),
    "Taiwan, Province of China": (121.00, 23.70),
    "Ireland": (-8.24, 53.41),
    "Czechia": (15.47, 49.82),
    "Austria": (14.55, 47.52),
    "Belgium": (4.47, 50.50),
    "Greece": (21.82, 39.07),
}


CONTINENT_PATHS = [
    "M 93 113 L 140 90 L 181 93 L 219 110 L 242 144 L 242 190 L 223 215 L 211 260 L 188 307 L 152 344 L 122 337 L 103 315 L 85 278 L 73 233 L 59 200 L 56 162 L 68 132 Z",
    "M 235 341 L 260 355 L 277 388 L 285 430 L 280 487 L 266 534 L 247 575 L 231 559 L 223 514 L 218 473 L 220 430 L 224 391 Z",
    "M 319 98 L 358 88 L 406 86 L 447 99 L 483 114 L 517 120 L 557 113 L 599 126 L 641 154 L 684 184 L 718 183 L 754 176 L 789 190 L 801 223 L 780 239 L 746 242 L 713 249 L 686 267 L 657 278 L 623 288 L 585 300 L 550 321 L 521 344 L 496 377 L 472 401 L 451 431 L 428 460 L 406 446 L 396 414 L 386 391 L 372 369 L 360 343 L 347 315 L 337 281 L 324 246 L 309 207 L 300 174 L 302 141 Z",
    "M 478 359 L 507 364 L 530 386 L 541 424 L 534 464 L 519 501 L 495 529 L 469 519 L 455 487 L 450 450 L 456 410 Z",
    "M 715 406 L 742 424 L 776 446 L 809 468 L 845 500 L 838 536 L 806 545 L 776 531 L 744 509 L 719 486 L 700 452 Z",
    "M 778 128 L 797 120 L 813 127 L 814 146 L 798 154 L 782 145 Z",
]


def project(lon: float, lat: float, width: int, height: int) -> tuple[float, float]:
    x = (lon + 180.0) / 360.0 * width
    y = (90.0 - lat) / 180.0 * height
    return x, y


def fetch_rows(db_path: Path, top_n: int) -> list[tuple[str, int]]:
    with sqlite3.connect(db_path) as conn:
        return conn.execute(TOP_COUNTRIES_SQL, (top_n,)).fetchall()


def build_svg(rows: list[tuple[str, int]], output_path: Path) -> None:
    width = 960
    height = 560
    map_top = 70
    map_height = 430
    legend_y = 520

    max_count = max(count for _, count in rows)
    min_radius = 4
    max_radius = 34

    def radius(count: int) -> float:
        if count <= 0:
            return min_radius
        return min_radius + (math.sqrt(count) / math.sqrt(max_count)) * (max_radius - min_radius)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="480" y="34" text-anchor="middle" font-size="28" font-weight="700" fill="#111">Photo Frequency World Bubble Map</text>',
        '<text x="480" y="58" text-anchor="middle" font-size="15" fill="#555">Bubble radius represents photo capture volume by country/region</text>',
        f'<rect x="20" y="{map_top}" width="920" height="{map_height}" rx="14" ry="14" fill="#eef6fb" stroke="#d6e3ec"/>',
    ]

    for path in CONTINENT_PATHS:
        parts.append(
            f'<path d="{path}" transform="translate(40,{map_top - 10}) scale(1.05,1.02)" fill="#dfe7dc" stroke="#b6c1b0" stroke-width="1.2"/>'
        )

    for idx, (country, count) in enumerate(rows):
        coords = COUNTRY_POINTS.get(country)
        if not coords:
            continue
        x, y = project(coords[0], coords[1], 920, map_height)
        x += 20
        y += map_top
        r = radius(count)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#d62728" fill-opacity="0.42" stroke="#b01818" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.8" fill="#8f1010"/>')

        label_y = y - r - 6 if y > map_top + 130 else y + r + 16
        anchor = "middle"
        parts.append(
            f'<text x="{x:.1f}" y="{label_y:.1f}" text-anchor="{anchor}" font-size="12" fill="#222">{country}</text>'
        )

        if idx < 8:
            list_y = 92 + idx * 18
            parts.append(
                f'<text x="765" y="{list_y}" font-size="12" fill="#333">{idx + 1}. {country}: {count:,}</text>'
            )

    sample_counts = [max_count, int(max_count * 0.1), int(max_count * 0.02)]
    sample_labels = ["Top market", "Mid volume", "Smaller market"]
    for i, (sample, label) in enumerate(zip(sample_counts, sample_labels)):
        r = radius(sample)
        cx = 120 + i * 150
        cy = legend_y - 12
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="#d62728" fill-opacity="0.35" stroke="#b01818" stroke-width="1.2"/>')
        parts.append(f'<text x="{cx}" y="{legend_y + 26}" text-anchor="middle" font-size="12" fill="#333">{label}</text>')

    parts.append("</svg>")
    output_path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, help="Path to SQLite database")
    parser.add_argument("--output", required=True, help="Output SVG path")
    parser.add_argument("--top-countries", type=int, default=20, help="Number of countries/regions to include")
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = fetch_rows(db_path, args.top_countries)
    build_svg(rows, output_path)


if __name__ == "__main__":
    main()
