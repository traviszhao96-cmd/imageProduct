#!/usr/bin/env python3
"""Generate a pie chart PNG for adjusted exposure_new distribution."""

from __future__ import annotations

import argparse
import csv
import math
import sqlite3
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


COLORS = [
    "#2E7D32",
    "#66BB6A",
    "#A5D6A7",
    "#F9A825",
    "#FFB300",
    "#FB8C00",
    "#EF6C00",
    "#E53935",
    "#C62828",
    "#8E24AA",
    "#90A4AE",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plot exposure_new percentage distribution pie chart.")
    parser.add_argument("--db", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--csv-output")
    parser.add_argument("--top-n", type=int, default=10)
    return parser.parse_args()


def load_data(db_path: str) -> list[tuple[str, int, float]]:
    sql = """
    WITH extracted AS (
      SELECT CAST(substr(raw_photo_info, instr(raw_photo_info, 'exposure_new:') + 13,
             instr(substr(raw_photo_info, instr(raw_photo_info, 'exposure_new:') + 13), ';') - 1) AS REAL) AS exposure_new
      FROM photo_events_parsed
      WHERE exposure_adjust = 1
        AND raw_photo_info LIKE '%exposure_new:%'
    ),
    totals AS (
      SELECT COUNT(*) AS total_events FROM extracted
    )
    SELECT printf('%g', exposure_new) AS exposure_new_label,
           COUNT(*) AS events,
           ROUND(COUNT(*) * 100.0 / totals.total_events, 2) AS pct
    FROM extracted CROSS JOIN totals
    GROUP BY exposure_new
    ORDER BY events DESC
    """
    with sqlite3.connect(db_path) as conn:
        return [(str(row[0]), int(row[1]), float(row[2])) for row in conn.execute(sql)]


def write_csv(path: str, rows: list[tuple[str, int, float]]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["exposure_new", "events", "pct_in_adjusted_events"])
        writer.writerows(rows)


def make_chart(rows: list[tuple[str, int, float]], output: str, top_n: int) -> None:
    top_rows = rows[:top_n]
    other_pct = round(sum(row[2] for row in rows[top_n:]), 2)
    if other_pct > 0:
        top_rows.append(("其他", sum(row[1] for row in rows[top_n:]), other_pct))

    width, height = 1600, 1000
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
        text_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 24)
        small_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 20)
    except Exception:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    draw.text((60, 40), "India 4.1-4.7 曝光值分布饼图（仅已手动调节曝光样本）", fill="#111111", font=title_font)

    cx, cy = 450, 540
    radius = 290
    bbox = (cx - radius, cy - radius, cx + radius, cy + radius)

    start_angle = -90
    for idx, (_, _, pct) in enumerate(top_rows):
        sweep = 360 * pct / 100.0
        end_angle = start_angle + sweep
        color = COLORS[idx % len(COLORS)]
        draw.pieslice(bbox, start=start_angle, end=end_angle, fill=color, outline="white", width=3)

        mid = math.radians((start_angle + end_angle) / 2.0)
        tx = cx + math.cos(mid) * (radius * 0.66)
        ty = cy + math.sin(mid) * (radius * 0.66)
        if pct >= 4:
            label = f"{pct:.2f}%"
            draw.text((tx - 25, ty - 10), label, fill="white", font=small_font)
        start_angle = end_angle

    legend_x = 860
    legend_y = 170
    line_h = 58
    for idx, (label, _, pct) in enumerate(top_rows):
        y = legend_y + idx * line_h
        color = COLORS[idx % len(COLORS)]
        draw.rounded_rectangle((legend_x, y, legend_x + 28, y + 28), radius=6, fill=color)
        draw.text((legend_x + 42, y - 2), f"{label}: {pct:.2f}%", fill="#222222", font=text_font)

    draw.text((60, 900), "说明：饼图展示曝光值 Top 10 + 其他，完整百分比分布见同页表格。", fill="#555555", font=text_font)
    image.save(output, format="PNG")


def main() -> int:
    args = parse_args()
    rows = load_data(args.db)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if args.csv_output:
        write_csv(args.csv_output, rows)
    make_chart(rows, args.output, args.top_n)
    print(f"Wrote chart to {args.output}")
    if args.csv_output:
        print(f"Wrote csv to {args.csv_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
