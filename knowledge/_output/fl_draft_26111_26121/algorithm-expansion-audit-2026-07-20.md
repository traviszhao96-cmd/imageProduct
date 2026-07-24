# Legacy Split FL Algorithm Expansion Audit

- Scope: local legacy `26111_fl_final.json` and `26121_fl_final.json`.
- The online unified v2.0 FL already contains Portrait Bokeh, Motion Photo
  Frame Interpolation, and TF 50MP HDR/MMF; the missing items below only
  describe the older split local artifacts.

- KB algorithm definitions: 26
- Rule: KB defines the mode universe; project FL keeps the same algorithm identity and varies support by camera/project.
- Exception: Hex Zoom is a 26111 HP5-specific path and is not expanded into 26121.

## 26111

- Algorithm rows: 43
- Unique algorithms: 23
- Status: {'已确认': 41, '待确认': 2}
- Owners: {('HAL SE', 'Tuning SE'): 3, ('HAL SE',): 29, ('Tuning SE',): 10, ('Tuning SE', 'HAL SE'): 1}
- Missing KB expansions: 3
- Unexpected expansions: 0
- All-camera unsupported candidates requiring SE review: 9

### Missing

- 人像 / Portrait / 人像虚化 / Portrait Bokeh
- 照片 / Photo / 动态照片插帧 / Motion Photo Frame Interpolation
- 高像素 / High Resolution / TF 50MP HDR/MMF

### All-camera Unsupported

- 照片 / Photo / Photo EIS: UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。
- 视频 / Video / Video HDR 算法: Main: 26111 当前项目不提供 Video HDR 算法链路。；UW: 26111 当前项目不提供 Video HDR 算法链路。；Front: 26111 当前项目不提供 Video HDR 算法链路。
- 夜景 / Night / Remosaic: 缺少原因
- 夜景 / Night / 极夜: 缺少原因
- 夜景 / Night / Photo EIS: 缺少原因
- 慢动作 / Slow Motion / Video EIS: 缺少原因
- 专业 / Expert / Photo EIS: 缺少原因
- 高像素 / High Resolution / 超分 / Super Resolution（SR）: UW: 该摄像头不进入当前模式的 SR 算法链路。；Front: 该摄像头不进入当前模式的 SR 算法链路。
- 高像素 / High Resolution / Photo EIS: UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。

## 26121

- Algorithm rows: 42
- Unique algorithms: 22
- Status: {'待确认': 31, '已确认': 11}
- Owners: {('HAL SE', 'Tuning SE'): 2, ('HAL SE',): 29, ('Tuning SE',): 10, ('Tuning SE', 'HAL SE'): 1}
- Missing KB expansions: 3
- Unexpected expansions: 0
- All-camera unsupported candidates requiring SE review: 0

### Missing

- 人像 / Portrait / 人像虚化 / Portrait Bokeh
- 照片 / Photo / 动态照片插帧 / Motion Photo Frame Interpolation
- 高像素 / High Resolution / TF 50MP HDR/MMF
