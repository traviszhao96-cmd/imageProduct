#!/usr/bin/env python3
"""Plot photo capture frequency by date and by hour-of-day from a local SQLite DB."""

from __future__ import annotations

import argparse
import html
import sqlite3
from pathlib import Path


DATE_SQL = """
SELECT event_date, COUNT(*) AS photo_count
FROM photo_events_parsed
GROUP BY 1
ORDER BY 1
"""


HOUR_SQL = """
SELECT
    substr(datetime(event_timestamp / 1000, 'unixepoch'), 12, 2) AS hour_of_day,
    COUNT(*) AS photo_count
FROM camera_events_raw
WHERE photo_info_raw IS NOT NULL
GROUP BY 1
ORDER BY 1
"""


def fetch_rows(db_path: Path, sql: str) -> list[tuple]:
    with sqlite3.connect(db_path) as conn:
        return conn.execute(sql).fetchall()


def svg_line_chart(
    labels: list[str],
    values: list[int],
    title: str,
    x_label: str,
    y_label: str,
    color: str,
    rotate_x: bool = False,
) -> str:
    width = 1100
    height = 620
    left = 90
    right = 40
    top = 70
    bottom = 110 if rotate_x else 80
    plot_width = width - left - right
    plot_height = height - top - bottom

    max_value = max(values) if values else 1
    min_value = 0
    value_span = max(max_value - min_value, 1)

    def x_pos(index: int) -> float:
        if len(labels) == 1:
            return left + plot_width / 2
        return left + (plot_width * index / (len(labels) - 1))

    def y_pos(value: int) -> float:
        return top + plot_height - ((value - min_value) / value_span) * plot_height

    points = " ".join(f"{x_pos(i):.2f},{y_pos(v):.2f}" for i, v in enumerate(values))

    y_ticks = 5
    grid_lines = []
    y_tick_labels = []
    for i in range(y_ticks + 1):
        tick_value = min_value + value_span * i / y_ticks
        y = y_pos(tick_value)
        grid_lines.append(
            f'<line x1="{left}" y1="{y:.2f}" x2="{left + plot_width}" y2="{y:.2f}" '
            'stroke="#d9d9d9" stroke-dasharray="4 4" stroke-width="1"/>'
        )
        y_tick_labels.append(
            f'<text x="{left - 12}" y="{y + 5:.2f}" text-anchor="end" '
            f'font-size="14" fill="#555">{int(round(tick_value))}</text>'
        )

    x_tick_labels = []
    for i, label in enumerate(labels):
        x = x_pos(i)
        safe_label = html.escape(label)
        if rotate_x:
            x_tick_labels.append(
                f'<text x="{x:.2f}" y="{top + plot_height + 28}" '
                f'transform="rotate(35 {x:.2f},{top + plot_height + 28})" '
                f'text-anchor="start" font-size="13" fill="#555">{safe_label}</text>'
            )
        else:
            x_tick_labels.append(
                f'<text x="{x:.2f}" y="{top + plot_height + 28}" text-anchor="middle" '
                f'font-size="13" fill="#555">{safe_label}</text>'
            )

    markers = []
    for i, value in enumerate(values):
        markers.append(
            f'<circle cx="{x_pos(i):.2f}" cy="{y_pos(value):.2f}" r="4.5" fill="{color}"/>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#ffffff"/>
  <text x="{width / 2}" y="36" text-anchor="middle" font-size="28" font-weight="700" fill="#111">{html.escape(title)}</text>
  <text x="{width / 2}" y="{height - 22}" text-anchor="middle" font-size="18" fill="#333">{html.escape(x_label)}</text>
  <text x="28" y="{height / 2}" transform="rotate(-90 28,{height / 2})" text-anchor="middle" font-size="18" fill="#333">{html.escape(y_label)}</text>
  <line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_height}" stroke="#444" stroke-width="1.5"/>
  <line x1="{left}" y1="{top + plot_height}" x2="{left + plot_width}" y2="{top + plot_height}" stroke="#444" stroke-width="1.5"/>
  {''.join(grid_lines)}
  {''.join(y_tick_labels)}
  {''.join(x_tick_labels)}
  <polyline fill="none" stroke="{color}" stroke-width="3" points="{points}"/>
  {''.join(markers)}
</svg>
"""


def write_svg(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, help="Path to SQLite database")
    parser.add_argument("--output-dir", required=True, help="Directory to write charts into")
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    date_rows = fetch_rows(db_path, DATE_SQL)
    hour_rows = fetch_rows(db_path, HOUR_SQL)
    if not date_rows:
        raise SystemExit("No rows returned for date-based query.")
    if not hour_rows:
        raise SystemExit("No rows returned for hour-based query.")

    date_labels = [row[0] for row in date_rows]
    date_values = [int(row[1]) for row in date_rows]

    hour_count_map = {int(row[0]): int(row[1]) for row in hour_rows if row[0] is not None}
    hour_labels = [f"{hour:02d}" for hour in range(24)]
    hour_values = [hour_count_map.get(hour, 0) for hour in range(24)]

    date_svg = svg_line_chart(
        date_labels,
        date_values,
        title="Photo Capture Frequency by Date",
        x_label="Date",
        y_label="Photo Count",
        color="#1f77b4",
        rotate_x=True,
    )
    hour_svg = svg_line_chart(
        hour_labels,
        hour_values,
        title="Photo Capture Frequency by Hour of Day",
        x_label="Hour of Day",
        y_label="Photo Count",
        color="#d62728",
        rotate_x=False,
    )

    write_svg(output_dir / "photo_frequency_by_date.svg", date_svg)
    write_svg(output_dir / "photo_frequency_by_hour.svg", hour_svg)


if __name__ == "__main__":
    main()
