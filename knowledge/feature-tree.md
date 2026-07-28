# Camera Feature Tree

<!-- GENERATED FILE: DO NOT EDIT. Edit the canonical KB builder instead. -->

> 本文件由 `scripts/build_feature_tree.py` 从 canonical KB 的 `节点 ID / 父节点 ID` 生成。
> Tree 不是独立数据源，禁止手工维护；节点解释、代码绑定、门控和 FL 展开条件以 KB 为准。

## FL 投影语义

- `不进入 FL`：目录或纯知识节点。
- `父节点汇总`：FL 默认只保留父能力一行，子能力留在 KB 中解释。
- `随父节点`：不独立成行，除非它改变父能力的验收结论。
- `独立行`：默认形成一条 FL 验收行。
- `条件展开`：只有项目、模式、摄像头或规格差异会改变支持/验收结论时展开。
- `规格展开`：按明确的摄像头 × 分辨率/帧率/像素档等规格笛卡尔积生成候选行。

核心原则：**KB 可以细，FL 只展开会产生关键项目或摄像头差异的节点。**

## 统计

- KB 节点总数：142
- 知识/能力节点：122
- 目录节点：20
- 独立行：57
- 条件展开：43
- 规格展开：11
- 父节点汇总/随父节点：11

## 业务树

