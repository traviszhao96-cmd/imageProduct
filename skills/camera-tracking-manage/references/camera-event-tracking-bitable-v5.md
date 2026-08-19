# Camera App SW 埋点（在线快照）

> Source: https://nothing-tech.sg.larksuite.com/base/N2azb9muvaqqmwsIB7IlPmFGgpg?table=tblh05JLoheZIXfr
> 拉取日期: 2026-08-19
> Records: 254

| event_name | key | key_note | label | label_note | string_value | value_note | 默认值 | 备注 | 当前状态 | 软件版本 |
|---|---|---|---|---|---|---|---|---|---|---|
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | photo | Photo 照片 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | expert | Expert 专业 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | protrait | Portrait 人像 | 无 | 存在拼写错误，正确应为 portrait，系历史遗留，实现时保持原值 |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | pano | Pano 全景 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | macro | 微距模式。使用独立镜头，或者是长焦镜头，拍摄微距 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | video_shot | 视频中点击快门进行拍照 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | night | 夜景模式 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | photoMode | 拍摄模式 | action | 运动模式 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | exposure_adjust | 拍摄前用户是否手动调节曝光<br>这个动作发生在按下快门前,但是成片曝光受此影响 | 0 | 未调节 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | exposure_adjust | 拍摄前用户是否手动调节曝光<br>这个动作发生在按下快门前,但是成片曝光受此影响 | 1 | 调节 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | exposure_new | 用户手动调节后的曝光值 | xx | 曝光值，用正负数表示，如-0.5，+0.3 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | timer | 倒计时选项 | 0 | 无倒计时 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | timer | 倒计时选项 | 3 | 3s | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | timer | 倒计时选项 | 10 | 10s | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | autotone | 色彩模式的选择 | 0 | Off | 0 |  |  |  |
| NTCamera | photo_info | 拍照成片时上报参数 | autotone | 色彩模式的选择 | 1 | Vivid | 0 |  |  |  |
| NTCamera | photo_info | 拍照成片时上报参数 | filter | 滤镜的选择<br>因为滤镜改动频繁,直接报滤镜英文名 | 0 | 无滤镜 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | filter | 滤镜的选择<br>因为滤镜改动频繁,直接报滤镜英文名 | xxx | 滤镜名称 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | filter_strength | 滤镜强度 | 0-10.0 | 对应滤镜调节强度 | 10 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_apply | 对「调色」功能的对应操作 | 0/1 | 拍摄的这张照片是否开启 调色 功能。0代表不应用，1代表应用 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_contrast | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「对比度」的具体参数值 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_saturation | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「饱和度」的具体参数值 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_warmth | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色温」的具体参数值 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_tint | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色调」的具体参数值 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_shapen | 对「调色」功能的对应操作 | 0～10.0 | 对应「锐度」的具体参数值 | 0 | 拼写错误，正确应为 tuning_sharpen（锐度），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_grain | 对「调色」功能的对应操作 | 0～10.0 | 对应「噪点」的具体参数值 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | tuning_vignette | 对「调色」功能的对应操作 | 0～10.0 | 对应「暗角」的具体参数值 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | ratio | 画幅比例的选择 | 1 | 4：3 | 1 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | ratio | 画幅比例的选择 | 2 | 16：9 | 1 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | ratio | 画幅比例的选择 | 3 | Full | 1 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | ratio | 画幅比例的选择 | 4 | 1：1 | 1 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | motion | 动态照片的选择 | 0 | 关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | motion | 动态照片的选择 | 1 | 打开 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | watermark | 水印开关,使用的水印风格 | 0 | 关闭 | 0 |  |  | Camera 3.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | watermark | 水印开关,使用的水印风格 | 1 | 文字水印 | 0 |  |  | Camera 3.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | watermark | 水印开关,使用的水印风格 | 2 | 画框水印 | 0 |  |  | Camera 3.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | camera_id | 照片由哪颗镜头拍摄 | 0 | 主摄，后置广角 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | camera_id | 照片由哪颗镜头拍摄 | 1 | 前置镜头 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | camera_id | 照片由哪颗镜头拍摄 | 2 | 后置超广 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | camera_id | 照片由哪颗镜头拍摄 | 3 | 后置长焦 | 无 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | zoom_ratio | 变焦倍数（基于设备的后置广角而言） | xx | 基于 1 的数值，如 1.2、1.5 | 1 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | image_quality | 是否采用高像素拍摄 | 0 | 12MP | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | image_quality | 是否采用高像素拍摄 | 1 | 50MP 108MP 200MP等具体高像素 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | glyph_mirror | 是否开启了glyph_mirror拍摄 | 0 | 关 | 0 | label_note 中 glyph_mirro 缺字母 r，正确应为 glyph_mirror，系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | glyph_mirror | 是否开启了glyph_mirror拍摄 | 1 | 开 | 0 | label_note 中 glyph_mirro 缺字母 r，正确应为 glyph_mirror，系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | flash | 闪光灯模式选择 | 0 | 闪光灯关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | flash | 闪光灯模式选择 | 1 | 闪光灯强制开 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | flash | 闪光灯模式选择 | 2 | 闪光灯常亮 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | flash | 闪光灯模式选择 | 3 | Glyph 补光 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | retouching | 美颜程度的选择 | 0 | Off | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | retouching | 美颜程度的选择 | 1 | Natural | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | retouching | 美颜程度的选择 | 2 | Strong | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | bokeh | 虚化程度的选择 | xx | 按照实际值记录 | 5.6 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | effects | 光斑效果的选择 | 0 | 无 | 0 |  |  | Camera 3.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | effects | 光斑效果的选择 | 1 | 天鹅绒：Velvet | 0 |  |  | Camera 3.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | effects | 光斑效果的选择 | 2 | 旋焦：Twist | 0 |  |  | Camera 3.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | effects | 光斑效果的选择 | 3 | 五角星：Pentacle | 0 |  |  | Camera 3.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | effects | 光斑效果的选择 | 4 | 雪花：Snowflake | 0 |  |  | Camera 3.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | nightmode | 是否使用自动夜景模式 | 0 | 未检测到，自动关闭 | 0 | 未检测到为 0<br>检测到为 1 |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | nightmode | 是否使用自动夜景模式 | 1 | 自动打开 | 0 | 未检测到为 0<br>检测到为 1 |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | nightmode | 是否使用自动夜景模式 | 2 | 手动关闭 | 0 | 未检测到为 0<br>检测到为 1 |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | macro_fb | 是否使用fallback微距模式 | 0 | 未检测到，自动关闭 | 0 | 未检测到为 0 检测到为 1 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | macro_fb | 是否使用fallback微距模式 | 1 | 触发，且开启时拍摄 | 0 | 未检测到为 0 检测到为 1 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | macro_fb | 是否使用fallback微距模式 | 2 | 触发，并手动关闭后拍摄 | 0 | 未检测到为 0 检测到为 1 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | ai_zoom | 20x以上触发长焦aigc增强后,是否手动关闭 | 0 | 触发，手动关闭拍摄 | off/1 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | ai_zoom | 20x以上触发长焦aigc增强后,是否手动关闭 | 1 | 触发，且开启时拍摄 | off/1 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | hdr | hdr 开关的选择,及拍摄时是否开启 | 0 | 手动关闭 | 无，默认为自动检测 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | hdr | hdr 开关的选择,及拍摄时是否开启 | 1 | 自动-关闭 | 无，默认为自动检测 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | hdr | hdr 开关的选择,及拍摄时是否开启 | 2 | 自动-打开 | 无，默认为自动检测 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | hdr | hdr 开关的选择,及拍摄时是否开启 | 3 | 强制打开 | 无，默认为自动检测 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | raw | 在 Expert 模式中是否开启 raw 格式拍照 | 0 | 关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | raw | 在 Expert 模式中是否开启 raw 格式拍照 | 1 | 打开 | 0 |  |  | Camera 2.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | exposure | 曝光补偿的调节值 | xxx | 真实数值，如 +-0.3 | 0 |  |  | Camera 3.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | preset | 拍摄照片时应用的preset名称 | 0 | 未应用preset | 0 |  |  | Camera 3.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | preset | 拍摄照片时应用的preset名称 | xxx | 对应的preset名称 | 0 |  |  | Camera 3.5 |
| NTCamera | photo_info | 拍照成片时上报参数 | shot_algo | 拍摄照片时使用的算法名称 | xxx | 具体的算法名称 | xxx |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | if_moon | 是否使用月亮模式 | 0/1 | 0代表没有，1代表有 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | frame_count | 取帧数量 | xxx | 具体的取帧数量 | xxx |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | exp_time | 每一帧的曝光的具体曝光时间 | xxx, xxx, ... | 上报每一帧的具体曝光时间，整合成数组上报 | xxx |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | lux | 拍照时的环境亮度 | xxx | 具体的亮度值 | xxx |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | adrc | 拍照时的DRC值,代表动态范围 | xxx | 具体的DRC值 | xxx |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | cct | 拍照时的色温值 | xxx | 具体的色温值 | xxx |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | face_count | 人脸数量,上报具体人脸数量 | xxx | 具体的人脸数量 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | face_ratio | 人脸占比,横纵方向 | [[heightRatio,widthRatio],[heightRatio,widthRatio]...] | 二维数组记录，heightRatio 为 纵方向在整个预览框占比（0-1， 保留两位小数），widthRatio 同上 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | orientation | 拍摄照片时,手机的方向状态 | 0 | vertical，竖屏状态 | 0 |  |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | orientation | 拍摄照片时,手机的方向状态 | 1 | horizontal，横屏状态 | 0 |  |  | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | video_mode | 拍摄模式 | 1 | Video | 无 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | video_mode | 拍摄模式 | 2 | Slo-mo | 无 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | video_mode | 拍摄模式 | 3 | Time-lapse | 无 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | exposure_adjust | 该视频中,用户是否手动调节曝光<br>可发生在按下快门前<br>只要曝光调节对成片产生影响就记录 | 0 | 未调节 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | exposure_adjust | 该视频中,用户是否手动调节曝光<br>可发生在按下快门前<br>只要曝光调节对成片产生影响就记录 | 1 | 调节 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | video_length | 视频拍摄时长 | xx | 以秒为单位 | 无 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | nightmode | 是否使用自动夜景模式 | 0 | 自动关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | nightmode | 是否使用自动夜景模式 | 1 | 手动打开 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | hdr | hdr开启 HDR 功能（新项目以下线） | 0 | 关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | hdr | hdr开启 HDR 功能（新项目以下线） | 1 | 打开 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | action_mode | 防抖模式 | 0 | 关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | action_mode | 防抖模式 | 1 | 打开 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | flash | 闪光灯模式选择 | 0 | 闪光灯关闭 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | flash | 闪光灯模式选择 | 2 | 闪光灯常亮 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | flash | 闪光灯模式选择 | 3 | Glyph 补光 | 0 |  |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 1080p-30 | 1080p-30 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=1 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 1080p-60 | 1080p-60 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=2 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 4k-30 | 4k-30 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=3 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 4k-60 | 4k-60 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=4 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 1080p-120 | 1080p-120 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=5 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 1080p-240 | 1080p-240 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=6 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 1080p-480 | 1080p-480 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=7 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 | 4k-120 | 4k-120 | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=8 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 \| 延时摄影 | 1080 | 1080（延时摄影规格） | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=9 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | quality | 清晰度&帧率 \| 延时摄影 | 4k | 4k（延时摄影规格） | video=1080p-60<br>slo-mo=1080p-120<br>time-lapse=1080 | @Zhongmin Long 已处理：sv改为实际规格。原索引值=10 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | if_HLG | 是否使用HDR规格录制,以及录制时使用的HDR格式 | 0 | 未使用HDR录制 | 0 |  |  | Camera 3.5 |
| NTCamera | video_info | 录像成片时上报参数 | if_HLG | 是否使用HDR规格录制,以及录制时使用的HDR格式 | 1 | 使用HDR录制，且为HLG格式 | 0 |  |  | Camera 3.5 |
| NTCamera | video_info | 录像成片时上报参数 | Rec_light | 在录制时是否开启了录影灯 | 0 | 关闭录影灯 | 1 |  |  | Camera 3.5 |
| NTCamera | video_info | 录像成片时上报参数 | Rec_light | 在录制时是否开启了录影灯 | 1 | 开启录影灯（默认） | 1 |  |  | Camera 3.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 15x | 15 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=1 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 30x | 30 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=2 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 60x | 60 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=3 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 120x | 120 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=4 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 240x | 240 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=5 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 480x | 480 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=6 |  | Camera 2.5 |
| NTCamera | video_info | 录像成片时上报参数 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 960x | 960 | 1 | @Zhongmin Long 已处理：sv改为实际值。原索引sv=7 |  | Camera 2.5 |
| NTCamera | activate_type | 功能激活时上报 |  |  | 1 | 冷启动 | 无 | 启动相机时记录 |  | Camera 2.5 |
| NTCamera | activate_type | 功能激活时上报 |  |  | 2 | 热启动 | 无 | 启动相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 1 | 点击图标 | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 2 | 双击电源键 | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 3 | 第三方调用 | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 4 | 多任务 | 无 | @Zhongmin Long 已处理：多任务已拆分为分屏/小窗，本项保留为通用多任务 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 5 | 锁屏长按 | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 6 | Shortcut Widget | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 7 | Xpand Widget | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 8 | unknown，区别于上述之外 | 无 | 进入相机时记录 |  | Camera 2.5 |
| NTCamera | brightness_adjust | 手动调亮度时上报 | brightness_if_adjust | 是否手动调亮度 | 0 | 未调节 | 0 | 这三个记录在同一事件中<br>名称为：<br>brightness_adjust |  | Camera 2.5 |
| NTCamera | brightness_adjust | 手动调亮度时上报 | brightness_if_adjust | 是否手动调亮度 | 1 | 调节 | 0 | 这三个记录在同一事件中<br>名称为：<br>brightness_adjust |  | Camera 2.5 |
| NTCamera | brightness_adjust | 手动调亮度时上报 | brightness_auto | 进入相机时读取到的系统亮度值<br>or 理解为这时的自动亮度值 | xx | 亮度值 | 无 | 这三个记录在同一事件中<br>名称为：<br>brightness_adjust |  | Camera 2.5 |
| NTCamera | brightness_adjust | 手动调亮度时上报 | brightness_new | 用户手动调节后的亮度值与上述项的差值 | xx | 差值<br>正值表示用户增加亮度<br>负值表示用户调暗亮度 | 无 | 这三个记录在同一事件中<br>名称为：<br>brightness_adjust |  | Camera 2.5 |
| NTCamera | grid | 网格线——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | grid | 网格线——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | shutter_sound | 快门声音——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | shutter_sound | 快门声音——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | mirror_front | 镜像前置——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | mirror_front | 镜像前置——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | qr_scan | 二维码扫描——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | qr_scan | 二维码扫描——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | tap_shoot | 轻触拍照——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | tap_shoot | 轻触拍照——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | save_location | 保存位置变更时上报 |  |  | 0 | 将存储位置切换到sd card时上报 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | save_location | 保存位置变更时上报 |  |  | 1 | 将存储位置切换到 internal storage 时上报 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | level | 水平辅助线——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | level | 水平辅助线——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | watermark | 水印变更时上报 |  |  | 0 | 关闭 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | watermark | 水印变更时上报 |  |  | 1 | 打开 | 0 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | press_hold_shutter | 长按快门的操作 |  |  | 1 | Burst shot | 2 | 用户更改时记录 |  | Camera 2.5 |
| NTCamera | press_hold_shutter | 长按快门的操作 |  |  | 2 | Record video | 2 | 用户更改时记录 |  | Camera 2.5 |
| NTCamera | recording_light | 录像指示灯——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | recording_light | 录像指示灯——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | video_encoding | 视频编码 |  |  | 1 | H.264 | 1 | 用户更改时记录 |  | Camera 2.5 |
| NTCamera | video_encoding | 视频编码 |  |  | 2 | H.265 | 1 | 用户更改时记录 |  | Camera 2.5 |
| NTCamera | ultra_XDR | UHDR——功能开关 |  |  | 0 | 关闭 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | ultra_XDR | UHDR——功能开关 |  |  | 1 | 打开 | 1 | 点击开关时记录 |  | Camera 2.5 |
| NTCamera | quality | 画质变更时上报 |  |  | 1 | 12MP | 1 | ⚠️ 与50mp_ps功能重叠，待确认是否去重 \| 用户更改时记录 |  | Camera 2.5 |
| NTCamera | quality | 画质变更时上报 |  |  | 2 | 50MP | 1 | 用户更改时记录 |  | Camera 2.5 |
| NTCamera | mode_ps | 模式记忆开关变更时上报 |  |  | 0 | 关闭 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | mode_ps | 模式记忆开关变更时上报 |  |  | 1 | 打开 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | bokeh_ps | 虚化记忆开关变更时上报 |  |  | 0 | 关闭 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | bokeh_ps | 虚化记忆开关变更时上报 |  |  | 1 | 打开 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | filter_ps | 滤镜记忆开关变更时上报 |  |  | 0 | 关闭 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | filter_ps | 滤镜记忆开关变更时上报 |  |  | 1 | 打开 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | 50mp_ps | 50MP记忆开关变更时上报 |  |  | 0 | 关闭 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | 50mp_ps | 50MP记忆开关变更时上报 |  |  | 1 | 打开 | ? | @Zhongmin Long 已处理：25111无此开关，标为已废弃 | 已废弃 |  |
| NTCamera | lut_control | LUT 相关操作的次数统计 |  |  | 0 | 通过本地文件，导入一个 LUT，成功，记录一次 | 无 | 操作结束后记录 |  | Camera 3.0 |
| NTCamera | lut_control | LUT 相关操作的次数统计 |  |  | 1 | 通过本地文件，导入一个 LUT，失败，记录一次 | 无 | 操作结束后记录 |  | Camera 3.0 |
| NTCamera | enter_mode | 用户冷启动进入 camera 的默认模式 |  |  | 0 | 默认的 Photo 模式（Origin Preset） | 0 | 进入相机时记录 |  | Camera 3.0 |
| NTCamera | enter_mode | 用户冷启动进入 camera 的默认模式 |  |  | 1 | Default Preset （冷启动后直接应用用户提前预选的 Preset） | 0 | 进入相机时记录 |  | Camera 3.0 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 |  |  | 1 | 用户手动创建一个 Preset 并点击 save 后创建成功，记录一次 | 无 | 操作结束后记录 |  | Camera 3.0 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 |  |  | 2 | 用户删除掉一个 Preset 后，记录一次 | 无 | 操作结束后记录 |  | Camera 3.0 |
| NTCamera | preset_control | Preset 创建和删除的次数统计 |  |  | 3 | 用户恢复删除的官方预设 | 无 | 操作结束后记录 |  | Camera 3.0 |
| NTCamera | preset_create | Preset 分享的次数统计 |  |  | 1 | 用户分享 Preset，生成二维码，成功，记录一次 | 无 | 操作结束后记录 |  | Camera 3.5 |
| NTCamera | preset_create | Preset 分享的次数统计 |  |  | 2 | 用户分享 Preset，生成二维码，失败，记录一次 | 无 | 操作结束后记录 |  | Camera 3.5 |
| NTCamera | preset_import | Preset 导入的次数统计 |  |  | 1 | 用户导入 Preset，成功，记录一次 | 无 | 操作结束后记录 |  | Camera 3.5 |
| NTCamera | preset_import | Preset 导入的次数统计 |  |  | 2 | 用户导入 Preset，失败，记录一次 | 无 | 操作结束后记录 |  | Camera 3.5 |
| NTCamera | preset_import | Preset 导入的次数统计 |  |  | xx | 用户导入 Preset成功上报，有网络上报 Preset 的下载 link，无网络则上报datamap | 无 | 操作结束后记录 |  | Camera 3.5 |
| NTCamera | pef_info | 相机性能埋点 | coldStart | 冷启动 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | hotStart | 热启动 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | capturePrepare | 快门响应完成app下发拍照请求 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | capture2Thumbnail | 小图刷新 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | capture2Photo | 大图刷新（JPEG） | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | click2RecordStart | 录制开始响应速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | click2RecordFinish | 结束录像响应速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | switchMode | 切换模式速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | pef_info | 相机性能埋点 | switchCamera | 切换镜头速度 | xx | 以ms为单位 | 无 | 疑似拼写错误，正确应为 perf_info（性能），系历史遗留，实现时保持原值 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | event_timestamp_local | 用户本地时间戳带时区偏移用于直接查询用户操作时间。每次按下拍照快门并成功产出一张照片时上报。 | 2026-04-27T15:13:00+08:00 | ISO 8601 格式，如 2026-04-27T15:13:00+08:00 | 无 |  |  | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | event_timestamp_local | 用户本地时间戳带时区偏移用于直接查询用户操作时间。每次停止录制并成功生成一个视频时上报。 | 2026-04-27T15:13:00+08:00 | ISO 8601 格式，如 2026-04-27T15:13:00+08:00 | 无 |  |  | Camera 4.0 |
| NTCamera | auto_fps | 视频自动帧率——功能开关 |  |  | off | 关 | 1 | 用户更改时记录 |  | Camera 4.0 |
| NTCamera | auto_fps | 视频自动帧率——功能开关 |  |  | auto_30 | 自动30fps | 1 | 用户更改时记录 |  | Camera 4.0 |
| NTCamera | auto_fps | 视频自动帧率——功能开关 |  |  | auto_30_60 | 自动30&60fps | 1 | 用户更改时记录 |  | Camera 4.0 |
| NTCamera | lock_lens | 锁定镜头——功能开关 |  |  | 0 | 关闭 | 0 | 点击开关时记录 |  | Camera 4.0 |
| NTCamera | lock_lens | 锁定镜头——功能开关 |  |  | 1 | 打开 | 0 | 点击开关时记录 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | doc_mode | 是否使用文档模式 | 0 | 未检测到，自动关闭 | 0 | 未检测到为 0 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | doc_mode | 是否使用文档模式 | 1 | 自动打开 | 0 | 检测到，并且拍摄 为 1 |  | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | doc_mode | 是否使用文档模式 | 2 | 手动关闭 | 0 | 0=未检测 1=检测到且使用 2=检测到但用户关闭 \| 当前状态改为待开发 \| @Zhongmin Long 已更新值含义 |  | Camera 4.0 |
| NTCamera | exit_camera | 性能相关参数 | pop_photo_count | 退出相机时后台剩余处理照片数 | 0 | 剩余照片数（整数） | 0 | 相机退到后台时上报（含打开相册查看照片）。记录当前后台正在处理的剩余照片数量 |  | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | filter | 滤镜名称 | 0 | 无滤镜 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | filter | 滤镜名称 | xxx | 滤镜名称 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | filter_strength | 对应滤镜调节强度 | 0-10.0 | 对应滤镜调节强度 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_apply | 拍摄视频是否开启调色功能 | 0/1 | 0=不应用,1=应用 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_contrast | 对应「对比度」的具体参数值 | -10.0～+10.0 | 对应对比度的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_saturation | 对应「饱和度」的具体参数值 | -10.0～+10.0 | 对应饱和度的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_warmth | 对应「色温」的具体参数值 | -10.0～+10.0 | 对应色温的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_tint | 对应「色调」的具体参数值 | -10.0～+10.0 | 对应色调的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_shapen | 对应「锐度」的具体参数值 | 0～10.0 | 对应锐度的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_grain | 对应「噪点」的具体参数值 | 0～10.0 | 对应噪点的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | video_info | 录像成片时上报参数 | tuning_vignette | 对应「暗角」的具体参数值 | 0～10.0 | 对应暗角的具体参数值 | 无 | @Zhongmin Long 已处理：从 photo_info 同步至 video_info，待确认视频侧是否适用 | 待开发 | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | flash | 闪光灯模式选择 | 4 | auto 模式，目前仅 前置支持 | 4 | @Zhongmin Long 已确认：前置flash已有AUTO(sv=4)，无需新增 |  | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 9 | 多任务-分屏 | 无 | @Zhongmin Long 已处理：多任务细分为分屏(sv=9)/小窗(sv=10) | 待开发 | Camera 2.5 |
| NTCamera | enter_method | 进入相机时上报 |  |  | 10 | 多任务-小窗 | 无 | @Zhongmin Long 已处理：多任务细分为分屏(sv=9)/小窗(sv=10) | 待开发 | Camera 2.5 |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| NTCamera | photo_info | 拍照成片时上报参数 | flicker_sensor_output | 拍照时 Flicker sensor 输出的光源频率值，对应代码变量 m_currentLightFrequency | xxx | Flicker sensor 原始数值，如 0, 100, 120, 240 等 | 0 | 2026-06-17 新增 | 待开发 | Camera 4.0 |
| NTCamera | photo_info | 拍照成片时上报参数 | motion_level | 当前场景检测到的运动速度等级，对应代码变量 m_currentMotionLevel。拍照模式下触发运动抓拍时上报 | xxx | 运动速度等级的具体数值 | 0 | 2026-06-17 新增，原计划整合到 shot_algo，经讨论改为独立 key | 待开发 | Camera 4.0 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报,记录该视频对应参数,包含录制前和录制中的临时必要操作。 | video_mode | 在哪个模式拍摄的视频 | 4 | 前后双录 (Dual Recording) | 无 | 2026-06-25 新增 | 待开发 | Camera 2.5 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | dual_split | 前后双录的拼接方式 | top_bottom / pip | 上下分屏 / 画中画 | 无 | 2026-06-25 新增 | 待开发 | Camera 4.1 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | dual_lens | 前后双录的镜头组合（数字编码，见 camera_id） | 1+0 / 1+2 | 前置+主摄 / 前置+超广角 | 无 | 2026-06-25 新增 | 待开发 | Camera 4.1 |
| NTCamera | photo_info | 拍照成片时上报参数 | ai_scene | 拍照时 AI 场景识别结果 | xxx | 上报算法识别的场景类型或枚举值 | none | 2026-07-16 新增 | 待开发 | Camera 4.1 |
| NTCamera | photo_info | 拍照成片时上报参数 | gyro_level | 拍照时陀螺仪检测到的运动等级 | xxx | 陀螺仪运动等级的具体数值 | 0 | 2026-07-16 新增 | 待开发 | Camera 4.1 |
| NTCamera | photo_info | 拍照成片时上报参数 | face_luma_ratio | 拍照时人脸区域亮度与画面亮度的比值 | xxx | 上报实际比值，具体精度以算法输出为准 | 0 | 2026-07-16 新增 | 待开发 | Camera 4.1 |
| NTCamera | photo_info | 拍照成片时上报参数 | ISO | 拍照时的感光度（ISO） | xxx | 实际 ISO 数值，如 100、400、1600 | xxx | 2026-07-16 新增 | 待开发 | Camera 4.1 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | camera_id | 视频由哪颗镜头录制 | 0 | 主摄，后置广角 | 无 | 2026-08-18 补充文档；代码已通过 video_record_info 上报 CameraId | 已上线 |  |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | camera_id | 视频由哪颗镜头录制 | 1 | 前置镜头 | 无 | 2026-08-18 补充文档；代码已通过 video_record_info 上报 CameraId | 已上线 |  |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | camera_id | 视频由哪颗镜头录制 | 2 | 后置超广 | 无 | 2026-08-18 补充文档；代码已通过 video_record_info 上报 CameraId | 已上线 |  |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | camera_id | 视频由哪颗镜头录制 | 3 | 后置长焦 | 无 | 2026-08-18 补充文档；代码已通过 video_record_info 上报 CameraId | 已上线 |  |
| NTCamera | front_auto_wide_switch | 前置自动小广角——自动焦段切换 | from_zoom | 切换前焦段 | 1x / 0.8x | 切换前的前置焦段 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；自动切换时记录 | 待开发 | Camera 5.1 |
| NTCamera | front_auto_wide_switch | 前置自动小广角——自动焦段切换 | to_zoom | 切换后焦段 | 0.8x / 1x | 切换后的前置焦段 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；自动切换时记录 | 待开发 | Camera 5.1 |
| NTCamera | tuning_panel | Tuning Palette——面板操作 | action | 面板操作 | open / collapse / reset | 打开 / 收起 / 重置 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；操作完成时记录 | 待开发 | Camera 5.1 |
| NTCamera | pro_mode_metering_mode | 照片专业模式——测光模式 |  |  | spot / center_weighted / matrix | 点测光 / 中央重点 / 矩阵测光 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；切换时记录 | 待开发 | Camera 5.1 |
| NTCamera | pro_mode_interval_shots | 照片专业模式——间隔拍摄张数 |  |  | 5-600 | 本次间隔拍摄设定张数 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；开始间隔拍摄时记录 | 待开发 | Camera 5.1 |
| NTCamera | pro_mode_interval_seconds | 照片专业模式——间隔拍摄间隔 |  |  | 1-60 | 间隔秒数 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；开始间隔拍摄时记录 | 待开发 | Camera 5.1 |
| NTCamera | pro_mode_peaking_toggle | 照片专业模式——峰值对焦开关 |  |  | on / off | 开启 / 关闭 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；切换时记录 | 待开发 | Camera 5.1 |
| NTCamera | photo_info | 拍照成片时上报参数 | photo_style | 拍摄时照片风格 | natural / vivid | 自然 / 鲜明 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；每次拍摄成片时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_info | 每次停止录制并成功生成一个视频时上报 | isz_used | 本次录像是否使用 ISZ | 0 / 1 | 未使用 / 使用 | 0 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；录像成片时记录 | 待开发 | Camera 5.1 |
| NTCamera | eis_switch | 视频防抖——功能开关 |  |  | 0 / 1 | 关闭 / 打开 | 1 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；点击开关时记录 | 待开发 | Camera 5.1 |
| NTCamera | lock_wb | 视频锁定白平衡——功能开关 |  |  | 0 / 1 | 关闭 / 打开 | 0 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；点击开关时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_ev_toggle | 视频专业参数——曝光开关 |  |  | 0 / 1 | 关闭 / 打开 | 1 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；点击开关时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_ev_changed | 视频专业参数——EV 调节 | ev_value | EV 偏移值 | -2.0 ~ +2.0 | 当前 EV 偏移值 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；滑轨松手时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_ev_changed | 视频专业参数——EV 调节 | is_recording | 是否正在录像 | 0 / 1 | 录制前 / 录制中 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；与 EV 值同时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_wb_toggle | 视频专业参数——白平衡开关 |  |  | 0 / 1 | 关闭 / 打开 | 1 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；点击开关时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_wb_changed | 视频专业参数——白平衡调节 | wb_value | 白平衡色温值 | 绝对 K 值 | 当前设定色温 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；滑轨松手时记录 | 待开发 | Camera 5.1 |
| NTCamera | video_wb_changed | 视频专业参数——白平衡调节 | is_recording | 是否正在录像 | 0 / 1 | 录制前 / 录制中 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；与 WB 值同时记录 | 待开发 | Camera 5.1 |
| NTCamera | ai_composition | AI 构图助手——关键操作 | action | 用户操作 | open / close / shoot | 打开 / 关闭 / 开启后拍摄 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；仅记录关键操作 | 待开发 | Camera 5.1 |
| NTCamera | motion_guide | 运动场景引导——胶囊结果 | action | 引导结果 | show / click / close / auto_dismiss | 展示 / 点击 / 关闭 / 自动消失 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；不记录检测中间过程 | 待开发 | Camera 5.1 |
| NTCamera | beauty_guide | 美颜首次开启引导 | action | 用户行为 | show / select | 引导曝光 / 完成选择 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；仅记录曝光和选择 | 待开发 | Camera 5.1 |
| NTCamera | beauty_guide | 美颜首次开启引导 | beauty_level | 用户选择后的美颜等级 | off / natural / strong | 关闭 / 自然 / 强 | off | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；完成选择时记录 | 待开发 | Camera 5.1 |
| NTCamera | tips_feedback | Tips and feedback——跳转结果 |  |  | success / failed | 跳转成功 / 跳转失败 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；点击入口后记录最终结果 | 待开发 | Camera 5.1 |
| NTCamera | ai_preset | AI Preset——关键操作 | action | 用户行为 | show / apply | 推荐展示 / 应用推荐 | 无 | 2026-08-18 Camera 5.1（26111）需求补充，按 PRD 最小化设计；仅记录推荐展示和应用 | 待开发 | Camera 5.1 |

