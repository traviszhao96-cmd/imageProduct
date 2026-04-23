# Photo

- Source workbook: `/Users/travis.zhao/Downloads/Camera App SW 埋点 2025 v4.0.xlsx`
- Extracted rows: `83`

## Sheet Note

此表为针对每张照片的参数记录，可以理解为导出数据的每一行均需包含以下字段

## Table

| event_name | key | key_note | label | label_note | string_value | value_note | 默认值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | photo | Photo 照片 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | expert | Expert 专业 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | protrait | Portrait 人像 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | pano | Pano 全景 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | macro | 微距模式。使用独立镜头，或者是长焦镜头，拍摄微距 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | video_shot | 视频中点击快门进行拍照 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | night | 夜景模式 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | photoMode | 在哪个模式拍摄的照片 | action | 运动模式 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exposure_adjust | 拍摄前用户是否手动调节曝光<br>这个动作发生在按下快门前，但是成片曝光受此影响 | 0 | 未调节 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exposure_adjust | 拍摄前用户是否手动调节曝光<br>这个动作发生在按下快门前，但是成片曝光受此影响 | 1 | 调节 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exposure_new | 用户手动调节后的曝光值 | xx | 曝光值，用正负数表示，如-0.5，+0.3 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | timer | 倒计时选项 | 0 | 无倒计时 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | timer | 倒计时选项 | 3 | 3s | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | timer | 倒计时选项 | 10 | 10s | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | autotone | 色彩模式的选择 | 0 | Off | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | autotone | 色彩模式的选择 | 1 | Vivid | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | filter | 滤镜的选择<br>因为滤镜改动频繁，直接报滤镜英文名 | 0 | 无滤镜 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | filter | 滤镜的选择<br>因为滤镜改动频繁，直接报滤镜英文名 | xxx | 滤镜名称 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | filter_strength | 滤镜强度 | 0-10.0 | 对应滤镜调节强度 | 10 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_apply | 对「调色」功能的对应操作 | 0/1 | 拍摄的这张照片是否开启 调色 功能。0代表不应用，1代表应用 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_contrast | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「对比度」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_saturation | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「饱和度」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_warmth | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色温」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_tint | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色调」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_shapen | 对「调色」功能的对应操作 | 0～10.0 | 对应「锐度」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_grain | 对「调色」功能的对应操作 | 0～10.0 | 对应「噪点」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_vignette | 对「调色」功能的对应操作 | 0～10.0 | 对应「暗角」的具体参数值 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | ratio | 画幅比例的选择 | 1 | 4：3 | 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | ratio | 画幅比例的选择 | 2 | 16：9 | 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | ratio | 画幅比例的选择 | 3 | Full | 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | ratio | 画幅比例的选择 | 4 | 1：1 | 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | motion | 动态照片的选择 | 0 | 关闭 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | motion | 动态照片的选择 | 1 | 打开 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | watermark | 水印开关，使用的水印风格 | 0 | 关闭 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | watermark | 水印开关，使用的水印风格 | 1 | 文字水印 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | watermark | 水印开关，使用的水印风格 | 2 | 画框水印 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | camera_id | 照片由哪颗镜头拍摄 | 0 | 主摄，后置广角 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | camera_id | 照片由哪颗镜头拍摄 | 1 | 前置镜头 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | camera_id | 照片由哪颗镜头拍摄 | 2 | 后置超广 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | camera_id | 照片由哪颗镜头拍摄 | 3 | 后置长焦 | 无 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | zoom_ratio | 变焦倍数（基于设备的后置广角而言） | xx | 基于 1 的数值，如 1.2、1.5 | 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | image_quality | 是否采用高像素拍摄 | 0 | 12MP | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | image_quality | 是否采用高像素拍摄 | 1 | 50MP 108MP 200MP等具体高像素 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | glyph_mirror | 是否开启了glyph_mirro拍摄 | 0 | 关 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | glyph_mirror | 是否开启了glyph_mirro拍摄 | 1 | 开 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 0 | 闪光灯关闭 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 1 | 闪光灯强制开 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 2 | 闪光灯常亮 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 3 | Glyph 补光 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | retouching | 美颜程度的选择 | 0 | Off | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | retouching | 美颜程度的选择 | 1 | Natural | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | retouching | 美颜程度的选择 | 2 | Strong | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | bokeh | 虚化程度的选择 | xx | 按照实际值记录 | 5.6 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | effects | 光斑效果的选择 | 0 | 无 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | effects | 光斑效果的选择 | 1 | 天鹅绒：Velvet | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | effects | 光斑效果的选择 | 2 | 旋焦：Twist | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | effects | 光斑效果的选择 | 3 | 五角星：Pentacle | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | effects | 光斑效果的选择 | 4 | 雪花：Snowflake | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | nightmode | 是否使用自动夜景模式 | 0 | 未检测到，自动关闭 | 未检测到为 0<br>检测到为 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | nightmode | 是否使用自动夜景模式 | 1 | 自动打开 | 未检测到为 0<br>检测到为 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | nightmode | 是否使用自动夜景模式 | 2 | 手动关闭 | 未检测到为 0<br>检测到为 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | macro_fb | 是否使用fallback微距模式 | 0 | 未检测到，自动关闭 | 未检测到为 0 检测到为 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | macro_fb | 是否使用fallback微距模式 | 1 | 触发，且开启时拍摄 | 未检测到为 0 检测到为 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | macro_fb | 是否使用fallback微距模式 | 2 | 触发，并手动关闭后拍摄 | 未检测到为 0 检测到为 1 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | hdr | hdr 开关的选择，及拍摄时是否开启 | 0 | 手动关闭 | 无，默认为自动检测 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | hdr | hdr 开关的选择，及拍摄时是否开启 | 1 | 自动-关闭 | 无，默认为自动检测 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | hdr | hdr 开关的选择，及拍摄时是否开启 | 2 | 自动-打开 | 无，默认为自动检测 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | hdr | hdr 开关的选择，及拍摄时是否开启 | 3 | 强制打开 | 无，默认为自动检测 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | raw | 在 Expert 模式中是否开启 raw 格式拍照 | 0 | 关闭 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | raw | 在 Expert 模式中是否开启 raw 格式拍照 | 1 | 打开 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exposure | 曝光补偿的调节值 | xxx | 真实数值，如 +-0.3 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | preset | 拍摄照片时应用的preset名称 | 0 | 未应用preset | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | preset | 拍摄照片时应用的preset名称 | xxx | 对应的preset名称 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | shot_algo | 拍摄照片时使用的算法名称 | xxx | 具体的算法名称 | xxx |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | if_moon | 是否使用月亮模式 | 0/1 | 0代表没有，1代表有 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | frame_count | 取帧数量 | xxx | 具体的取帧数量 | xxx |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exp_time | 每一帧的曝光的具体曝光时间 |   | 具体的曝光时间 | xxx |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | lux | 拍照时的环境亮度 | xxx | 具体的亮度值 | xxx |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | adrc | 拍照时的DRC值，代表动态范围 | xxx | 具体的DRC值 | xxx |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | cct | 拍照时的色温值 | xxx | 具体的色温值 | xxx |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | face_count | 人脸数量 | xxx | 具体的人脸数量 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | orientation | 拍摄照片时，手机的方向状态 | 0 | vertical，竖屏状态 | 0 |
| NTCamera | photo_info | 单张照片所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | orientation | 拍摄照片时，手机的方向状态 | 1 | horizontal，横屏状态 | 0 |
