# Charting

## Main Plot Script

Use:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/plot_lux_cct_adrc_scatter.py \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db \
  --output /Users/travis.zhao/imageProduct/outputs/lux_cct_adrc_scatter.svg
```

## Default Scatter Semantics

- x-axis: `cct`
- y-axis: `lux`
- color: `adrc`
- lower ADRC: green
- higher ADRC: red

## Supported Plot Controls

- subgroup filter:

```bash
--where "camera_id = 0"
```

- subgroup title:

```bash
--title "CCT vs Lux by Camera ID 0 (ADRC color)"
```

## Typical Subgroup Splits

- by `camera_id`
- by `photo_mode`

## Interpretation Notes

- Apparent opacity differences mostly come from point overlap, not per-point alpha changes.
- When density is too high, subgroup plots are often more readable than one global scatter.
- If the user wants more stable density comparison, consider lowering fixed opacity or switching to a density-style chart in a future iteration.
