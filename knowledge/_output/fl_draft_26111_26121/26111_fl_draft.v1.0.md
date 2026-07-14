# 26111 Camera FL Draft

> Phone 5a Base; HP5 200MP main, IMX355 UW, OV32D front, no tele.

Rows: 224

| 模式 | 一级分类 | 二级分类 | 名称 | Main | UW | Front | 不支持原因 | 状态 | 确认负责人 | 验证方法 |
|---|---|---|---|---|---|---|---|---|---|---|
| 照片 / Photo | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | TBD | TBD | TBD |  | 待确认 | Product | 短按预览区域，预览是否有AE调节UI；长按预览区域，是否有AE&AF锁定功能 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Exposure | ✓ | ✓ | ✓ |  | 已确认 | Product | 单独EV调节功能，支持-2 ~ 2 范围EV调节。支持HDR/夜景 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Filter | TBD | TBD | TBD |  | 待确认 | Product | 选择内置和导入滤镜，确认预览/成片效果；具体列表看 filter 文档。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Flash | ✗ | ✗ | ✓ | Main: 该功能限定前置摄像头。；UW: 该功能限定前置摄像头。 | 已确认 | Product | 分别切换后置/前置检查 Flash 选项；验证后置 Off/On/Torch 和前置屏幕补光/Auto。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Glyph Mirror | TBD | TBD | TBD |  | 待确认 | Product | 开启 Glyph Mirror 后使用后摄自拍，确认背面 Glyph 预览和拍摄流程。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Grid | TBD | TBD | ✓ |  | 待确认 | Product | 切换 On / Off，确认网格显示和隐藏。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | HDR | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | HDR 算法 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | More settings | TBD | TBD | ✓ |  | 待确认 | Product | 点击 More settings，确认进入 Camera Settings。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Motion Photo | TBD | TBD | TBD |  | 待确认 | Product | 开启 Motion Photo 后拍摄，确认相册中可播放动态照片。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Motion Photo cover HDR | TBD | TBD | TBD |  | 待确认 | Product | HDR 场景拍摄动态照片，确认封面帧 HDR 信息和显示效果。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Photo Style | ✓ | ✓ | ✗ | Front: Photo Style PRD 当前范围为后置自然/鲜明风格，前置风格未纳入本期。 | 已确认 | Product | Photo Style 与 Filter、Tuning、Preset 的互斥/叠加顺序需在 KB 中写清。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Quality | ✓ | ✗ | ✗ | UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Ratio | TBD | TBD | ✓ |  | 待确认 | Product | 普通质量下切换比例；切到最大像素后确认 Ratio 不可切换。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Timer | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Tuning | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 打开 Tuning，分别验证 Palette Mode、Parameter Mode、Strength、7 参数调节、Reset、Preset 保存/恢复，以及与 Filter、Photo Style 的叠加顺序。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | Watermark | TBD | TBD | ✓ |  | 待确认 | Product | 点击切换并拍照确认；长按进入水印设置页。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | 动态照片 - 无效信息截取 | ✓ | ✓ | ✗ | Front: 当前基线 FL 未覆盖该摄像头的 Motion Photo 无效片段裁剪链路，需 PM/SE 确认是否纳入。 | 已确认 | Product | 按下快门后快速撤手，视频中截取掉无效信息 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | 动态照片-视频支持录制声音 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 照片 / Photo | 功能 / Feature | 工具栏 / Toolbar | 风格-滤镜 / Style-Filter | ✓ | ✓ | ✓ |  | 已确认 | Product | 单击滤镜图标，选择一种滤镜效果，查看是否有滤镜效果 |
| 照片 / Photo | 功能 / Feature | 变焦 / Zoom | OIS | ✓ | ✗ | ✗ | UW: 该摄像头没有 OIS 硬件。；Front: 该摄像头没有 OIS 硬件。 | 已确认 | SE | 查硬件物料和驱动日志确认 OIS 初始化；在当前模式使用对应摄像头手持拍摄，验证稳定性，并检查 OIS/EIS 叠加与模式切换。 |
| 照片 / Photo | 功能 / Feature | 变焦 / Zoom | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 是否把 SAT 体验优化作为独立项目需求，还是只更新 SAT KB 的验证方法和风险？ |
| 照片 / Photo | 功能 / Feature | 变焦 / Zoom | 前置自动小广角 | ✗ | ✗ | ✓ | Main: 该功能限定前置摄像头。；UW: 该功能限定前置摄像头。 | 已确认 | Product | 已找到 PRD 009，范围为系统相机前置照片模式。后续只需确认 26111/26121 前置焦段命名和陀螺仪/方向事件实现。 |
| 照片 / Photo | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 照片 / Photo | 功能 / Feature | 右侧暂态开关 / Right Transient Switch | AI Zoom | ✗ | ✗ | ✗ | Main: 依赖长焦/高倍率链路，该摄像头不在支持范围。；UW: 依赖长焦/高倍率链路，该摄像头不在支持范围。；Front: 依赖长焦/高倍率链路，该摄像头不在支持范围。 | 已确认 | Product | 在 30x 以上场景确认 AI Zoom 暂态开关是否出现；点击后拍摄高细节目标，检查成片清晰度和生成伪影。 |
| 照片 / Photo | 功能 / Feature | 右侧暂态开关 / Right Transient Switch | Text Mode（文本模式） | TBD | TBD | TBD |  | 待确认 | Product | 用照片模式预览文档/文字内容，确认开关出现；点击后确认边缘框选、透视矫正和清晰度增强。 |
| 照片 / Photo | 功能 / Feature | 右侧暂态开关 / Right Transient Switch | 自动夜景 | TBD | TBD | TBD |  | 待确认 | Product | 在低照场景确认夜景暂态开关出现；拍照后检查算法 tag、曝光时间和成片效果。 |
| 照片 / Photo | 功能 / Feature | 左侧暂态开关 / Left Transient Switch | 自动微距控制 | TBD | TBD | TBD |  | 待确认 | Product | 近距离拍摄目标，确认开关出现；关闭后确认不再自动切换微距/近距摄像头。 |
| 照片 / Photo | 功能 / Feature | 系统 / System | 长时间无交互息屏以节约电量 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | PRD-相机息屏交互 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | 二维码识别 | TBD | TBD | TBD |  | 待确认 | Product | 二维码识别框优化更像已有二维码识别与识别框 UI 的更新，除非 PM 明确新增独立入口，否则不新建功能行。 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | TBD | TBD |  | 待确认 | Product | 在单人、多人、逆光、口罩/墨镜等场景下预览，确认人脸框和相关策略稳定。 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | 识别框视觉动效 | TBD | TBD | TBD |  | 待确认 | Product | 识别框动效只更新已有对焦框/人脸框/二维码框等视觉表现；宠物框不推进，不拆独立 KB/FL 行。 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | 运动场景引导 | TBD | TBD | TBD |  | 待确认 | Product | 胶囊展示区域是否归预览框，而不是暂态开关？触发阈值和生效焦段仍待确认。 |
| 照片 / Photo | 功能 / Feature | 预览框 / Preview | 镜头脏污检测 / AI 去油污 / 提示引导 | ✓ | TBD | ✓ |  | 待确认 | Product | PM 已确认有交互且需作为新功能；仍需把硬件/配件项从 Camera FL 中排除，只保留相机内检测、修复和提示交互。 |
| 照片 / Photo | 算法 / Algorithm | 取帧策略 / Frame Capture Strategy | PZL | TBD | TBD | TBD |  | 待确认 | SE | 结合算法 tag 或日志确认快门后的取帧起点、帧数和时序，并检查快门延迟、运动拖影及成片效果 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | AI Zoom / AIGC SR | TBD | ✗ | ✗ | UW: 依赖长焦/高倍率链路，该摄像头不在支持范围。；Front: 依赖长焦/高倍率链路，该摄像头不在支持范围。 | 待确认 | SE | 高倍场景确认最终算法、入口、触发倍率、内存、性能与伪影；未确认前不得标为已支持 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | HDSR | ✓ | ✗ | ✗ | UW: 依赖长焦/高倍率链路，该摄像头不在支持范围。；Front: 依赖长焦/高倍率链路，该摄像头不在支持范围。 | 已确认 | SE | 暗光长焦/高倍 zoom 场景；确认 HDR 与 SR 均生效 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | Ultra HDR | ✓ | ✓ | ✓ |  | 已确认 | SE | 检查文件编码和 gain map / 元数据，并在支持 Ultra HDR 与仅支持 SDR 的查看器中验证显示兼容性 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 人脸畸变矫正 | TBD | TBD | TBD |  | 待确认 | SE | 将单人和多人放在画面中心、边缘及角落拍摄，对比开关或算法 tag，检查脸型比例、边缘连续性、背景形变和多人一致性。 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 光学畸变矫正 | ✗ | ✓ | ✗ | Main: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 切到超广角镜头，检查预览是否有畸变矫正功能 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 多帧降噪 / MFNR | ✓ | ✓ | ✓ |  | 已确认 | SE | 覆盖正常光、中低照、HDR/夜景阈值和运动场景，结合算法 tag 确认 MFNR 生效区间、帧数、互斥关系、噪声、鬼影和耗时 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超分 / Super Resolution（SR） | ✓ | ✗ | ✗ | UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 在生效边界前一档、边界点和后一档拍摄并检查算法 tag，确认逐摄像头实际生效焦段、细节、伪影、耗时和功耗 |
| 照片 / Photo | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超级夜景 | TBD | TBD | TBD |  | 待确认 | SE | 低照场景拍摄，确认算法 tag、曝光时间、噪声、亮度和细节。 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | ASD / AI场景检测 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 可以检测到AI场景检测算法定义中的场景 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | CFR / 紫边去除 | ✓ | ✓ | ✓ |  | 已确认 | SE | 高反差边缘场景；验证进出平滑，无跳变 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | ISZ / In Sensor Zoom | ✓ | ✗ | ✗ | UW: 该摄像头不提供照片模式 In-Sensor Zoom（ISZ）通路。；Front: 该摄像头不提供照片模式 In-Sensor Zoom（ISZ）通路。 | 已确认 | SE | 照片模式使用 Main 在 2x 检查 sensor setting、输出尺寸和切换过程；确认非 seamless 行为，并与 4x SR / remosaic 链路区分。 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Photo EIS | ✓ | ✗ | ✗ | UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | Zoom到高倍率预览需要支持EIS；高倍变焦支持门槛按项目配置确认 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Raw HDR / TF HDR | ✓ | ✓ | ✓ |  | 已确认 | SE | 暗光 HDR 场景触发；确认不与夜景同时触发 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 广角、主摄之间可以平滑切换 |
| 照片 / Photo | 算法 / Algorithm | 实时算法 / Realtime Algorithm | 运动抓拍 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 运动场景自动提升快门；检查普通模式引导入口 |
| 照片 / Photo | 算法 / Algorithm | 自然质感人像 / Natural Texture Portrait | FRT / 人像清晰度提升 | ✓ | ✓ | ✓ |  | 已确认 | SE | 逐模式、逐摄像头拍摄单人/多人、远近人脸、侧脸、遮挡和低照样张，结合算法 tag 确认 FRT 生效，并检查细节提升、身份特征保持、伪影和过度锐化。 |
| 照片 / Photo | 算法 / Algorithm | 自然质感人像 / Natural Texture Portrait | 美颜升级 / Beauty Upgrade | ✗ | ✗ | ✓ | Main: 本期美颜升级仅在照片和人像模式的前置摄像头生效。；UW: 本期美颜升级仅在照片和人像模式的前置摄像头生效。 | 已确认 | SE | 在照片与人像模式使用 Front 验证 Natural/Strong 档位、首次引导、现有参数优化及新增能力；覆盖多肤色、性别、年龄、多人、低光、逆光、遮挡与浓妆，确认不可靠识别回退到中性策略且无假白、塑料感、毛发损失或背景形变。 |
| 人像 / Portrait | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | Product | 点击预览、人脸入镜、长按锁定、移动被摄体，确认对焦/测光/锁定/CAF 行为符合模式定义。 |
| 人像 / Portrait | 功能 / Feature | 工具栏 / Toolbar | Photo Style | ✓ | ✗ | ✗ | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。；Front: Photo Style PRD 当前范围为后置自然/鲜明风格，前置风格未纳入本期。 | 已确认 | Product | Photo Style 与 Filter、Tuning、Preset 的互斥/叠加顺序需在 KB 中写清。 |
| 人像 / Portrait | 功能 / Feature | 变焦 / Zoom | 人像模式 Consistent Zoom | ✓ | ✗ | ✓ | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 已确认 | Product | 底层是否支持中间焦段人像链路、人像虚化连续曲线、默认焦段记忆仍需开发/算法确认。 |
| 人像 / Portrait | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 人像 / Portrait | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 人像 / Portrait | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | Product | 在单人、多人、逆光、口罩/墨镜等场景下预览，确认人脸框和相关策略稳定。 |
| 人像 / Portrait | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 人像 / Portrait | 功能 / Feature | 预览框 / Preview | 镜头脏污检测 / AI 去油污 / 提示引导 | ✓ | ✗ | ✓ | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 已确认 | Product | PM 已确认有交互且需作为新功能；仍需把硬件/配件项从 Camera FL 中排除，只保留相机内检测、修复和提示交互。 |
| 人像 / Portrait | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | Ultra HDR | ✓ | ✗ | ✓ | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 已确认 | SE | 检查文件编码和 gain map / 元数据，并在支持 Ultra HDR 与仅支持 SDR 的查看器中验证显示兼容性 |
| 人像 / Portrait | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 人脸畸变矫正 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | SE | 将单人和多人放在画面中心、边缘及角落拍摄，对比开关或算法 tag，检查脸型比例、边缘连续性、背景形变和多人一致性。 |
| 人像 / Portrait | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 多帧降噪 / MFNR | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | SE | 在正常光、中低照、HDR 场景、超级夜景阈值附近及运动场景拍摄，结合算法 tag 确认 MFNR 的生效区间、帧数和切换策略，并检查噪声、细节、鬼影和耗时。 |
| 人像 / Portrait | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超级夜景+美颜 | TBD | ✗ | TBD | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 待确认 | SE | 低照人脸场景开启美颜拍摄，确认夜景和美颜同时生效且自然。 |
| 人像 / Portrait | 算法 / Algorithm | 实时算法 / Realtime Algorithm | 人像 HDR | ✓ | ✗ | ✓ | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 已确认 | SE | 人像逆光场景；确认虚化和 HDR 同时稳定 |
| 人像 / Portrait | 算法 / Algorithm | 自然质感人像 / Natural Texture Portrait | FRT / 人像清晰度提升 | ✓ | ✗ | ✓ | UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 已确认 | SE | 逐模式、逐摄像头拍摄单人/多人、远近人脸、侧脸、遮挡和低照样张，结合算法 tag 确认 FRT 生效，并检查细节提升、身份特征保持、伪影和过度锐化。 |
| 人像 / Portrait | 算法 / Algorithm | 自然质感人像 / Natural Texture Portrait | 美颜升级 / Beauty Upgrade | ✗ | ✗ | ✓ | Main: 本期美颜升级仅在照片和人像模式的前置摄像头生效。；UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。 | 已确认 | SE | 在照片与人像模式使用 Front 验证 Natural/Strong 档位、首次引导、现有参数优化及新增能力；覆盖多肤色、性别、年龄、多人、低光、逆光、遮挡与浓妆，确认不可靠识别回退到中性策略且无假白、塑料感、毛发损失或背景形变。 |
| 运动 / Action | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 运动 / Action | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 运动 / Action | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 视频 / Video | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | TBD | TBD | TBD |  | 待确认 | Product | 点击预览、人脸入镜、长按锁定、移动被摄体，确认对焦/测光/锁定/CAF 行为符合模式定义。 |
| 视频 / Video | 功能 / Feature | 模式栏 / Mode Switch | 前后双录 | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入前后双录，验证镜头组合、布局、文件输出和录制稳定性。 |
| 视频 / Video | 功能 / Feature | 模式栏 / Mode Switch | 录像中拍照（VSS） | TBD | TBD | TBD |  | 待确认 | Product | VSS 位于快门行为附近，但这是差异化录制中能力，建议作为快门区域例外进入 FL；需你确认。 |
| 视频 / Video | 功能 / Feature | 模式栏 / Mode Switch | 录制中前后镜头切换 | ✓ | ✓ | ✓ |  | 已确认 | Product | 录制中切换前后镜头，确认不中断、音画同步、文件正常。 |
| 视频 / Video | 功能 / Feature | 工具栏 / Toolbar | Filter | ✓ | ✓ | ✓ |  | 已确认 | Product | 在 1080P30 下验证预览和成片滤镜一致；切换 1080P60、4K30、4K60、HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。 |
| 视频 / Video | 功能 / Feature | 工具栏 / Toolbar | Log 视频 | ✗ | ✗ | ✗ | Main: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在视频 Toolbar 开启 Log，按支持规格录制样片，确认入口、编码/位深、颜色曲线、LUT 还原、相册识别和不支持规格的置灰/提示。 |
| 视频 / Video | 功能 / Feature | 工具栏 / Toolbar | Style | ✓ | ✓ | ✓ |  | 已确认 | Product | 在 1080P30 下验证入口、预览、成片和 Preset；切换其他帧率、分辨率或 HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。 |
| 视频 / Video | 功能 / Feature | 工具栏 / Toolbar | 录影灯 / Recording Light | ✓ | ✓ | ✗ | Front: Nothing 品牌项目的录影灯默认支持范围为后置摄像头，Front 不在默认范围。 | 已确认 | Product | 分别使用每个后置摄像头开始、暂停/停止录制，确认录影灯按定义亮起/闪烁并及时关闭；检查切换模式、锁屏、来电或异常退出后无错误残留。 |
| 视频 / Video | 功能 / Feature | 工具栏 / Toolbar | 视频曝光调节 / 视频白平衡调节 | TBD | TBD | TBD |  | 待确认 | Product | 入口是“视频录制界面下拉菜单”，需要 tree 中新增 Video Toolbar 子区，还是复用 Toolbar？ |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 1080P 30FPS | ✓ | ✓ | ✓ |  | 已确认 | SE | 切到视频模式，分别选择 1080P 30FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 1080P 30FPS HLG | ✓ | ✓ | TBD |  | 待确认 | SE | 切到视频模式，分别选择 1080P 30FPS HLG，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 1080P 60FPS | ✗ | ✗ | ✗ | Main: 26111 Base 项目配置标注无 1080P60。；UW: 26111 Base 项目配置标注无 1080P60。；Front: 26111 Base 项目配置标注无 1080P60。 | 已确认 | SE | 切到视频模式，分别选择 1080P 60FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 1080P 60FPS HLG | ✗ | ✗ | ✗ | Main: 26111 Base 项目配置标注无 1080P60。；UW: 26111 Base 项目配置标注无 1080P60。；Front: 26111 Base 项目配置标注无 1080P60。 | 已确认 | SE | 切到视频模式，分别选择 1080P 60FPS HLG，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 4K 30FPS | ✗ | TBD | ✓ | Main: 26111 Base 项目配置标注无通用 4K；当前仅前置 4K PRD 明确进入评估。 | 待确认 | SE | 切到视频模式，分别选择 4K 30FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 4K 30FPS HLG | ✗ | TBD | TBD | Main: 26111 Base 项目配置标注无通用 4K；当前仅前置 4K PRD 明确进入评估。 | 待确认 | SE | 切到视频模式，分别选择 4K 30FPS HLG，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 4K 60FPS | ✗ | ✗ | ✗ | Main: 26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。；UW: 26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。；Front: 26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。 | 已确认 | SE | 切到视频模式，分别选择 4K 60FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 视频规格 / Video Specs | 4K 60FPS HLG | ✗ | ✗ | ✗ | Main: 26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。；UW: 26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。；Front: 26111 Base 项目配置标注无 4K/4K60；前置 4K PRD 也锁定 30fps。 | 已确认 | SE | 切到视频模式，分别选择 4K 60FPS HLG，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性、发热和降帧提示。 |
| 视频 / Video | 功能 / Feature | 变焦 / Zoom | ISZ / In Sensor Zoom | ✗ | ✗ | ✗ | Main: 视频切换 ISZ setting 会造成效果跳变并增加功耗，因此项目不开放视频 ISZ。；UW: 视频切换 ISZ setting 会造成效果跳变并增加功耗，因此项目不开放视频 ISZ。；Front: 视频切换 ISZ setting 会造成效果跳变并增加功耗，因此项目不开放视频 ISZ。 | 已确认 | SE | 逐个摄像头进入视频模式并跨倍率变焦，确认不进入 ISZ setting，且不提供视频无损变焦点。 |
| 视频 / Video | 功能 / Feature | 变焦 / Zoom | OIS | ✓ | ✗ | ✗ | UW: 该摄像头没有 OIS 硬件。；Front: 该摄像头没有 OIS 硬件。 | 已确认 | SE | 查硬件物料和驱动日志确认 OIS 初始化；在当前模式使用对应摄像头手持拍摄，验证稳定性，并检查 OIS/EIS 叠加与模式切换。 |
| 视频 / Video | 功能 / Feature | 变焦 / Zoom | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 是否把 SAT 体验优化作为独立项目需求，还是只更新 SAT KB 的验证方法和风险？ |
| 视频 / Video | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 视频 / Video | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 视频 / Video | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | TBD | TBD |  | 待确认 | Product | 在单人、多人、逆光、口罩/墨镜等场景下预览，确认人脸框和相关策略稳定。 |
| 视频 / Video | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 视频 / Video | 功能 / Feature | 风格-滤镜 / Style-Filter | 风格-滤镜 / Style-Filter | TBD | TBD | ✓ |  | 待确认 | Product | 在 1080P30 下验证预览和成片滤镜一致；切换 1080P60、4K30、4K60、HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。 |
| 视频 / Video | 功能 / Feature | 风格-调色 / Style-Tuning | 风格-调色 / Style-Tuning | TBD | TBD | ✓ |  | 待确认 | Product | 在 1080P30 下验证入口、预览、成片和 Preset；切换其他帧率、分辨率或 HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。 |
| 视频 / Video | 功能 / Feature | 风格-调色盘 / Style-Tuning Palette | 风格-调色盘 / Style-Tuning Palette | TBD | TBD | ✓ |  | 待确认 | Product | 在 1080P30 下验证调色盘交互、预览和成片；切换其他视频规格时确认入口禁用、隐藏或提示切回 1080P30。 |
| 视频 / Video | 算法 / Algorithm | 实时算法 / Realtime Algorithm | HLG / HDR 规格 | TBD | TBD | TBD |  | 待确认 | SE | 按摄像头和规格确认 HLG 入口、sensor mode、编码、屏幕提亮、温升和稳定性 |
| 视频 / Video | 算法 / Algorithm | 实时算法 / Realtime Algorithm | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 变焦跨镜头点；确认 SAT/硬切、亮度/色彩/视角过渡，并验证无 Fallback 时的近焦行为 |
| 视频 / Video | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Video EIS | ✓ | ✓ | ✓ |  | 已确认 | SE | 1080P30 手持录制；确认稳定、视角裁切和 OIS/EIS 叠加 |
| 视频 / Video | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Video HDR 算法 | ✗ | ✗ | ✗ | Main: 26111 当前项目不提供 Video HDR 算法链路。；UW: 26111 当前项目不提供 Video HDR 算法链路。；Front: 26111 当前项目不提供 Video HDR 算法链路。 | 已确认 | SE | 对支持摄像头逐项验证 1080P30/60、4K30/60，确认 Sensor mode、HDR 编码/元数据、动态范围、EIS/变焦/风格/Log 互斥以及功耗温升；不支持摄像头确认入口不可用。 |
| 视频 / Video | 算法 / Algorithm | 实时算法 / Realtime Algorithm | 视频夜景 | ✓ | ✓ | ✓ |  | 已确认 | SE | 暗光录像；确认噪声和帧率稳定 |
| 夜景 / Night | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | TBD | TBD | TBD |  | 待确认 | Product | 在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。 |
| 夜景 / Night | 功能 / Feature | 工具栏 / Toolbar | Flash | ✗ | ✗ | ✗ | Main: 夜景模式依赖环境光长曝光和多帧合成，不开放 LED Flash、Torch 或前置屏幕补光。；UW: 夜景模式依赖环境光长曝光和多帧合成，不开放 LED Flash、Torch 或前置屏幕补光。；Front: 夜景模式依赖环境光长曝光和多帧合成，不开放 LED Flash、Torch 或前置屏幕补光。 | 已确认 | Product | 进入夜景模式确认 Flash 入口隐藏或不可用；从照片模式携带不同 Flash 状态切入夜景，确认状态不继承且拍摄过程不会触发 LED、Torch 或屏幕补光。 |
| 夜景 / Night | 功能 / Feature | 工具栏 / Toolbar | Photo Style | ✓ | ✓ | ✗ | Front: Photo Style PRD 当前范围为后置自然/鲜明风格，前置风格未纳入本期。 | 已确认 | Product | Photo Style 与 Filter、Tuning、Preset 的互斥/叠加顺序需在 KB 中写清。 |
| 夜景 / Night | 功能 / Feature | 工具栏 / Toolbar | Ultra HDR | ✗ | ✗ | ✓ | Main: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 夜景 / Night | 功能 / Feature | 变焦 / Zoom | OIS | ✓ | ✗ | ✗ | UW: 该摄像头没有 OIS 硬件。；Front: 该摄像头没有 OIS 硬件。 | 已确认 | SE | 查硬件物料和驱动日志确认 OIS 初始化；在当前模式使用对应摄像头手持拍摄，验证稳定性，并检查 OIS/EIS 叠加与模式切换。 |
| 夜景 / Night | 功能 / Feature | 变焦 / Zoom | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 是否把 SAT 体验优化作为独立项目需求，还是只更新 SAT KB 的验证方法和风险？ |
| 夜景 / Night | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 在对应模式点击默认变焦点并拖动变焦条，确认倍率范围、镜头切换、画质和稳定性符合项目规格。 |
| 夜景 / Night | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 夜景 / Night | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | TBD | TBD |  | 待确认 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 夜景 / Night | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 取帧策略 / Frame Capture Strategy | PZL | TBD | TBD | TBD |  | 待确认 | SE | 结合算法 tag 或日志确认按下快门后的取帧起点、帧数和时序，并检查快门延迟、运动拖影及成片效果。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | Remosaic | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。 | 已确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | Ultra HDR | ✓ | ✓ | ✓ |  | 已确认 | SE | 检查文件编码和 gain map / 元数据，并在支持 Ultra HDR 与仅支持 SDR 的查看器中验证显示兼容性 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 人脸畸变矫正 | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 光学畸变矫正 | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 多帧降噪 / MFNR | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 极夜 | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超分 / Super Resolution（SR） | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超级夜景 | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超级夜景+美颜 | TBD | TBD | TBD |  | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 夜景 / Night | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Photo EIS | TBD | TBD | TBD |  | 待确认 | SE | 在项目定义的高倍率手持场景拍摄，确认取景稳定、裁切范围、OIS/EIS 叠加关系和成片清晰度。 |
| 夜景 / Night | 算法 / Algorithm | 实时算法 / Realtime Algorithm | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 变焦跨镜头点；确认 SAT/硬切、亮度/色彩/视角过渡，并验证无 Fallback 时的近焦行为 |
| 夜景 / Night | 算法 / Algorithm | 实时算法 / Realtime Algorithm | TF SN / Super Night | ✓ | ✓ | ✓ |  | 已确认 | SE | luxindex 进入夜景阈值后触发；确认 HDR 关闭 |
| 夜景 / Night | 算法 / Algorithm | 自然质感人像 / Natural Texture Portrait | FRT / 人像清晰度提升 | ✓ | ✓ | ✓ |  | 已确认 | SE | 逐模式、逐摄像头拍摄单人/多人、远近人脸、侧脸、遮挡和低照样张，结合算法 tag 确认 FRT 生效，并检查细节提升、身份特征保持、伪影和过度锐化。 |
| 慢动作 / Slow Motion | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | TBD | TBD | TBD |  | 待确认 | Product | 在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。 |
| 慢动作 / Slow Motion | 功能 / Feature | 慢动作规格 / Slow Motion Specs | 1080P 120FPS | TBD | TBD | TBD |  | 待确认 | SE | 切到慢动作模式，选择 1080P 120FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。 |
| 慢动作 / Slow Motion | 功能 / Feature | 慢动作规格 / Slow Motion Specs | 1080P 240FPS | TBD | TBD | TBD |  | 待确认 | SE | 切到慢动作模式，选择 1080P 240FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。 |
| 慢动作 / Slow Motion | 功能 / Feature | 慢动作规格 / Slow Motion Specs | 1080P 30FPS | TBD | TBD | TBD |  | 待确认 | SE | 切到慢动作模式，选择 1080P 30FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。 |
| 慢动作 / Slow Motion | 功能 / Feature | 慢动作规格 / Slow Motion Specs | 720P 120FPS | TBD | TBD | TBD |  | 待确认 | SE | 切到慢动作模式，选择 720P 120FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。 |
| 慢动作 / Slow Motion | 功能 / Feature | 慢动作规格 / Slow Motion Specs | 720P 240FPS | TBD | TBD | TBD |  | 待确认 | SE | 切到慢动作模式，选择 720P 240FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。 |
| 慢动作 / Slow Motion | 功能 / Feature | 慢动作规格 / Slow Motion Specs | 720P 480FPS | TBD | TBD | TBD |  | 待确认 | SE | 切到慢动作模式，选择 720P 480FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、播放倍率、稳定性和发热。 |
| 慢动作 / Slow Motion | 功能 / Feature | 工具栏 / Toolbar | 1080P@ 120fps | ✓ | ✗ | ✗ | UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 慢动作 / Slow Motion | 功能 / Feature | 工具栏 / Toolbar | Flash | ✗ | ✗ | ✗ | Main: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 前置无后置闪光灯/Glyph 硬件链路。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 慢动作 / Slow Motion | 功能 / Feature | 工具栏 / Toolbar | 录影灯 / Recording Light | ✓ | ✓ | ✗ | Front: Nothing 品牌项目的录影灯默认支持范围为后置摄像头，Front 不在默认范围。 | 已确认 | Product | 分别使用每个后置摄像头开始、暂停/停止录制，确认录影灯按定义亮起/闪烁并及时关闭；检查切换模式、锁屏、来电或异常退出后无错误残留。 |
| 慢动作 / Slow Motion | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 在对应模式点击默认变焦点并拖动变焦条，确认倍率范围、镜头切换、画质和稳定性符合项目规格。 |
| 慢动作 / Slow Motion | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 慢动作 / Slow Motion | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | TBD | TBD |  | 待确认 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 慢动作 / Slow Motion | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 慢动作 / Slow Motion | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Video EIS | ✓ | ✓ | ✓ |  | 已确认 | SE | 在支持规格下手持录制，确认开启/关闭视频防抖后的稳定性、视角裁切、果冻效应和发热功耗符合规格。 |
| 全景 / Panorama | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 全景 / Panorama | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 全景 / Panorama | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 专业 / Expert | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | Product | 在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。 |
| 专业 / Expert | 功能 / Feature | 模式栏 / Mode Switch | Expert Mode 2.0 | ✓ | ✓ | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 已确认本地缓存标题为 Camera 5.1 - 照片专业模式 2.0；内部文档信息仍写 4.2，应以 5.1 文档标题/目录为准。 |
| 专业 / Expert | 功能 / Feature | 工具栏 / Toolbar | Flash | ✓ | ✓ | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 专业 / Expert | 功能 / Feature | 工具栏 / Toolbar | Photo Style | ✓ | ✓ | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | Photo Style 与 Filter、Tuning、Preset 的互斥/叠加顺序需在 KB 中写清。 |
| 专业 / Expert | 功能 / Feature | 工具栏 / Toolbar | 各项专业模式参数极值范围 | ✓ | ✓ | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | SE | 逐个后置摄像头读取并记录 HAL 的 sensitivity/exposure range，验证 ISO 最小值、最大值及边界档位可正常预览和拍摄；验证 WB/AWB 可从 2300K 调至 10000K；同时检查快门、EV、Focus 的首尾值、步进、显示和成片一致性。 |
| 专业 / Expert | 功能 / Feature | 变焦 / Zoom | OIS | ✓ | ✗ | ✗ | UW: 该摄像头没有 OIS 硬件。；Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 查硬件物料和驱动日志确认 OIS 初始化；在当前模式使用对应摄像头手持拍摄，验证稳定性，并检查 OIS/EIS 叠加与模式切换。 |
| 专业 / Expert | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | Product | 在对应模式点击默认变焦点并拖动变焦条，确认倍率范围、镜头切换、画质和稳定性符合项目规格。 |
| 专业 / Expert | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 专业 / Expert | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 专业 / Expert | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 专业 / Expert | 算法 / Algorithm | 取帧策略 / Frame Capture Strategy | PZL | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | SE | 结合算法 tag 或日志确认按下快门后的取帧起点、帧数和时序，并检查快门延迟、运动拖影及成片效果。 |
| 专业 / Expert | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 光学畸变矫正 | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | SE | 按项目算法规格拍摄典型场景，确认成片效果、耗时、分辨率、功耗和异常恢复符合规格。 |
| 专业 / Expert | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Photo EIS | TBD | TBD | ✗ | Front: 专业模式不支持前置摄像头，因此该功能在 Front 不适用。 | 待确认 | SE | 在项目定义的高倍率手持场景拍摄，确认取景稳定、裁切范围、OIS/EIS 叠加关系和成片清晰度。 |
| 前后双录 / Dual View Video | 功能 / Feature | 模式栏 / Mode Switch | 前后双录 | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入前后双录，验证镜头组合、布局、文件输出和录制稳定性。 |
| 前后双录 / Dual View Video | 功能 / Feature | 模式栏 / Mode Switch | 录制中前后镜头切换 | ✓ | ✓ | ✓ |  | 已确认 | Product | 录制中切换前后镜头，确认不中断、音画同步、文件正常。 |
| 前后双录 / Dual View Video | 功能 / Feature | 工具栏 / Toolbar | 录影灯 / Recording Light | ✓ | ✓ | ✗ | Front: Nothing 品牌项目的录影灯默认支持范围为后置摄像头，Front 不在默认范围。 | 已确认 | Product | 分别使用每个后置摄像头开始、暂停/停止录制，确认录影灯按定义亮起/闪烁并及时关闭；检查切换模式、锁屏、来电或异常退出后无错误残留。 |
| 前后双录 / Dual View Video | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 前后双录 / Dual View Video | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 前后双录 / Dual View Video | 功能 / Feature | 预览框 / Preview | 前后双录主副互换 / 小窗大小 | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入前后双录，切换主副画面并调整小窗大小，录制后确认画面布局和文件结果一致。 |
| 前后双录 / Dual View Video | 功能 / Feature | 预览框 / Preview | 前后双录后置镜头选择 | ✓ | ✓ | ✗ | Front: 依赖长焦/高倍率链路，该摄像头不在支持范围。 | 已确认 | Product | 进入前后双录，在预览中切换后置镜头，确认可选镜头、预览布局、录制结果和切换状态符合规格。 |
| 前后双录 / Dual View Video | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 前后双录 / Dual View Video | 功能 / Feature | 风格-滤镜 / Style-Filter | 风格-滤镜 / Style-Filter | TBD | TBD | ✓ |  | 待确认 | Product | 在 1080P30 下验证预览和成片滤镜一致；切换 1080P60、4K30、4K60、HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。 |
| 前后双录 / Dual View Video | 功能 / Feature | 风格-调色 / Style-Tuning | 风格-调色 / Style-Tuning | TBD | TBD | ✓ |  | 待确认 | Product | 在 1080P30 下验证入口、预览、成片和 Preset；切换其他帧率、分辨率或 HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。 |
| 前后双录 / Dual View Video | 功能 / Feature | 风格-调色盘 / Style-Tuning Palette | 风格-调色盘 / Style-Tuning Palette | TBD | TBD | ✓ |  | 待确认 | Product | 在 1080P30 下验证调色盘交互、预览和成片；切换其他视频规格时确认入口禁用、隐藏或提示切回 1080P30。 |
| 前后双录 / Dual View Video | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Video EIS | ✓ | ✓ | ✓ |  | 已确认 | SE | 在支持规格下手持录制，确认开启/关闭视频防抖后的稳定性、视角裁切、果冻效应和发热功耗符合规格。 |
| 高像素 / High Resolution | 功能 / Feature | AE/AF | 自动对焦-自动曝光 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。 |
| 高像素 / High Resolution | 功能 / Feature | 模式栏 / Mode Switch | 200MP | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 进入高像素模式选择 200MP，逐个支持摄像头拍摄并确认入口、分辨率、处理耗时、RAW HDR/Ultra 标记和成片画质。 |
| 高像素 / High Resolution | 功能 / Feature | 模式栏 / Mode Switch | 200MP Ultra | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 进入高像素模式选择 200MP Ultra，逐个支持摄像头拍摄并确认入口、分辨率、处理耗时、RAW HDR/Ultra 标记和成片画质。 |
| 高像素 / High Resolution | 功能 / Feature | 模式栏 / Mode Switch | 50MP | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 进入高像素模式选择 50MP，逐个支持摄像头拍摄并确认入口、分辨率、处理耗时、RAW HDR/Ultra 标记和成片画质。 |
| 高像素 / High Resolution | 功能 / Feature | 工具栏 / Toolbar | Flash | ✗ | ✗ | ✗ | Main: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 更新为 nothing 项目，支持 glyph |
| 高像素 / High Resolution | 功能 / Feature | 工具栏 / Toolbar | Photo Style | ✓ | ✓ | ✗ | Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | Photo Style 与 Filter、Tuning、Preset 的互斥/叠加顺序需在 KB 中写清。 |
| 高像素 / High Resolution | 功能 / Feature | 工具栏 / Toolbar | 风格-滤镜 / Style-Filter | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 高像素 / High Resolution | 功能 / Feature | 变焦 / Zoom | OIS | ✓ | ✗ | ✗ | UW: 该摄像头没有 OIS 硬件。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 查硬件物料和驱动日志确认 OIS 初始化；在当前模式使用对应摄像头手持拍摄，验证稳定性，并检查 OIS/EIS 叠加与模式切换。 |
| 高像素 / High Resolution | 功能 / Feature | 变焦 / Zoom | 变焦 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 高像素 / High Resolution | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 高像素 / High Resolution | 功能 / Feature | 预览框 / Preview | 人脸检测 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 高像素 / High Resolution | 功能 / Feature | 预览框 / Preview | 脏污检测 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 高像素 / High Resolution | 算法 / Algorithm | 取帧策略 / Frame Capture Strategy | PZL | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 结合算法 tag 或日志确认按下快门后的取帧起点、帧数和时序，并检查快门延迟、运动拖影及成片效果。 |
| 高像素 / High Resolution | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | Remosaic | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 逐摄像头、逐高像素档位并覆盖高亮/中亮/低照场景拍摄，结合 Sensor mode 和算法 tag 确认实际路径、输出分辨率、耗时、内存及伪色/摩尔纹。 |
| 高像素 / High Resolution | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 超分 / Super Resolution（SR） | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 在 SR 生效边界的前一档、边界点和后一档分别拍摄细节目标，结合算法 tag 确认实际生效焦段，并检查清晰度、伪影、耗时和功耗。 |
| 高像素 / High Resolution | 算法 / Algorithm | 后处理算法 / Post-processing Algorithm | 高像素场景自适应链路 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 分亮度和动态范围拍摄，确认实际链路、输出分辨率、耗时、内存和产品选项映射 |
| 高像素 / High Resolution | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Photo EIS | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 在项目定义的高倍率手持场景拍摄，确认取景稳定、裁切范围、OIS/EIS 叠加关系和成片清晰度。 |
| 高像素 / High Resolution | 算法 / Algorithm | 自然质感人像 / Natural Texture Portrait | FRT / 人像清晰度提升 | ✓ | ✗ | ✗ | UW: 依赖高像素 sensor 输出或 remosaic 链路，该摄像头不满足规格。；Front: 高像素模式不支持前置摄像头，因此该功能在 Front 不适用。 | 已确认 | SE | 逐模式、逐摄像头拍摄单人/多人、远近人脸、侧脸、遮挡和低照样张，结合算法 tag 确认 FRT 生效，并检查细节提升、身份特征保持、伪影和过度锐化。 |
| 延时摄影 / Timelapse | 功能 / Feature | 工具栏 / Toolbar | 4K | ✓ | ✗ | ✗ | UW: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。；Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 延时摄影 / Timelapse | 功能 / Feature | 工具栏 / Toolbar | Flash | ✓ | ✓ | ✗ | Front: 前置无后置闪光灯/Glyph 硬件链路。 | 已确认 | Product | 在对应模式打开顶部工具栏，确认入口、选项、状态保持，以及对成片/录制结果的影响符合规格。 |
| 延时摄影 / Timelapse | 功能 / Feature | 工具栏 / Toolbar | 录影灯 / Recording Light | ✓ | ✓ | ✗ | Front: Nothing 品牌项目的录影灯默认支持范围为后置摄像头，Front 不在默认范围。 | 已确认 | Product | 分别使用每个后置摄像头开始、暂停/停止录制，确认录影灯按定义亮起/闪烁并及时关闭；检查切换模式、锁屏、来电或异常退出后无错误残留。 |
| 延时摄影 / Timelapse | 功能 / Feature | 变焦 / Zoom | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 是否把 SAT 体验优化作为独立项目需求，还是只更新 SAT KB 的验证方法和风险？ |
| 延时摄影 / Timelapse | 功能 / Feature | 变焦 / Zoom | 变焦 | TBD | TBD | TBD |  | 待确认 | Product | 检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。 |
| 延时摄影 / Timelapse | 功能 / Feature | 预览框 / Preview | ASD / AI场景检测 | TBD | TBD | TBD |  | 待确认 | Product | 使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。 |
| 延时摄影 / Timelapse | 功能 / Feature | 预览框 / Preview | 人脸检测 | TBD | TBD | TBD |  | 待确认 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 延时摄影 / Timelapse | 功能 / Feature | 预览框 / Preview | 脏污检测 | TBD | TBD | TBD |  | 待确认 | Product | 制造镜头脏污场景，确认提示出现、消失和误触发情况。 |
| 延时摄影 / Timelapse | 算法 / Algorithm | 实时算法 / Realtime Algorithm | SAT / 平滑镜头切换 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | SE | 变焦跨镜头点；确认 SAT/硬切、亮度/色彩/视角过渡，并验证无 Fallback 时的近焦行为 |
| 延时摄影 / Timelapse | 算法 / Algorithm | 实时算法 / Realtime Algorithm | Video EIS | ✓ | ✓ | ✓ |  | 已确认 | SE | 在支持规格下手持录制，确认开启/关闭视频防抖后的稳定性、视角裁切、果冻效应和发热功耗符合规格。 |
| 通用 / Common | 预设 / Preset | 预设 / Preset | Preset | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入底部 Preset 区域，验证选择、保存、导入、分享和卡片展示。 |
| 通用 / Common | 预设 / Preset | 预设 / Preset | 顶部快捷保存入口 | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 按项目 FL 规格确认 `顶部快捷保存入口` 的入口、支持范围、默认值和结果表现。 |
| 通用 / Common | 设置 / Settings | 通用设置 / General Settings | Level | ✓ | ✓ | ✓ |  | 已确认 | Product | 开启后旋转设备，确认水平辅助显示和随姿态变化。 |
| 通用 / Common | 设置 / Settings | 通用设置 / General Settings | Mirror front camera | ✓ | ✓ | ✓ |  | 已确认 | Product | 切换后用前置拍摄，确认输出方向。 |
| 通用 / Common | 设置 / Settings | 通用设置 / General Settings | Save location | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入设置切换保存位置，确认照片/视频保存路径。 |
| 通用 / Common | 设置 / Settings | 通用设置 / General Settings | Shutter sound | ✓ | ✓ | ✓ |  | 已确认 | Product | 切换快门声并拍照验证；地区 SKU 验证强制策略。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | Auto Tone | ✓ | ✓ | ✗ | Front: 按当前项目硬件、PRD 或基线 FL，该摄像头不在支持范围。 | 已确认 | Product | 进入 Camera Settings 修改该项，返回对应模式后确认设置生效、持久化和默认值符合规格。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | Press and hold shutter | ✓ | ✓ | ✓ |  | 已确认 | Product | 切换选项后长按快门，确认行为符合设置。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | QR code scanner | ✓ | ✓ | ✓ |  | 已确认 | Product | 开启后对准二维码，确认识别浮层和点击跳转。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | Tap to take a photo | ✓ | ✓ | ✓ |  | 已确认 | Product | 开启后点击预览区域，确认触发拍照。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | Ultra XDR | ✓ | ✓ | ✓ |  | 已确认 | Product | 分别开启和关闭后拍摄高动态范围场景，检查 Ultra HDR 编码/gain map 是否随设置生效，并验证设置持久化。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | Watermark settings | ✓ | ✓ | ✓ |  | 已确认 | Product | 调整水印设置后拍照，确认成片水印内容和样式。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | 影像基调 / Image Tone | ✓ | ✓ | ✓ |  | 已确认 | Product | 首次启动相机验证影调提示；在 Settings > Photo 切换自然/标准，确认默认值和持久化，并逐摄像头验证预览与成片效果；检查各照片类模式 Toolbar 中不存在重复入口。 |
| 通用 / Common | 设置 / Settings | 照片设置 / Photo Settings | 色彩模式 / Color Mode | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入 Settings > Photo 切换色彩模式，确认各拍照类模式 Toolbar 中不存在该入口；逐摄像头拍摄并检查设置生效、默认值、持久化及与 Auto Tone、影像基调、滤镜/调色、Ultra HDR 的关系。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | Auto FPS | ✓ | ✓ | ✓ |  | 已确认 | Product | 切换 Off / Auto 30 / Auto 30&60，在不同光照场景录制并确认帧率策略。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | Power saving recording | ✓ | ✓ | ✓ |  | 已确认 | Product | 开启后开始录制并保持设备静止，确认预览屏幕关闭且录制不中断。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | Video encoding | ✓ | ✓ | ✓ |  | 已确认 | Product | 切换 H.264/H.265 后分别录制普通视频、慢动作、延时摄影和前后双录样片，确认文件编码、默认 H.265 策略、HLG 强制 H.265 以及异常提示符合规格。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | 前后双录分开保存 | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入 Settings > Video 切换前后双录分开保存，录制前后双录样片并确认文件数量、命名、音画同步和相册展示。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | 视频防抖开关 | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入 Settings > Video 切换视频防抖开关，在支持 EIS 的视频规格下录制并确认防抖开关生效；在不支持规格下确认置灰或隐藏策略。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | 锁定白平衡 | ✓ | ✓ | ✓ |  | 已确认 | Product | 开启锁定白平衡后在不同色温光源间移动录制，确认白平衡保持起始状态；关闭后确认 WB 正常收敛。 |
| 通用 / Common | 设置 / Settings | 视频设置 / Video Settings | 锁定镜头 | TBD | TBD | TBD |  | 待确认 | Product | 开启锁定镜头后开始录制，跨镜头倍率点变焦，确认不发生物理镜头切换且录制不中断。 |
| 通用 / Common | 设置 / Settings | 帮助与反馈 / Help & Support | Tips and feedback | ✓ | ✓ | ✓ |  | 已确认 | Product | 进入 Camera Settings 点击 Tips and feedback，确认跳转系统帮助/反馈入口，并能返回 Camera。 |
| 通用 / Common | 小组件 / Widget | 小组件 / Widget | Preset Widget | ✓ | ✓ | ✓ |  | 已确认 | Product | 添加或使用预装 Preset Widget，选择最多 5 个 Preset，点击不同卡片唤起相机，确认应用的 Preset、顺序同步、空状态和上限提示符合规格。 |
| 通用 / Common | 功能 / Feature | 模式栏 / Mode Switch | 模式栏 | ✓ | ✓ | ✓ |  | 已确认 | Product | 打开相机并滑动模式栏，确认项目要求的模式是否存在且能进入。 |
| 通用 / Common | 功能 / Feature | 工具栏 / Toolbar | 工具栏热区呼出 | TBD | TBD | TBD |  | 待确认 | Product | 快门形态、slider 字体属于视觉规范，是否明确不进 FL？右下角工具栏热区是否需要作为 Toolbar 交互能力进入 KB？ |
| 通用 / Common | 功能 / Feature | 预览框 / Preview | AI Preset 预览引导入口 / 场景推荐 | TBD | TBD | TBD |  | 待确认 | Product | 入口位置已确认在相机预览页、位于 preset 按键附近；仍需确认覆盖“所有模式/所有焦段”是否缩小为首版场景范围。 |
