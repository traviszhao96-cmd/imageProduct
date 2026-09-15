<!-- source: https://nothing-tech.sg.larksuite.com/docx/HIdPdtWOmotqKCxVBoBlPsvggNw | fetched: 2026-09-15 | revision: 460 -->
<title>【PRD】Camera 5.1 - 录像中拍照（VSS）效果提升</title>

# **此需求关闭**

## 决策内容

### 一、背景

VSS（录像中拍照）优化 需求于早期通过 77 人用户问卷及竞品分析验证需求成立，随后进入开发，目前尚未正式上线，处于开发验证阶段。



### 二、开发过程中暴露的核心问题

| 问题类别 | 现象描述 | 问题性质(是否架构性) | 修复难度/预估周期 | 备注 |
|-|-|-|-|-|
| 流畅性/掉帧 | 任意分辨率或叠加滤镜下,录像过程中拍照存在掉帧,连续拍照越多掉帧越严重;即便改为"上一张保存完才允许下一次拍照"的节流方案,单次拍照仍掉帧 |  | 风险较大，6g 差异比较难处理 |  |
| FOV 裁切偏差 | uw 下，VSS 拍照取的是带畸变的 full size raw 图,与预览侧(Morpho EIS)畸变计算路径不一致,导致裁切后存在 FOV 偏差 | 裁剪框是预估值，无法保证准确性 | 解不了 | 但是差异不算很大 |
| 低光画质效果 | 光线较差场景下,当前裁切方案输出效果实测不如 4K 视频截帧(PM 走查发现) | 单帧画质限制 |  |  |
| 高倍率清晰度问题 |  |  |  |  |



### 三、继续投入 vs 现在停止的判断

- 继续投入需要解决：①掉帧的性能瓶颈 ②预览与拍照链路的畸变模型统一,带来的画质效果提升是否能达到可用标准,目前判断存疑。
- 更关键的是:**已有更优的替代方案**——同样的交互位置、同样的用户操作路径,改为可选拍摄 Live 图,可直接复用当前 4K Live 这一 KSP 卖点,优先级明显更高,资源应向此倾斜。

### 四、本次会议需要对齐的 Ask



1. 是否同意 VSS 现阶段停止投入，资源转向 4K Live 可选拍摄方案，或其他更高优先级需求。
2. 已投入的开发工作是否有可复用部分？
3. 明确一点对外/对上的说明口径：**当前技术方案无法达到可用体验，** VSS优化 已有更优替代实现路径。
4.  **各模块意见**



产品：当前方案很难达到可用体验，建议释放资源到优先级更高的功能上 - NG

APP：效果不行则觉得没有意义继续进行 - NG

HAL：效果不行则觉得没有意义继续进行-NG

Tuning：因性能和内存压力，vss无法做多帧降噪，只能走单帧拍照；室外vss细节有收益，但是室内和暗环境以及高倍zoom 画质劣化无法解决---NG

测试：现阶段验证来看，掉帧问题不能接受，所以 - NG





# 0. 文档信息

| **字段** | **内容** |
|-|-|
| 文档标题 | 【PRD】录像中拍照（VSS）效果提升 |
| 项目代号 | 26111 / 26121 |
| 作者 | Tiger Xu |
| 更新时间 | 2026/6/5 |
| 上市时间 | 未上市 |
| 销售地区 | India / Global |
| 审核人 | — |

---

# 变更日志

| **时间** | **版本号** | **变更人** | **主要变更内容** |
|-|-|-|-|
| 2026/6/5 | v0.1 | Tiger Xu | 创建文档 |

---

# 需求背景

### 2.1 产品 / 数据现状

当前 VSS（录像中拍照）实现方式为视频截帧：1080P 下输出仅 2MP，4K 下输出 8MP，画质显著低于单帧拍照水平。

