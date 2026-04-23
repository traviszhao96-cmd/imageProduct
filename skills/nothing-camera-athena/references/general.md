# General

- Source workbook: `/Users/travis.zhao/Downloads/Camera App SW 埋点 2025 v4.0.xlsx`
- Extracted rows: `71`

## Sheet Note

此表为 Camera App 中用户的设置项选择，可针对每个字段导出单独的数据表

## Table

| event_name | key | event_note | string_value | value_note | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| NTCamera | activate_type | Camera App 启动类型 | 1 | 冷启动 | 无 | 启动相机时记录 |
| NTCamera | activate_type | Camera App 启动类型 | 2 | 热启动 | 无 | 启动相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 1 | 点击图标 | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 2 | 双击电源键 | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 3 | 第三方调用 | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 4 | 多任务 | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 5 | 锁屏长按 | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 6 | Shortcut Widget | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 7 | Xpand Widget | 无 | 进入相机时记录 |
| NTCamera | enter_method | 进入 Camera App 的方式 | 8 | unknown，区别于上述之外 | 无 | 进入相机时记录 |
| NTCamera | brightness_adjust | 进入相机后用户是否手动调节亮度 | xx | 调节前的亮度 | xx | 在用户每次手动调节屏幕亮度时记录 |
| NTCamera | brightness_adjust | 进入相机后用户是否手动调节亮度 | xx | 调节后的亮度 | xx | 在用户每次手动调节屏幕亮度时记录 |
| NTCamera | grid | 网格线——功能开关 | 0 | 关闭 | 0 | 点击开关时记录 |
| NTCamera | grid | 网格线——功能开关 | 1 | 打开 | 0 | 点击开关时记录 |
| NTCamera | shutter_sound | 快门声音——功能开关 | 0 | 关闭 | 1 | 点击开关时记录 |
| NTCamera | shutter_sound | 快门声音——功能开关 | 1 | 打开 | 1 | 点击开关时记录 |
| NTCamera | mirror_front | 镜像前置——功能开关 | 0 | 关闭 | 1 | 点击开关时记录 |
| NTCamera | mirror_front | 镜像前置——功能开关 | 1 | 打开 | 1 | 点击开关时记录 |
| NTCamera | qr_scan | 二维码扫描——功能开关 | 0 | 关闭 | 1 | 点击开关时记录 |
| NTCamera | qr_scan | 二维码扫描——功能开关 | 1 | 打开 | 1 | 点击开关时记录 |
| NTCamera | tap_shoot | 轻触拍照——功能开关 | 0 | 关闭 | 0 | 点击开关时记录 |
| NTCamera | tap_shoot | 轻触拍照——功能开关 | 1 | 打开 | 0 | 点击开关时记录 |
| NTCamera | save_location | 保存位置 | 0 | 将存储位置切换到sd card时上报 | 1 | 点击开关时记录 |
| NTCamera | save_location | 保存位置 | 1 | 将存储位置切换到 internal storage 时上报 | 1 | 点击开关时记录 |
| NTCamera | level | 水平辅助线——功能开关 | 0 | 关闭 | 0 | 点击开关时记录 |
| NTCamera | level | 水平辅助线——功能开关 | 1 | 打开 | 0 | 点击开关时记录 |
| NTCamera | watermark | 水印——功能开关 | 0 | 关闭 | 0 | 点击开关时记录 |
| NTCamera | watermark | 水印——功能开关 | 1 | 打开 | 0 | 点击开关时记录 |
| NTCamera | press_hold_shutter | 长按快门的操作 | 1 | Burst shot | 2 | 用户更改时记录 |
| NTCamera | press_hold_shutter | 长按快门的操作 | 2 | Record video | 2 | 用户更改时记录 |
| NTCamera | scene_detection | 场景检测——功能开关 | 0 | 关闭 | 1 | 点击开关时记录 |
| NTCamera | scene_detection | 场景检测——功能开关 | 1 | 打开 | 1 | 点击开关时记录 |
| NTCamera | recording_light | 录像指示灯——功能开关 | 0 | 关闭 | 1 | 点击开关时记录 |
| NTCamera | recording_light | 录像指示灯——功能开关 | 1 | 打开 | 1 | 点击开关时记录 |
| NTCamera | video_encoding | 视频编码 | 1 | H.264 | 1 | 用户更改时记录 |
| NTCamera | video_encoding | 视频编码 | 2 | H.265 | 1 | 用户更改时记录 |
| NTCamera | auto_fps | 视频自动帧率 | off | 关 | auto_30_60 | 用户更改时记录 |
| NTCamera | auto_fps | 视频自动帧率 | auto_30 | 自动 30 fps | auto_30_60 | 用户更改时记录 |
| NTCamera | auto_fps | 视频自动帧率 | auto_30_60 | 自动 30&60 fps | auto_30_60 | 用户更改时记录 |
| NTCamera | ultra_XDR | UHDR——功能开关 | 0 | 关闭 | 1 | 点击开关时记录 |
| NTCamera | ultra_XDR | UHDR——功能开关 | 1 | 打开 | 1 | 点击开关时记录 |
| NTCamera | quality | 照片画质 | 1 | 12MP | 1 | 用户更改时记录 |
| NTCamera | quality | 照片画质 | 2 | 50MP | 1 | 用户更改时记录 |
| NTCamera | mode_ps | 保留上次退出前使用的模式 | 0 | 关闭 | ? | 点击开关时记录 |
| NTCamera | mode_ps | 保留上次退出前使用的模式 | 1 | 打开 | ? | 点击开关时记录 |
| NTCamera | bokeh_ps | 人像模式，虚化程度的记忆 | 0 | 关闭 | ? | 点击开关时记录 |
| NTCamera | bokeh_ps | 人像模式，虚化程度的记忆 | 1 | 打开 | ? | 点击开关时记录 |
| NTCamera | filter_ps | 滤镜 | 0 | 关闭 | ? | 点击开关时记录 |
| NTCamera | filter_ps | 滤镜 | 1 | 打开 | ? | 点击开关时记录 |
| NTCamera | 50mp_ps | 50MP（用户反馈） | 0 | 关闭 | ? | 点击开关时记录 |
| NTCamera | 50mp_ps | 50MP（用户反馈） | 1 | 打开 | ? | 点击开关时记录 |
| NTCamera | lut_control | LUT 相关操作的次数统计 | 1 | 通过本地文件，导入一个 LUT，成功，记录一次 | 无 | 操作结束后记录 |
| NTCamera | lut_control | LUT 相关操作的次数统计 | 0 | 通过本地文件，导入一个 LUT，失败，记录一次 | 无 | 操作结束后记录 |
| NTCamera | macro_fb_ctrl | 在预览时对微距控制开关的操作 | 0 | 用户手动点击关闭，上报一次 | 无 | 点击相关操作时记录 |
| NTCamera | macro_fb_ctrl | 在预览时对微距控制开关的操作 | 1 | 用户手动开启，上报一次 | 无 | 点击相关操作时记录 |
| NTCamera | google_lens | 用户点击调用Google lens | 1 | 点击一次 google lens，上报一次 | 无 | 点击相关操作时记录 |
| NTCamera | enter_mode | 用户冷启动进入 camera 的默认模式 | 0 | 默认的 Photo 模式（Origin Preset） | 0 | 进入相机时记录 |
| NTCamera | enter_mode | 用户冷启动进入 camera 的默认模式 | 1 | Default Preset （冷启动后直接应用用户提前预选的 Preset） | 0 | 进入相机时记录 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 | 1 | 用户手动创建一个 Preset 并点击 save 后创建成功，记录一次 | 无 | 点击相关操作时记录 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 | 2 | 用户删除掉一个 Preset 后，记录一次 | 无 | 点击相关操作时记录 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 | 3 | 用户恢复删除的官方预设 | 无 | 点击相关操作时记录 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 | 4 | 用户点击创建预设进入预设创建界面 | 无 | 点击相关操作时记录 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 | 5 | 用户在预设创建界面给预设添加封面 | 无 | 点击相关操作时记录 |
| NTCamera | preset_create | Preset 分享的次数统计 | 1 | 用户分享 Preset，生成二维码，成功，记录一次 | 无 | 操作结束后记录 |
| NTCamera | preset_create | Preset 分享的次数统计 | 2 | 用户分享 Preset，生成二维码，失败，记录一次 | 无 | 操作结束后记录 |
| NTCamera | preset_import | Preset 导入的次数统计 | 1 | 用户导入 Preset，成功，记录一次 | 无 | 操作结束后记录 |
| NTCamera | preset_import | Preset 导入的次数统计 | 2 | 用户导入 Preset，失败，记录一次 | 无 | 操作结束后记录 |
| NTCamera | preset_import | Preset 导入的次数统计 | xx | 用户导入 Preset成功上报，有网络上报 Preset 的下载 link，无网络则上报datamap | 无 | 操作结束后记录 |
| NTCamera | preset_save | Preset 快速保存使用统计 | 1 | 用户点击preset保存按键时上报 | 无 | 点击相关操作时记录 |
| NTCamera | preset_save | Preset 快速保存使用统计 | 2 | 选择覆盖原preset上报 | 无 | 点击相关操作时记录 |
| NTCamera | preset_save | Preset 快速保存使用统计 | 3 | 选择存为新preset上报 | 无 | 点击相关操作时记录 |
