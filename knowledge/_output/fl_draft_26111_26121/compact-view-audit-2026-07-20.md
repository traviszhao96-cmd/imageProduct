# 26111 / 26121 Compact FL View Audit

## Result

- 26111: 209 -> 209 rows
- 26121: 224 -> 208 rows
- Complete online snapshots remain unchanged; this script only builds compact local review views.

## Structural Alignment

- 删除 26121 夜景模式重复的‘变焦 / Zoom’，保留规范名称‘变焦’。
- 删除 26111 独立前后双录模式下的重复 Video EIS；前后双录能力归入视频模式。
- 将 26111 长时间无交互息屏移动到通用，与 26121 对齐。
- SAT 合并到变焦能力，不再保留独立算法行。
- 删除 HLG/HDR 汇总算法行，由逐规格视频行表达支持范围。
- TF SN / Super Night 合并到规范名称‘超级夜景’。
- 补齐人像模式 MFNR 与人脸畸变矫正算法行。

## Hidden In 26111


## Hidden In 26121

- 照片 / Photo / 前置自动小广角
- 照片 / Photo / Quality
- 运动 / Action / 脏污检测
- 视频 / Video / 脏污检测
- 夜景 / Night / Flash
- 夜景 / Night / Motion Photo cover HDR
- 夜景 / Night / 动态照片 - 无效信息截取
- 夜景 / Night / 动态照片-视频支持录制声音
- 夜景 / Night / 长按快门连拍 / Press and Hold Burst
- 夜景 / Night / 脏污检测
- 慢动作 / Slow Motion / Flash
- 慢动作 / Slow Motion / 脏污检测
- 延时摄影 / Timelapse / 脏污检测
- 全景 / Panorama / 脏污检测
- 专业 / Expert / 脏污检测
- 高像素 / High Resolution / 脏污检测

## Remaining Project-only Rows

### 26111

- 照片 / Photo / Hex Zoom
- 高像素 / High Resolution / 200MP Ultra

### 26121

- 高像素 / High Resolution / 50MP Ultra
