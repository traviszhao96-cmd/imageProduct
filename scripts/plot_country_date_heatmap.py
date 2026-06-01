#!/usr/bin/env python3
"""Generate a country-by-date photo frequency heatmap from a local SQLite DB."""

from __future__ import annotations

import argparse
import html
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


DATE_SQL = """
SELECT DISTINCT event_date
FROM photo_events_parsed
ORDER BY 1
"""


HEATMAP_SQL = """
SELECT country, event_date, COUNT(*) AS photo_count
FROM photo_events_parsed
WHERE country IN ({country_placeholders})
GROUP BY 1, 2
"""


def fetch_all(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[tuple]:
    return conn.execute(sql, params).fetchall()


def color_for_ratio(ratio: float) -> str:
    # White -> light blue -> deep blue
    start = (243, 248, 252)
    end = (31, 119, 180)
    r = int(start[0] + (end[0] - start[0]) * ratio)
    g = int(start[1] + (end[1] - start[1]) * ratio)
    b = int(start[2] + (end[2] - start[2]) * ratio)
    return f"rgb({r},{g},{b})"


def text_color_for_ratio(ratio: float) -> str:
    return "#ffffff" if ratio >= 0.58 else "#1f2a33"


def build_svg(countries: list[str], dates: list[str], values: dict[tuple[str, str], int], output_path: Path) -> None:
    cell_w = 116
    cell_h = 34
    left = 290
    top = 120
    right = 40
    bottom = 80
    width = left + len(dates) * cell_w + right
    height = top + len(countries) * cell_h + bottom

    max_value = max(values.values()) if values else 1

    rows = []
    for row_idx, country in enumerate(countries):
        y = top + row_idx * cell_h
        rows.append(
            f'<text x="{left - 12}" y="{y + 22}" text-anchor="end" font-size="14" fill="#222">{html.escape(country)}</text>'
        )
        for col_idx, date in enumerate(dates):
            x = left + col_idx * cell_w
            count = values.get((country, date), 0)
            ratio = count / max_value if max_value else 0
            fill = color_for_ratio(ratio)
            label = f"{count:,}"
            rows.append(
                f'<rect x="{x}" y="{y}" width="{cell_w - 2}" height="{cell_h - 2}" rx="4" ry="4" fill="{fill}"/>'
            )
            rows.append(
                f'<text x="{x + (cell_w - 2) / 2}" y="{y + 22}" text-anchor="middle" font-size="12" fill="{text_color_for_ratio(ratio)}">{label}</text>'
            )

    date_labels = []
    for col_idx, date in enumerate(dates):
        x = left + col_idx * cell_w + (cell_w - 2) / 2
        date_labels.append(
            f'<text x="{x}" y="{top - 14}" text-anchor="middle" font-size="14" fill="#222">{html.escape(date)}</text>'
        )

    legend_x = left
    legend_y = height - 46
    legend_w = 260
    legend_steps = 40
    legend_rects = []
    for i in range(legend_steps):
        x = legend_x + legend_w * i / legend_steps
        ratio = i / (legend_steps - 1)
        legend_rects.append(
            f'<rect x="{x:.2f}" y="{legend_y}" width="{legend_w / legend_steps + 1:.2f}" height="14" fill="{color_for_ratio(ratio)}"/>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#ffffff"/>
  <text x="{width / 2}" y="42" text-anchor="middle" font-size="28" font-weight="700" fill="#111">Photo Capture Frequency Heatmap by Country and Date</text>
  <text x="{width / 2}" y="72" text-anchor="middle" font-size="16" fill="#444">Top countries/regions by photo volume, local SQLite dataset</text>
  {''.join(date_labels)}
  {''.join(rows)}
  {''.join(legend_rects)}
  <text x="{legend_x}" y="{legend_y - 8}" font-size="13" fill="#333">Lower</text>
  <text x="{legend_x + legend_w}" y="{legend_y - 8}" text-anchor="end" font-size="13" fill="#333">Higher</text>
</svg>
"""
    output_path.write_text(svg, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, help="Path to SQLite database")
    parser.add_argument("--output", required=True, help="Output SVG path")
    parser.add_argument("--top-countries", type=int, default=15, help="Number of countries to include")
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        top_country_rows = fetch_all(conn, TOP_COUNTRIES_SQL, (args.top_countries,))
        date_rows = fetch_all(conn, DATE_SQL)

        countries = [row[0] for row in top_country_rows]
        dates = [row[0] for row in date_rows]

        placeholders = ",".join("?" for _ in countries)
        heatmap_rows = fetch_all(
            conn,
            HEATMAP_SQL.format(country_placeholders=placeholders),
            tuple(countries),
        )

    value_map = {(country, date): count for country, date, count in heatmap_rows}
    build_svg(countries, dates, value_map, output_path)


if __name__ == "__main__":
    main()
