# Video

- Source workbook: `/Users/travis.zhao/Downloads/Camera App SW 埋点 2025 v4.0.xlsx`
- Extracted rows: `64`

## Sheet Note

此表为针对每个视频的参数记录，可以理解为导出数据的每一行均需包含以下字段

## Table

| event_name | key | event_note | label | label_note | string_value | value_note | 默认值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | video_mode | 在哪个模式拍摄的视频 | 1 | Video | 无 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | video_mode | 在哪个模式拍摄的视频 | 2 | Slo-mo | 无 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | video_mode | 在哪个模式拍摄的视频 | 3 | Time-lapse | 无 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exposure_adjust | 该视频中，用户是否手动调节曝光<br>可发生在按下快门前<br>只要曝光调节对成片产生影响就记录 | 0 | 未调节 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | exposure_adjust | 该视频中，用户是否手动调节曝光<br>可发生在按下快门前<br>只要曝光调节对成片产生影响就记录 | 1 | 调节 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | video_length | 视频拍摄时长 | xx | 以秒为单位 | 无 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | nightmode | 是否使用自动夜景模式 | 0 | 自动关闭 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | nightmode | 是否使用自动夜景模式 | 1 | 手动打开 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | hdr | hdr开启 HDR 功能（新项目以下线） | 0 | 关闭 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | hdr | hdr开启 HDR 功能（新项目以下线） | 1 | 打开 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | action_mode | 防抖模式 | 0 | 关闭 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | action_mode | 防抖模式 | 1 | 打开 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 0 | 闪光灯关闭 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 2 | 闪光灯常亮 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | flash | 闪光灯模式选择 | 3 | Glyph 补光 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 1080p-30 | 视频 1080p-30 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 1080p-60 | 视频 1080p-60 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 4k-30 | 视频 4k-30 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 4k-60 | 视频 4k-60 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 1080p-120 | 慢动作 1080p-120 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 1080p-240 | 慢动作 1080p-240 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 1080p-480 | 慢动作 1080p-480 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 4k-120 | 慢动作 4k-120 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 1080 | 延时摄影 1080 | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | quality | 清晰度&帧率<br>直接用 value_note 的值 | 4k | 延时摄影 4k | video 为 2<br>slo-mo 为 5<br>time-lapse 为 9 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | if_HLG | 是否使用HDR规格录制，以及录制时使用的HDR格式 | 0 | 未使用HDR录制 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | if_HLG | 是否使用HDR规格录制，以及录制时使用的HDR格式 | 1 | 使用HDR录制，且为HLG格式 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | Rec_light | 在录制时是否开启了录影灯 | 0 | 关闭录影灯 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | Rec_light | 在录制时是否开启了录影灯 | 1 | 开启录影灯（默认） | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | auto_fps | 视频自动帧率 | off | 关 | auto_30_60 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | auto_fps | 视频自动帧率 | auto_30 | 自动 30 fps | auto_30_60 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | auto_fps | 视频自动帧率 | auto_30_60 | 自动 30&60 fps | auto_30_60 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | filter | 滤镜的选择<br>因为滤镜改动频繁，直接报滤镜英文名 | 0 | 无滤镜 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | filter | 滤镜的选择<br>因为滤镜改动频繁，直接报滤镜英文名 | xxx | 滤镜名称 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | filter_strength | 滤镜强度 | 0-10.0 | 对应滤镜调节强度 | 10 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_apply | 对「调色」功能的对应操作 | 0/1 | 拍摄的这条视频是否开启 调色 功能。0代表不应用，1代表应用 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_contrast | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「对比度」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_saturation | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「饱和度」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_warmth | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色温」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_tint | 对「调色」功能的对应操作 | -10.0～+10.0 | 对应「色调」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_shapen | 对「调色」功能的对应操作 | 0～10.0 | 对应「锐度」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_grain | 对「调色」功能的对应操作 | 0～10.0 | 对应「噪点」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | tuning_vignette | 对「调色」功能的对应操作 | 0～10.0 | 对应「暗角」的具体参数值 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | first_zoom_ratio | 第一帧的变焦倍数（基于后置主摄） | xx | 基于 1 的数值，如 1.2、1.5 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | last_zoom_ratio | 最后一帧的变焦倍数（基于后置主摄） | xx | 基于 1 的数值，如 1.2、1.5 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 1 | 15 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 2 | 30 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 3 | 60 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 4 | 120 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 5 | 240 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 6 | 480 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | speed | 延时摄影的速度<br>直接用 value_note 的值 | 7 | 960 | 1 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | preset | 拍摄视频时应用的preset名称 | 0 | 未应用preset | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | preset | 拍摄视频时应用的preset名称 | xxx | 对应的preset名称 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | orientation | 开始拍摄视频时，手机的方向状态 | 0 | vertical，竖屏状态 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | orientation | 开始拍摄视频时，手机的方向状态 | 1 | horizontal，横屏状态 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | first_lux | 拍摄视频第一帧时的环境亮度 | xxx | 具体的亮度值 | xxx |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | last_lux | 拍摄视频最后一帧时的环境亮度 | xxx | 具体的亮度值 | xxx |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | first_adrc | 拍摄视频第一帧时的DRC值，代表动态范围 | xxx | 具体的DRC值 | xxx |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | last_adrc | 拍摄视频最后一帧时的DRC值，代表动态范围 | xxx | 具体的DRC值 | xxx |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | first_cct | 拍摄视频第一帧时的色温值 | xxx | 具体的色温值 | xxx |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | last_cct | 拍摄视频最后一帧时的色温值 | xxx | 具体的色温值 | xxx |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | first_face_count | 拍摄视频第一帧时的人脸数量 | xxx | 具体的人脸数量 | 0 |
| NTCamera | video_info | 单个视频所包含的参数信息<br>+<br>用户在拍摄前和拍摄中做的临时且必要的操作 | last_face_count | 拍摄视频最后一帧时的人脸数量 | xxx | 具体的人脸数量 | 0 |