```text
Camera Knowledge Base  `kb.root`
├── 启动与入口 / Launch & Entry  `kb.launch`
│   └── 相机启动入口 / Camera Launch Entry  `kb.launch.entry` 〔入口｜FL: 条件展开｜维度: 项目 / 入口〕
├── 预览与场景感知 / Preview & Scene  `kb.preview`
│   ├── 人脸检测  `kb.preview.face_detection` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── ASD / AI场景检测  `kb.preview.asd` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   ├── 脏污检测  `kb.preview.dirt_detection` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   └── 人脸畸变矫正  `kb.capability.57d411015e88` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
├── 对焦与曝光 / Focus & Exposure  `kb.focus`
│   └── 自动对焦-自动曝光  `kb.focus.auto` 〔能力｜FL: 父节点汇总｜维度: 项目 / 模式 / 摄像头〕
│       ├── Touch AE/AF  `kb.focus.touch_ae_af` 〔交互｜FL: 条件展开｜维度: 模式 / 摄像头〕
│       ├── Face AE/AF  `kb.focus.face_ae_af` 〔能力｜FL: 条件展开｜维度: 模式 / 摄像头〕
│       ├── Touch AE/AF Lock  `kb.focus.lock` 〔交互｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头〕
│       ├── CAF / 连续自动对焦  `kb.focus.caf` 〔能力｜FL: 条件展开｜维度: 模式 / 摄像头 / 规格〕
│       └── EV 曝光补偿  `kb.focus.ev` 〔规格｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
├── 变焦与镜头切换 / Zoom & Lens  `kb.zoom`
│   ├── 变焦  `kb.zoom.control` 〔能力｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   │   ├── 变焦交互 / Zoom Gestures  `kb.zoom.gestures` 〔交互｜FL: 随父节点｜维度: 模式〕
│   │   ├── 变焦倍率范围 / Zoom Range  `kb.zoom.range` 〔规格｜FL: 规格展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   │   └── 镜头切换策略 / Lens Switching Strategy  `kb.zoom.switch_strategy` 〔能力｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   ├── OIS  `kb.zoom.ois` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── ISZ / In Sensor Zoom  `kb.zoom.isz` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   └── 超分 / Super Resolution（SR）  `kb.zoom.super_resolution` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
├── 暂态开关 / Transient Switches  `kb.transient`
│   ├── AI Zoom 开关 / AI Zoom Switch  `kb.transient.ai_zoom` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 自动微距控制  `kb.transient.auto_macro` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 自动夜景开关 / Auto Night Switch  `kb.transient.auto_night` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   └── Text Mode（文本模式）  `kb.transient.text` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
├── 拍摄与录制交互 / Capture & Recording  `kb.capture`
│   ├── 前后翻转 / Front-Rear Camera Switch  `kb.capture.camera_switch` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 录制中前后置切换 / Front-Rear Switch While Recording  `kb.capture.camera_switch_recording` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 录制中拍照 / Video Snapshot  `kb.capture.video_snapshot` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 录制中拍摄动态照片 / Motion Photo While Recording  `kb.capture.motion_photo_while_recording` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   └── 视频暂停与恢复 / Video Pause & Resume  `kb.video.pause_resume` 〔交互｜FL: 独立行｜维度: 项目 / 规格〕
├── 工具栏 / Toolbar  `kb.toolbar`
│   ├── Flash  `kb.capability.flash` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 录影灯 / Recording Light  `kb.capability.recording.light` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── Timer  `kb.capability.timer` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── HDR 开关 / HDR Switch  `kb.capability.hdr.hdr.switch` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── Exposure  `kb.capability.exposure` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 风格 / Style  `kb.toolbar.style` 〔能力｜FL: 父节点汇总｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   │   ├── Filter  `kb.toolbar.style.filter.photo` 〔能力｜FL: 随父节点｜维度: 项目 / 模式 / 摄像头〕
│   │   ├── 风格-滤镜 / Style-Filter  `kb.toolbar.style.filter.video` 〔能力｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   │   ├── 风格-调色 / Style-Tuning  `kb.toolbar.style.tuning.video` 〔能力｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   │   ├── 风格-调色盘 / Style-Tuning Palette  `kb.toolbar.style.palette.video` 〔能力｜FL: 随父节点｜维度: 项目 / 模式 / 摄像头 / 规格〕
│   │   └── Tuning  `kb.toolbar.style.tuning.photo` 〔能力｜FL: 随父节点｜维度: 项目 / 模式 / 摄像头〕
│   ├── Motion Photo  `kb.toolbar.motion_photo` 〔能力｜FL: 父节点汇总｜维度: 项目 / 摄像头〕
│   │   ├── 动态照片 - 无效信息截取  `kb.toolbar.motion_photo.trim` 〔能力｜FL: 条件展开｜维度: 项目〕
│   │   ├── 动态照片-视频支持录制声音  `kb.toolbar.motion_photo.audio` 〔能力｜FL: 条件展开｜维度: 项目 / 摄像头〕
│   │   └── Motion Photo cover HDR  `kb.toolbar.motion_photo.cover_hdr` 〔能力｜FL: 条件展开｜维度: 项目 / 摄像头 / 规格〕
│   │       └── 动态照片插帧 / Motion Photo Frame Interpolation  `kb.algorithms.motion_photo_interpolation` 〔算法｜FL: 随父节点｜维度: 项目 / 摄像头〕
│   ├── Quality  `kb.capability.quality` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── Grid  `kb.capability.grid` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── Ratio  `kb.capability.ratio` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── Watermark  `kb.capability.watermark` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── More settings  `kb.capability.more.settings` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── Glyph Mirror  `kb.capability.glyph.mirror` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   ├── 美颜控制 / Beauty Control  `kb.toolbar.beauty` 〔交互｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
│   └── 虚化控制 / Bokeh Control  `kb.toolbar.bokeh` 〔交互｜FL: 独立行｜维度: 项目 / 摄像头〕
├── 模式 / Modes  `kb.modes`
│   ├── 模式栏  `kb.modes.switcher` 〔能力｜FL: 父节点汇总｜维度: 项目〕
│   ├── 快速模式切换 / Quick Mode Switch  `kb.modes.quick_switch` 〔能力｜FL: 条件展开｜维度: 项目〕
│   ├── 高像素输出规格 / High Resolution Specs  `kb.mode.high_resolution.specs` 〔能力｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   ├── 照片模式 / Photo Mode  `kb.mode.photo` 〔模式｜FL: 独立行｜维度: 项目 / 摄像头〕
│   ├── 视频模式 / Video Mode  `kb.mode.video` 〔模式｜FL: 独立行｜维度: 项目 / 摄像头 / 规格〕
│   │   └── 视频规格 / Video Specs  `kb.mode.video.specs` 〔能力｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   ├── 人像模式 / Portrait Mode  `kb.mode.portrait` 〔模式｜FL: 独立行｜维度: 项目 / 摄像头〕
│   ├── 夜景模式 / Night Mode  `kb.mode.night` 〔模式｜FL: 独立行｜维度: 项目 / 摄像头〕
│   ├── 慢动作模式 / Slow Motion Mode  `kb.mode.slow_motion` 〔模式｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   │   └── 慢动作规格 / Slow Motion Specs  `kb.mode.slow_motion.specs` 〔能力｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   ├── 延时摄影模式 / Timelapse Mode  `kb.mode.timelapse` 〔模式｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   │   └── 延时摄影规格 / Timelapse Specs  `kb.mode.timelapse.specs` 〔能力｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   ├── 全景模式 / Panorama Mode  `kb.mode.panorama` 〔模式｜FL: 独立行｜维度: 项目 / 摄像头 / 规格〕
│   ├── 专业模式 / Expert Mode  `kb.mode.expert` 〔模式｜FL: 父节点汇总｜维度: 项目 / 摄像头〕
│   │   ├── 各项专业模式参数极值范围  `kb.mode.expert.parameter_ranges` 〔能力｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   │   │   ├── ISO 范围 / ISO Range  `kb.mode.expert.iso` 〔规格｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   │   │   ├── 快门范围 / Shutter Range  `kb.mode.expert.shutter` 〔规格｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   │   │   ├── 白平衡范围 / WB Range  `kb.mode.expert.wb` 〔规格｜FL: 条件展开｜维度: 项目 / 摄像头 / 规格〕
│   │   │   └── 手动对焦范围 / Manual Focus Range  `kb.mode.expert.focus` 〔规格｜FL: 规格展开｜维度: 项目 / 摄像头 / 规格〕
│   │   ├── RAW / DNG 输出  `kb.mode.expert.raw` 〔能力｜FL: 条件展开｜维度: 项目 / 摄像头 / 规格〕
│   │   └── 直方图 / Histogram  `kb.mode.expert.histogram` 〔交互｜FL: 独立行｜维度: 项目 / 摄像头〕
│   ├── 微距模式 / Macro Mode  `kb.mode.macro` 〔模式｜FL: 条件展开｜维度: 项目 / 摄像头〕
│   └── 运动模式 / Action Mode  `kb.mode.action` 〔模式｜FL: 条件展开｜维度: 项目 / 摄像头〕
├── 通用能力 / Common  `kb.common`
│   ├── 预设 / Preset  `kb.common.preset`
│   │   └── Preset  `kb.common.preset.capability` 〔设置｜FL: 父节点汇总｜维度: 项目〕
│   ├── 小组件 / Widget  `kb.common.widget`
│   │   └── Preset Widget  `kb.common.widget.preset` 〔设置｜FL: 独立行｜维度: 项目〕
│   └── 设置 / Settings  `kb.settings`
│       ├── 通用设置 / General Settings  `kb.settings.general`
│       │   ├── Save location  `kb.capability.save.location` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Shutter sound  `kb.capability.shutter.sound` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Mirror front camera  `kb.capability.mirror.front.camera` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Level  `kb.capability.level` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Default gallery / 默认相册  `kb.settings.general.default_gallery` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   └── Storage location / 存储位置  `kb.settings.general.storage` 〔设置｜FL: 独立行｜维度: 项目〕
│       ├── 照片设置 / Photo Settings  `kb.settings.photo`
│       │   ├── Auto Tone  `kb.capability.auto.tone` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── 影像基调 / Image Tone  `kb.capability.image.tone` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── 色彩模式 / Color Mode  `kb.capability.color.mode` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Watermark settings  `kb.capability.watermark.settings` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Tap to take a photo  `kb.capability.tap.to.take.a.photo` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── QR code scanner  `kb.capability.qr.code.scanner` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Press and hold shutter  `kb.capability.press.and.hold.shutter` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Ultra XDR  `kb.capability.ultra.xdr` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   └── Fallback macro control / 自动微距设置  `kb.settings.photo.fallback_macro` 〔设置｜FL: 独立行｜维度: 项目 / 摄像头〕
│       ├── 视频设置 / Video Settings  `kb.settings.video`
│       │   ├── Video encoding  `kb.capability.video.encoding` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Power saving recording  `kb.capability.power.saving.recording` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── Auto FPS  `kb.capability.auto.fps` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── 视频防抖开关  `kb.capability.0a814575aebf` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── 锁定镜头  `kb.capability.4781fcfefead` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   ├── 锁定白平衡  `kb.capability.6337f26e73fc` 〔设置｜FL: 独立行｜维度: 项目〕
│       │   └── 视频静音录制 / Video Mute  `kb.video.mute` 〔设置｜FL: 独立行｜维度: 项目〕
│       ├── 帮助与反馈 / Help & Support  `kb.settings.help`
│       │   └── Tips and feedback  `kb.capability.tips.and.feedback` 〔设置｜FL: 独立行｜维度: 项目〕
│       └── 重置相机设置 / Reset Camera Settings  `kb.settings.reset` 〔设置｜FL: 独立行｜维度: 项目〕
├── 系统交互 / System Interactions  `kb.system`
│   └── Ultra HDR  `kb.capability.ultra.hdr` 〔能力｜FL: 独立行｜维度: 项目 / 模式 / 摄像头〕
├── 相册联动 / Gallery Integration  `kb.gallery`
└── 算法能力 / Algorithms  `kb.algorithms`
    ├── FRT / 人像清晰度提升  `kb.algorithms.frt` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 美颜算法 / Beauty Algorithm  `kb.algorithms.beauty` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 人像虚化 / Portrait Bokeh  `kb.algorithms.portrait_bokeh` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── Photo EIS  `kb.algorithms.photo_eis` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── Video EIS  `kb.algorithms.video_eis` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── Video HDR 算法  `kb.algorithms.video_hdr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── AIGC SR  `kb.capability.aigc.sr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── HDSR  `kb.capability.hdsr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 运动抓拍  `kb.capability.040e8fa9f66f` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── RAW HDR  `kb.capability.raw.hdr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── CFR / 紫边去除  `kb.capability.cfr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── Hex Zoom  `kb.capability.hex.zoom` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 视频夜景  `kb.capability.5dcd48858f41` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 人像 HDR  `kb.capability.hdr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 多帧降噪 / MFNR  `kb.capability.mfnr` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── LDC / 光学畸变矫正  `kb.capability.ldc` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 超级夜景  `kb.capability.a799a33020a4` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 极夜  `kb.capability.2d7af193d39a` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── 超级夜景+美颜  `kb.capability.8894db500e77` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    ├── Remosaic  `kb.capability.remosaic` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
    └── TF 50MP HDR/MMF  `kb.capability.tf.50mp.hdr.mmf` 〔算法｜FL: 条件展开｜维度: 项目 / 模式 / 摄像头 / 规格〕
```

## 生成与审计

```bash
python3 scripts/build_kb_functions_algorithms.py
```

生成后检查 `knowledge/_output/kb-functions-algorithms.v7.audit.md`；任何孤儿父节点、重复节点 ID 或无效 FL 投影都必须为 0。