<table><colgroup><col/><col/></colgroup><thead><tr><th><b>25111P ——视频下拍照和单帧拍照的放大对比图</b></th><th>原图</th></tr></thead><tbody><tr><td><img name="image.png" alt="The image shows three screenshots of a red envelope with &#34;心想事成&#34; written on it, placed among oranges and green leaves. The red envelope has patterns of apples, a red envelope, and a flower. This photo is related to the context discussing the effect enhancement of taking photos during video recording (VSS) in Camera 5.1, where users capture moments by pressing the VSS shutter, aiming to save them as photos." caption="&#xA;" mime="image/png" scale="1.000000" src="TJGGbJ9sqoo5SpxGpsMl5LrHgRc"/><grid><column width-ratio="0.333333"><p>当前 4K录像VSS</p></column><column width-ratio="0.333333"><p>单帧拍照</p></column><column width-ratio="0.333333"><p>当前 1080P录像VSS</p></column></grid></td><td><grid><column width-ratio="0.333333"><img name="25111p_vss_4k_1.jpg" caption="4k vss&#xA;" mime="image/jpeg" scale="0.337963" src="D7Snby8b8opTlfxEemrlbuhEgwb"/></column><column width-ratio="0.333333"><img name="25111p_vss_a_1.jpg" caption="单帧拍照&#xA;" mime="image/jpeg" scale="0.316840" src="K9lVbdD6SoN2qQxLZMjlaAXdgSh"/></column><column width-ratio="0.333333"><img name="25111p_vss_fhd_1.jpg" caption="1080P vss&#xA;" mime="image/jpeg" scale="0.675926" src="XISebtkclo1oMQxPL6TlHDz6gog"/></column></grid></td></tr><tr><td><img name="image.png" alt="The image shows three side-by-side screenshots of a display of cups with &#34;SHENZHEN&#34; and &#34;CHINA&#34; printed on them, placed on a shelf with boxes and a mat. The left screenshot is labeled &#34;25111P——视频下拍照和单帧拍照的放大对比图|原图&#34;, the middle one is &#34;当前4K录像VSS&#34;, and the right one is &#34;当前1080P录像VSS&#34;. These screenshots are used to compare the effects of video and single-frame photo shooting under different resolutions, as mentioned in the context about the demand for improving the VSS effect in Camera 5.1." caption="&#xA;" mime="image/png" scale="1.000000" src="Pzz8bjmx8oXNgOxJtZylU1RDgtg"/><grid><column width-ratio="0.333333"><p>当前 4K录像VSS</p></column><column width-ratio="0.333333"><p>单帧拍照</p></column><column width-ratio="0.333333"><p>当前 1080P录像VSS</p></column></grid></td><td><grid><column width-ratio="0.333333"><img name="25111p_vss_4k_3.jpg" caption="4k vss&#xA;" mime="image/jpeg" scale="0.337963" src="RKg7bIg5VoZrN0x0P8ilGsxsgKd"/></column><column width-ratio="0.333333"><img name="25111p_vss_a_3.jpg" caption="单帧拍照&#xA;" mime="image/jpeg" scale="0.316840" src="DUErbn4q3ofsigxAFv5laEaSgNh"/></column><column width-ratio="0.333333"><img name="25111p_vss_fhd_3.jpg" caption="1080p vss&#xA;" mime="image/jpeg" scale="0.675926" src="UBVkbp3wSoG38XxMgJVljo05gnb"/></column></grid></td></tr></tbody></table>

用户在录视频时按下 VSS 快门，本质是一个**质量声明**：「我要把这个瞬间以照片的标准保存下来。」如果只是需要视频里的某一帧，用户不需要这个按钮——视频本身已包含所有帧，事后随时可截。VSS 的存在价值在于：**以照片级别的质量，捕捉用户在录像中看到的那个瞬间。** 当前截帧方案无法满足这一本质需求。



**埋点数据：**

- 印度用户 VSS 使用率是 Global 的 2 倍
- 在印度，46% 的视频用户会使用录像中拍照
- 印度用户平均每 9 次录像会触发 1 次 VSS

当前 4K VSS 实测清晰度在同价位竞品中处于末位；APP 端 Demo 已验证改为 9MP 单帧出图的基础可行性。



### 2.2 用户调研

调研方式：问卷（78 份有效回收，印度试用 & 社区用户）。

