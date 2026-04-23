# 性能

- Source workbook: `/Users/travis.zhao/Downloads/Camera App SW 埋点 2025 v4.0.xlsx`
- Extracted rows: `9`

## Sheet Note

此表为针对每张照片的参数记录，可以理解为导出数据的每一行均需包含以下字段

## Table

| event_name | key | key_note | label | label_note | string_value | value_note | 默认值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NTCamera | pef_info | 相机性能埋点 | coldStart | 冷启动 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | hotStart | 热启动 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | capturePrepare | 快门响应完成app下发拍照请求 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | capture2Thumbnail | 小图刷新 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | capture2Photo | 大图刷新（JPEG） | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | click2RecordStart | 录制开始响应速度 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | click2RecordFinish | 结束录像响应速度 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | switchMode | 切换模式速度 | xx | 以ms为单位 | 无 |
| NTCamera | pef_info | 相机性能埋点 | switchCamera | 切换镜头速度 | xx | 以ms为单位 | 无 |
