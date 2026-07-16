# Camera App SW 埋点 2026 v5.0 (含历史备注)

> Source: https://nothing-tech.sg.larksuite.com/wiki/NMt0wr2Q2iTWevkSc0hlFcBAgJg
> 含备注表: https://nothing-tech.sg.larksuite.com/base/N2azb9muvaqqmwsIB7IlPmFGgpg?table=tblh05JLoheZIXfr
> Records: 213, 历史备注: 13
> 本地增量同步日期: 2026-07-16

## 历史拼写兼容

| 原值 | 正确拼写 | 说明 |
| --- | --- | --- |
| protrait | portrait | photoMode string_value |
| tuning_shapen | tuning_sharpen | 锐度 label |
| glyph_mirro | glyph_mirror | label_note 描述 |
| pef_info | perf_info | key 字段名 |

| event_name | key | key_note | label | label_note | string_value | value_note | 默认值 | 备注 | 当前状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | photo | Photo 照片 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | expert | Expert 专业 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | protrait | Portrait 人像 | 无 | 疑似拼写错误，正确应为 portrait，系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | pano | Pano 全景 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | macro | 微距模式。使用独立镜头，或者是长焦镜头，拍摄微距 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | video_shot | 视频中点击快门进行拍照 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | night | 夜景模式 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | photoMode | 在哪个模式拍摄的照片 | action | 运动模式 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | exposure_adjust | 拍摄前用户是否手动调节曝光 这个动作发生在按下快门前,但是成片曝光受此影响 | 0 | 未调节 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | exposure_adjust | 拍摄前用户是否手动调节曝光 这个动作发生在按下快门前,但是成片曝光受此影响 | 1 | 调节 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | exposure_new | 用户手动调节后的曝光值 | xx | 曝光值，用正负数表示，如-0.5，+0.3 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | timer | 倒计时选项 | 0 | 无倒计时 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | timer | 倒计时选项 | 3 | 3s | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | timer | 倒计时选项 | 10 | 10s | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | autotone | 色彩模式的选择 | 0 | Off | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | autotone | 色彩模式的选择 | 1 | Vivid | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | filter | 滤镜的选择 因为滤镜改动频繁,直接报滤镜英文名 | 0 | 无滤镜 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | filter | 滤镜的选择 因为滤镜改动频繁,直接报滤镜英文名 | xxx | 滤镜名称 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | filter_strength | 滤镜强度 | 0-10.0 | 对应滤镜调节强度 | 10 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_apply | 对「调色」功能的对应操作 | 0/1 | 拍摄的这张照片是否开启 调色 功能。0代表不应用，1代表应用 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_contrast | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「对比度」的具体参数值 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_saturation | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「饱和度」的具体参数值 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_warmth | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色温」的具体参数值 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_tint | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色调」的具体参数值 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_shapen | 对「调色」功能的对应操作 | 0～10.0 | 对应「锐度」的具体参数值 | 0 | 疑似拼写错误，正确应为 tuning_sharpen（锐度），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_grain | 对「调色」功能的对应操作 | 0～10.0 | 对应「噪点」的具体参数值 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | tuning_vignette | 对「调色」功能的对应操作 | 0～10.0 | 对应「暗角」的具体参数值 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | ratio | 画幅比例的选择 | 1 | 4：3 | 1 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | ratio | 画幅比例的选择 | 2 | 16：9 | 1 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | ratio | 画幅比例的选择 | 3 | Full | 1 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | ratio | 画幅比例的选择 | 4 | 1：1 | 1 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | motion | 动态照片的选择 | 0 | 关闭 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | motion | 动态照片的选择 | 1 | 打开 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | watermark | 水印开关,使用的水印风格 | 0 | 关闭 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | watermark | 水印开关,使用的水印风格 | 1 | 文字水印 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | watermark | 水印开关,使用的水印风格 | 2 | 画框水印 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | camera_id | 照片由哪颗镜头拍摄 | 0 | 主摄，后置广角 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | camera_id | 照片由哪颗镜头拍摄 | 1 | 前置镜头 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | camera_id | 照片由哪颗镜头拍摄 | 2 | 后置超广 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | camera_id | 照片由哪颗镜头拍摄 | 3 | 后置长焦 | 无 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | zoom_ratio | 变焦倍数（基于设备的后置广角而言） | xx | 基于 1 的数值，如 1.2、1.5 | 1 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | image_quality | 是否采用高像素拍摄 | 0 | 12MP | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | image_quality | 是否采用高像素拍摄 | 1 | 50MP 108MP 200MP等具体高像素 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | glyph_mirror | 是否开启了glyph_mirro拍摄 | 0 | 关 | 0 | label_note 中 glyph_mirro 缺字母 r，正确应为 glyph_mirror，系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | glyph_mirror | 是否开启了glyph_mirro拍摄 | 1 | 开 | 0 | label_note 中 glyph_mirro 缺字母 r，正确应为 glyph_mirror，系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | flash | 闪光灯模式选择 | 0 | 闪光灯关闭 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | flash | 闪光灯模式选择 | 1 | 闪光灯强制开 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | flash | 闪光灯模式选择 | 2 | 闪光灯常亮 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | flash | 闪光灯模式选择 | 3 | Glyph 补光 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | retouching | 美颜程度的选择 | 0 | Off | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | retouching | 美颜程度的选择 | 1 | Natural | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | retouching | 美颜程度的选择 | 2 | Strong | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | bokeh | 虚化程度的选择 | xx | 按照实际值记录 | 5.6 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | effects | 光斑效果的选择 | 0 | 无 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | effects | 光斑效果的选择 | 1 | 天鹅绒：Velvet | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | effects | 光斑效果的选择 | 2 | 旋焦：Twist | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | effects | 光斑效果的选择 | 3 | 五角星：Pentacle | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | effects | 光斑效果的选择 | 4 | 雪花：Snowflake | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | nightmode | 是否使用自动夜景模式 | 0 | 未检测到，自动关闭 | 0 | 未检测到为 0 检测到为 1 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | nightmode | 是否使用自动夜景模式 | 1 | 自动打开 | 0 | 未检测到为 0 检测到为 1 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | nightmode | 是否使用自动夜景模式 | 2 | 手动关闭 | 0 | 未检测到为 0 检测到为 1 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | macro_fb | 是否使用fallback微距模式 | 0 | 未检测到，自动关闭 | 0 | 未检测到为 0 检测到为 1 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | macro_fb | 是否使用fallback微距模式 | 1 | 触发，且开启时拍摄 | 0 | 未检测到为 0 检测到为 1 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | macro_fb | 是否使用fallback微距模式 | 2 | 触发，并手动关闭后拍摄 | 0 | 未检测到为 0 检测到为 1 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | ai_zoom | 20x以上触发长焦aigc增强后,是否手动关闭 | 0 | 触发，手动关闭拍摄 | off/1 |  | 待开发 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | ai_zoom | 20x以上触发长焦aigc增强后,是否手动关闭 | 1 | 触发，且开启时拍摄 | off/1 |  | 待开发 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | hdr | hdr 开关的选择,及拍摄时是否开启 | 0 | 手动关闭 | 无，默认为自动检测 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | hdr | hdr 开关的选择,及拍摄时是否开启 | 1 | 自动-关闭 | 无，默认为自动检测 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | hdr | hdr 开关的选择,及拍摄时是否开启 | 2 | 自动-打开 | 无，默认为自动检测 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | hdr | hdr 开关的选择,及拍摄时是否开启 | 3 | 强制打开 | 无，默认为自动检测 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | raw | 在 Expert 模式中是否开启 raw 格式拍照 | 0 | 关闭 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | raw | 在 Expert 模式中是否开启 raw 格式拍照 | 1 | 打开 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | exposure | 曝光补偿的调节值 | xxx | 真实数值，如 +-0.3 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | preset | 拍摄照片时应用的preset名称 | 0 | 未应用preset | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | preset | 拍摄照片时应用的preset名称 | xxx | 对应的preset名称 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | shot_algo | 拍摄照片时使用的算法名称 | xxx | 具体的算法名称 | xxx |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | if_moon | 是否使用月亮模式 | 0/1 | 0代表没有，1代表有 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | frame_count | 取帧数量 | xxx | 具体的取帧数量 | xxx |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | exp_time | 每一帧的曝光的具体曝光时间 | xxx, xxx, ... | 上报每一帧的具体曝光时间，整合成数组上报 | xxx |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | lux | 拍照时的环境亮度 | xxx | 具体的亮度值 | xxx |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | adrc | 拍照时的DRC值,代表动态范围 | xxx | 具体的DRC值 | xxx |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | cct | 拍照时的色温值 | xxx | 具体的色温值 | xxx |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | face_count | 人脸数量,上报具体人脸数量 | xxx | 具体的人脸数量 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | face_ratio | 人脸占比,横纵方向 | [[heightRatio,widthRatio],[heightRatio,widthRatio]...] | 二维数组记录，heightRatio 为 纵方向在整个预览框占比（0-1， 保留两位小数），widthRatio 同上 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | orientation | 拍摄照片时,手机的方向状态 | 0 | vertical，竖屏状态 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | orientation | 拍摄照片时,手机的方向状态 | 1 | horizontal，横屏状态 | 0 |  | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | flicker_sensor_output | 拍照时 Flicker sensor 输出的光源频率值，对应代码变量 m_currentLightFrequency | xxx | Flicker sensor 原始数值，如 0, 100, 120, 240 等 | 0 | 2026-06-17 新增 | 待开发 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | motion_level | 当前场景检测到的运动速度等级，对应代码变量 m_currentMotionLevel。拍照模式下触发运动抓拍时上报 | xxx | 运动速度等级的具体数值 | 0 | 2026-06-17 新增，原计划整合到 shot_algo，经讨论改为独立 key | 待开发 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | video_mode | 在哪个模式拍摄的视频 | 1 | Video | 无 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | video_mode | 在哪个模式拍摄的视频 | 2 | Slo-mo | 无 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | video_mode | 在哪个模式拍摄的视频 | 3 | Time-lapse | 无 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | video_mode | 在哪个模式拍摄的视频 | 4 | 前后双录 (Dual Recording) | 无 | 2026-06-25 新增 | 待开发 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | dual_split | 前后双录的拼接方式 | top_bottom / pip | 上下分屏 / 画中画 | 0 | 2026-06-25 新增 | 待开发 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | dual_lens | 前后双录的镜头组合（数字编码，见 camera_id） | 1+0 / 1+2 | 前置+主摄 / 前置+超广角 | 0 | 2026-06-25 新增 | 待开发 |
| NTCamera | photo_info | 拍照成片时上报参数 | ai_scene | 拍照时 AI 场景识别结果 | xxx | 上报算法识别的场景类型或枚举值 | none | 2026-07-16 新增 | 待开发 |
| NTCamera | photo_info | 拍照成片时上报参数 | gyro_level | 拍照时陀螺仪检测到的运动等级 | xxx | 陀螺仪运动等级的具体数值 | 0 | 2026-07-16 新增 | 待开发 |
| NTCamera | photo_info | 拍照成片时上报参数 | face_luma_ratio | 拍照时人脸区域亮度与画面亮度的比值 | xxx | 上报实际比值，具体精度以算法输出为准 | 0 | 2026-07-16 新增 | 待开发 |
| NTCamera | photo_info | 拍照成片时上报参数 | ISO | 拍照时的感光度（ISO） | xxx | 实际 ISO 数值，如 100、400、1600 | xxx | 2026-07-16 新增 | 待开发 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | exposure_adjust | 该视频中,用户是否手动调节曝光 可发生在按下快门前 只要曝光调节对成片产生影响就记录 | 0 | 未调节 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | exposure_adjust | 该视频中,用户是否手动调节曝光 可发生在按下快门前 只要曝光调节对成片产生影响就记录 | 1 | 调节 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | video_length | 视频拍摄时长 | xx | 以秒为单位 | 无 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | nightmode | 是否使用自动夜景模式 | 0 | 自动关闭 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | nightmode | 是否使用自动夜景模式 | 1 | 手动打开 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | hdr | hdr开启 HDR 功能（新项目以下线） | 0 | 关闭 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | hdr | hdr开启 HDR 功能（新项目以下线） | 1 | 打开 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | action_mode | 防抖模式 | 0 | 关闭 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | action_mode | 防抖模式 | 1 | 打开 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | flash | 闪光灯模式选择 | 0 | 闪光灯关闭 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | flash | 闪光灯模式选择 | 2 | 闪光灯常亮 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | flash | 闪光灯模式选择 | 3 | Glyph 补光 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 1 | 1080p-30 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 2 | 1080p-60 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 3 | 4k-30 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 4 | 4k-60 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 5 | 1080p-120 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 6 | 1080p-240 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 7 | 1080p-480 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 8 | 4k-120 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 9 | 1080 | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | quality | 清晰度&帧率 直接用 value_note 的值 | 10 | 4k | video 为 2 slo-mo 为 5 time-lapse 为 9 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | if_HLG | 是否使用HDR规格录制,以及录制时使用的HDR格式 | 0 | 未使用HDR录制 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | if_HLG | 是否使用HDR规格录制,以及录制时使用的HDR格式 | 1 | 使用HDR录制，且为HLG格式 | 0 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | Rec_light | 在录制时是否开启了录影灯 | 0 | 关闭录影灯 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | Rec_light | 在录制时是否开启了录影灯 | 1 | 开启录影灯（默认） | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 1 | 15 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 2 | 30 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 3 | 60 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 4 | 120 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 5 | 240 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 6 | 480 | 1 |  | 已上线 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | speed | 延时摄影的速度 直接用 value_note 的值 | 7 | 960 | 1 |  | 已上线 |
| NTCamera | activate_type | Camera App 启动类型 |  |  | 1 | 冷启动 | 无 | 启动相机时记录 | 已上线 |
| NTCamera | activate_type | Camera App 启动类型 |  |  | 2 | 热启动 | 无 | 启动相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 1 | 点击图标 | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 2 | 双击电源键 | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 3 | 第三方调用 | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 4 | 多任务 | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 5 | 锁屏长按 | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 6 | Shortcut Widget | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 7 | Xpand Widget | 无 | 进入相机时记录 | 已上线 |
| NTCamera | enter_method | 进入 Camera App 的方式 |  |  | 8 | unknown，区别于上述之外 | 无 | 进入相机时记录 | 已上线 |
| NTCamera | brightness_adjust | brightness_adjust 事件上报的参数集合。 | brightness_if_adjust | 进入相机后用户是否手动调节亮度 | 0 | 未调节 | 0 | 这三个记录在同一事件中 名称为： brightness_adjust | 已上线 |
| NTCamera | brightness_adjust | brightness_adjust 事件上报的参数集合。 | brightness_if_adjust | 进入相机后用户是否手动调节亮度 | 1 | 调节 | 0 | 这三个记录在同一事件中 名称为： brightness_adjust | 已上线 |
| NTCamera | brightness_adjust | brightness_adjust 事件上报的参数集合。 | brightness_auto | 进入相机时读取到的系统亮度值 or 理解为这时的自动亮度值 | xx | 亮度值 | 无 | 这三个记录在同一事件中 名称为： brightness_adjust | 已上线 |
| NTCamera | brightness_adjust | brightness_adjust 事件上报的参数集合。 | brightness_new | 用户手动调节后的亮度值与上述项的差值 | xx | 差值 正值表示用户增加亮度 负值表示用户调暗亮度 | 无 | 这三个记录在同一事件中 名称为： brightness_adjust | 已上线 |
| NTCamera | grid | 网格线——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | grid | 网格线——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | shutter_sound | 快门声音——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | shutter_sound | 快门声音——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | mirror_front | 镜像前置——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | mirror_front | 镜像前置——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | qr_scan | 二维码扫描——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | qr_scan | 二维码扫描——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | tap_shoot | 轻触拍照——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | tap_shoot | 轻触拍照——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | save_location | 保存位置 |  |  | 0 | 将存储位置切换到sd card时上报 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | save_location | 保存位置 |  |  | 1 | 将存储位置切换到 internal storage 时上报 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | level | 水平辅助线——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | level | 水平辅助线——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | watermark | 水印——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | watermark | 水印——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 | 已上线 |
| NTCamera | press_hold_shutter | 长按快门的操作 |  |  | 1 | Burst shot | 2 | 用户更改时记录 | 已上线 |
| NTCamera | press_hold_shutter | 长按快门的操作 |  |  | 2 | Record video | 2 | 用户更改时记录 | 已上线 |
| NTCamera | scene_detection | 场景检测——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | scene_detection | 场景检测——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | recording_light | 录像指示灯——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | recording_light | 录像指示灯——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | video_encoding | 视频编码 |  |  | 1 | H.264 | 1 | 用户更改时记录 | 已上线 |
| NTCamera | video_encoding | 视频编码 |  |  | 2 | H.265 | 1 | 用户更改时记录 | 已上线 |
| NTCamera | ultra_XDR | UHDR——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | ultra_XDR | UHDR——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 | 已上线 |
| NTCamera | quality | 照片画质 |  |  | 1 | 12MP | 1 | 用户更改时记录 | 已上线 |
| NTCamera | quality | 照片画质 |  |  | 2 | 50MP | 1 | 用户更改时记录 | 已上线 |
| NTCamera | mode_ps | 保留上次退出前使用的模式 |  |  | 0 | 关闭 | ? | 点击开关时记录 | 已上线 |
| NTCamera | mode_ps | 保留上次退出前使用的模式 |  |  | 1 | 打开 | ? | 点击开关时记录 | 已上线 |
| NTCamera | bokeh_ps | 人像模式,虚化程度的记忆 |  |  | 0 | 关闭 | ? | 点击开关时记录 | 已上线 |
| NTCamera | bokeh_ps | 人像模式,虚化程度的记忆 |  |  | 1 | 打开 | ? | 点击开关时记录 | 已上线 |
| NTCamera | filter_ps | 滤镜 |  |  | 0 | 关闭 | ? | 点击开关时记录 | 已上线 |
| NTCamera | filter_ps | 滤镜 |  |  | 1 | 打开 | ? | 点击开关时记录 | 已上线 |
| NTCamera | 50mp_ps | 50MP（用户反馈） |  |  | 0 | 关闭 | ? | 点击开关时记录 | 已上线 |
| NTCamera | 50mp_ps | 50MP（用户反馈） |  |  | 1 | 打开 | ? | 点击开关时记录 | 已上线 |
| NTCamera | lut_control | LUT 相关操作的次数统计 |  |  | 0 | 通过本地文件，导入一个 LUT，成功，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | lut_control | LUT 相关操作的次数统计 |  |  | 1 | 通过本地文件，导入一个 LUT，失败，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | enter_mode | 用户冷启动进入 camera 的默认模式 |  |  | 0 | 默认的 Photo 模式（Origin Preset） | 0 | 进入相机时记录 | 已上线 |
| NTCamera | enter_mode | 用户冷启动进入 camera 的默认模式 |  |  | 1 | Default Preset （冷启动后直接应用用户提前预选的 Preset） | 0 | 进入相机时记录 | 已上线 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 |  |  | 1 | 用户手动创建一个 Preset 并点击 save 后创建成功，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 |  |  | 2 | 用户删除掉一个 Preset 后，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 |  |  | 3 | 用户恢复删除的官方预设 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_create | Preset 分享的次数统计 |  |  | 1 | 用户分享 Preset，生成二维码，成功，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_create | Preset 分享的次数统计 |  |  | 2 | 用户分享 Preset，生成二维码，失败，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_import | Preset 导入的次数统计 |  |  | 1 | 用户导入 Preset，成功，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_import | Preset 导入的次数统计 |  |  | 2 | 用户导入 Preset，失败，记录一次 | 无 | 操作结束后记录 | 已上线 |
| NTCamera | preset_import | Preset 导入的次数统计 |  |  | xx | 用户导入 Preset成功上报，有网络上报 Preset 的下载 link，无网络则上报datamap | 无 | 操作结束后记录 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | coldStart | 冷启动 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | hotStart | 热启动 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | capturePrepare | 快门响应完成app下发拍照请求 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | capture2Thumbnail | 小图刷新 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | capture2Photo | 大图刷新（JPEG） | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | click2RecordStart | 录制开始响应速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | click2RecordFinish | 结束录像响应速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | switchMode | 切换模式速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | pef_info | 相机性能埋点 | switchCamera | 切换镜头速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 | 已上线 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | event_timestamp_local | 用户本地时间戳，带时区偏移，用于直接查询用户操作时间。每次按下拍照快门并成功产出一张照片时上报。 | 2026-04-27T15:13:00+08:00 | ISO 8601 格式，如 2026-04-27T15:13:00+08:00 | 无 |  | 已上线 |
| NTCamera | video_info |  | event_timestamp_local | 用户本地时间戳，带时区偏移，用于直接查询用户操作时间。每次停止录制并成功生成一个视频时上报。 | 2026-04-27T15:13:00+08:00 | ISO 8601 格式，如 2026-04-27T15:13:00+08:00 | 无 |  | 已上线 |
| NTCamera | auto_fps | 视频自动帧率——功能开关 |  |  | off | 关 | 1 | 用户更改时记录 | 待开发 |
| NTCamera | auto_fps | 视频自动帧率——功能开关 |  |  | auto_30 | 自动30fps | 1 | 用户更改时记录 | 待开发 |
| NTCamera | auto_fps | 视频自动帧率——功能开关 |  |  | auto_30_60 | 自动30&60fps | 1 | 用户更改时记录 | 待开发 |
| NTCamera | lock_lens | 锁定镜头——功能开关 |   |  | 0 | 关闭 | 0 | 点击开关时记录 | 待开发 |
| NTCamera | lock_lens | 锁定镜头——功能开关 |   |  | 1 | 打开 | 0 | 点击开关时记录 | 待开发 |
|  |  |  |  |  |  |  |  |  | 待开发 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | doc_mode | 是否使用文档模式 | 0 | 未检测到，自动关闭 | 0 | 未检测到为 0 | 待开发 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | doc_mode | 是否使用文档模式 | 1 | 自动打开 | 0 | 检测到，并且拍摄 为 1 | 待开发 |
| NTCamera | photo_info | 每次按下拍照快门并成功产出一张照片时上报,记录该照片对应参数,包含拍摄前和拍摄中的临时必要操作。 | doc_mode | 是否使用文档模式 | 2 | 手动关闭 | 0 | 检测到，但是用户关闭拍摄 为 2 | 待开发 |

---

## 修改记录 (Changelog)

| 日期 | 版本 | 类型 | 变更项 | 变更前 | 变更后 | 影响范围 | 作者 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-17 | v5.2 | 新增 | photo_info 新增 label `flicker_sensor_output` | 无（此前误命名为 flicker_freq，已废弃） | 新增光源频率字段，对应代码变量 m_currentLightFrequency，值为 Flicker sensor 原始数值（如 0, 100, 120, 240） | photo_info | Maico / Travis / Zhongmin |
| 2026-06-17 | v5.2 | 新增 | photo_info 新增 label `motion_level` | 无（原计划整合到 shot_algo，经讨论改为独立 key） | 新增运动速度等级字段，对应代码变量 m_currentMotionLevel | photo_info | Maico / Travis / Zhongmin |
| 2026-07-16 | v5.3 | 新增 | photo_info 新增 4 个拍摄参数 | 无 | 新增 `ai_scene`、`gyro_level`、`face_luma_ratio`、`ISO` | photo_info | Travis Zhao |