- 92% 受访者会使用 VSS；86% 对当前画质不满意或处于「凑合用」状态
- 使用场景集中于「不想错过瞬间」的高情绪场景（演唱会/赛事 82%，旅行风景 75%）
- 81% 倾向「宁可等待处理也要高质量」
- 仅 4% 对「VSS 照片清晰度高于视频」有负面感知——画质提升不存在感知风险
- 61%+ 用户对照片 FOV 比视频更宽有不同程度的负面感知

详见<cite doc-id="Ro5nwT7PYitQGDknLe4lneDMgUg" file-type="wiki" title="录像中拍照 功能用户问卷调研" type="doc"></cite>



### 2.3 竞品情况

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>层级</b></th><th vertical-align="middle"><b>机型</b></th><th vertical-align="middle"><b>出图方式</b></th><th vertical-align="middle"><b>分辨率</b></th><th vertical-align="middle"><b>更多</b></th><th vertical-align="middle"><b>FOV</b></th></tr></thead><tbody><tr><td rowspan="4" vertical-align="middle">旗舰参考</td><td>苹果 iPhone 17 Pro</td><td>拍照</td><td>7mp（动态裁切）</td><td>有一定拍照算法+XDR</td><td>与视频一致</td></tr><tr><td>三星 S25 Ultra</td><td>拍照</td><td>9mp</td><td>有一定拍照算法+XDR</td><td>与照片一致</td></tr><tr><td>华为 Pura 90</td><td>拍照</td><td>9mp</td><td>—</td><td>与照片一致</td></tr><tr><td>Vivo X300 Ultra</td><td>拍照</td><td>9mp</td><td>有一定拍照算法+XDR</td><td>与照片一致</td></tr><tr><td rowspan="3" vertical-align="middle">中端分化</td><td>OPPO Reno 16</td><td>视频截Live</td><td>同视频分辨率</td><td>—</td><td>与视频一致</td></tr><tr><td>荣耀 600</td><td>视频截Live</td><td>同视频分辨率</td><td>—</td><td>与视频一致</td></tr><tr><td>华为 Nova 16</td><td>拍照</td><td>9mp</td><td>—</td><td>与照片一致</td></tr><tr><td vertical-align="middle">中端普通</td><td>Vivo S60</td><td>视频截帧</td><td>同视频分辨率</td><td>—</td><td>与视频一致</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

**从演进方向看**，单帧路线正在从旗舰向中端下渗：三星和苹果已在旗舰上稳定运行多年；vivo 在 X300 Ultra 上引入独立拍照通路；华为今年 nova16 系列专项宣传录中拍照画质优化。



**结论：** 旗舰机型已全面采用单帧拍照路线，输出 9MP（苹果动态裁切至 7MP），部分叠加轻量算法与 XDR 效果。中端市场出现分化，OPPO、荣耀走视频截 Live Photo 路线，华为从 nova16 开始优化，也走拍照路线，Vivo S60 等仍为视频截帧无优化。**清晰度是当前中端 录像中拍照 的普遍短板，也是最直接的差距所在。**

---

# 需求目标

**核心目标：** 提升录像中拍照的拍照质量，用更佳的质量帮助用户留住瞬间。

完整的体验改善需同时满足以下三项，三者为不可分割的最小完整单元：

1. **照片该有的质量**：改为单帧拍照，统一输出 9MP；有性能余量时叠加 MFNR
2. **用户看到的那个画面**：照片视野（FOV）和色彩与视频预览保持一致
3. **捕捉准确的瞬间**：取帧时机准确，偏差可控

**预期效果：**

- 录像中拍照清晰度达到同档位最佳
- 照片视野、色彩与视频一致，能准确捕捉到想要的瞬间

---

# 需求范围

### 4.1 范围内

- **项目范围：** 26111 / 26121首次上项
- **模式范围：** 视频模式
- **出图逻辑：** 触发 VSS 时启动独立拍照流，不从视频流截帧
- **输出像素：** 统一 9MP（16:9），不随视频录制分辨率变化
- **FOV：** 拍照后裁切至与视频预览相同 FOV
- **色彩 / 影调：** 照片色温、亮度 follow 视频预览

