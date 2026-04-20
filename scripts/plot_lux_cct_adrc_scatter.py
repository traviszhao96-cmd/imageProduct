#!/usr/bin/env python3
"""Generate an SVG scatter plot for lux/cct/adrc from the local SQLite DB."""

from __future__ import annotations

import argparse
import html
import math
import random
import sqlite3
from pathlib import Path


PLOT_WIDTH = 1120
PLOT_HEIGHT = 760
MARGIN_LEFT = 90
MARGIN_RIGHT = 40
MARGIN_TOP = 60
MARGIN_BOTTOM = 80
BG = "#f7f5ef"
AXIS = "#221f1a"
GRID = "#d7d2c8"
TITLE = "#1b1711"
X_MIN = 200.0
X_MAX = 10000.0
Y_MIN = 0.0
Y_MAX = 500.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create lux/cct/adrc scatter plot SVG.")
    parser.add_argument("--db", required=True, help="SQLite database path")
    parser.add_argument("--output", required=True, help="Output SVG path")
    parser.add_argument("--table", default="photo_events_raw", help="Source table")
    parser.add_argument(
        "--where",
        default="",
        help="Optional SQL condition appended inside WHERE for subgroup plots",
    )
    parser.add_argument(
        "--title",
        default="CCT vs Lux Scatter with ADRC Color",
        help="Plot title shown at the top of the SVG",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=35000,
        help="Number of points to sample for plotting",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser.parse_args()


def nice_step(span: float, target_ticks: int = 6) -> float:
    raw = span / max(target_ticks, 1)
    magnitude = 10 ** math.floor(math.log10(raw))
    residual = raw / magnitude
    if residual <= 1:
        nice = 1
    elif residual <= 2:
        nice = 2
    elif residual <= 5:
        nice = 5
    else:
        nice = 10
    return nice * magnitude


def sample_rows(
    connection: sqlite3.Connection,
    table: str,
    sample_size: int,
    seed: int,
    where: str,
) -> list[tuple[float, float, float]]:
    filter_sql = f" AND ({where})" if where.strip() else ""
    total = connection.execute(
        f"""
        SELECT COUNT(*)
        FROM {table}
        WHERE lux IS NOT NULL AND cct IS NOT NULL AND adrc IS NOT NULL
        {filter_sql}
        """
    ).fetchone()[0]
    if total <= sample_size:
        cursor = connection.execute(
            f"""
            SELECT cct, lux, adrc
            FROM {table}
            WHERE lux IS NOT NULL AND cct IS NOT NULL AND adrc IS NOT NULL
            {filter_sql}
            """
        )
        return [(float(cct), float(lux), float(adrc)) for cct, lux, adrc in cursor]

    rng = random.Random(seed)
    threshold = sample_size / total
    rows: list[tuple[float, float, float]] = []
    cursor = connection.execute(
        f"""
        SELECT cct, lux, adrc
        FROM {table}
        WHERE lux IS NOT NULL AND cct IS NOT NULL AND adrc IS NOT NULL
        {filter_sql}
        """
    )
    for cct, lux, adrc in cursor:
        if rng.random() < threshold:
            rows.append((float(cct), float(lux), float(adrc)))
    if len(rows) > sample_size:
        rows = rng.sample(rows, sample_size)
    return rows


def interp_color(value: float, min_value: float, max_value: float) -> str:
    if max_value <= min_value:
        t = 0.5
    else:
        t = (value - min_value) / (max_value - min_value)
    t = max(0.0, min(1.0, t))

    # Low ADRC = green, high ADRC = red, midpoint gets a warm yellow.
    if t < 0.5:
        local = t / 0.5
        start = (38, 166, 91)
        end = (247, 201, 72)
    else:
        local = (t - 0.5) / 0.5
        start = (247, 201, 72)
        end = (210, 59, 54)
    rgb = tuple(round(start[i] + (end[i] - start[i]) * local) for i in range(3))
    return f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"


def scale(value: float, src_min: float, src_max: float, dst_min: float, dst_max: float) -> float:
    if src_max <= src_min:
        return (dst_min + dst_max) / 2
    ratio = (value - src_min) / (src_max - src_min)
    return dst_min + ratio * (dst_max - dst_min)


def build_svg(rows: list[tuple[float, float, float]], title: str) -> str:
    rows = [row for row in rows if X_MIN <= row[0] <= X_MAX and Y_MIN <= row[1] <= Y_MAX]
    if not rows:
        raise ValueError("No rows remain after applying the requested axis ranges.")

    adrcs = [row[2] for row in rows]

    min_cct, max_cct = X_MIN, X_MAX
    min_lux, max_lux = Y_MIN, Y_MAX
    min_adrc, max_adrc = min(adrcs), max(adrcs)

    chart_x0 = MARGIN_LEFT
    chart_x1 = PLOT_WIDTH - MARGIN_RIGHT
    chart_y0 = MARGIN_TOP
    chart_y1 = PLOT_HEIGHT - MARGIN_BOTTOM

    x_span = max_cct - min_cct
    y_span = max_lux - min_lux
    x_step = nice_step(x_span)
    y_step = nice_step(y_span)

    x_tick_start = math.floor(min_cct / x_step) * x_step
    y_tick_start = math.floor(min_lux / y_step) * y_step

    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{PLOT_WIDTH}" height="{PLOT_HEIGHT}" viewBox="0 0 {PLOT_WIDTH} {PLOT_HEIGHT}">'
    )
    parts.append(f'<rect width="100%" height="100%" fill="{BG}"/>')
    parts.append(
        f'<text x="{MARGIN_LEFT}" y="30" font-size="28" font-family="Helvetica, Arial, sans-serif" fill="{TITLE}" font-weight="700">{html.escape(title)}</text>'
    )
    parts.append(
        f'<text x="{MARGIN_LEFT}" y="52" font-size="14" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}">x: CCT, y: Lux, color: ADRC (green = lower, red = higher)</text>'
    )

    x = x_tick_start
    while x <= max_cct + x_step:
        px = scale(x, min_cct, max_cct, chart_x0, chart_x1)
        parts.append(
            f'<line x1="{px:.2f}" y1="{chart_y0}" x2="{px:.2f}" y2="{chart_y1}" stroke="{GRID}" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{px:.2f}" y="{chart_y1 + 24}" text-anchor="middle" font-size="12" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}">{int(x)}</text>'
        )
        x += x_step

    y = y_tick_start
    while y <= max_lux + y_step:
        py = scale(y, min_lux, max_lux, chart_y0, chart_y1)
        parts.append(
            f'<line x1="{chart_x0}" y1="{py:.2f}" x2="{chart_x1}" y2="{py:.2f}" stroke="{GRID}" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{chart_x0 - 12}" y="{py + 4:.2f}" text-anchor="end" font-size="12" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}">{int(y)}</text>'
        )
        y += y_step

    parts.append(
        f'<line x1="{chart_x0}" y1="{chart_y1}" x2="{chart_x1}" y2="{chart_y1}" stroke="{AXIS}" stroke-width="2"/>'
    )
    parts.append(
        f'<line x1="{chart_x0}" y1="{chart_y0}" x2="{chart_x0}" y2="{chart_y1}" stroke="{AXIS}" stroke-width="2"/>'
    )
    parts.append(
        f'<text x="{(chart_x0 + chart_x1) / 2:.2f}" y="{PLOT_HEIGHT - 24}" text-anchor="middle" font-size="16" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}">CCT</text>'
    )
    parts.append(
        f'<text x="24" y="{(chart_y0 + chart_y1) / 2:.2f}" text-anchor="middle" font-size="16" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}" transform="rotate(-90 24 {(chart_y0 + chart_y1) / 2:.2f})">Lux</text>'
    )

    for cct, lux, adrc in rows:
        px = scale(cct, min_cct, max_cct, chart_x0, chart_x1)
        py = scale(lux, min_lux, max_lux, chart_y0, chart_y1)
        color = interp_color(adrc, min_adrc, max_adrc)
        parts.append(
            f'<circle cx="{px:.2f}" cy="{py:.2f}" r="2.1" fill="{color}" fill-opacity="0.32"/>'
        )

    legend_x = chart_x1 - 230
    legend_y = chart_y0 + 10
    parts.append(
        f'<rect x="{legend_x}" y="{legend_y}" width="190" height="74" rx="10" fill="#fffdf8" stroke="{GRID}"/>'
    )
    parts.append(
        f'<text x="{legend_x + 12}" y="{legend_y + 22}" font-size="13" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}" font-weight="700">ADRC Color Legend</text>'
    )
    for i in range(120):
        x0 = legend_x + 12 + i
        parts.append(
            f'<line x1="{x0}" y1="{legend_y + 40}" x2="{x0}" y2="{legend_y + 54}" stroke="{interp_color(min_adrc + (max_adrc - min_adrc) * (i / 119), min_adrc, max_adrc)}" stroke-width="1"/>'
        )
    parts.append(
        f'<text x="{legend_x + 12}" y="{legend_y + 68}" font-size="11" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}">{min_adrc:.2f} low</text>'
    )
    parts.append(
        f'<text x="{legend_x + 132}" y="{legend_y + 68}" font-size="11" font-family="Helvetica, Arial, sans-serif" fill="{AXIS}">{max_adrc:.2f} high</text>'
    )

    meta = (
        f"points={len(rows)}, cct={min_cct:.0f}-{max_cct:.0f}, "
        f"lux={min_lux:.1f}-{max_lux:.1f}, adrc={min_adrc:.2f}-{max_adrc:.2f}"
    )
    parts.append(f"<desc>{html.escape(meta)}</desc>")
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> int:
    args = parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(args.db) as connection:
        rows = sample_rows(
            connection, args.table, args.sample_size, args.seed, args.where
        )

    svg = build_svg(rows, args.title)
    output.write_text(svg, encoding="utf-8")
    print(f"Wrote {output} with {len(rows)} sampled points")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