<table><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th><b>项目</b></th><th><b>优先级</b></th><th>行为说明</th><th><b>备注</b></th><th>研发评估结论（6G&amp;8G分开）</th></tr></thead><tbody><tr><td>单帧拍照（9MP）</td><td>P0</td><td>触发 VSS 时启动独立拍照流，与视频流并行；1080P / 4K 统一输出 9MP（16:9）</td><td>APP 端 Demo 已验证可行</td><td>Ap：<cite type="user" user-id="ou_b4b23e5c6d5908a6fc7de29a84f7da3a" user-name="Neal Huang"></cite><br/>Tuning：<cite type="user" user-id="ou_7b21d02c54cdc8eb86b49e3c0635a011" user-name="John Li"></cite><br/>hal：<cite type="user" user-id="ou_99b4b6e081e4ca83820583d10a59d6ae" user-name="Delevin Yao"></cite><br/>sw：<cite type="user" user-id="ou_0f73f46ea1880c836c57b76143458281" user-name="Kenny Yuan"></cite></td></tr><tr><td>FOV 与录像对齐</td><td>P0</td><td>拍照后将 9MP 原图裁切至与视频预览相同 FOV；默认对齐，不提供用户自选</td><td>裁切逻辑需工程确认</td><td></td></tr><tr><td>色彩与录像对齐</td><td>P0</td><td>照片的 tuning 跟随视频预览</td><td>当前 Demo 饱和度偏高，需调优</td><td></td></tr><tr><td>MFNR</td><td>P1</td><td>进一步提升照片画质</td><td>单帧跑通后评估 26111 平台性能余量，可行则纳入本版本</td><td></td></tr><tr><td>保留滤镜效果</td><td>P1</td><td>视频滤镜效果保留至 VSS 照片</td><td>滤镜叠加冲突需逐一验证</td><td></td></tr><tr><td>取帧时刻偏差优化</td><td>P1</td><td>目标偏差 ≤ 200ms</td><td>重载场景帧率影响待测</td><td></td></tr></tbody></table>

### 4.2 范围外

- XDR 显示效果（仅旗舰竞品有此能力，后续版本评估）
- Motion Photo（可作为视频编辑导出功能独立评估，不属于 VSS 职责范围）
- 老项目回落

---

# 产品流程与交互

VSS 为视频录制中触发的瞬时操作，无复杂状态流转：

1. 用户进入视频模式，开始录制
2. 点击 VSS 快门按钮，触发独立拍照流，输出 9MP 单帧照片
3. 照片 FOV 自动裁切至与视频预览一致；色彩 / 影调与视频预览保持一致
4. 拍照完成，录像继续，照片存入相册

用户侧无新增交互入口，体验与当前一致，差异仅在输出结果质量上。



互斥说明

| 场景 | VSS行为 |
|-|-|
| 所有规格 SDR 录像 | 正常触发，单帧拍照 |
| 1080P 30帧，开启滤镜/调色录像 | 正常触发，单帧拍照，同时套上对应滤镜/调色 |
| 所有规格 HLG 录像 | 正常触发，单帧拍照 |



---

# 关键依赖与约束

（待补充，需与算法 / 平台团队确认）



内存性能风险

---

# 词条定义

（待补充）

---

# 埋点

（待补充）

---

# 指标与验收

### 9.1 成功指标

- 1080P 下 VSS 输出 9MP，清晰度成为同价位最优
- 4K 下 VSS 输出 9MP，清晰度追平 vivo T4R
- 照片 FOV 与视频预览一致，用户感知无画幅突变
- 照片色温 / 亮度与视频预览方向一致

### 9.2 验收标准

| **#** | **验收项** | **预期结果** |
|-|-|-|
| 1 | 1080P 视频中触发 VSS | 输出 9MP 照片（非 2MP 截帧） |
| 2 | 4K 视频中触发 VSS | 输出 9MP 照片（非 8MP 截帧） |
| 3 | VSS 照片 FOV | 与视频预览画幅一致，无明显变宽 |
| 4 | VSS 照片色温 / 亮度 | 与视频预览方向一致 |
| 5 | VSS 照片清晰度主观评级 | 优于同价位竞品截帧方案 |
| 6 | 触发 VSS 后视频帧率 | 无明显掉帧 |
| 7 | 取帧时刻偏差 | ≤ 200ms |
| 8 | 滤镜效果保留 | 视频滤镜在 VSS 照片中生效 |