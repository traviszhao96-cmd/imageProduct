# 003 26111 用户调研相关
source: CGpAdLYuzo531ox9n6Kl0elkgMe | revision: 7 | bytes: 27
CONTENT_STATUS: empty_or_placeholder
# 26111 用户调研相关

# 004 【26111】25MP 超清模式需求文档
source: Tvdkdo0eDop9lPxFcSllwzFVgDd | revision: 265 | bytes: 11332
## headings
# 25MP 超清模式需求文档
## 1. 背景与目标
### 需求背景
### 用户痛点/机会点
### 目标用户与场景
### 预期收益
### 行业 12MP vs 25MP <cite type="user" user-id="ou_bde858e2c287e45bb799791c3cea03c7" user-name="Alex Huang"></cite>
### 虹软算法说明
## 2. 功能定义
### 功能名称
### 功能描述
### 适用模式/入口--待定
### 范围说明（In Scope）
### 明确不做（Out of Scope）
## 3. 方案说明
### 核心策略
### 关键交互或流程
### 算法/画质策略
### 硬件或平台依赖
## 4. 关键依赖与约束
### 硬件依赖
### 算法依赖
### 软件平台依赖
### 跨团队依赖
### 合规或区域约束
## 5. 指标与验收
### 用户体验指标
### 画质指标
### 性能指标
### 稳定性指标
### 验收方式
## 6. 项目计划
### 关键里程碑
### 责任团队
### 版本计划
### 风险与兜底
## 7. 待确认/待补充信息
## 8. 初步评审
### 开发评审
### 测试评审
### 高风险项
### 需要补充的信息
## selected snippets
```
<title>【26111】25MP 超清模式需求文档</title>

# 25MP 超清模式需求文档

## 1. 背景与目标
```
```
# 25MP 超清模式需求文档

## 1. 背景与目标

### 需求背景
```
```
## 1. 背景与目标

### 需求背景

当前默认输出4合一12MP，且高像素选项仅提供 50MP。12MP有时无法释放sensor最大解析力，而高像素与hdr算法互斥，成片速度和存储占用大。用户在追求更高解析力的同时，对成片速度和存储占用较为敏感。行业竞品（iPhone、华为、OPPO）已布局中间档位高像素方案，其中 iPhone 将类似能力集成至默认模式，华为支持全焦段/暗光场景。
```
```
### 需求背景

当前默认输出4合一12MP，且高像素选项仅提供 50MP。12MP有时无法释放sensor最大解析力，而高像素与hdr算法互斥，成片速度和存储占用大。用户在追求更高解析力的同时，对成片速度和存储占用较为敏感。行业竞品（iPhone、华为、OPPO）已布局中间档位高像素方案，其中 iPhone 将类似能力集成至默认模式，华为支持全焦段/暗光场景。

### 用户痛点/机会点
```
```
当前默认输出4合一12MP，且高像素选项仅提供 50MP。12MP有时无法释放sensor最大解析力，而高像素与hdr算法互斥，成片速度和存储占用大。用户在追求更高解析力的同时，对成片速度和存储占用较为敏感。行业竞品（iPhone、华为、OPPO）已布局中间档位高像素方案，其中 iPhone 将类似能力集成至默认模式，华为支持全焦段/暗光场景。

### 用户痛点/机会点

-
```
```
### 用户痛点/机会点

- 
- 50MP 模式下 shot-to-shot 间隔较长，连拍体验受限，且无法支持hdr等算法
- 用户需要一档"画质优于默认、速度优于 50MP"的中间选项
```
```
- 
- 50MP 模式下 shot-to-shot 间隔较长，连拍体验受限，且无法支持hdr等算法
- 用户需要一档"画质优于默认、速度优于 50MP"的中间选项

### 目标用户与场景
```
```
- 50MP 模式下 shot-to-shot 间隔较长，连拍体验受限，且无法支持hdr等算法
- 用户需要一档"画质优于默认、速度优于 50MP"的中间选项

### 目标用户与场景

- **目标用户**：对画质有进阶要求但不愿牺牲拍摄效率的日常用户
```
```
### 目标用户与场景

- **目标用户**：对画质有进阶要求但不愿牺牲拍摄效率的日常用户
- **核心场景**：
```
```
- **目标用户**：对画质有进阶要求但不愿牺牲拍摄效率的日常用户
- **核心场景**：

  - 明亮户外/室内环境的主摄/长焦拍摄
  - 静态/慢速运动主体/人像
```
```
- **目标用户**：对画质有进阶要求但不愿牺牲拍摄效率的日常用户
- **核心场景**：

  - 明亮户外/室内环境的主摄/长焦拍摄
  - 静态/慢速运动主体/人像
  - 社交媒体分享前需要更高解析力的场景
```
```
- 静态/慢速运动主体/人像
  - 社交媒体分享前需要更高解析力的场景

### 预期收益

- 提升默认模式高像素档位使用率（替代现有 50MP 成为主力高像素选项）
```

# 005 供应商能力汇总
source: HecgdhPozofJ7IxRcglloihXgYf | revision: 30 | bytes: 24
CONTENT_STATUS: empty_or_placeholder
# 供应商能力汇总

# 006 【PRD】Camera 5.1 - 对焦/人脸/宠物识别框视觉动效优化
source: KujNdEhujoltg1x6xgAluzLpgdT | revision: 125 | bytes: 10159
## headings
# 前言
# 一、 版本信息
# 二、 变更日志
# 三、 需求背景
## 产品 / 数据现状
## 竞品分析
# 四、需求目标
### 五、 需求范围
## 需求列表&需求单
# 六、 功能详细说明
### 人脸识别框动效
### 点击对焦框动效优化
### 人像模式识别框高亮
### 宠物识别框
## 需求词条-不涉及
# 七、 非功能需求
# 八、 埋点
# 九、 项目规划
# 附录
## selected snippets
```
<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td><b>时间</b></td><td><b>版本号</b></td><td><b>变更人</b></td><td><b>主要变更内容</b></td></tr><tr><td>2026/1/13</td><td>1.0</td><td>Travis </td><td>梳理当前存在问题</td></tr><tr><td>2026/5/11</td><td>2.0</td><td>Travis </td><td><ol><li seq="1">根据澄清问题，更新确认需求细节</li><li>需求更新到 26111 的需求中</li></ol></td></tr></tbody></table>

# 三、 需求背景

## 产品 / 数据现状
```
```
# 三、 需求背景

## 产品 / 数据现状

当前相机中的各种识别框存在以下问题：
```
```
1. 人脸识别框简陋，且不稳定，只是一个细线方框，比较欠缺美感的同时，在识别到人脸后会不停跳动
2. 不支持宠物识别框，导致宠物的对焦准确性并不高，而该功能在iPhone和绝大多数安卓机上都支持
3. 点击对焦时，对焦框没有缩放的动画效果
4. 二维码识别框一次识别很多，而且也并不稳定，不方便用户点击跳转，看起来也混乱

## 竞品分析
```
```
<table><colgroup><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td></td><td>人脸框</td><td>宠物框</td><td>点击对焦</td><td>二维码</td><td>其他</td><td></td></tr><tr><td>iPhone</td><td>最多 9 个<br/>有较为平滑的切换弹跳动画<br/>有淡出的消失动画</td><td>只识别猫狗<br/>最多识别 7 个<br/>有较为平滑的切换弹跳动画<br/>有淡出的消失动画</td><td>快速的动画，淡入淡出效果<br/>锁定动效效果</td><td>只识别一个最大的<br/>有稳定动效</td><td>在人像模式下由白色框变为黄色的锁定动效<br/>照片/人像/视频的识别框都有所不同</td><td><grid><column width-ratio="0.680283"><img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmZjZGExNzUzZDljYTA0OWI0ZWIwMTgwMGMxNjg2MDZfZjQzZDEwMTllMjFkMWZiMTc1MTZmZGYyMGRmNzY0MjJfSUQ6NzYzODQ3NjYyMTM1NTYzNDQwNV8xNzgzNDA2MzA3OjE3ODM0MDk5MDdfVjM" mime="image/png" scale="0.201769" src="HmjBb70llou3PWxwMWjlTXJZgTg"/></column><column width-ratio="0.159859"><img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGM4ZmJmYjllMzYxYTJiYzYzNzg4NDQ5ZjBiMjU2ZjNfODUyNjE0OWM2ZWNkNGU3ZTc5OWNiY2Y3MmNlNzQ1ZmNfSUQ6NzYzODQ3NjYyMTA4Njk4NTk1MV8xNzgzNDA2MzA3OjE3ODM0MDk5MDdfVjM" mime="image/png" scale="0.955497" src="F3pSbc3CfoaA8WxSgNdl9DQGgya"/></column><column width-ratio="0.159859"><img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MGVhYzE5NzI2MmY4NTM0ZmM4MzJkN2YyMGQ3MjY0ZThfOGZiMWU1Yjk2ZmIwZWM3N2NiMjc1MmNjNGVhMTU2NGFfSUQ6NzYzODQ3NjYyMjUxMjg4NTQ3MV8xNzgzNDA2MzA3OjE3ODM0MDk5MDdfVjM" mime="image/png" scale="0.955497" src="GlHab89AqoJaZGx9DqilvDt1gwc"/></column></grid></td></tr><tr><td>OPPO</td><td>最多 6 个<br/>只有稳定动画，帧率较低<br/>没有淡入淡出的动画</td><td>只识别猫狗<br/>最多识别 5 个<br/>有稳定动画</td><td>淡入淡出动画<br/>锁定对焦动画<br/>帧率相比iPhone看起来更低</td><td>默认模式下不支持</td><td>人像和照片模式下的识别框有不同<br/>人像模式通过白色转为橙色，提示识别成功<br/>没有平滑的切换动画</td><td></td></tr><tr>
```
```
# 四、需求目标



### 五、 需求范围
```
```
### 五、 需求范围

> 可条理性地罗列需求范围或信息架构

1. 项目范围：纯软件需求，对硬件没有限制。预计分 2-3 期完成，均支持回落。
```
```
> 可条理性地罗列需求范围或信息架构

1. 项目范围：纯软件需求，对硬件没有限制。预计分 2-3 期完成，均支持回落。
2. 模式范围：覆盖所有模式
3. 焦段范围：覆盖所有焦段
```
```
1. 项目范围：纯软件需求，对硬件没有限制。预计分 2-3 期完成，均支持回落。
2. 模式范围：覆盖所有模式
3. 焦段范围：覆盖所有焦段
4. 老项目回落：支持回落，老项目默认 NOS 5.0 升级带出
```
```
1. 项目范围：纯软件需求，对硬件没有限制。预计分 2-3 期完成，均支持回落。
2. 模式范围：覆盖所有模式
3. 焦段范围：覆盖所有焦段
4. 老项目回落：支持回落，老项目默认 NOS 5.0 升级带出

## 需求列表&需求单
```
```
2. 模式范围：覆盖所有模式
3. 焦段范围：覆盖所有焦段
4. 老项目回落：支持回落，老项目默认 NOS 5.0 升级带出

## 需求列表&需求单
```
```
3. 焦段范围：覆盖所有焦段
4. 老项目回落：支持回落，老项目默认 NOS 5.0 升级带出

## 需求列表&需求单

<bitable table-id="tblCBKZy8DCB12lu" token="ZULBbVmOraoGt3sggT5lPcWvgof"></bitable>
```
```
## 需求列表&需求单

<bitable table-id="tblCBKZy8DCB12lu" token="ZULBbVmOraoGt3sggT5lPcWvgof"></bitable>

# 六、 功能详细说明
```

# 007 【PRD】Camera 5.1 - 相机设计改版
source: XOpvdfIjBoVwSPxq6QElp9W8gMg | revision: 84 | bytes: 8493
## headings
# 【PRD】Camera 5.1 - 相机设计改版
## 文档信息
## 背景
## 目标
## 目标用户与使用场景
### 4.1 目标用户
### 4.2 典型场景
## 需求范围
## 功能方案
### 6.1 快门按键视觉升级
#### 6.1.1 设计目标
#### 6.1.2 适用范围
#### 6.1.4 状态定义
### 6.2 右下角工具栏呼出入口
#### 6.2.1 问题定义
#### 6.2.2 设计目标
#### 6.2.3 交互要求
#### 6.2.4 视觉原则
### 6.3 Slider 字体统一优化
#### 6.3.1 目标范围
## 设计依赖
## 交互要求
## 版本与落地要求
## 非功能要求
### 10.1 性能
### 10.2 兼容性
## 验收标准
### 11.1 椭圆快门
### 11.2 工具栏呼出优化
### 11.3 Slider 字体统一
## selected snippets
```
- 文档状态：初稿
- 本次更新范围：

  - 快门按键视觉与动效升级：圆形快门升级为椭圆形快门
  - 相机右下角工具栏呼出方式优化：新增热区开关能力
  - 各类数字型 Slider 字体统一优化
```
```
## 背景

当前相机主界面在视觉层面仍存在以下问题：

- 快门按键采用传统圆形方案，底部视觉重心较强，占用纵向注意力，不利于释放取景区域的视觉空间
```
```
- 快门按键采用传统圆形方案，底部视觉重心较强，占用纵向注意力，不利于释放取景区域的视觉空间
- 工具栏呼出方式不够直观，用户在单手持机场景下调用效率不足
- 多个 Slider 中的数字字体风格不统一，辨识度和整体美感存在提升空间

随着 NOS 5.0 在 Phone3 上首发，相机主界面需要进一步强化品牌化视觉语言，提升交互一致性与高级感，并为后续升级项目建立统一设计基线。
```
```
随着 NOS 5.0 在 Phone3 上首发，相机主界面需要进一步强化品牌化视觉语言，提升交互一致性与高级感，并为后续升级项目建立统一设计基线。

## 目标

- 通过椭圆形快门重塑相机底部核心视觉焦点，释放更多取景视觉空间
```
```
## 目标

- 通过椭圆形快门重塑相机底部核心视觉焦点，释放更多取景视觉空间
- 优化快门动效，增强照片、视频等不同模式下的状态表达与操作反馈
- 优化右下角工具栏呼出方式，提升用户在热区内调出工具栏的易用性
```
```
- 通过椭圆形快门重塑相机底部核心视觉焦点，释放更多取景视觉空间
- 优化快门动效，增强照片、视频等不同模式下的状态表达与操作反馈
- 优化右下角工具栏呼出方式，提升用户在热区内调出工具栏的易用性
- 统一各类数字型 Slider 的字体表现，提升识别效率与整体界面美感
- 形成可在后续升级项目中复用的相机交互视觉规范
```
```
- 统一各类数字型 Slider 的字体表现，提升识别效率与整体界面美感
- 形成可在后续升级项目中复用的相机交互视觉规范

## 目标用户与使用场景

### 4.1 目标用户
```
```
## 目标用户与使用场景

### 4.1 目标用户

- 高频使用系统相机的普通用户
```
```
### 4.1 目标用户

- 高频使用系统相机的普通用户
- 偏好单手拍摄、快速切模式、快速调参数的用户
- 对产品视觉质感与交互反馈敏感的核心用户
```
```
- 高频使用系统相机的普通用户
- 偏好单手拍摄、快速切模式、快速调参数的用户
- 对产品视觉质感与交互反馈敏感的核心用户

### 4.2 典型场景
```
```
- 偏好单手拍摄、快速切模式、快速调参数的用户
- 对产品视觉质感与交互反馈敏感的核心用户

### 4.2 典型场景

- 用户在照片、视频、人像、夜景、专业等模式间快速切换并拍摄
```
```
### 4.2 典型场景

- 用户在照片、视频、人像、夜景、专业等模式间快速切换并拍摄
- 用户单手持机时，需要从右下角快速呼出工具栏完成参数调整
- 用户在缩放、滤镜、曝光、人像光圈等 Slider 上频繁查看和调整数值
```

# 009 【PRD】Camera 5.1 - 前置自动小广角
source: J8lkd4KGEobGtuxf3EelmToBg3E | revision: 12 | bytes: 12937
## headings
# 前置自动小广角
## 变更日志
## 1. 背景与目标
### 问题陈述
### 证据与数据
### 目标用户与场景
### 预期收益
### 竞品方案参考
## 2. 假设
## 3. 功能定义
### 功能描述
### 范围
### 适用模式/入口
## 4. 需求
### R1 · 横屏自动切广角
### R2 · 竖屏恢复 1x
### R3 · 手动变焦后不再自动切换
### R4 · 前置焦段命名统一
### 兼容性要求
## 5. 方案说明
### 核心行为
## 6. 关键依赖
## 7. 指标与验收
### 成功指标
### 验收条件
## 8. 埋点设计
### 上报示例
## 9. 干系人
## 10. 待确认/待补充
## 11. 初步评审
### agent 开发评审
### agent 测试评审
### agent Solution Smuggling 检查
### agent 全文评分
### agent 高风险项
### agent 推荐第一版最小切片
## 12. 附录
### A. 考虑过但放弃的方案
## selected snippets
```
| 2026-05-15 | 1.1 | Travis | 补充 4a/4a Pro 埋点数据；重新定义前置焦段 |
| 2026-05-15 | 1.2 | Travis | 新增 US-04；删除技术实现章节，回归产品需求 |
| 2026-05-15 | 1.3 | Travis | 放弃方案移至附录；需求章改为叙事格式 |
| 2026-05-15 | 1.4 | Travis | 补充交叉分析数据表；修正横屏广角结论 |
| 2026-05-15 | 1.5 | Travis | 埋点补充 parameter 定义；删除护栏指标 |
```
```
| 2026-05-15 | 1.2 | Travis | 新增 US-04；删除技术实现章节，回归产品需求 |
| 2026-05-15 | 1.3 | Travis | 放弃方案移至附录；需求章改为叙事格式 |
| 2026-05-15 | 1.4 | Travis | 补充交叉分析数据表；修正横屏广角结论 |
| 2026-05-15 | 1.5 | Travis | 埋点补充 parameter 定义；删除护栏指标 |

---
```
```
| 2026-05-15 | 1.4 | Travis | 补充交叉分析数据表；修正横屏广角结论 |
| 2026-05-15 | 1.5 | Travis | 埋点补充 parameter 定义；删除护栏指标 |

---

## 1. 背景与目标
```
```
## 1. 背景与目标

### 问题陈述

前置摄像头默认 1x（25-26mm，含约 15% 裁切）。用户竖屏自拍时构图尚可，但横屏使用时（合影、风景自拍等），裁切后视场角明显受限，用户需手动切换到 0.8x（21-22mm）才能获得理想的广角效果。
```
```
同时，横竖屏切换时因裁切比例和屏幕方向变化，取景范围会产生感知上的"跳跃"，体验不连贯。

此外，前置焦段历史命名混乱：旧称 1.0x（实际 21-22mm）/ 1.2x（实际 25-26mm），用户和工程侧理解不一致，需借本次需求统一命名。

### 证据与数据
```
```
此外，前置焦段历史命名混乱：旧称 1.0x（实际 21-22mm）/ 1.2x（实际 25-26mm），用户和工程侧理解不一致，需借本次需求统一命名。

### 证据与数据

数据源：Phone 4a / 4a Pro，印度（2026-04-15\~21，82.2 万张） + ROW（2026-03-23\~29，3.5 万张）
```
```
横竖屏焦段分布非常接近，差异仅 2-3 个百分点。值得注意的是，**横屏广角占比甚至略低于竖屏**——说明用户在横屏时并没有更主动去切广角。这不是"不想用"，更可能是没意识到裁切、或手动切换有摩擦。横屏合影恰好是最需要广角的场景，自动切换可以消除这个摩擦。

**结论：** 横屏用户中 84%（印度）/ 81%（ROW）停留在默认焦段，且横屏广角使用率不比竖屏高。自动广角有望显著改善横屏合影体验。\~20% 用户已主动使用广角，验证需求存在。

### 目标用户与场景
```
```
**结论：** 横屏用户中 84%（印度）/ 81%（ROW）停留在默认焦段，且横屏广角使用率不比竖屏高。自动广角有望显著改善横屏合影体验。\~20% 用户已主动使用广角，验证需求存在。

### 目标用户与场景

- 用户角色：前置摄像头用户，尤其是横屏合影、横屏自拍场景
```
```
### 目标用户与场景

- 用户角色：前置摄像头用户，尤其是横屏合影、横屏自拍场景
- 核心场景：
```
```
- 用户角色：前置摄像头用户，尤其是横屏合影、横屏自拍场景
- 核心场景：

  1. 用户横屏使用前置摄像头合影 → 自动切 0.8x 广角，容纳更多人
  2. 用户从竖屏转横屏 → FOV 自动适配，无明显压缩变化
```
```
- 用户角色：前置摄像头用户，尤其是横屏合影、横屏自拍场景
- 核心场景：

  1. 用户横屏使用前置摄像头合影 → 自动切 0.8x 广角，容纳更多人
  2. 用户从竖屏转横屏 → FOV 自动适配，无明显压缩变化
  3. 用户手动选择焦段后 → 本次使用中不再自动切换，尊重用户意图
```
```
- 横屏合影场景无需手动缩放，即拍即用
- 横竖切换时取景范围平滑过渡，无感知跳跃
- 预期覆盖横屏前置场景中 > 80% 的拍照量（当前 84% 横屏照片停留在默认焦段）
- 统一前置焦段命名，消除跨项目理解偏差
```

# 010 【PRD】Camera 5.1 - Tuning Palette 调色板
> **已过期快照：** 本节固定为 revision 55，仅保留历史审计，不得作为当前 Style/调色需求依据。当前版本请读取 `docx_md/010.md` 或线上文档 AQY0d37afoixBNxovr0l1fwmgDd；调色盘模式已取消复古滑杆，颗粒与暗角仅在参数模式中独立调节。

source: AQY0d37afoixBNxovr0l1fwmgDd | revision: 55 | bytes: 20832
## headings
# Camera Tuning Palette PRD
## 1. 文档信息
## 2. 本次更新摘要
## 3. 背景与决策
### 3.1 原功能问题
### 3.2 用户心智
### 3.3 行业方案判断
### 3.4 方案决策
## 4. 目标
## 5. 名词约定
## 6. 需求范围
### 6.1 本期包含
### 6.2 本期不包含
## 7. 参数范围与归属
## 8. Tuning Panel
### 8.1 入口与打开状态
### 8.2 组件结构
### 8.3 收起与保存
## 9. 两种编辑模式
### 9.1 模式原则
### 9.2 Palette Mode
### 9.3 Parameter Mode
### 9.4 模式切换
#### Palette Mode -> Parameter Mode
#### Parameter Mode -> Palette Mode
## 10. 参数映射
### 10.1 底层真值
### 10.2 Palette Strength
### 10.3 Color Palette 映射
### 10.4 Vintage Control 映射
### 10.5 Parameter Slider
## 11. Reset 规则
## 12. Preset 与兼容
### 12.1 保存策略
### 12.2 老项目兼容
### 12.3 Preset 展示
## 13. 与现有 Tuning 管线关系
## 14. 埋点
## 15. 非功能要求
### 15.1 性能
### 15.2 可用性
### 15.3 Onboarding
## 16. 验收标准
### 16.1 基础状态
### 16.2 Palette Mode
### 16.3 Parameter Mode
### 16.4 Reset 与兼容
## 17. 测试建议
## 18. 待确认事项
## selected snippets
```
- 产品模块：Camera / 相机
- 功能名称：Tuning / 调色
- 文档状态：交互逻辑建议稿
- 创建日期：2026/5/28
- 更新日期：2026/6/11
- 原型路径：`/Users/travis.zhao/imageProduct/tuning-palette-prototype`
```
```
- 功能名称：Tuning / 调色
- 文档状态：交互逻辑建议稿
- 创建日期：2026/5/28
- 更新日期：2026/6/11
- 原型路径：`/Users/travis.zhao/imageProduct/tuning-palette-prototype`
- 原型预览：`http://127.0.0.1:4173/tuning-palette-prototype/?v=palette-strength1`
```
```
本轮根据开发沟通和原型验证，将 Tuning 收敛为两个显式切换、互不同时编辑的模式：

- 左侧新增 `Palette / Parameters` 模式切换按钮
- 默认进入 Palette Mode
- Palette Mode 隐藏独立参数入口，底部仅展示整体 `Strength`
```
```
- 左侧新增 `Palette / Parameters` 模式切换按钮
- 默认进入 Palette Mode
- Palette Mode 隐藏独立参数入口，底部仅展示整体 `Strength`
- Strength 默认值为 `70%`，对应当前已验证的调色盘效果
- Strength 使用线性函数缩放 Color Palette 和 Vintage Control 的参数贡献
```
```
- 默认进入 Palette Mode
- Palette Mode 隐藏独立参数入口，底部仅展示整体 `Strength`
- Strength 默认值为 `70%`，对应当前已验证的调色盘效果
- Strength 使用线性函数缩放 Color Palette 和 Vintage Control 的参数贡献
- Parameter Mode 恢复完整 7 项参数精调，包括 `Tint` 和 `Sharpen`
- `Tint` 和 `Sharpen` 与调色盘无关，只允许在 Parameter Mode 中调整
```
```
- `Tint` 和 `Sharpen` 与调色盘无关，只允许在 Parameter Mode 中调整
- 模式切换由明确按钮负责，不再依赖点击控件外区域自动返回
- Tuning 暂不合并 Filter，避免面板承担过多功能

## 3. 背景与决策
```
```
- 模式切换由明确按钮负责，不再依赖点击控件外区域自动返回
- Tuning 暂不合并 Filter，避免面板承担过多功能

## 3. 背景与决策

### 3.1 原功能问题
```
```
## 3. 背景与决策

### 3.1 原功能问题

现有 Tuning 功能以多个独立参数 Slider 为主要交互。用户需要先理解 Contrast、Saturation、Warmth、Tint、Sharpen、Grain、Vignette 等参数分别代表什么，再判断应该调整哪个参数、调整方向以及调整幅度。
```
```
### 3.1 原功能问题

现有 Tuning 功能以多个独立参数 Slider 为主要交互。用户需要先理解 Contrast、Saturation、Warmth、Tint、Sharpen、Grain、Vignette 等参数分别代表什么，再判断应该调整哪个参数、调整方向以及调整幅度。

这种交互对熟悉影像后期的高级用户有效，但对大部分普通相机用户存在明显门槛：
```
```
现有 Tuning 功能以多个独立参数 Slider 为主要交互。用户需要先理解 Contrast、Saturation、Warmth、Tint、Sharpen、Grain、Vignette 等参数分别代表什么，再判断应该调整哪个参数、调整方向以及调整幅度。

这种交互对熟悉影像后期的高级用户有效，但对大部分普通相机用户存在明显门槛：

- 参数名称专业，用户难以提前理解调整后的实际效果
```
```
这种交互对熟悉影像后期的高级用户有效，但对大部分普通相机用户存在明显门槛：

- 参数名称专业，用户难以提前理解调整后的实际效果
- 单个参数只能描述局部变化，用户很难通过多个 Slider 快速建立完整风格
- 用户需要在参数之间反复切换并观察预览，试错路径较长
```
```
- 多项参数组合后容易产生过度调节，用户难以恢复到协调状态
- 功能虽然提供了较强能力，但复杂度会降低用户发现、尝试和持续使用的意愿

因此，本需求并不是简单替换 Slider 的视觉形式，而是希望重新设计普通用户进入调色功能后的第一层交互。

### 3.2 用户心智
```

# 011 【PRD】Camera 5.1 - 200MP 自动裁切
source: S9cVdbeQLoIyYvx51tzlXDqfgUc | revision: 30 | bytes: 4908
## headings
# 【PRD】Camera 5.1 - 200MP 自动裁切
## 一、项目背景
## 二、行业
## 三、方案
### 相机内「一拍多得」
#### 功能定位
### 用户流程
#### Step1：进入拍摄
#### Step2：拍摄
#### Step3：结果页
### 算法需求
#### （1）主体检测
#### （2）精彩区域发现（Highlight Discovery）
#### （3）智能裁切（Auto Crop）
#### （4）拼图生成（Collage Layout）
### 输出规则
## 三、方案二：相册后处理「自动构图」
### 功能定位
### 用户流程
### 算法需求
#### （1）自动构图建议
#### （2）构图质量要求
#### （3）质量评估
## 四、体验目标
## selected snippets
```
## 一、项目背景

基于 200MP 超高解析力，打造：

> **裁切也清晰，一拍多得**
```
```
目标是提升：

1. 用户出片率
2. 内容可玩性
3. 分享价值
```
```
## 三、方案

在相机相机部署一拍多得和拍后构图功能

### 相机内「一拍多得」
```
```
在相机相机部署一拍多得和拍后构图功能

### 相机内「一拍多得」

#### 功能定位
```
```
#### 功能定位

路径：

**Camera → 200MP → Auto Reframe / 一拍多得**
```
```
拍摄时支持选择：

**拼图模板（Collage Template）**

例如：
```
```
支持：

- 编辑裁切
- 更换模板
- 调整顺序
```
```
### 算法需求

#### （1）主体检测

识别：
```
```
支持多主体。

---

#### （2）精彩区域发现（Highlight Discovery）
```
```
目标：

> 自动讲故事

---
```
```
支持：

不同 crop ratio：

- 1:1
```
```
## 三、方案二：相册后处理「自动构图」

### 功能定位

路径：
```

# 012 【PRD】Camera 5.1 - 200MP 高像素
source: QCdGdErD6omTlzx9AtzlgxpIgWe | revision: 46 | bytes: 10671
## headings
# 前言
# 一、 版本信息
# 二、 变更日志
# 三、 需求背景
## 产品 / 数据现状
## 竞品分析
# 四、 需求范围
## 需求列表&需求单
# 五、 功能详细说明
## 产品流程图（略）
## 交互原型图
## 功能说明
## 需求词条--无需翻译
# 七、 非功能需求
# 八、 埋点
# 九、 项目规划
# 附录
## selected snippets
```
# 三、 需求背景

## 产品 / 数据现状

1. 26111/26121 首次采用**200MP（HP5）**主摄，具备输出200MP高像素照片的能力，我们需要结合技术实现和用户拍摄需求制定高像素模式的功能交互
```
```
1. 26111/26121 首次采用**200MP（HP5）**主摄，具备输出200MP高像素照片的能力，我们需要结合技术实现和用户拍摄需求制定高像素模式的功能交互
2. Ksp文档：
3. 可行性文档：<cite doc-id="XwYUwdXlQikqznkwtChlSgc8gec" file-type="wiki" title="25131  Blastoise Pro Camera KSP" type="doc"></cite>
4. 线上机型高像素模式数据分析<cite type="user" user-id="ou_1e068f80b2831f5bc95787032143a546" user-name="Travis Zhao"></cite>
```
```
3. 可行性文档：<cite doc-id="XwYUwdXlQikqznkwtChlSgc8gec" file-type="wiki" title="25131  Blastoise Pro Camera KSP" type="doc"></cite>
4. 线上机型高像素模式数据分析<cite type="user" user-id="ou_1e068f80b2831f5bc95787032143a546" user-name="Travis Zhao"></cite>

<sheet sheet-id="yJjWK1" token="Whg7s1cA5hlFTNtU9TkllyW4gsb"></sheet>
```
```
<table><colgroup><col/><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>机型</td><td>摄像头</td><td>高像素-入口</td><td>记忆状态</td><td>快门体验</td><td>后处理</td><td>相册管理</td><td>特性功能</td></tr><tr><td>x300 pro</td><td>长焦</td><td><img name="1.jpeg" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDdiYzk1ZjEwM2ZhNzgyMTJmNDZkMWExZjQ0ZTNmZTVfZWY1ZDc1ODJkYTE3YjU3NWQ4NGFmYTdiMGU5Nzk0YjdfSUQ6NzY0Nzc5MjUzNDMzNjU3MzE1MV8xNzgzNDA2MzE5OjE3ODM0MDk5MTlfVjM" mime="image/jpeg" scale="0.675926" src="HCYYbewqAo0mMjxaXikl3yvMgMe"/></td><td>杀进程后恢复默认</td><td>快门动画3s+<figure view-type="Preview"><source href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDA0MjlmNmRlZDNlMGU4N2RlNDg1NDkwYTI5NzY2OWZfMjE1ODRmNmQ3ZTViN2Y4OTBiN2E5MjlhNDY0ZDE0MDBfSUQ6NzY0Nzc5MjUzNTgyMTI0MjA4MF8xNzgzNDA2MzE5OjE3ODM0MDk5MTlfVjM" mime="video/mp4" origin-height="960.000000" origin-width="540.000000" token="T3SibsbVeo7fdPxxQGklU3oZgcd"/></figure></td><td>/</td><td>有单独的高像素相册<img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGI1M2Y1YjUwNTEzYTBjNjdmNmYyZmUwYmE0ZTZhZWRfMmZiYWNiYjc0NmQ1OTRiNzk2NzViMzFhMTI4OTQyOGRfSUQ6NzY0Nzc5MjUzNDAwOTQzMzgyM18xNzgzNDA2MzE5OjE3ODM0MDk5MTlfVjM" mime="image/png" scale="1.000000" src="VZiAbu8VeoAJxOxQX0jluhCogZc"/></td><td>支持人像2亿、支持电影分镜自动裁图拼图<img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGQ2MTYwYzQxMzAxMDdmYjg4YjcyYzE5Y2IwZTUyNThfYWY5NTg3YTQ2ZTI5NjEwNWIzYjQ2OTA1YjFmYmE0ZDlfSUQ6NzY0Nzc5MjUzNDA0ODgyMDk2Ml8xNzgzNDA2MzE5OjE3ODM0MDk5MTlfVjM" mime="image/png" scale="0.109687" src="XbXpbtsO7oVcAsx1PgHlF77agvb"/></td></tr><tr><td>Findx9 pro</td><td>长焦</td><td></td><td></td><td>
```
```
# 四、 需求范围

> 可条理性地罗列需求范围或信息架构

1. 项目范围：对硬件。首上项项目为26111/26121，后续200MP项目默认继承
```
```
> 可条理性地罗列需求范围或信息架构

1. 项目范围：对硬件。首上项项目为26111/26121，后续200MP项目默认继承
2. 老项目回落：不支持回落，具体回落计划根据回落排期确
```
```
1. 项目范围：对硬件。首上项项目为26111/26121，后续200MP项目默认继承
2. 老项目回落：不支持回落，具体回落计划根据回落排期确

## 需求列表&需求单
```
```
1. 项目范围：对硬件。首上项项目为26111/26121，后续200MP项目默认继承
2. 老项目回落：不支持回落，具体回落计划根据回落排期确

## 需求列表&需求单

<table><colgroup><col/><col/></colgroup><tbody><tr><td>需求名称</td><td>需求描述</td></tr><tr><td>200MP高像素</td><td><ol><li seq="1">首次进入相机，对200MP的入口、使用体验做个说明--看下其他手机的体验</li><li>开启200MP后，顶部栏有入口，支持点击关闭和开启</li><li>拍摄预计有3s的处理时长，过程中不可再次点击快门，需要有快门动画，建议做的有风格一些，提升用户的耐心；以及有处理中文案提醒</li><li>专业模式支持高像素拍摄</li><li>打开的记忆状态规则</li><li>功能兼容状态-- follow 25111 50MP高像素</li><li>算法兼容状态待明确</li></ol></td></tr></tbody></table>
```
```
## 需求列表&需求单

<table><colgroup><col/><col/></colgroup><tbody><tr><td>需求名称</td><td>需求描述</td></tr><tr><td>200MP高像素</td><td><ol><li seq="1">首次进入相机，对200MP的入口、使用体验做个说明--看下其他手机的体验</li><li>开启200MP后，顶部栏有入口，支持点击关闭和开启</li><li>拍摄预计有3s的处理时长，过程中不可再次点击快门，需要有快门动画，建议做的有风格一些，提升用户的耐心；以及有处理中文案提醒</li><li>专业模式支持高像素拍摄</li><li>打开的记忆状态规则</li><li>功能兼容状态-- follow 25111 50MP高像素</li><li>算法兼容状态待明确</li></ol></td></tr></tbody></table>

# 五、 功能详细说明
```
```
<table><colgroup><col/><col/></colgroup><tbody><tr><td>需求名称</td><td>需求描述</td></tr><tr><td>200MP高像素</td><td><ol><li seq="1">首次进入相机，对200MP的入口、使用体验做个说明--看下其他手机的体验</li><li>开启200MP后，顶部栏有入口，支持点击关闭和开启</li><li>拍摄预计有3s的处理时长，过程中不可再次点击快门，需要有快门动画，建议做的有风格一些，提升用户的耐心；以及有处理中文案提醒</li><li>专业模式支持高像素拍摄</li><li>打开的记忆状态规则</li><li>功能兼容状态-- follow 25111 50MP高像素</li><li>算法兼容状态待明确</li></ol></td></tr></tbody></table>

# 五、 功能详细说明

## 产品流程图（略）
```
```
# 五、 功能详细说明

## 产品流程图（略）

> 将鼠标悬浮至下方空白图形模块，点击**编辑**，即可进入流程图创作你的产品流程图
```
```
## 交互原型图

> 在空白行输入“/Figma” ，插入 Figma 设计稿
> 
> 或直接粘贴设计稿地址至文档，并展示为“内嵌网页”
```

# 013 【PRD】Camera 5.1 - 照片专业模式 2.0（Expert Mode 2.0）
source: Kl8pd7g4FoK52px0LkTlqqn7gdd | revision: 488 | bytes: 10484
## headings
# 0. 文档信息
# 1. 变更日志
# 2. 需求背景
## 2.1 产品 / 数据现状
# 3. 需求目标
# 4. 需求范围
## 4.1 范围内
## 4.2 范围外
# 5. 功能设计
## 5.1 视觉更新（Slide Bar + 工具栏）
### 功能支持范围
### Slide Bar
### 工具栏
#### 设计方向建议
## 5.2 测光方式切换
### 功能支持范围
### 交互与流程
### 测光方式定义
### 限制
## 5.3 Preset 扩展
### 功能说明
## 5.4 间隔拍摄
### 功能支持范围
### 交互与流程
### 自定义设置
### 行为
## 5.5 峰值对焦
### 功能支持范围
### 交互与流程
# 6. 关键依赖与约束
## 6.1 技术依赖
## 6.2 素材 / 文案依赖
# 7. 效果定义与验收标准
## 7.1 预期效果
## 7.2 验收口径
# 8. 词条定义
# 9. 埋点
## 9.1 埋点目标
## 9.2 埋点定义
# 10. 项目计划与风险
## 10.1 风险与兜底
# 11. 待确认事项
## selected snippets
```
<title>【PRD】Camera 5.1 - 照片专业模式 2.0（Expert Mode 2.0）</title>

# 0. 文档信息

- 文档标题：【PRD】Camera 4.2 - 照片专业模式 2.0（Expert Mode 2.0）
```
```
- 文档标题：【PRD】Camera 4.2 - 照片专业模式 2.0（Expert Mode 2.0）
- 项目 / 机型 / 代号：[待补充]
- 所属版本：[待补充]
- 作者：Travis Zhao
- 更新时间：2026-06-08
```
```
- 文档标题：【PRD】Camera 4.2 - 照片专业模式 2.0（Expert Mode 2.0）
- 项目 / 机型 / 代号：[待补充]
- 所属版本：[待补充]
- 作者：Travis Zhao
- 更新时间：2026-06-08
- 项目阶段：[待补充]
```
```
- 项目 / 机型 / 代号：[待补充]
- 所属版本：[待补充]
- 作者：Travis Zhao
- 更新时间：2026-06-08
- 项目阶段：[待补充]
- 上市时间：[待补充]
```
```
- 更新时间：2026-06-08
- 项目阶段：[待补充]
- 上市时间：[待补充]
- 销售地区：[待补充]

---
```
```
- 项目阶段：[待补充]
- 上市时间：[待补充]
- 销售地区：[待补充]

---
```
```
- 上市时间：[待补充]
- 销售地区：[待补充]

---

# 1. 变更日志
```
```
| 2026-04-24 | v0.1 | Travis Zhao | 初稿创建 |
| 2026-06-08 | v0.2 | Travis Zhao | 砍掉自动/手动混合模式、峰值对焦恢复、新增间隔拍摄、Preset 扩展、测光逻辑完善、视觉更新合并 |

---

# 2. 需求背景
```
```
# 2. 需求背景

## 2.1 产品 / 数据现状

- 当前现状：专业模式为全手动参数调节，功能相对基础
```
```
- 当前现状：专业模式为全手动参数调节，功能相对基础
- 已有方案：现有专业模式支持 ISO、Shutter、EV、WB、Focus 手动调节
- 已知问题：

  - Slide bar 和工具栏视觉风格偏基础，缺乏专业感
```
```
- 当前现状：专业模式为全手动参数调节，功能相对基础
- 已有方案：现有专业模式支持 ISO、Shutter、EV、WB、Focus 手动调节
- 已知问题：

  - Slide bar 和工具栏视觉风格偏基础，缺乏专业感
  - 缺少测光方式切换、峰值对焦等专业工具
```
```
- 缺少测光方式切换、峰值对焦等专业工具
  - 专业模式参数（EV/ISO/S/WB/AF）不支持保存到 Preset
- 数据结论：[待补充：当前专业模式使用率数据]
- 竞品 / 对标情况：

  - iPhone ProRAW / Samsung Expert RAW 支持多种测光模式、峰值对焦等专业工具
```

# 014 【PRD】Camera 4.0 - 美颜效果定义
source: JhhKdNT9wof7q2xpOE6lOL6qgdh | revision: 2721 | bytes: 17804
## headings
# 【PRD】Camera 4.0 - 美颜效果定义
## 零、 修订记录
## 一、需求背景
## 二、需求范围
## 三、需求说明
### 模式定义
### 现有问题说明
### 调优覆盖：色温 × 亮度 × 性别 × 年龄
### 目标效果
### 总体改善方向
## 四、开发计划
### 25131 Pro
### 附件
## selected snippets
```
| 20250909 | 1.0 | LaylaHuang | 创建 |
| 20250919 | 1.1 | LaylaHuang | 1.欧洲用户调研中的美颜洞察；2.典型场景及男女目标效果；3.23112美颜参数设置 |
| 20251027 | 1.2 | LaylaHuang | 更新25131 Pro的性能增量与目标，并同步调整当前需求项优先级。 |
```
```
| 20250919 | 1.1 | LaylaHuang | 1.欧洲用户调研中的美颜洞察；2.典型场景及男女目标效果；3.23112美颜参数设置 |
| 20251027 | 1.2 | LaylaHuang | 更新25131 Pro的性能增量与目标，并同步调整当前需求项优先级。 |



## 一、需求背景
```
```
## 一、需求背景

1. **美颜现状 & 优化诉求**Nothing 当前重点市场为印度与英国，出于产品定位以及市场特性，美颜保持默认不开启。当前美颜需求总体定位为【在现有框架内优化】
```
```
1. **美颜现状 & 优化诉求**Nothing 当前重点市场为印度与英国，出于产品定位以及市场特性，美颜保持默认不开启。当前美颜需求总体定位为【在现有框架内优化】



1. **现有模式 & 覆盖范围**目前提供 “Natural” 与 “Strong” 两种美颜模式（内置整套参数，不开放可调节的小项），覆盖用户的基础需求。
```
```
1. **现有模式 & 覆盖范围**目前提供 “Natural” 与 “Strong” 两种美颜模式（内置整套参数，不开放可调节的小项），覆盖用户的基础需求。



1. **数据验证 & 优化点**
```
```
1. **印度用户对美颜的需求度和敏感度明显高于其他地区**，可能存在更多效果不满或过度修饰的问题。
   
      1. 前后置各个模式，均设为默认美颜不开启，但在印度有约 14% 用户会开启美颜拍摄，美颜需求更频繁。
      2. 印度美颜开启后再关闭的情况比例也更高，印度对美颜效果敏感度高。
   2. 整体市场“Natural”的使用率更高—— **“像自己，但更好看” 的轻度修饰美颜，能普适大部分用户的需求。**
```
```
1. 前后置各个模式，均设为默认美颜不开启，但在印度有约 14% 用户会开启美颜拍摄，美颜需求更频繁。
      2. 印度美颜开启后再关闭的情况比例也更高，印度对美颜效果敏感度高。
   2. 整体市场“Natural”的使用率更高—— **“像自己，但更好看” 的轻度修饰美颜，能普适大部分用户的需求。**
   3. 欧洲线下调研反馈中，**欧洲用户多数对强美颜抗拒，尤其男性。**
   4. 但如果用户的**皮肤瑕疵明显，对修饰会有比较强诉求，包括男性和女性用户。**
```
```
2. 印度美颜开启后再关闭的情况比例也更高，印度对美颜效果敏感度高。
   2. 整体市场“Natural”的使用率更高—— **“像自己，但更好看” 的轻度修饰美颜，能普适大部分用户的需求。**
   3. 欧洲线下调研反馈中，**欧洲用户多数对强美颜抗拒，尤其男性。**
   4. 但如果用户的**皮肤瑕疵明显，对修饰会有比较强诉求，包括男性和女性用户。**

<table><colgroup><col/><col/></colgroup><tbody><tr><td>埋点数据</td><td>欧洲用户调研反馈</td></tr><tr><td><img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWU4MDcxY2Q4ZmY5ZTgzY2ExOWRlYjI4YjkxYjI4OTlfYzI3ZTVkMWE3NmNhOWU4Nzk2MmE2YjgzNTY5YjY0MzFfSUQ6NzU0ODM0MzQzMTM2MjQ3ODExMV8xNzgzNDA2MzI0OjE3ODM0MDk5MjRfVjM" mime="image/png" scale="1.000000" src="V1B6bhKQAobrEwxox89lnGdEgEd"/></td><td><img name="image.png" caption="“Strong” 模式的目标：满足对美化有强诉求的用户。&#xA;" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTc2ZDE0Yzc3ZDFjYWRlNDIyZGY3NGFiNDZkNzJhMDFfZjM5NGJmZDg4ZDY4NTYyNzI4MjI1ZjZmZGRmZjQwMmRfSUQ6NzU1MTYzNjI2NjUxODAwMzc0M18xNzgzNDA2MzI0OjE3ODM0MDk5MjRfVjM" mime="image/png" scale="1.000000" src="MeiYbrzwbotQL4xlKkelm759gUg"/></td></tr></tbody></table>
```
```
<table><colgroup><col/><col/></colgroup><tbody><tr><td>埋点数据</td><td>欧洲用户调研反馈</td></tr><tr><td><img name="image.png" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWU4MDcxY2Q4ZmY5ZTgzY2ExOWRlYjI4YjkxYjI4OTlfYzI3ZTVkMWE3NmNhOWU4Nzk2MmE2YjgzNTY5YjY0MzFfSUQ6NzU0ODM0MzQzMTM2MjQ3ODExMV8xNzgzNDA2MzI0OjE3ODM0MDk5MjRfVjM" mime="image/png" scale="1.000000" src="V1B6bhKQAobrEwxox89lnGdEgEd"/></td><td><img name="image.png" caption="“Strong” 模式的目标：满足对美化有强诉求的用户。&#xA;" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTc2ZDE0Yzc3ZDFjYWRlNDIyZGY3NGFiNDZkNzJhMDFfZjM5NGJmZDg4ZDY4NTYyNzI4MjI1ZjZmZGRmZjQwMmRfSUQ6NzU1MTYzNjI2NjUxODAwMzc0M18xNzgzNDA2MzI0OjE3ODM0MDk5MjRfVjM" mime="image/png" scale="1.000000" src="MeiYbrzwbotQL4xlKkelm759gUg"/></td></tr></tbody></table>



## 二、需求范围
```
```
## 二、需求范围

1. 

| 肤质处理 | 磨皮 | 全脸细节肌理平滑 |
```
```
- 算法实际值：分别为 0、12、30



## 三、需求说明
```
```
## 三、需求说明

### 模式定义

<table><colgroup><col/><col/></colgroup><tbody><tr><td colspan="2">“自然”和“强”两种模式面向两类不同的审美需求。</td></tr><tr><td>自然</td><td>偏好原生质感的用户，通常对自身皮肤状态较为接受，拍摄时更注重画面真实感与后期可调空间。</td></tr><tr><td>强</td><td>对自身皮肤状态不满，面部修饰需求更高的用户，希望通过相机直出获得改善和美化效果，减少后期处理。</td></tr></tbody></table>
```

# 015 【PRD】Camera 5.1 - 照片风格（自然 & 鲜明）
source: OmaEd4Re8oKF5WxHd5glNVjGgbd | revision: 18 | bytes: 9019
## headings
# 【PRD】Camera 5.1 - 照片风格（自然 & 鲜明）
## 变更日志
## 1. 背景与目标
### 问题陈述
### 目标用户与场景
### 预期收益
## 2. 功能定义
### 功能描述
### 范围
### 适用入口
## 3. 需求
### R1 · 鲜明风格（Vivid）— 默认
### R2 · 自然风格（Natural）
### R3 · 下拉工具栏入口
### R4 · 兼容范围
### R5 · Preset 兼容
### 兼容性要求
## 4. 方案说明
### 核心行为
### 风格参数参考 <cite type="user" user-id="ou_bde858e2c287e45bb799791c3cea03c7" user-name="Alex Huang"></cite>
## 5. 需求词条
## 6. 关键依赖
## 7. 指标与验收
### 成功指标
### 验收条件
## 8. 埋点设计
## 9. 干系人
## 10. 待确认/待补充
## 11. 初步评审
### agent 开发评审
### agent 测试评审
### agent 全文评分
## 12. 附录
### 考虑过但放弃的方案
## selected snippets
```
## 1. 背景与目标

### 问题陈述

效果分析显示，大多数用户偏好高对比度、高饱和度的照片效果，但存在另一部分用户非常反感这种处理带来的不真实感。两类用户的偏好是审美取向差异，与拍摄场景无关。需要在不增加操作门槛的前提下，同时服务两类人群。
```
```
效果分析显示，大多数用户偏好高对比度、高饱和度的照片效果，但存在另一部分用户非常反感这种处理带来的不真实感。两类用户的偏好是审美取向差异，与拍摄场景无关。需要在不增加操作门槛的前提下，同时服务两类人群。

### 目标用户与场景

- 大多数用户：追求"出片感"，希望拍完即用，不关心参数
```
```
### 目标用户与场景

- 大多数用户：追求"出片感"，希望拍完即用，不关心参数
- 少数用户：追求真实感，反感过度处理，偏好保留细节层次的克制风格
```
```
[TBD — 需量化：风格使用率、照片分享率提升目标]

## 2. 功能定义

### 功能描述
```
```
## 2. 功能定义

### 功能描述

功能名称：照片风格（Photo Style）
```
```
### 功能描述

功能名称：照片风格（Photo Style）  
一句话描述：相机默认以「鲜明」风格输出照片，提供「自然」风格作为可选手动切换项，用户可随时在下拉工具栏中切换。
```
```
功能名称：照片风格（Photo Style）  
一句话描述：相机默认以「鲜明」风格输出照片，提供「自然」风格作为可选手动切换项，用户可随时在下拉工具栏中切换。

### 范围
```
```
### 范围

In Scope:

- 两种内置风格：自然（Natural）、鲜明（Vivid）
```
```
In Scope:

- 两种内置风格：自然（Natural）、鲜明（Vivid）
- 鲜明为默认风格，开箱即用
- 下拉工具栏提供风格切换入口，用户可随时切换
```
```
- 鲜明为默认风格，开箱即用
- 下拉工具栏提供风格切换入口，用户可随时切换
- 风格基于底层 ISP 参数（tone mapping 等）实现
- 与滤镜及其他调色功能兼容
- Preset 中支持风格配置
```
```
- 风格基于底层 ISP 参数（tone mapping 等）实现
- 与滤镜及其他调色功能兼容
- Preset 中支持风格配置

Out of Scope:
```
```
- 与滤镜及其他调色功能兼容
- Preset 中支持风格配置

Out of Scope:

| 不做什么 | 原因 | 未来是否考虑 |
```

# 016 【PRD】Camera 5.1-AI Preset
source: R6bPdX8BOoAQWfxaSGpllX6ngGg | revision: 128 | bytes: 13641
## headings
# 【PRD】Camera 5.1-AI Preset
## 变更日志
## 1. 背景与目标
### 问题陈述
### 证据与数据
### 目标用户与场景
### 预期收益
## 2. 假设
## 3. 功能定义
### 功能描述
### 范围
### 适用模式/入口
## 4. 需求
### R1 · AI Preset 场景推荐
### R2 · 推荐风格选择-待定
### R3 · 场景支持列表和滤镜推荐规则
## 5. 方案说明
### 核心行为
### 效果约束
## 6. 需求词条
## 7. 关键依赖
## 8. 指标与验收
### 成功指标
### 验收条件
## 9. 埋点设计
## 10. 干系人
## 11. 待确认/待补充
## 12. 初步评审
### agent 开发评审
### agent 测试评审
### agent Solution Smuggling 检查
### agent 全文评分
### agent 高风险项
### agent 推荐第一版最小切片
## 13. 附录
### 竞品分析摘要
### 考虑过但放弃的方案
## selected snippets
```
|-|-|-|-|
| 2026/1/13 | 1.0 | Travis | 梳理大致 AI preset 方案 |
| 2026/3/9 | 1.1 | Travis | 输出初版交互方案 |
| 2026/3/17 | 1.2 | Travis | 补充竞品分析内容 |
| [TBD] | 1.3 | Travis | 精简版：聚焦滤镜推荐+preset推荐，移除仿色 |
```
```
| 2026/1/13 | 1.0 | Travis | 梳理大致 AI preset 方案 |
| 2026/3/9 | 1.1 | Travis | 输出初版交互方案 |
| 2026/3/17 | 1.2 | Travis | 补充竞品分析内容 |
| [TBD] | 1.3 | Travis | 精简版：聚焦滤镜推荐+preset推荐，移除仿色 |

---
```
```
## 1. 背景与目标

### 问题陈述

当前的 preset 功能绑定了模式、焦段等全部相机设置，用户只想应用一套调色参数（滤镜 + tuning + EV）时，却被迫设置所有功能，使用门槛过高。同时，普通用户面对数十个滤镜选项时缺乏选择依据，不知道该用哪个。
```
```
当前的 preset 功能绑定了模式、焦段等全部相机设置，用户只想应用一套调色参数（滤镜 + tuning + EV）时，却被迫设置所有功能，使用门槛过高。同时，普通用户面对数十个滤镜选项时缺乏选择依据，不知道该用哪个。

### 证据与数据

- 竞品参考：DOKA 相机已上线场景识别 + 滤镜推荐功能，根据画面内容分析后推荐合适的滤镜并给出理由
```
```
- 竞品参考：DOKA 相机已上线场景识别 + 滤镜推荐功能，根据画面内容分析后推荐合适的滤镜并给出理由
- [TBD — 需补充用户反馈/埋点数据]

### 目标用户与场景
```
```
### 目标用户与场景

- 用户角色：普通拍照用户，不希望手动调试参数
- 核心场景：打开相机 → 对准拍摄目标 → 一键获得适合当前场景的调色方案
- 使用频率：[TBD — 需数据验证]
```
```
- 用户角色：普通拍照用户，不希望手动调试参数
- 核心场景：打开相机 → 对准拍摄目标 → 一键获得适合当前场景的调色方案
- 使用频率：[TBD — 需数据验证]

### 预期收益
```
```
1. 让用户轻松应用合适的效果风格，提升照片和视频拍摄的满意度
2. 降低 preset 功能的使用门槛，让用户可以一键快速应用合适的 preset

---

## 2. 假设
```
```
|-|-|-|-|
| 我们相信 **AI 场景分析 + 滤镜推荐** 对 **普通拍照用户** 会带来 **preset 使用率提升**，因为 **降低了选择成本** | Medium | preset 应用率无显著变化 | 埋点对比 AI preset vs 手动 preset 使用率 |
| [TBD] |  |  |  |

---
```
```
## 3. 功能定义

### 功能描述

- 功能名称：AI Preset
```
```
### 功能描述

- 功能名称：AI Preset
- 一句话描述：基于当前拍摄场景的实时分析，自动推荐合适的滤镜+调色 preset，用户一键应用
```
```
- 功能名称：AI Preset
- 一句话描述：基于当前拍摄场景的实时分析，自动推荐合适的滤镜+调色 preset，用户一键应用

### 范围
```

# 017 【PRD】Camera 5.1 - 视频 ISZ（无损变焦）
source: RCTgdoQ0toQzfzxsknvlGBO9guh | revision: 128 | bytes: 5790
## headings
# 【PRD】Camera 5.1 - 视频 ISZ（无损变焦）
## 0. 文档信息
## 变更日志
## 背景与目标
### 2.1 用户问题
### 2.2 行业现状
### 2.3 用户目标
### 2.4 产品目标
## 功能定义
### 3.1 功能名称
### 3.2 一句话描述
### 3.3 范围
## 设计稿
## 需求
### R1 · 焦段与变焦指示器定义
### R2 · 视频模式 ISZ
### R3 · 慢动作模式 ISZ
### R4 · 与 EIS / 效果链路的关系
## 关键依赖与约束
## 词条定义
## 指标与验收
### 8.1 成功指标
### 8.2 验收标准
## 埋点
### 9.1 埋点目标
### 9.2 埋点定义
## 风险与待确认项
## selected snippets
```
## 背景与目标

### 2.1 用户问题

- 拍照模式下主摄与长焦均已支持 ISZ，视频模式没有，用户在视频中变焦至同等倍率只能使用数码变焦，画质明显劣化。
```
```
- 拍照模式下主摄与长焦均已支持 ISZ，视频模式没有，用户在视频中变焦至同等倍率只能使用数码变焦，画质明显劣化。
- 变焦指示器在视频模式下缺少对应点位，用户无法感知/直达更优画质的倍率。

### 2.2 行业现状
```
```
- 拍照模式下主摄与长焦均已支持 ISZ，视频模式没有，用户在视频中变焦至同等倍率只能使用数码变焦，画质明显劣化。
- 变焦指示器在视频模式下缺少对应点位，用户无法感知/直达更优画质的倍率。

### 2.2 行业现状

- 主流竞品在视频模式下普遍支持基于 sensor 裁切的无损变焦点位，并在变焦条上显式标出，属于中高端机型的基础能力。
```
```
- 主流竞品在视频模式下普遍支持基于 sensor 裁切的无损变焦点位，并在变焦条上显式标出，属于中高端机型的基础能力。
- 通用背景见<cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>。

### 2.3 用户目标
```
```
- 主流竞品在视频模式下普遍支持基于 sensor 裁切的无损变焦点位，并在变焦条上显式标出，属于中高端机型的基础能力。
- 通用背景见<cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>。

### 2.3 用户目标

- 视频变焦到常用倍率（2x / 4x / 8x）时获得明显优于数码变焦的画质。
```
```
### 2.3 用户目标

- 视频变焦到常用倍率（2x / 4x / 8x）时获得明显优于数码变焦的画质。
- 变焦交互与拍照模式一致，无新增学习成本。
```
```
- 视频变焦到常用倍率（2x / 4x / 8x）时获得明显优于数码变焦的画质。
- 变焦交互与拍照模式一致，无新增学习成本。

### 2.4 产品目标
```
```
- 视频变焦到常用倍率（2x / 4x / 8x）时获得明显优于数码变焦的画质。
- 变焦交互与拍照模式一致，无新增学习成本。

### 2.4 产品目标

- 视频类模式补齐 ISZ 能力，拉齐拍照与视频的变焦画质，消除能力断档。
```
```
### 2.4 产品目标

- 视频类模式补齐 ISZ 能力，拉齐拍照与视频的变焦画质，消除能力断档。

## 功能定义
```
```
- 视频类模式补齐 ISZ 能力，拉齐拍照与视频的变焦画质，消除能力断档。

## 功能定义

### 3.1 功能名称
```
```
## 功能定义

### 3.1 功能名称

视频 ISZ（In-Sensor Zoom）
```
```
### 3.1 功能名称

视频 ISZ（In-Sensor Zoom）

### 3.2 一句话描述
```

# 018 【PRD】Camera 5.1 - 前置 4K 视频
source: TfcwdgkqboAiHhxcCH3lIPxgg4g | revision: 60 | bytes: 2769
## headings
# 【PRD】Camera 5.1 - 前置 4K 视频
## 文档信息
## 变更日志
## 需求背景
## 需求目标
## 需求范围
## 交互说明
## 关键依赖
## 词条定义
## 埋点
## 指标与验收
## selected snippets
```
## 需求背景

参见《26111 视频能力建设 Overview》。

当前前置视频最高支持 1080P，4K 仅覆盖后置主摄。前置 4K 已是中高端价位主流配置（iPhone、三星、OPPO、vivo 均已支持），当前缺位在媒体评测和用户横评中会被直接识别。本功能以竞品对标作为需求依据，无专项用户调研。
```
```
当前前置视频最高支持 1080P，4K 仅覆盖后置主摄。前置 4K 已是中高端价位主流配置（iPhone、三星、OPPO、vivo 均已支持），当前缺位在媒体评测和用户横评中会被直接识别。本功能以竞品对标作为需求依据，无专项用户调研。

---

## 需求目标
```
```
## 需求目标

在 26111 全机型录像模式下支持前置摄像头 4K 30fps 录制，提升前置视频录制的画质，补齐与主流竞品的规格断档。

---
```
```
在 26111 全机型录像模式下支持前置摄像头 4K 30fps 录制，提升前置视频录制的画质，补齐与主流竞品的规格断档。

---

## 需求范围
```
```
## 需求范围

**范围内**

- 模式：录像模式
```
```
**范围内**

- 模式：录像模式
- 摄像头：前置
- 规格：4K（3840×2160）30fps
```
```
- 模式：录像模式
- 摄像头：前置
- 规格：4K（3840×2160）30fps
- 入口：录像模式顶部工具栏分辨率切换
```
```
- 摄像头：前置
- 规格：4K（3840×2160）30fps
- 入口：录像模式顶部工具栏分辨率切换

**范围外**
```
```
- 规格：4K（3840×2160）30fps
- 入口：录像模式顶部工具栏分辨率切换

**范围外**

- 慢动作、人像视频、夜景视频等其他模式——前置分辨率上限维持现状，不受影响
```
```
**范围外**

- 慢动作、人像视频、夜景视频等其他模式——前置分辨率上限维持现状，不受影响
- 前置 4K 60fps
- 前置 4K HLG（待评估）
```
```
- 慢动作、人像视频、夜景视频等其他模式——前置分辨率上限维持现状，不受影响
- 前置 4K 60fps
- 前置 4K HLG（待评估）
- 超广角 4K（另行规划）
- 前后双录模式下的 4K 规格（以《前后双录 PRD》定义为准）
```
```
- 超广角 4K（另行规划）
- 前后双录模式下的 4K 规格（以《前后双录 PRD》定义为准）

---

## 交互说明
```

# 019 【PRD】Camera 5.1 - 视频 EIS 开关
source: Vk4Od6Se3otT2MxUlVglBZfDg1d | revision: 436 | bytes: 8540
## headings
# 0. 文档信息
# **1. 变更日志**
# **2. 需求背景**
## **2.1 产品 / 数据现状**
## **2.2 用户调研**
## **2.3 竞品 / 对标情况**
# **3. 需求目标**
# **4. 需求范围**
## **4.1 范围内**
## **4.2 范围外**
# **5. 产品流程与交互**
## **5.1 交互原则**
## **5.2 流程说明**
## **5.3 交互设计稿 / 流程图**
# **6. 需求说明**
## **6.1 视频模式 / 慢动作模式新增「电子防抖（EIS）」设置项**
# **7. 关键依赖与约束**
# **8. 词条定义**
# **9. 埋点**
## **9.1 埋点目标**
## **9.2 埋点定义**
# **10. 指标与验收**
## **10.1 成功指标**
## **10.2 验收标准**
# **11. 风险与待确认项**
## selected snippets
```
# **2. 需求背景**

## **2.1 产品 / 数据现状**

- <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>
```
```
- <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>
- Nothing 相机视频模式目前默认开启 EIS（电子防抖），但缺少面向用户的显式开关。用户无法主动关闭 EIS，也无法感知当前 EIS 是否生效。
- EIS 在提升手持稳定性的同时，会对画面进行裁切，导致视角（FOV）缩小，并可能出现画面的偏移。**对于使用三脚架固定机位拍摄、或追求最大画角的创作者而言，强制开启的 EIS 反而会带来负面体验。**
```
```
- 对标结论：Nothing 可参考主流竞品方案，在相机设置的视频区域新增「视频防抖」开关，默认开启，允许用户按需关闭。

<grid>
<column width-ratio="0.500000">
Pixel：
```
```
- 关闭时，视频EIS关闭，仅有OIS防抖
- 适用范围

  - 所有摄像头
  - 视频模式、夜景视频模式、模糊处理视频模式、影片效果视频模式、延时摄影
  - 慢动作模式不支持EIS
```
```
- 所有摄像头
  - 视频模式、夜景视频模式、模糊处理视频模式、影片效果视频模式、延时摄影
  - 慢动作模式不支持EIS
  - 任意模式进入设置，开关不会置灰，均可以操作
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWJiNDI2NzIwZjBjMGM3ZDg3NWQyMGFkMGFkNTc5MTlfMDlhYTgwYTI4ODhiMDgyN2JiYmU3YTljYTIzNTRiNWVfSUQ6NzYzNDAwNjMyNTg3MzI5OTE2OF8xNzgzNDA2MzM1OjE3ODM0MDk5MzVfVjM)
</column>
```
```
- 视频模式、夜景视频模式、模糊处理视频模式、影片效果视频模式、延时摄影
  - 慢动作模式不支持EIS
  - 任意模式进入设置，开关不会置灰，均可以操作
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWJiNDI2NzIwZjBjMGM3ZDg3NWQyMGFkMGFkNTc5MTlfMDlhYTgwYTI4ODhiMDgyN2JiYmU3YTljYTIzNTRiNWVfSUQ6NzYzNDAwNjMyNTg3MzI5OTE2OF8xNzgzNDA2MzM1OjE3ODM0MDk5MzVfVjM)
</column>
<column width-ratio="0.500000">
```
```
- 慢动作模式不支持EIS
  - 任意模式进入设置，开关不会置灰，均可以操作
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWJiNDI2NzIwZjBjMGM3ZDg3NWQyMGFkMGFkNTc5MTlfMDlhYTgwYTI4ODhiMDgyN2JiYmU3YTljYTIzNTRiNWVfSUQ6NzYzNDAwNjMyNTg3MzI5OTE2OF8xNzgzNDA2MzM1OjE3ODM0MDk5MzVfVjM)
</column>
<column width-ratio="0.500000">
三星：
```
```
- 放在视频选项的一级菜单，并不是在“高级选项”中
- 适用范围

  - 仅对后置的摄像头生效，对前置无效
  - 视频模式、专业视频模式、延时摄影、人像视频、前后双拍
  - 慢动作模式不支持EIS
```
```
- 仅对后置的摄像头生效，对前置无效
  - 视频模式、专业视频模式、延时摄影、人像视频、前后双拍
  - 慢动作模式不支持EIS
  - 在慢动作模式下进入设置，开关置灰
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mjk5YzBhOTdhODE1NGRlYjRjMGI0MTZiODg1NThmMDBfNjdhNDY0ZjFhYWEzNjU4NmNjMTM2YWY0ODAzZjg5MGJfSUQ6NzYzNzM0MDM2MTE4MjEwNTMxNF8xNzgzNDA2MzM1OjE3ODM0MDk5MzVfVjM)
</column>
```
```
- 视频模式、专业视频模式、延时摄影、人像视频、前后双拍
  - 慢动作模式不支持EIS
  - 在慢动作模式下进入设置，开关置灰
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mjk5YzBhOTdhODE1NGRlYjRjMGI0MTZiODg1NThmMDBfNjdhNDY0ZjFhYWEzNjU4NmNjMTM2YWY0ODAzZjg5MGJfSUQ6NzYzNzM0MDM2MTE4MjEwNTMxNF8xNzgzNDA2MzM1OjE3ODM0MDk5MzVfVjM)
</column>
</grid>
```
```
- 慢动作模式不支持EIS
  - 在慢动作模式下进入设置，开关置灰
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Mjk5YzBhOTdhODE1NGRlYjRjMGI0MTZiODg1NThmMDBfNjdhNDY0ZjFhYWEzNjU4NmNjMTM2YWY0ODAzZjg5MGJfSUQ6NzYzNzM0MDM2MTE4MjEwNTMxNF8xNzgzNDA2MzM1OjE3ODM0MDk5MzVfVjM)
</column>
</grid>
```
```
# **3. 需求目标**

1. 在相机设置中新增「视频防抖」功能开关，允许用户选择在视频模式和前后双录模式录制时是否启用防抖。
2. 默认开启 EIS，保持当前用户体验；用户可主动关闭以获取最大画角。
3. 对齐竞品的用户感知逻辑，降低用户理解成本。
```

# 020 【PRD】Camera 4.0-视频锁定镜头
source: DTD2dpTlLop7yFxzWAPlm9bPgHe | revision: 210 | bytes: 5190
## headings
# 前言
# 一、 版本信息
# 二、 变更日志
# 三、 需求背景
## 产品 / 数据现状
## 竞品分析
### OPPO
### iPhone
# 四、需求目标
# 五、 需求范围
## 需求列表&需求单
# 六、 功能详细说明
## 需求词条
# 七、 非功能需求
# 八、 埋点
# 附录
## test heading
## selected snippets
```
# 三、 需求背景

## 产品 / 数据现状

当前 25111 Base 4K SAT 方案存在镜头切换跳变问题：在录像过程中变焦触发 SAT 切换时，画面出现明显的位移跳变，影响视频录制质量。
```
```
当前 25111 Base 4K SAT 方案存在镜头切换跳变问题：在录像过程中变焦触发 SAT 切换时，画面出现明显的位移跳变，影响视频录制质量。

SAT 能力本身具有实质收益——变焦时可调用长焦镜头，画质大幅优于同倍率下的数码变焦；但在当前方案下，切换过程的跳变体验抵消了部分用户对该能力的信任。

因此需向用户提供主动选择的开关：接受跳变以换取更好的长焦画质，或锁定单镜头牺牲光学变焦范围以保证录制画面的连续稳定性。
```
```
SAT 能力本身具有实质收益——变焦时可调用长焦镜头，画质大幅优于同倍率下的数码变焦；但在当前方案下，切换过程的跳变体验抵消了部分用户对该能力的信任。

因此需向用户提供主动选择的开关：接受跳变以换取更好的长焦画质，或锁定单镜头牺牲光学变焦范围以保证录制画面的连续稳定性。

## 竞品分析
```
```
因此需向用户提供主动选择的开关：接受跳变以换取更好的长焦画质，或锁定单镜头牺牲光学变焦范围以保证录制画面的连续稳定性。

## 竞品分析

> 列出竞品对比的主要信息和关键结论，可输入 @ 在此附上详细的竞品分析报告并添加在【附录】中
```
```
### OPPO
在相机的设置项中，视频设置小项，支持用户选择「锁定镜头」，
1. 关闭。 开启SAT能力，录像时可切换镜头
2. 开启。 开始录像前仍可切换镜头，但是开始录制后锁定在当前镜头，无论怎么变焦都是数码变焦。
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=Y2VmYTM5ODliYjNkMmEwOGU1Nzg3ZTBkNjI1ZTYwNjVfMzdjMmY5Mzk4ZWIyYTJmNTM3ZWE3MTFiMmIxZTY3ZjVfSUQ6NzYyOTY2OTI1ODA2MjEyMjcyNV8xNzgzNDA2MzM4OjE3ODM0MDk5MzhfVjM)
</column>
```
```
### iPhone
1. 交互逻辑和OPPO类似。
![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MDcwN2M4MGJjYWMyMjBjNzE0ZmM5YTk3ZTUwZDFhMDJfNjU4ZGUzZDNhYzVjMjMzNGNhNjE4Y2YxNTVmYWZlNjhfSUQ6NzYyOTY2OTMxNzMxMTI4NzAwNl8xNzgzNDA2MzM4OjE3ODM0MDk5MzhfVjM)
</column>
</grid>
```
```
# 四、需求目标

在视频模式中新增「锁定镜头」功能开关，允许用户选择录制时是否允许 SAT 自动切换镜头

- 开关关闭时（默认）：保持现有 SAT 行为，录像过程中可自动切换物理镜头
```
```
在视频模式中新增「锁定镜头」功能开关，允许用户选择录制时是否允许 SAT 自动切换镜头

- 开关关闭时（默认）：保持现有 SAT 行为，录像过程中可自动切换物理镜头
- 开关开启时：录制开始后锁定当前镜头，用户的变焦行为降级为数码变焦，避免跳变
- 对齐 OPPO / iPhone 等主流竞品的用户感知逻辑，降低用户理解成本
```
```
# 五、 需求范围

> 可条理性地罗列需求范围或信息架构

1. 项目范围：在 25111 base/pro 上首次上项
```
```
> 可条理性地罗列需求范围或信息架构

1. 项目范围：在 25111 base/pro 上首次上项
2. 模式范围：仅限于视频模式
3. 生效范围：对所有视频规格生效
```
```
1. 项目范围：在 25111 base/pro 上首次上项
2. 模式范围：仅限于视频模式
3. 生效范围：对所有视频规格生效
4. 老项目回落：不支持回落
```
```
1. 项目范围：在 25111 base/pro 上首次上项
2. 模式范围：仅限于视频模式
3. 生效范围：对所有视频规格生效
4. 老项目回落：不支持回落

## 需求列表&需求单
```

# 021 【PRD】Camera 5.1 - 视频锁定白平衡
source: GVaHdfT0eouHxJxawuqlwLpjgme | revision: 378 | bytes: 8407
## headings
# 0. 文档信息
# 1. 变更日志
# 2. 需求背景
## 2.1 产品 / 数据现状
## 2.2 用户调研
## 2.3 竞品 / 对标情况
# 3. 需求目标
# 4. 需求范围
## 4.1 范围内
## 4.2 范围外
# 5. 产品流程与交互
## 5.1 交互原则
## 5.2 流程说明
## 5.3 交互设计稿 / 流程图
# 6. 需求说明
## 6.1 视频模式新增「锁定白平衡」设置项
### 功能支持范围
### 功能详细说明
### 限制与说明
# 7. 关键依赖与约束
## 7.1 技术依赖
## 7.2 产品与配置依赖
# 8. 词条定义
# 9. 埋点
## 9.1 埋点目标
## 9.2 埋点定义
# 10. 指标与验收
## 10.1 成功指标
## 10.2 验收标准
# 11. 风险与待确认项
## selected snippets
```
# 2. 需求背景

## 2.1 产品 / 数据现状

- <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>
```
```
- <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>
- Nothing 相机视频模式目前仅支持自动白平衡（AWB），录制全程由算法动态调整白平衡数值，用户无法干预。
- 此机制在混合光源环境、长时间固定机位录制的场景会产生明显的问题，可能因为环境光的变化导致白平衡漂移，影响素材的色彩一致性。对于有创作需求的用户他们希望对自己的录制可以有基础的控制。特别是对后期有需求的用户来说，录制中白平衡不稳定可能会增加后期修正的工作量，甚至导致部分镜头无法修复。需要给用户提供主动选择权，在有需要的场景自行锁定白平衡。
- OPPO、iPhone 等主流竞品均已提供「录制过程中锁定白平衡」能力，**Nothing 当前缺失该功能**，在专业用户与内容创作者群体中存在明显的竞争劣势。

## 2.2 用户调研
```
```
- Nothing 相机视频模式目前仅支持自动白平衡（AWB），录制全程由算法动态调整白平衡数值，用户无法干预。
- 此机制在混合光源环境、长时间固定机位录制的场景会产生明显的问题，可能因为环境光的变化导致白平衡漂移，影响素材的色彩一致性。对于有创作需求的用户他们希望对自己的录制可以有基础的控制。特别是对后期有需求的用户来说，录制中白平衡不稳定可能会增加后期修正的工作量，甚至导致部分镜头无法修复。需要给用户提供主动选择权，在有需要的场景自行锁定白平衡。
- OPPO、iPhone 等主流竞品均已提供「录制过程中锁定白平衡」能力，**Nothing 当前缺失该功能**，在专业用户与内容创作者群体中存在明显的竞争劣势。

## 2.2 用户调研
```
```
- 此机制在混合光源环境、长时间固定机位录制的场景会产生明显的问题，可能因为环境光的变化导致白平衡漂移，影响素材的色彩一致性。对于有创作需求的用户他们希望对自己的录制可以有基础的控制。特别是对后期有需求的用户来说，录制中白平衡不稳定可能会增加后期修正的工作量，甚至导致部分镜头无法修复。需要给用户提供主动选择权，在有需要的场景自行锁定白平衡。
- OPPO、iPhone 等主流竞品均已提供「录制过程中锁定白平衡」能力，**Nothing 当前缺失该功能**，在专业用户与内容创作者群体中存在明显的竞争劣势。

## 2.2 用户调研

- 调研方式：竞品体验分析
```
```
- 调研方式：竞品体验分析
- 样本情况：OPPO、iPhone 视频模式相关能力对比
- 核心结论：主流竞品均提供“录制过程中锁定白平衡”的能力，交互逻辑相似，用户理解成本较低。

## 2.3 竞品 / 对标情况
```
```
- 样本情况：OPPO、iPhone 视频模式相关能力对比
- 核心结论：主流竞品均提供“录制过程中锁定白平衡”的能力，交互逻辑相似，用户理解成本较低。

## 2.3 竞品 / 对标情况

- 对标结论：Nothing 可参考主流竞品方案，在视频模式下提供明确的「锁定白平衡」开关，降低用户理解门槛。
```
```
- 对标结论：Nothing 可参考主流竞品方案，在视频模式下提供明确的「锁定白平衡」开关，降低用户理解门槛。

<grid>
<column width-ratio="0.500000">
- **OPPO**
```
```
- 在相机设置的视频设置项中支持「锁定白平衡」。
  - 关闭时，视频录制中使用自动白平衡
  - 开启后，视频录制前仍为自动白平衡，录制中锁定。

  ![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmFjNDMzZmM0NTY3M2EwNzhkNjIxODI1NWIwZWI5MjhfMTVlNTExOTEwNjUwZTNiZWE2ZGIzYTFlNTUwZmE0MjNfSUQ6NzYzMTQyNzUxMTIyMTc1MTUyNV8xNzgzNDA2MzQxOjE3ODM0MDk5NDFfVjM)
```
```
- 交互逻辑与 OPPO 类似。

  ![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmI4YzY1YTJiY2RlZmZhYTE0MjU2MTliMTU2YmEyMGJfNWIwY2Q3ODI4YzU2ZTU4OTZmZTQ3MDMyNzc5NmI0MDdfSUQ6NzYzMTQyNzUxMTcyNjY5MDAxNV8xNzgzNDA2MzQxOjE3ODM0MDk5NDFfVjM)
</column>
</grid>
```
```
# 3. 需求目标

1. 在视频模式中新增「锁定白平衡」功能开关，允许用户选择录制时是否允许白平衡自动变化。
2. 对齐 OPPO、iPhone 等主流竞品的用户感知逻辑，降低用户理解成本。
```
```
1. 在视频模式中新增「锁定白平衡」功能开关，允许用户选择录制时是否允许白平衡自动变化。
2. 对齐 OPPO、iPhone 等主流竞品的用户感知逻辑，降低用户理解成本。

---
```
```
# 4. 需求范围

## 4.1 范围内

- 项目范围：26111首次上项。
```

# 022 【PRD】Camera 5.1 - 视频模式专业参数调节
source: Ny4HdTqI3oLtYLx2m1wlDP9Mgdg | revision: 780 | bytes: 16987
## headings
# 0. 文档信息
# 变更日志
# 需求背景
### 2.1 产品 / 数据现状
### 2.2 用户调研
### 2.3 竞品 / 对标情况
# 需求目标
# 需求范围
### 4.1 范围内
### 4.2 范围外
# 产品流程与交互
### 5.1 交互原则
### 5.2 流程说明
### 5.3 交互设计稿 / 流程图
# 需求说明
### 6.1 视频模式下拉菜单新增「曝光」开关
### 6.2 视频模式下拉菜单新增「白平衡」开关
### 6.3 功能互斥表
# 关键依赖与约束
### 7.1 技术依赖
### 7.2 产品与配置依赖
# 词条定义
# 埋点
### 9.1 埋点目标
### 9.2 埋点定义
# 指标与验收
### 10.1 成功指标
### 10.2 验收标准
## selected snippets
```
<title>【PRD】Camera 5.1 - 视频模式专业参数调节</title>



# 0. 文档信息
```
```
- 文档标题：`【PRD】Camera 5.0-视频模式专业参数调节`
- 项目 / 机型 / 代号：26111 Base / Pro
- 所属版本：Camera 5.0
- 作者：Tiger Xu
- 更新时间：2026/5/8
```
```
# 需求背景

### 2.1 产品 / 数据现状

- <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>
```
```
- <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频能力建设 Overview" type="doc"></cite>
- Nothing 相机视频模式目前缺少面向用户的专业参数控制能力。用户在录制视频时无法常态调节曝光偏移（EV），也无法手动指定白平衡，只能依赖全自动的 3A 算法。
- 自动 AE 算法在持续调整曝光的过程中，可能出现曝光跳变，在逆光、混合光源等场景下尤为明显，被评测者指出是「削弱对整个系统信心」的核心痛点之一。
- 自动白平衡（AWB）在室内混合光源、场景转换等场景下容易出现色温大幅度变化，影响成片一致性。
- 25111 Pro 目前仅支持「小太阳」触摸曝光，且对焦框消失后即失效，不具备持久调节能力。
```
```
- Nothing 相机视频模式目前缺少面向用户的专业参数控制能力。用户在录制视频时无法常态调节曝光偏移（EV），也无法手动指定白平衡，只能依赖全自动的 3A 算法。
- 自动 AE 算法在持续调整曝光的过程中，可能出现曝光跳变，在逆光、混合光源等场景下尤为明显，被评测者指出是「削弱对整个系统信心」的核心痛点之一。
- 自动白平衡（AWB）在室内混合光源、场景转换等场景下容易出现色温大幅度变化，影响成片一致性。
- 25111 Pro 目前仅支持「小太阳」触摸曝光，且对焦框消失后即失效，不具备持久调节能力。

### 2.2 用户调研
```
```
- 自动 AE 算法在持续调整曝光的过程中，可能出现曝光跳变，在逆光、混合光源等场景下尤为明显，被评测者指出是「削弱对整个系统信心」的核心痛点之一。
- 自动白平衡（AWB）在室内混合光源、场景转换等场景下容易出现色温大幅度变化，影响成片一致性。
- 25111 Pro 目前仅支持「小太阳」触摸曝光，且对焦框消失后即失效，不具备持久调节能力。

### 2.2 用户调研
```
```
- 自动白平衡（AWB）在室内混合光源、场景转换等场景下容易出现色温大幅度变化，影响成片一致性。
- 25111 Pro 目前仅支持「小太阳」触摸曝光，且对焦框消失后即失效，不具备持久调节能力。

### 2.2 用户调研

- **调研方式：**竞品体验分析
```
```
- **样本情况：**Pixel 9 Pro、三星 S25 Ultra、iPhone 17 Pro、Vivo X300、Vivo V70、OPPO Reno 15 视频专业参数能力对比
- **核心结论：** 独立 EV 调节已是主流竞品视频模式标配，但绝大多数在录制中只提供「小太阳」触摸曝光，并非真正意义上的独立 EV 控件；手动白平衡则是更高层次的差异化能力，仅少数竞品支持。Pixel 9 Pro 提供了一套兼顾专业度与易用性的实现方案，具有较高参考价值。

### 2.3 竞品 / 对标情况

**对标结论：**以 Pixel 9 Pro 为主要参考，在标准视频模式下提供独立的 Exposure 和 White Balance 调节入口，以简化的交互控件降低上手门槛，同时给予用户真实的参数控制权。
```
```
**对标结论：**以 Pixel 9 Pro 为主要参考，在标准视频模式下提供独立的 Exposure 和 White Balance 调节入口，以简化的交互控件降低上手门槛，同时给予用户真实的参数控制权。

| **能力** | Pixel 9 Pro | 三星S25 Ultra | iPhone 17 Pro | Vivo X300 | Vivo V70 | Reno 15 | 25111Pro |
|-|-|-|-|-|-|-|-|
| 视频模式是否有独立EV调节 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️只能拉小太阳 |
```
```
|-|-|-|-|-|-|-|-|
| 视频模式是否有独立EV调节 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️只能拉小太阳 |
| EV 调节范围 | 未标注  <br/>约-3EV～+4EV | -2EV～+2EV | -2EV～+2EV | -100～+100  <br/>⚠️只能拉小太阳 | -100～+100  <br/>约-2EV～+2EV | -2EV～+2EV | 未标注  <br/>约-2EV～+2EV |
| 是否有白平衡调节 | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 白平衡调节路径 | 视频模式-右下角参数 | 专业视频 | / | 专业视频 | / | / | / |
| 是否有预设值 | 🈚️ | 🈚️ | / | ✅晴、阴、多云、白炽灯、钨丝灯、夕阳；灰卡自动校准 | / | / | / |
```
```
| 视频模式是否有独立EV调节 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️只能拉小太阳 |
| EV 调节范围 | 未标注  <br/>约-3EV～+4EV | -2EV～+2EV | -2EV～+2EV | -100～+100  <br/>⚠️只能拉小太阳 | -100～+100  <br/>约-2EV～+2EV | -2EV～+2EV | 未标注  <br/>约-2EV～+2EV |
| 是否有白平衡调节 | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 白平衡调节路径 | 视频模式-右下角参数 | 专业视频 | / | 专业视频 | / | / | / |
| 是否有预设值 | 🈚️ | 🈚️ | / | ✅晴、阴、多云、白炽灯、钨丝灯、夕阳；灰卡自动校准 | / | / | / |
| 白平衡调节范围 | 检测值-2000K～检测值+3500K | 色温：2300K～10000K | / | 色温：2300K～10000K  <br/>色调：-100～+100 | / | / | / |
```
```
| 是否有白平衡调节 | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 白平衡调节路径 | 视频模式-右下角参数 | 专业视频 | / | 专业视频 | / | / | / |
| 是否有预设值 | 🈚️ | 🈚️ | / | ✅晴、阴、多云、白炽灯、钨丝灯、夕阳；灰卡自动校准 | / | / | / |
| 白平衡调节范围 | 检测值-2000K～检测值+3500K | 色温：2300K～10000K | / | 色温：2300K～10000K  <br/>色调：-100～+100 | / | / | / |
| 如何处理色调 | 保留检测值 | 手动时还原为0  <br/>且不可调整 | / | 手动设置 | / | / | / |
| 录制中实时调节 | ✅EV和白平衡均可随时调整 | ⚠️视频模式：只能拉小太阳改变曝光  <br/>专业模式：所有参数可视化存在可调 | ⚠️只能拉小太阳 | ⚠️视频模式：只能拉小太阳改变曝光  <br/>专业模式：所有参数可视化存在可调 | ⚠️只能拉小太阳 | ⚠️只能拉小太阳 | ⚠️只能拉小太阳 |
```

# 023 【PRD】Camera 5.1 - 视频默认 H.265 编码
source: MoVidaFWooY5enx6IIGldnI5ghe | revision: 124 | bytes: 5604
## headings
# 【PRD】Camera 5.1 - 视频默认 H.265 编码
## 0. 文档信息
## 变更日志
## 背景与目标
### 2.1 用户问题
### 2.2 行业现状
### 2.3 用户目标
### 2.4 产品目标
## 功能定义
### 3.1 功能名称
### 3.2 一句话描述
### 3.3 范围
## 设计稿
## 需求
### R1 · 默认编码变更为 H.265
### R2 · 编码设置全模式一致生效(录屏链路改造)
### R3 · HLG 联动逻辑维持现状
### 5.1 编码生效逻辑表
## 关键依赖与约束
## 词条定义
## 指标与验收
### 8.1 成功指标
### 8.2 验收标准
## 埋点
## 风险与待确认项
## selected snippets
```
## 背景与目标

### 2.1 用户问题

- 当前默认 H.264,同画质下文件体积比 H.265 大约 30%,用户存储被无意义地多占用。
```
```
- 当前默认 H.264,同画质下文件体积比 H.265 大约 30%,用户存储被无意义地多占用。
- 当前编码逻辑对用户不透明且不自洽: 

  - 用户手动选择 H.265 后,视频、慢动作、延时按 H.265 录制;但视频开滤镜、或使用前后双录(预览录屏链路)时,实际输出静默回落为 H.264——用户选了 H.265,拿到的却可能是 H.264 文件。
  - 默认 H.264 下开启 HLG 时,系统因 10-bit 依赖自动切换为 H.265——系统已默认 H.265 是更高能力的编码,默认值却停留在 H.264。
```
```
- 用户手动选择 H.265 后,视频、慢动作、延时按 H.265 录制;但视频开滤镜、或使用前后双录(预览录屏链路)时,实际输出静默回落为 H.264——用户选了 H.265,拿到的却可能是 H.264 文件。
  - 默认 H.264 下开启 HLG 时,系统因 10-bit 依赖自动切换为 H.265——系统已默认 H.265 是更高能力的编码,默认值却停留在 H.264。

### 2.2 行业现状

- iPhone、三星、Pixel 等主流厂商均已默认 HEVC/H.265 多年,是行业共识性默认选择。
```
```
- iPhone、三星、Pixel 等主流厂商均已默认 HEVC/H.265 多年,是行业共识性默认选择。
- 2026 年当下,主流平台与设备对 H.265 的解码与分享支持已普及,兼容性风险基本消除。

### 2.3 用户目标

- 不做任何设置,即获得同画质、更小体积的视频文件。
```
```
### 2.3 用户目标

- 不做任何设置,即获得同画质、更小体积的视频文件。
- 自己的编码选择在任何模式下都被一致执行,不出现静默回落。
```
```
- 不做任何设置,即获得同画质、更小体积的视频文件。
- 自己的编码选择在任何模式下都被一致执行,不出现静默回落。

### 2.4 产品目标
```
```
- 不做任何设置,即获得同画质、更小体积的视频文件。
- 自己的编码选择在任何模式下都被一致执行,不出现静默回落。

### 2.4 产品目标

- 26111 / 26121 新机型出厂默认编码改为 H.265。
```
```
### 2.4 产品目标

- 26111 / 26121 新机型出厂默认编码改为 H.265。
- 编码设置在全部视频相关模式下一致生效,消除链路差异导致的编码不一致。
```
```
- 26111 / 26121 新机型出厂默认编码改为 H.265。
- 编码设置在全部视频相关模式下一致生效,消除链路差异导致的编码不一致。



## 功能定义
```
```
## 功能定义

### 3.1 功能名称

视频默认 H.265 编码
```
```
### 3.1 功能名称

视频默认 H.265 编码

### 3.2 一句话描述
```
```
新机型视频默认编码由 H.264 改为 H.265,并使编码设置在所有模式(含滤镜、前后双录等录屏链路)下一致生效。

### 3.3 范围

**范围内**
```

# 024 【PRD】Camera 5.1 - 前后双录 v2
source: Xh3udZK6RoAVv3xfELWlAODggLc | revision: 624 | bytes: 17127
## headings
# 0. 文档信息
# 变更日志
# 需求背景
## 产品 / 数据现状
# 需求目标
# 需求范围
## 范围内
## 范围外（本期不包含）
# 功能设计
## ~~【评估项】4K 分辨率支持~~
#### 功能支持范围
#### 功能详细说明
#### 限制与说明
## 录制前后置镜头选择
#### 功能支持范围
#### 功能详细说明
#### 限制与说明
## 录制中前后摄主副位置互换
#### 功能支持范围
#### 功能详细说明
#### 限制与说明
## 小窗大小两档切换（画中画模式）
#### 功能支持范围
#### 功能详细说明
#### 限制与说明
## 双文件独立保存
#### 功能支持范围
#### 功能详细说明
#### 限制与说明
## 5.6 功能互斥
## 5.7 Feature List（v2 增量视图）
# 效果定义与验收标准
## 预期效果
## 验收口径
# 词条定义
# 埋点
## 埋点目标
##  埋点定义
# 项目计划与风险
## 项目计划
## 风险与兜底
# 待确认事项
## 待确认清单
## 评审关注点（按需）
## selected snippets
```
只记录影响需求理解的修改。

| 时间 | 版本号 | 变更人 | 主要变更内容 |
|-|-|-|-|
| 2026-5-14 | v0.1 | Tiger | 创建 |
```
```
# 需求背景

> 只回答一个问题：为什么现在要做。这里写现状、问题、证据，不写目标，不写方案。

## 产品 / 数据现状
```
```
> 只回答一个问题：为什么现在要做。这里写现状、问题、证据，不写目标，不写方案。

## 产品 / 数据现状

当前在25131上落地了前后双录的基础能力，实现了从无到有的突破。根据规划，部分能力要在26111上进行升级
```
```
# 需求目标

> 只回答一个问题：这次做完后，要得到什么结果。直接写结果，不重复背景，不展开实现方式。

- ~~在Pro机型（26121）上实现4K的前后双录能力~~
```
```
> 只回答一个问题：这次做完后，要得到什么结果。直接写结果，不重复背景，不展开实现方式。

- ~~在Pro机型（26121）上实现4K的前后双录能力~~
- 用户可在录制前选择想使用的后置镜头（透过变焦指示器），支持所有后置镜头
- 双文件独立保存 （可能有性能风险）
```
```
- ~~在Pro机型（26121）上实现4K的前后双录能力~~
- 用户可在录制前选择想使用的后置镜头（透过变焦指示器），支持所有后置镜头
- 双文件独立保存 （可能有性能风险）
- 用户在双录录制过程中可随时互换主副摄，无需中断录制
- ~~画中画模式下小窗支持两档大小调节~~
```
```
- 用户可在录制前选择想使用的后置镜头（透过变焦指示器），支持所有后置镜头
- 双文件独立保存 （可能有性能风险）
- 用户在双录录制过程中可随时互换主副摄，无需中断录制
- ~~画中画模式下小窗支持两档大小调节~~

---
```
```
- 用户在双录录制过程中可随时互换主副摄，无需中断录制
- ~~画中画模式下小窗支持两档大小调节~~

---

# 需求范围
```
```
# 需求范围

> 写清做什么，不做什么。

## 范围内
```
```
> 写清做什么，不做什么。

## 范围内

- ~~Pro机型前后双录支持4K30帧输出~~
```
```
## 范围内

- ~~Pro机型前后双录支持4K30帧输出~~
- 录制前后置镜头可以在所有可支持的后置摄像头中选择（base：超广/主摄；Pro：超广/主摄/长焦）
- 录制中支持前后摄主副位置互换，无需停止录制。
```
```
- ~~Pro机型前后双录支持4K30帧输出~~
- 录制前后置镜头可以在所有可支持的后置摄像头中选择（base：超广/主摄；Pro：超广/主摄/长焦）
- 录制中支持前后摄主副位置互换，无需停止录制。
- 画中画模式下，小窗支持大小两档切换，录制前与录制中均可操作。
- 前后摄像头文件分别独立保存的能力
```

# 025 【PRD】Camera 5.1 - 录像中拍照（VSS）效果提升
source: HIdPdtWOmotqKCxVBoBlPsvggNw | revision: 428 | bytes: 12884
## headings
# 0. 文档信息
# 变更日志
# 需求背景
### 2.1 产品 / 数据现状
### 2.2 用户调研
### 2.3 竞品情况
# 需求目标
# 需求范围
### 4.1 范围内
### 4.2 范围外
# 产品流程与交互
# 关键依赖与约束
# 词条定义
# 埋点
# 指标与验收
### 9.1 成功指标
### 9.2 验收标准
## selected snippets
```
# 需求背景

### 2.1 产品 / 数据现状

当前 VSS（录像中拍照）实现方式为视频截帧：1080P 下输出仅 2MP，4K 下输出 8MP，画质显著低于单帧拍照水平。
```
```
当前 VSS（录像中拍照）实现方式为视频截帧：1080P 下输出仅 2MP，4K 下输出 8MP，画质显著低于单帧拍照水平。

<table><colgroup><col/><col/></colgroup><thead><tr><th><b>25111P ——视频下拍照和单帧拍照的放大对比图</b></th><th>原图</th></tr></thead><tbody><tr><td><img name="image.png" caption="&#xA;" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZDdhYWQxOTQ0MzNmZTcyOTY1NGUxYmM5OTBmMzU4OThfZmNjMjYxMmMzMDEwYzE4OWZmMmY5MmZhNmIxOGE5NzZfSUQ6NzY0Nzg0NDY5NTY5MDgyNTQ0NV8xNzgzNDA2MzUxOjE3ODM0MDk5NTFfVjM" mime="image/png" scale="1.000000" src="TJGGbJ9sqoo5SpxGpsMl5LrHgRc"/><grid><column width-ratio="0.333333"><p>当前 4K录像VSS</p></column><column width-ratio="0.333333"><p>单帧拍照</p></column><column width-ratio="0.333333"><p>当前 1080P录像VSS</p></column></grid></td><td><grid><column width-ratio="0.333333"><img name="25111p_vss_4k_1.jpg" caption="4k vss&#xA;" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NTllZWZmMWRkYmFiNGI4NzI2MzAyNWE5MzNhMzQ4ZDJfMTU3MTY5NGZhOThjZmY2ZTdjYWFlZmYzZDhmNjg0MWVfSUQ6NzY0Nzg0NDY5NDQ0OTQ0MjUyNF8xNzgzNDA2MzUxOjE3ODM0MDk5NTFfVjM" mime="image/jpeg" scale="0.337963" src="D7Snby8b8opTlfxEemrlbuhEgwb"/></column><column width-ratio="0.333333"><img name="25111p_vss_a_1.jpg" caption="单帧拍照&#xA;" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODYzNmU1MDI0ZWUzZmQ1Y2M4MTRhOTU0MWViMDQwMTRfMzRjNzZjYzU4MWRkMWMzYjgzN2EyNDNiOTRkNTNkNDNfSUQ6NzY0Nzg0NDY5Mjg0MzA1Njg2MV8xNzgzNDA2MzUxOjE3ODM0MDk5NTFfVjM" mime="image/jpeg" scale="0.316840" src="K9lVbdD6SoN2qQxLZMjlaAXdgSh"/></column><column width-ratio="0.333333"><img name="25111p_vss_fhd_1.jpg" caption="1080P vss&#xA;" href="https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGE5MWVhMmY0ZTNjYmZiMzI0MTM1ZjQ1MjcxYjhmMjhfOGEzY
```
```
用户在录视频时按下 VSS 快门，本质是一个**质量声明**：「我要把这个瞬间以照片的标准保存下来。」如果只是需要视频里的某一帧，用户不需要这个按钮——视频本身已包含所有帧，事后随时可截。VSS 的存在价值在于：**以照片级别的质量，捕捉用户在录像中看到的那个瞬间。** 当前截帧方案无法满足这一本质需求。



**埋点数据：**
```
```
- 92% 受访者会使用 VSS；86% 对当前画质不满意或处于「凑合用」状态
- 使用场景集中于「不想错过瞬间」的高情绪场景（演唱会/赛事 82%，旅行风景 75%）
- 81% 倾向「宁可等待处理也要高质量」
- 仅 4% 对「VSS 照片清晰度高于视频」有负面感知——画质提升不存在感知风险
- 61%+ 用户对照片 FOV 比视频更宽有不同程度的负面感知
```
```
- 81% 倾向「宁可等待处理也要高质量」
- 仅 4% 对「VSS 照片清晰度高于视频」有负面感知——画质提升不存在感知风险
- 61%+ 用户对照片 FOV 比视频更宽有不同程度的负面感知

详见<cite doc-id="Ro5nwT7PYitQGDknLe4lneDMgUg" file-type="wiki" title="录像中拍照 功能用户问卷调研" type="doc"></cite>
```
```
详见<cite doc-id="Ro5nwT7PYitQGDknLe4lneDMgUg" file-type="wiki" title="录像中拍照 功能用户问卷调研" type="doc"></cite>



### 2.3 竞品情况
```
```
<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>层级</b></th><th vertical-align="middle"><b>机型</b></th><th vertical-align="middle"><b>出图方式</b></th><th vertical-align="middle"><b>分辨率</b></th><th vertical-align="middle"><b>更多</b></th><th vertical-align="middle"><b>FOV</b></th></tr></thead><tbody><tr><td rowspan="4" vertical-align="middle">旗舰参考</td><td>苹果 iPhone 17 Pro</td><td>拍照</td><td>7mp（动态裁切）</td><td>有一定拍照算法+XDR</td><td>与视频一致</td></tr><tr><td>三星 S25 Ultra</td><td>拍照</td><td>9mp</td><td>有一定拍照算法+XDR</td><td>与照片一致</td></tr><tr><td>华为 Pura 90</td><td>拍照</td><td>9mp</td><td>—</td><td>与照片一致</td></tr><tr><td>Vivo X300 Ultra</td><td>拍照</td><td>9mp</td><td>有一定拍照算法+XDR</td><td>与照片一致</td></tr><tr><td rowspan="3" vertical-align="middle">中端分化</td><td>OPPO Reno 16</td><td>视频截Live</td><td>同视频分辨率</td><td>—</td><td>与视频一致</td></tr><tr><td>荣耀 600</td><td>视频截Live</td><td>同视频分辨率</td><td>—</td><td>与视频一致</td></tr><tr><td>华为 Nova 16</td><td>拍照</td><td>9mp</td><td>—</td><td>与照片一致</td></tr><tr><td vertical-align="middle">中端普通</td><td>Vivo S60</td><td>视频截帧</td><td>同视频分辨率</td><td>—</td><td>与视频一致</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

**从演进方向看**，单帧路线正在从旗舰向中端下渗：三星和苹果已在旗舰上稳定运行多年；vivo 在 X300 Ultra 上引入独立拍照通路；华为今年 nova16 系列专项宣传录中拍照画质优化。
```
```
**从演进方向看**，单帧路线正在从旗舰向中端下渗：三星和苹果已在旗舰上稳定运行多年；vivo 在 X300 Ultra 上引入独立拍照通路；华为今年 nova16 系列专项宣传录中拍照画质优化。



**结论：** 旗舰机型已全面采用单帧拍照路线，输出 9MP（苹果动态裁切至 7MP），部分叠加轻量算法与 XDR 效果。中端市场出现分化，OPPO、荣耀走视频截 Live Photo 路线，华为从 nova16 开始优化，也走拍照路线，Vivo S60 等仍为视频截帧无优化。**清晰度是当前中端 录像中拍照 的普遍短板，也是最直接的差距所在。**
```
```
**结论：** 旗舰机型已全面采用单帧拍照路线，输出 9MP（苹果动态裁切至 7MP），部分叠加轻量算法与 XDR 效果。中端市场出现分化，OPPO、荣耀走视频截 Live Photo 路线，华为从 nova16 开始优化，也走拍照路线，Vivo S60 等仍为视频截帧无优化。**清晰度是当前中端 录像中拍照 的普遍短板，也是最直接的差距所在。**

---

# 需求目标
```
```
# 需求目标

**核心目标：** 提升录像中拍照的拍照质量，用更佳的质量帮助用户留住瞬间。

完整的体验改善需同时满足以下三项，三者为不可分割的最小完整单元：
```
```
**核心目标：** 提升录像中拍照的拍照质量，用更佳的质量帮助用户留住瞬间。

完整的体验改善需同时满足以下三项，三者为不可分割的最小完整单元：

1. **照片该有的质量**：改为单帧拍照，统一输出 9MP；有性能余量时叠加 MFNR
```
```
# 需求范围

### 4.1 范围内

- **项目范围：** 26111 / 26121首次上项
```

# 026 SAT 体验优化
source: PlZVdBufqoC6oPx4MjxlgGmpgOd | revision: 2707 | bytes: 10204
## headings
# SAT 体验优化
### 点切
### 滑动变焦
### Fallback（长焦近距离切主摄）
## selected snippets
```
**结论**
- 跟手性上，主要问题在于点切时动画响应的时间较慢（特别在视频模式录制下），滑动变焦时变焦条不够跟手、画面变化存在较大延迟
- 平滑性上，或可优化动画变化曲线，提升点切时的流畅性
- 画面跳变上，画面视角、色彩均存在较为明显的跳变（OPPO、vivo同样有较为明显的跳变，跳变控制较好的是Samsung，reno16有一定优化）
**可优化维度**
1. 平滑性：优化点切变焦曲线（可参考 Reno16）
```
```
- 跟手性上，关注点击变焦到画面动画开始变化的间隔时间（T1），base/pro动画响应速度较慢（特别在视频模式录制下）

  - 照片模式下：reno15 > v70 > pro > s25ultra > base
  - 视频模式下（录制）：reno15 > v70/s25ultra > pro > base
- 平滑性上，关注变焦动画的帧率、变化曲线
```
```
- 照片模式下：reno15 > v70 > pro > s25ultra > base
  - 视频模式下（录制）：reno15 > v70/s25ultra > pro > base
- 平滑性上，关注变焦动画的帧率、变化曲线

  - 变焦动画帧率（有效动画帧数/T2-T1）上无明显差距
```
```
- 照片模式下：reno15 > v70 > pro > s25ultra > base
  - 视频模式下（录制）：reno15 > v70/s25ultra > pro > base
- 平滑性上，关注变焦动画的帧率、变化曲线

  - 变焦动画帧率（有效动画帧数/T2-T1）上无明显差距
  - 变化曲线上，base/pro/v70 变化速率曲线较平缓，reno15/s25ultra 曲线变化较大，其中 reno15 是从慢到较快再到慢，s25ultra 是从极快到慢。主观感受上，reno15/s25ultra 变焦体验更为丝滑，或可优化变化曲线提升 SAT 体验
```
```
以下测试照片模式、视频模式从1x到3x的变焦过程：  
（T1为从点击到画面开始变化的帧数，T2为从点击到变焦动画结束的帧数，T3为画面最后跳变发生的帧数，有效动画帧数记录真正变化的帧数）

<table><colgroup><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="2" vertical-align="middle">单位：帧</td><td vertical-align="middle">base</td><td vertical-align="middle">pro</td><td vertical-align="middle">reno15</td><td vertical-align="middle">v70</td><td vertical-align="middle">s25ultra</td></tr><tr><td rowspan="4" vertical-align="middle">照片模式</td><td vertical-align="middle">T1</td><td vertical-align="middle">14</td><td vertical-align="middle">10</td><td vertical-align="middle">5</td><td vertical-align="middle">7</td><td vertical-align="middle">13</td></tr><tr><td vertical-align="middle">T2</td><td vertical-align="middle">22</td><td vertical-align="middle">21</td><td vertical-align="middle">16</td><td vertical-align="middle">18</td><td vertical-align="middle">22</td></tr><tr><td vertical-align="middle">T3</td><td vertical-align="middle">23</td><td vertical-align="middle">23</td><td vertical-align="middle">17</td><td vertical-align="middle">17</td><td vertical-align="middle">26</td></tr><tr><td vertical-align="middle">有效动画帧数<br/>/T2-T1+1</td><td vertical-align="middle">6/9</td><td vertical-align="middle">6/12</td><td vertical-align="middle">7/12</td><td vertical-align="middle">7/12</td><td vertical-align="middle">6/10</td></tr><tr><td rowspan="4" vertical-align="middle">视频模式</td><td vertical-align="middle">T1</td><td vertical-align="middle">15</td><td vertical-align="middle">12</td><td vertical-align="middle">6</td><td vertical-align="middle">9</td><td vertical-align="middle">10</td></tr><tr><td vertical-align="middle">T2</td><td vertical-align="middle">27</td><td vertical-align="middle">22</td><td vertical-align="middle">23</td><td vertical-align="m
```
```
<table><colgroup><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td colspan="2" vertical-align="middle">单位：帧</td><td vertical-align="middle">base</td><td vertical-align="middle">pro</td><td vertical-align="middle">reno15</td><td vertical-align="middle">v70</td><td vertical-align="middle">s25ultra</td></tr><tr><td rowspan="4" vertical-align="middle">照片模式</td><td vertical-align="middle">T1</td><td vertical-align="middle">14</td><td vertical-align="middle">10</td><td vertical-align="middle">5</td><td vertical-align="middle">7</td><td vertical-align="middle">13</td></tr><tr><td vertical-align="middle">T2</td><td vertical-align="middle">22</td><td vertical-align="middle">21</td><td vertical-align="middle">16</td><td vertical-align="middle">18</td><td vertical-align="middle">22</td></tr><tr><td vertical-align="middle">T3</td><td vertical-align="middle">23</td><td vertical-align="middle">23</td><td vertical-align="middle">17</td><td vertical-align="middle">17</td><td vertical-align="middle">26</td></tr><tr><td vertical-align="middle">有效动画帧数<br/>/T2-T1+1</td><td vertical-align="middle">6/9</td><td vertical-align="middle">6/12</td><td vertical-align="middle">7/12</td><td vertical-align="middle">7/12</td><td vertical-align="middle">6/10</td></tr><tr><td rowspan="4" vertical-align="middle">视频模式</td><td vertical-align="middle">T1</td><td vertical-align="middle">15</td><td vertical-align="middle">12</td><td vertical-align="middle">6</td><td vertical-align="middle">9</td><td vertical-align="middle">10</td></tr><tr><td vertical-align="middle">T2</td><td vertical-align="middle">27</td><td vertical-align="middle">22</td><td vertical-align="middle">23</td><td vertical-align="middle">19</td><td vertical-align="middle">20</td></tr><tr><td vertical-align="middle">T3</td><td
```
```
- 跟手性主观评价：reno16 > s25ultra > pro/base
  - base/pro 变焦问题：单手拍摄时直接拉变焦条，拉一下变焦常常只能到二倍三倍区间，v70和17pro是变焦盘的形式，变焦效率好一些，而s25ultra同样是变焦条的形式，拉动变焦效率也比我们更高一些（印度调研同样有用户反馈变焦效率差，要滑很多次的问题）；同样这个问题，不只是大范围变焦，有时变焦后做精细化调整，也需要松开手后再次调整
- 平滑性上，关注滑动变焦过程中画面是否出现顿挫

  - 除 S25ultra 出现较明显的顿挫感外，其他手机平滑性无明显差距
- 画面跳变，关注切换镜头时是否有出现明显的视角、色彩跳变
```
```
1. base/pro  
跟手性上，变焦条效率差，大范围变焦受限，细节调整时也有手指滑动的阻塞感，同时画面存在较大延迟  
平滑性上，高倍变焦存在一定顿挫感  
画面跳变上，视角、色彩都发生较明显的跳变
2. Samsung（s25ultra）  
跟手性上，变焦条比较跟手，画面上存在较大延迟
```
```
5. 小米（Xiaomi15）  
跟手性上，变焦环比其他变焦环的行程长，在大范围反复变焦时手指容易错位，导致无法直接回到1x，画面比较跟手（但偶尔动画会出现卡顿）  
平滑性上不错  
画面跳变上，视角变化尚可，跳变集中在色彩上
6. Apple（iPhone17pro）  
跟手性上很好，变焦环和画面都很跟手
```

# 027 【PRD】Camera 5.0 构图助手
source: BIswd8SdhorzJJxIx7Kla2qZgEe | revision: 38 | bytes: 24877
## headings
## 1. 背景与目标
### 1.1 问题陈述
### 1.2 产品目标
### 1.3 目标用户与场景
## 2. 核心假设
## 3. 功能定义
### 3.1 功能名称
### 3.2 一句话描述
### 3.3 范围
## 4. 关键需求
### R1 · 顶部工具栏常驻入口
### R2 · 实时场景检测
### R3 · 构图推荐
### R4 · 圆点移入圆圈引导
### R5 · 自动变焦
### R6 · 对齐成功反馈
### R7 · 可随时退出
## 5. 场景与构图策略
## 6. 交互流程
## 7. 自动变焦规则
### 7.1 触发原则
### 7.2 不触发原则
### 7.3 用户感知
## 8. 状态设计
## 9. 文案与词条
## 10. 指标与验收
### 10.1 成功指标
### 10.2 验收条件
## 11. 关键依赖
## 12. 风险与兜底
## 13. 埋点建议
# Figma 交互文档：AI 构图助手关键页面
## A. 画板清单
## B. 全局布局规则
## C. 关键页面说明
### F01 · 后置拍照默认态，AI 构图关闭
### F02 · 首次开启轻提示
### F03 · AI 构图检测中
### F04 · 场景识别成功，开始引导
### F05 · 用户移动中，圆点靠近圆圈
### F06 · 自动变焦触发
### F07 · 对齐成功
### F08 · 不可用/主体不明确
### F09 · 关闭 AI 构图助手
## D. 原型连线
## E. 动效说明
## F. 设计注意事项
## 14. 待确认项
## 15. agent 初步评审
### agent 开发评审
### agent 测试评审
### agent Solution Smuggling 检查
### agent 推荐第一版最小切片
## selected snippets
```
> 
> 适用范围：相机 App 后置「拍照」模式  



---
```
```
## 1. 背景与目标



### 1.1 问题陈述
```
```
普通用户在后置拍照时，经常能识别「想拍什么」，但不确定手机该往哪个方向移动、主体应该占画面多大、是否需要拉近或拉远。结果容易出现主体偏小、画面歪斜、主体位置不佳、背景干扰过多等问题。



AI 构图助手希望在不打断拍照链路的前提下，基于实时场景识别和美学构图规则，给用户一个可执行的移动指引：把画面中的圆点移动到圆圈内，并在合适场景下自动调整变焦，使用户更容易得到一张构图更稳定、更好看的照片。
```
```
AI 构图助手希望在不打断拍照链路的前提下，基于实时场景识别和美学构图规则，给用户一个可执行的移动指引：把画面中的圆点移动到圆圈内，并在合适场景下自动调整变焦，使用户更容易得到一张构图更稳定、更好看的照片。



### 1.2 产品目标
```
```
### 1.2 产品目标



- 降低普通用户拍出「构图明显不佳」照片的概率。
```
```
- 将抽象构图建议转化为可操作的手机移动指引。
- 在后置拍照模式中提供轻量、可随时开关的构图辅助能力。
- 在主体占比明显不合适的场景下，自动辅助变焦，减少用户手动判断焦段的成本。

### 1.3 目标用户与场景
```
```
- 在后置拍照模式中提供轻量、可随时开关的构图辅助能力。
- 在主体占比明显不合适的场景下，自动辅助变焦，减少用户手动判断焦段的成本。

### 1.3 目标用户与场景
```
```
### 1.3 目标用户与场景



- 目标用户：日常拍照用户、旅行/打卡用户、对构图有需求但不熟悉专业摄影规则的用户。
```
```
- 目标用户：日常拍照用户、旅行/打卡用户、对构图有需求但不熟悉专业摄影规则的用户。
- 核心场景：建筑/城市、人物、食物、风景、花草/静物等后置拍照场景。
- 使用频率：[TBD — 需通过相机模式使用数据和用户研究确认]

---
```
```
- 核心场景：建筑/城市、人物、食物、风景、花草/静物等后置拍照场景。
- 使用频率：[TBD — 需通过相机模式使用数据和用户研究确认]

---
```
```
|-|-|-|-|
| 我们相信「圆点移入圆圈」的引导方式能让普通用户更快理解如何移动手机，因为它把构图调整转化为明确的空间目标。 | Medium | 用户开启后仍不知道该如何移动，或引导完成率低于 [TBD]。 | 可用性测试、灰度埋点、访谈回放。 |
| 我们相信主体占比是自动变焦的主要判断依据，因为多数构图失败来自主体过小或过满。 | Medium | 自动变焦后用户取消率高，或变焦后照片留存/分享没有提升。 | A/B 实验、自动变焦触发后拍摄率、撤销率。 |
| 我们相信功能默认关闭、顶部工具栏常驻，能兼顾可发现性和预览干扰控制。 | High | 入口点击率过低，或用户误触/抱怨顶部工具栏拥挤。 | 入口点击率、开关留存、用户反馈。 |
```
```
| 我们相信主体占比是自动变焦的主要判断依据，因为多数构图失败来自主体过小或过满。 | Medium | 自动变焦后用户取消率高，或变焦后照片留存/分享没有提升。 | A/B 实验、自动变焦触发后拍摄率、撤销率。 |
| 我们相信功能默认关闭、顶部工具栏常驻，能兼顾可发现性和预览干扰控制。 | High | 入口点击率过低，或用户误触/抱怨顶部工具栏拥挤。 | 入口点击率、开关留存、用户反馈。 |



---
```

# 028 相机 AI 推荐功能立项申请书
source: ZzVbdaiL5odgsyxTcKSlEDOBg9g | revision: 114 | bytes: 35117
## headings
## 1. 项目背景
## 2. 项目目标
### 2.1 落地项目
### 2.2 第一版功能目标
### 2.3 非目标范围
## 3. 可行性分析
### 3.1 市场可行性
### 3.2 技术可行性
### 3.3 成本可行性
## 4. 核心方案
### 4.1 preset / LUT 推荐方案
### 4.2 pose 推荐方案
## 5. 资源需求
### 5.1 人力需求
### 5.2 素材需求
## 6. 预期成果
### 6.1 技术成果
### 6.2 商业价值
## 7. 风险评估
## 8. 初步时间计划
## 9. PRD 需求文档输出计划
## 10. 立项建议
# 附录：智能相机场景标签与滤镜推荐规则
## A1. 文档目的
## A2. 标签体系设计原则
## A3. 关键标签范围 V1
### A3.1 手机拍摄关键 ML Kit 标签
### A3.2 关键标签到产品场景标签映射  <cite type="user" user-id="ou_b04086897ca8fd793d463a093afef8e2" user-name="Mandy Li"></cite>
## A4. 多标签命中优先级
### A4.1 典型裁决示例
## A5. 场景标签与滤镜风格映射
## A6. 推荐规则
### A6.1 推荐链路
### A6.2 推荐前过滤规则
### A6.3 推荐打分公式
### A6.4 基础推荐规则示例
## A7. 建议落库字段
### A7.1 场景标签字段
### A7.2 滤镜标签字段
### A7.3 推荐结果输出字段
## A8. 第一版 MVP 建议重点打磨场景
### A8.1 最小可行标签集
## A9. 需要产品 / 算法 / IQA 确认的问题
## A10. ML Kit 标签覆盖边界
## A11. 拍人 pose 推荐专用标签
### A11.1 pose 标签选择原则
### A11.2 手机拍人 pose 关键标签
### A11.3 pose 推荐规则
### A11.4 pose 推荐输出字段建议
## A12. 规则结论
## selected snippets
```
<title>相机 AI 推荐功能立项申请书</title>

## 1. 项目背景
```
```
## 1. 项目背景



当前手机影像能力已从“拍得清”逐步进入“拍得好、拍得像样、拍得有风格”的阶段。用户在日常拍摄中，尤其是人像、探店、旅行、街拍、聚会、美食分享等场景下，仍存在明显的拍摄决策成本：
```
```
当前手机影像能力已从“拍得清”逐步进入“拍得好、拍得像样、拍得有风格”的阶段。用户在日常拍摄中，尤其是人像、探店、旅行、街拍、聚会、美食分享等场景下，仍存在明显的拍摄决策成本：



1. 不知道当前场景适合使用什么滤镜、preset 或 LUT。
```
```
1. 不知道当前场景适合使用什么滤镜、preset 或 LUT。
2. 不知道拍人时应该如何摆 pose，容易出现动作僵硬、构图普通、多人合影不自然等问题。
3. 系统相机内已有滤镜、风格、模板资源，但用户发现成本高，使用率不稳定。
4. 第三方拍照和修图应用已在“场景推荐、风格模板、拍照姿势引导”方向形成用户认知，系统相机需要补齐智能引导能力。
```
```
3. 系统相机内已有滤镜、风格、模板资源，但用户发现成本高，使用率不稳定。
4. 第三方拍照和修图应用已在“场景推荐、风格模板、拍照姿势引导”方向形成用户认知，系统相机需要补齐智能引导能力。

因此，本项目拟围绕“智能相机推荐”方向，优先建设两个轻量但可验证的能力：
```
```
1. 基于场景识别推荐 preset / LUT / 滤镜。
2. 基于场景识别推荐拍人 pose 模板，并探索导入图片提取 pose 模板能力。

第一阶段不直接投入模型自研生成 LUT，而是优先采用“Google ML Kit Image Labeling 场景标签 + 产品滤镜库 + 标签映射关系 + 推荐规则”的方式落地，降低研发风险，快速验证用户价值。
```
```
第一阶段不直接投入模型自研生成 LUT，而是优先采用“Google ML Kit Image Labeling 场景标签 + 产品滤镜库 + 标签映射关系 + 推荐规则”的方式落地，降低研发风险，快速验证用户价值。



## 2. 项目目标
```
```
## 2. 项目目标



### 2.1 落地项目
```
```
| 子项目 | 第一版目标 | 优先级 | 上项目标 |
|-|-|-|-|
| 场景识别推荐 preset / LUT | 相机识别当前拍摄场景后，自动推荐适合的产品内置 preset / LUT / 滤镜 | P0 | 26111/26121  <br/>MP0 |
| 拍人 pose 推荐 | 在典型拍人场景下，推荐适合的 pose 模板；支持导入图片提取 pose 模板作为能力验证方向 | P1 | 26111/26121  <br/>MP2 |
```
```
|-|-|-|-|
| 场景识别推荐 preset / LUT | 相机识别当前拍摄场景后，自动推荐适合的产品内置 preset / LUT / 滤镜 | P0 | 26111/26121  <br/>MP0 |
| 拍人 pose 推荐 | 在典型拍人场景下，推荐适合的 pose 模板；支持导入图片提取 pose 模板作为能力验证方向 | P1 | 26111/26121  <br/>MP2 |
```
```
| 场景识别推荐 preset / LUT | 相机识别当前拍摄场景后，自动推荐适合的产品内置 preset / LUT / 滤镜 | P0 | 26111/26121  <br/>MP0 |
| 拍人 pose 推荐 | 在典型拍人场景下，推荐适合的 pose 模板；支持导入图片提取 pose 模板作为能力验证方向 | P1 | 26111/26121  <br/>MP2 |



### 2.2 第一版功能目标
```
```
### 2.2 第一版功能目标



1. 相机根据场景识别结果，推荐 1-3 个适合当前场景的 preset / LUT / 滤镜。
```

# 029 【PRD】Camera 5.1-人像模式 Consistent Zoom
source: Co3UdroAGos7ypxaAAKlPkzug6e | revision: 118 | bytes: 16654
## headings
## 变更日志
# 1. 背景与目标
## 问题陈述
## 证据与数据
## 目标用户与场景
## 预期收益
# 2. 功能定义
## 2.1 功能描述
## 2.2 范围
## 2.3适用模式/入口
# 3. 需求
## R1 · 后摄人像连续变焦
## R2 · 固定焦段快捷入口保留
## R3 · 默认光圈按焦段分段联动
## R4 · 虚化观感随焦段连续变化
## R5 · 手动光圈优先
## R6 · 预览与成片一致
# 4. 方案说明
## 核心行为
## 交互逻辑
## 手动光圈优先级
# 6. 需求词条
# 7. 关键依赖
# 8. 指标与验收
### 成功指标
### 验收条件
### 效果验收场景
# 9. 埋点设计
# 10. 干系人
# 11. 待确认/待补充
# 12. 附录
## selected snippets
```
<title>【PRD】Camera 5.1-人像模式 Consistent Zoom</title>

## 变更日志

| 日期 | 版本 | 变更人 | 变更内容 |
```
```
|-|-|-|-|
| 2026-06-05 | 1.0 | Riley Tang | 基于《【功能定义】｜人像模式 Consistent Zoom》 |

# 1. 背景与目标

## 问题陈述
```
```
# 1. 背景与目标

## 问题陈述

当前 25111 项目人像模式仅支持 1x、2x、3.5x 三个固定焦段切换。用户在人像模式中无法选择 1.5x、2.3x、3.0x 等中间焦段，导致部分真实拍摄场景下构图不够灵活。
```
```
当前 25111 项目人像模式仅支持 1x、2x、3.5x 三个固定焦段切换。用户在人像模式中无法选择 1.5x、2.3x、3.0x 等中间焦段，导致部分真实拍摄场景下构图不够灵活。

在人像拍摄中，固定焦段可以提供清晰、快速的入口，但无法覆盖所有构图需求。当用户遇到 1x 太广、2x 太近，或 2x 太广、3.5x 太近时，只能移动身体、退出人像模式使用普通拍照变焦，或拍摄后裁切。这会打断人像拍摄链路，也降低人像模式作为独立拍摄模式的完整性。

## 证据与数据
```
```
在人像拍摄中，固定焦段可以提供清晰、快速的入口，但无法覆盖所有构图需求。当用户遇到 1x 太广、2x 太近，或 2x 太广、3.5x 太近时，只能移动身体、退出人像模式使用普通拍照变焦，或拍摄后裁切。这会打断人像拍摄链路，也降低人像模式作为独立拍摄模式的完整性。

## 证据与数据

- 内部现状：当前人像模式仅支持 1x、2x、3.5x 固定焦段切换。
```
```
- 内部现状：当前人像模式仅支持 1x、2x、3.5x 固定焦段切换。
- 竞品参考：

  - iPhone 人像模式支持固定焦段切换、双指缩放和 Depth Control；
  - OPPO Find X9 人像模式支持 1-3.4 倍自由滑动变焦。
```
```
- iPhone 人像模式支持固定焦段切换、双指缩放和 Depth Control；
  - OPPO Find X9 人像模式支持 1-3.4 倍自由滑动变焦。

## 目标用户与场景
```
```
- iPhone 人像模式支持固定焦段切换、双指缩放和 Depth Control；
  - OPPO Find X9 人像模式支持 1-3.4 倍自由滑动变焦。

## 目标用户与场景

- 用户角色：使用后摄人像模式拍摄人物、多人合影、旅行街拍、室内生活人像的普通用户。
```
```
## 目标用户与场景

- 用户角色：使用后摄人像模式拍摄人物、多人合影、旅行街拍、室内生活人像的普通用户。
- 核心场景：半身人像、环境人像、多人合影、近景人像、旅行/街拍、室内空间受限场景。
```
```
- 用户角色：使用后摄人像模式拍摄人物、多人合影、旅行街拍、室内生活人像的普通用户。
- 核心场景：半身人像、环境人像、多人合影、近景人像、旅行/街拍、室内空间受限场景。

## 预期收益
```
```
- 用户角色：使用后摄人像模式拍摄人物、多人合影、旅行街拍、室内生活人像的普通用户。
- 核心场景：半身人像、环境人像、多人合影、近景人像、旅行/街拍、室内空间受限场景。

## 预期收益

- 用户可在人像模式中完成 1x、2x、3.5x 之外的中间焦段构图。
```
```
- 用户可在人像模式中完成 1x、2x、3.5x 之外的中间焦段构图。
- 用户不需要退出人像模式即可完成轻微构图调整。
- 人像模式预览和成片在连续变焦过程中的构图、虚化和主体分离保持连续、自然。

# 2. 功能定义
```

# 030 印度镜头脏污专项
source: HzVWdX7KfoP2FWxPVpJlFL68gUd | revision: 187 | bytes: 5150
## headings
## 一、项目背景
### 1. 用户问题
### 2. 场景特点（印度）
## 二、目标定义
### 1. 用户目标
### 2. 产品目标
## 三、整体解决方案框架
## 四、详细方案
# 4.1 硬件层（Prevent）@judy
### 4.1.1 镜头防油污涂层升级（P0）
### 4.1.2 镜头结构优化（P1）-id
# 4.2 算法层（Recover）【核心差异点】
### 4.2.1 脏污检测升级（Lens Dirt Detection）（P0）
### 4.2.2 AI去油污算法（P0）
### 4.2.3 多帧融合（P1）
### 4.2.4 成像质量评估闭环（P1）
# 4.3 交互层（Guide）-<cite type="user" user-id="ou_1e068f80b2831f5bc95787032143a546" user-name="Travis Zhao"></cite><cite type="user" user-id="ou_b27b86b715e34f93cafdd0d315e218b1" user-name="Allison Liu"></cite>
### 4.3.1 提示机制升级（P0）
### 4.3.2 动画引导（P0）<cite type="user" user-id="ou_b27b86b715e34f93cafdd0d315e218b1" user-name="Allison Liu"></cite>
### 4.3.4 擦拭反馈（P0）
# 4.4 配件与生态（Assist）
### 4.4.1 标配清洁布（P0）
### 4.4.2 新手引导（P1）
## 五、产品卖点包装
### 1. Always Clear Camera
### 2. Dirty Lens Recovery
### 3. Smart Lens Care
## 六、优先级建议
### P0（必须做）
### P1（增强体验）
### P2（长期优化）
## 七、SoC / 技术依赖
### 1. ISP能力
### 2. NPU能力
### 3. 多帧处理能力
## 八、效果评估指标
### 1. 体验指标
### 2. 算法指标
### 3. 用户行为
## 九、关键总结
## selected snippets
```
## 一、项目背景



### 1. 用户问题
```
```
### 2. 场景特点（印度）



- 高温 → 皮脂分泌旺盛
```
```
这是一个**高频 + 强感知 + 可优化的体验痛点**



---
```
```
## 二、目标定义



### 1. 用户目标
```
```
### 1. 用户目标



- 随时拍清楚（不受镜头脏污影响）
```
```
### 2. 产品目标



- 降低“脏镜头导致的差评”
```
```
## 三、整体解决方案框架



👉 核心策略：
```
```
👉 核心策略：

**减少用户依赖 + 系统自动兜底**
```
```
**减少用户依赖 + 系统自动兜底**



分为四层：
```
```
1. 硬件（减少脏污）
2. 算法（对抗脏污）
3. 交互（引导用户）
4. 配件（辅助解决）
```
```
1. 硬件（减少脏污）
2. 算法（对抗脏污）
3. 交互（引导用户）
4. 配件（辅助解决）

---
```
```
2. 算法（对抗脏污）
3. 交互（引导用户）
4. 配件（辅助解决）

---
```

# 031 【PRD】Camera 5.1 普通照片模式运动场景引导
source: TOPMdAsjDoOuW2x2XrQljB6hgOb | revision: 47 | bytes: 8633
## headings
# 【PRD】Camera 5.1 普通照片模式运动场景引导
## 1. 背景
## 2. 目标
## 3. 功能范围
## 4. 入口与交互
## 5. 需求描述
### R1 · 普通照片模式后置运动检测
### R2 · 展示 Try Action mode 引导胶囊
### R3 · 点击胶囊跳转运动模式
### R4 · 点击关闭后本次不再提示
### R5 · 提示频控
## 6. 关键规则汇总
## 7. 埋点建议
## 8. 验收标准
## 9. 待确认
## 10. 风险与说明
## selected snippets
```
# 【PRD】Camera 5.1 普通照片模式运动场景引导



> 状态：Draft
```
```
> 
> 适用范围：普通照片模式，后置摄像头  



## 1. 背景
```
```
## 1. 背景



普通照片模式下已有轻量化运动抓拍能力，可覆盖人走动等运动量较小的场景。对于体育、跳跃、宠物奔跑等运动量较大的场景，普通照片模式的抓拍效果有限，更适合使用运动模式。
```
```
普通照片模式下已有轻量化运动抓拍能力，可覆盖人走动等运动量较小的场景。对于体育、跳跃、宠物奔跑等运动量较大的场景，普通照片模式的抓拍效果有限，更适合使用运动模式。



因此，本需求在普通照片模式后置预览中增加运动检测。当检测到较大运动量并达到触发阈值时，展示 `Try Action mode` 引导胶囊，引导用户切换到运动模式拍摄。
```
```
因此，本需求在普通照片模式后置预览中增加运动检测。当检测到较大运动量并达到触发阈值时，展示 `Try Action mode` 引导胶囊，引导用户切换到运动模式拍摄。



## 2. 目标
```
```
## 2. 目标



- 在用户处于普通照片模式、后置摄像头时，识别较大运动场景。
```
```
- 在用户处于普通照片模式、后置摄像头时，识别较大运动场景。
- 达到触发条件后展示 `Try Action mode` 引导胶囊。
- 用户点击胶囊后跳转到运动模式。
- 控制提示频率，避免重复打扰。
```
```
- 达到触发条件后展示 `Try Action mode` 引导胶囊。
- 用户点击胶囊后跳转到运动模式。
- 控制提示频率，避免重复打扰。
```
```
## 3. 功能范围



**本次做：**
```
```
- 普通照片模式后置下（生效焦段待定<cite type="user" user-id="ou_bde858e2c287e45bb799791c3cea03c7" user-name="Alex Huang"></cite>）增加运动检测。
- 达到阈值后展示 `Try Action mode` 引导胶囊。**（判断条件需要再跟各模块一起定义，放在哪里决策）**
- 胶囊支持点击跳转运动模式。
- 胶囊支持点击关闭。
- 支持单次相机使用期间的提示频控。
```
```
- 达到阈值后展示 `Try Action mode` 引导胶囊。**（判断条件需要再跟各模块一起定义，放在哪里决策）**
- 胶囊支持点击跳转运动模式。
- 胶囊支持点击关闭。
- 支持单次相机使用期间的提示频控。

**本次不做：**
```
```
- 胶囊支持点击跳转运动模式。
- 胶囊支持点击关闭。
- 支持单次相机使用期间的提示频控。

**本次不做：**
```

# 032 【PRD】Camera 5.1 美颜功能首次开启引导
source: NOlCdnmtqo9etOx43PalXbUugvb | revision: 120 | bytes: 20164
## headings
# 【PRD】Camera 5.1 美颜功能首次开启引导
## 变更日志
## 1. 背景与目标
### 问题陈述
### 用户数据
### 目标用户与场景
### 预期收益
## 3. 功能定义
### 功能描述
### 范围
### 适用模式/入口
## 4. 需求
### R1 · 首次引导触发
### R2 · 三档等级选择
### R3 · 引导呈现形式
### R4 · 用户选择后的状态保存
### R5 · 跳过与关闭
### R6 · 原入口一致性
### 兼容性要求
## 5. 方案说明
### 核心行为
### 推荐默认体验
### 状态记录建议
## 6. 需求词条
## 7. 关键依赖
## 8. 指标与验收
### 成功指标
### 验收条件
## 9. 埋点设计
### 事件表
### JSON 示例
## 10. 干系人
## 11. 待确认/待补充
## 12. 初步评审
### agent 开发评审
### agent 测试评审
### agent Solution Smuggling 检查
### agent 全文评分
### agent 高风险项
### agent 推荐第一版最小切片
## 13. 附录
### 考虑过但放弃的方案
## selected snippets
```
# 【PRD】Camera 5.1 美颜功能首次开启引导

## 变更日志
```
```
|-|-|-|-|
| 2026-06-08 | v0.1 | Lia | 创建美颜功能首次开启引导需求草稿 |



---
```
```
## 1. 背景与目标



### 问题陈述
```
```
美颜效果已优化，但当前美颜入口默认关闭。对有自拍、人像修饰诉求的用户，尤其是女性用户(sunshine girl)和印度市场用户，美颜能力可能没有被及时发现或试用，导致优化后的效果无法充分转化为实际使用。



本需求希望在不改变默认关闭状态的前提下，通过首次开启引导降低用户发现和试用美颜等级的成本，让用户更容易理解 `Off / Natural / Strong` 三档效果，并主动选择适合自己的美颜强度。
```
```
本需求希望在不改变默认关闭状态的前提下，通过首次开启引导降低用户发现和试用美颜等级的成本，让用户更容易理解 `Off / Natural / Strong` 三档效果，并主动选择适合自己的美颜强度。



### 用户数据
```
```
- 前置摄像头美颜使用率为 24.09%，显著高于后置摄像头 5.36%，前置摄像头美颜使用率约为后置摄像头的 4.5 倍。
- **按模式开启率**：人像前置最高 55%+，拍照前置 \~36%，后置人像 \~40%
- **美颜用户 vs 非美颜用户人均拍摄量**：3.7x \~ 11.4x，差距显著
- 拍照模式前置、人像模式前后置均存在美颜入口，是引导覆盖的主要场景。

### 目标用户与场景
```
```
- **美颜用户 vs 非美颜用户人均拍摄量**：3.7x \~ 11.4x，差距显著
- 拍照模式前置、人像模式前后置均存在美颜入口，是引导覆盖的主要场景。

### 目标用户与场景
```
```
### 目标用户与场景



- 目标用户：印度市场中有自拍、人像修饰、肤色/肤质优化诉求的 Camera 用户，重点关注女性用户。
```
```
- 目标用户：印度市场中有自拍、人像修饰、肤色/肤质优化诉求的 Camera 用户，重点关注女性用户。
- 核心场景：用户首次进入支持美颜的拍照或人像场景时，希望快速理解美颜能力，并选择适合的美颜等级。

### 预期收益
```
```
- 提升支持场景下美颜功能发现率和开启率，重点观察前置拍照与人像模式。
- 帮助用户理解新机器上的美颜效果优化，提升自拍和人像出片满意度。
- 为拓展女性用户提供更直观的首次体验入口。

---
```
```
- 帮助用户理解新机器上的美颜效果优化，提升自拍和人像出片满意度。
- 为拓展女性用户提供更直观的首次体验入口。

---
```
```
## 3. 功能定义



### 功能描述
```

# 033 【PRD】Camera 5.1- 设置 增加 Tips and feedback 入口
source: KDpwdKtEso7lP4xgCsgllRHlgqh | revision: 17 | bytes: 5850
## headings
# 【PRD】Camera 5.1- 设置 增加 Tips and feedback 入口
## 1. 背景
## 2. 参考原型
## 3. 目标
## 4. 功能范围
## 5. 入口与交互
## 6. 需求描述
### R1 · 新增 Help & Support 分组
### R2 · 新增 Tips and feedback 入口
### R3 · 跳转系统 Tips and feedback
## 7. 文案
## 8. 验收标准
## 9. 埋点建议
## 10. 待确认
## 11. 风险
## selected snippets
```
# 【PRD】Camera 5.1- 设置 增加 Tips and feedback 入口



> 状态：Draft
```
```
## 1. 背景



用户在 Camera 使用中遇到问题或想提交建议时，目前需要离开 Camera，再从系统入口进入 Tips and feedback。路径较长，也不利于反馈系统识别用户来自 Camera 场景。
```
```
用户在 Camera 使用中遇到问题或想提交建议时，目前需要离开 Camera，再从系统入口进入 Tips and feedback。路径较长，也不利于反馈系统识别用户来自 Camera 场景。



本需求在 Camera settings 中增加一个支持入口，让用户可以从 Camera 设置页直接进入系统 Tips and feedback。
```
```
本需求在 Camera settings 中增加一个支持入口，让用户可以从 Camera 设置页直接进入系统 Tips and feedback。



## 2. 参考原型
```
```
## 3. 目标



- 在 Camera settings 页面增加 `Tips and feedback` 入口。
```
```
- 在 Camera settings 页面增加 `Tips and feedback` 入口。
- 入口点击后跳转到系统 Tips and feedback。
- 若系统支持，跳转时带上 Camera 来源信息，便于默认选择 Camera 分类或后台识别来源。

## 4. 功能范围
```
```
- 入口点击后跳转到系统 Tips and feedback。
- 若系统支持，跳转时带上 Camera 来源信息，便于默认选择 Camera 分类或后台识别来源。

## 4. 功能范围
```
```
## 4. 功能范围



**本次做：**
```
```
- 点击后进入系统 Tips and feedback。
- 支持多语言、暗色模式、大字体和 TalkBack。

**本次不做：**
```
```
**本次不做：**



- 不在 Camera 内自建反馈表单。
```
```
- 不修改 Tips and feedback 页面和表单字段。
- 不在拍摄页、模式页等高频拍摄界面增加反馈入口。
- 不改动反馈后台处理流程。

## 5. 入口与交互
```
```
## 5. 入口与交互



入口路径：
```

# 034 26121 视频 Log 功能评估
source: S8KDdD8reojpU9xcxgWlnFNHgRe | revision: 1415 | bytes: 10153
## headings
# 一、背景
## 1.1 用户需求
## 1.2 产品定位
## 1.3 Log 是什么，对用户有什么价值
## 1.4 我们怎么做
# 二、竞品分析
# 三、需求定义
# 四、可行性评估
## 26.6.29 - 第一次评估会议
# 附录：术语速查
## selected snippets
```
<title>26121 视频 Log 功能评估</title>



# 一、背景
```
```
# 一、背景

## 1.1 用户需求

在 26121 的用户画像中，我们可以看到有一部分极客用户和视频创作者群体；也有一部分用户需要明确的升级感。Log 功能不仅可以满足创作者和极客用户的实际创作需求，更可以增强用户对 Pro 机型的认知，建立明确的升级感。
```
```
## 1.1 用户需求

在 26121 的用户画像中，我们可以看到有一部分极客用户和视频创作者群体；也有一部分用户需要明确的升级感。Log 功能不仅可以满足创作者和极客用户的实际创作需求，更可以增强用户对 Pro 机型的认知，建立明确的升级感。  
具体实例：对使用 Nothing Phone 的影像专业用户进行一对一访谈的过程中，问到为何不用我们的手机进行视频创作，用户明确指出，我们的视频没有 Log 模式，同时无法控制曝光和色彩，无法满足他的专业创作诉求。
```
```
在 26121 的用户画像中，我们可以看到有一部分极客用户和视频创作者群体；也有一部分用户需要明确的升级感。Log 功能不仅可以满足创作者和极客用户的实际创作需求，更可以增强用户对 Pro 机型的认知，建立明确的升级感。  
具体实例：对使用 Nothing Phone 的影像专业用户进行一对一访谈的过程中，问到为何不用我们的手机进行视频创作，用户明确指出，我们的视频没有 Log 模式，同时无法控制曝光和色彩，无法满足他的专业创作诉求。

## 1.2 产品定位
```
```
在 26121 的用户画像中，我们可以看到有一部分极客用户和视频创作者群体；也有一部分用户需要明确的升级感。Log 功能不仅可以满足创作者和极客用户的实际创作需求，更可以增强用户对 Pro 机型的认知，建立明确的升级感。  
具体实例：对使用 Nothing Phone 的影像专业用户进行一对一访谈的过程中，问到为何不用我们的手机进行视频创作，用户明确指出，我们的视频没有 Log 模式，同时无法控制曝光和色彩，无法满足他的专业创作诉求。

## 1.2 产品定位

26121 的 KSP 方向是专业视频能力。Log 模式是目前旗舰影像手机中区分「普通视频」和「专业视频」的核心特性之一，对外能够直接支撑 Pro 属性的营销叙事，对内也为后续视频专业化方向建立了技术基础。
```
```
26121 的 KSP 方向是专业视频能力。Log 模式是目前旗舰影像手机中区分「普通视频」和「专业视频」的核心特性之一，对外能够直接支撑 Pro 属性的营销叙事，对内也为后续视频专业化方向建立了技术基础。

## 1.3 Log 是什么，对用户有什么价值

Log 是一条替代标准 Gamma 的对数编码曲线。标准视频（Rec.709）的 Gamma 是为「在屏幕上好看」设计的，高光区域码值少，传感器抓到的很多信息在 Tone Mapping 阶段就被丢掉了。Log 曲线压缩高光、拉升暗部，把更大的动态范围均匀地编码进码值空间里。
```
```
Log 是一条替代标准 Gamma 的对数编码曲线。标准视频（Rec.709）的 Gamma 是为「在屏幕上好看」设计的，高光区域码值少，传感器抓到的很多信息在 Tone Mapping 阶段就被丢掉了。Log 曲线压缩高光、拉升暗部，把更大的动态范围均匀地编码进码值空间里。

结果是：Log 画面看起来又灰又平，对比度低，饱和度低。**这是正常的——Log 素材不是给人直接看的，是给后期调色用的原材料。**

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2FjMDAyODViNmJjNzgzNjBmODVkNTIzMmU5YzA3Y2JfZTYwNWU3ODRmZGMyZTU5MmY5OTJmNGZkYWQzNzUzMDlfSUQ6NzY1NTI3OTg2OTIxOTMxMTMyNF8xNzgzNDA2Mzc5OjE3ODM0MDk5NzlfVjM)
```
```
对目标用户（有后期调色能力的创作者）的价值：

- **调色空间更大**：在 DaVinci、Premiere 里可以大幅推拉曝光、做二级调色，不容易出现色阶断裂或高光崩掉
- **绕开机内破坏性处理**：机内的锐化、降噪、风格化 Tone Mapping 都是单向不可逆的操作，Log 模式让 ISP 更透明，把这些决策权交给用户
- **LUT 驱动的工作流**：Log 素材 + 还原 LUT（还原 → Rec.709）+ Creative LUT（定义风格），是专业视频的标准流程
```
```
- **调色空间更大**：在 DaVinci、Premiere 里可以大幅推拉曝光、做二级调色，不容易出现色阶断裂或高光崩掉
- **绕开机内破坏性处理**：机内的锐化、降噪、风格化 Tone Mapping 都是单向不可逆的操作，Log 模式让 ISP 更透明，把这些决策权交给用户
- **LUT 驱动的工作流**：Log 素材 + 还原 LUT（还原 → Rec.709）+ Creative LUT（定义风格），是专业视频的标准流程

> Log 是 Pro 功能，不是给普通用户的。Log 需要使用软件进行调色处理才能恢复出正常的颜色和亮度。
>
```
```
> Log 是 Pro 功能，不是给普通用户的。Log 需要使用软件进行调色处理才能恢复出正常的颜色和亮度。
> 
> ![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGJmNDRkNDQxNDM1ZGFiMWFmZjhhNTkwYzVhM2EwYzFfNGM1NjM3YTU4MTdhZTVlMWUzNjY5YzdmNGI2ZWUxYTNfSUQ6NzY1NjcxNDA4NDU5NTA3NjgyN18xNzgzNDA2Mzc5OjE3ODM0MDk5NzlfVjM)

---
```
```
我们已经有了 **10-bit 编码 + Rec.2020 色域**，这条硬件链路 HLG 和 Log 可以完全共用——编码器不关心传进来的是什么信号，它只是在编 10-bit 的数字。

HLG 和 Log 的本质区别，**仅仅是 ISP 侧用的那条 Gamma 曲线不同**。

所以从底层来说我们要做的事情有两件：
```
```
1. **定义一条 Log 曲线**，替换掉当前视频模式的 Gamma
2. **制作一个配套的 还原 LUT**，让用户在后期软件里能一键还原到正常画面

作为轻量级实现，曲线设计可以参考 **DJI D-Log M**。D-Log M 是一条相对温和的 Log 曲线，目标动态范围约 12–13 stops，对传感器底噪要求不像 S-Log3 那么激进，非常适合手机平台。色域配套 BT.2020，与我们现有的编码链路直接对齐。
```

# 035 【PRD】Camera 5.1 - 200MP 高像素
source: YhNXdLBV6o1kfoxFVGOlXzyCgEf | revision: 36 | bytes: 12080
## headings
# 【PRD】Camera 5.1 - 200MP 高像素
## 一、版本信息
## 二、变更日志
## 三、需求背景
### 产品 / 数据现状
### 硬件与算法可行性（2026.07 更新）
### 商务决策（2026.07.02 群同步）
### 竞品分析
## 四、需求范围
### 项目范围
### In Scope
### Out of Scope
## 五、功能详细说明
### 5.1 入口与开关
### 5.2 像素规格\n\n**26111 Base（200MP HP5）**：\n\n| 规格 | 流水线 | 说明 |\n|---|---|---|\n| 50MP | HW Remosaic → 50MP RAW HDR | 不跑 AI Upscale |\n| 200MP | HW Remosaic → 50MP RAW HDR → AI Upscale → 200MP | 默认推荐 |\n| 200MP Ultra | 50MP RAW HDR 全流程 → AI Upscale → 200MP | 最高画质，RAW域算法全开 |\n\n**26121 Pro（IMX896/JN5）**：\n\n| 规格 | 流水线 | 说明 |\n|---|---|---|\n| 50MP | HW Remosaic → 50MP HDR | 标准高像素 |\n| 50MP Ultra | 50MP RAW HDR 全流程直出 | RAW域算法全开，大幅提升画质 |\n\n**Ultra 定义**：50MP 应用 RAW HDR 算法（泛虹软方案），相比普通 50MP HDR，动态范围显著提升。26111 加跑 AI Upscale 到 200MP。\n\n### 5.3 预览与画幅
### 5.4 功能兼容性\n\n独立模式下大幅简化兼容矩阵：\n\n| 功能 | 200MP | 说明 |\n|---|---|---|\n| HDR | ✗ | 高像素自身含HDR流程 |\n| 夜景 | ✗ | 不适用高像素场景 |\n| 滤镜 | ✓ | 仅叠加，不跑滤镜算法 |\n| 美颜 | ✗ | 人像不适合高像素 |\n| Motion Photo | ✗ | 帧率冲突 |\n| 变焦 | ✗ | 仅支持1x/光变点 |\n| 水印 | ✓ | 正常叠加 |\n| Preset | ✓ | 创建时可选择像素规格 |\n\n### 5.5 照片模式变更\n\n照片模式 Top Toolbar 移除 Quality（像素选择），高像素功能入口统一走独立模式。\n\n### 5.6 专业模式\n\n专业模式保留 Quality（像素选择），支持 12MP/50MP，不包含 200MP。200MP 仅在独立高像素模式下可用。\n\n### 5.7 模式和摄像头支持
### 5.3 功能兼容情况
### 5.4 200MP 开关状态记忆
### 5.5 拍摄交互 — 方案 A：预览保持 + 快门转圈
### 5.6 拍摄交互 — 方案 B：预览暂停 + 分模块点亮动画
### 5.7 两方案对比
### 5.8 方案决策标准
## 六、待决事项
## 七、非功能需求
## 八、埋点
## 九、项目规划
## ⚠️ 原版不清晰之处（v2.0 已修正）
## selected snippets
```
## 二、变更日志

| 时间 | 版本 | 变更人 | 主要变更内容 |
|-|-|-|-|
| 2025/10/23 | 1.0 | Lia | 创建文档 |
| 2026/06/11 | 1.1 | Lia | 补充产品定义、三档像素用户心智模型、待决事项 |
| 2026/07/02 | **2.0** | Travis / Codex | **重大更新**：① 修正技术流水线描述（200MP sensor → HW Remosaic → 50MP RAW HDR，非直出 200MP）；② 补充虹软可行性评估结论（7635 预计 7.4s、1.75GB 内存峰值、NZSL 强制）；③ 新增双套拍摄交互方案（A：预览保持+快门转圈 / B：预览暂停+分模块动画）；④ 标记 26121 (7750) 算法取消；⑤ 补充方案决策标准与待测指标 |

## 三、需求背景

### 产品 / 数据现状

26111 Base (Phone 5a) 首次采用 **200MP 三星 HP5** 主摄（SM7635 平台）。26121 Pro 复用 25111 Pro 相机配置（IMX896），不涉及 200MP。（SM7635 平台）。Sensor 支持通过 HW Remosaic 输出 50MP 标准 Bayer，技术流水线为：

> **200MP 模式：200MP sensor → HW Remosaic → 50MP RAW HDR（多帧融合）→ AI upscale → 200MP | 50MP 模式：200MP sensor → HW Remosaic → 50MP RAW HDR → 不跑 upscale → 50MP。两种模式共享 RAW 域算法流水线（多帧 HDR 合成），差异仅在于是否跑 AI upscale。输出均为 JPEG/HEIC，非 RAW 文件。**

用户选择 200MP 得到 200MP（50MP HDR + upscale），选择 50MP 得到 50MP（50MP HDR，不跑 upscale）。RAW 域算法指多帧融合在 RAW 域处理，非 RAW 文件输出。RAW 为独立功能，与本需求无关。
```

```
### 产品 / 数据现状

26111 Base (Phone 5a) 首次采用 **200MP 三星 HP5** 主摄（SM7635 平台）。26121 Pro 复用 25111 Pro 相机配置（IMX896），不涉及 200MP。（SM7635 平台）。Sensor 支持通过 HW Remosaic 输出 50MP 标准 Bayer，技术流水线为：

> **200MP 模式：200MP sensor → HW Remosaic → 50MP RAW HDR（多帧融合）→ AI upscale → 200MP | 50MP 模式：200MP sensor → HW Remosaic → 50MP RAW HDR → 不跑 upscale → 50MP。两种模式共享 RAW 域算法流水线（多帧 HDR 合成），差异仅在于是否跑 AI upscale。输出均为 JPEG/HEIC，非 RAW 文件。**

用户选择 200MP 得到 200MP（50MP HDR + upscale），选择 50MP 得到 50MP（50MP HDR，不跑 upscale）。RAW 域算法指多帧融合在 RAW 域处理，非 RAW 文件输出。RAW 为独立功能，与本需求无关。

### 硬件与算法可行性（2026.07 更新）

来自虹软 & 极感技术评估（详见 KSP 文档：`【NT&虹软】TF 50MP方案 可行性评估`）：

| 指标 | 标准要求 | 7635 预估 | 风险 |
|-|-|-|-|
| 处理时长 | <3s | **7.4s** | ❌ 超标 2.5x |
| 算法内存（不含 buffer） | \~500MB | **800-900MB** | ❌ |
| 图像 Buffer（4 帧 50MP） | — | 400MB | — |
| 内存峰值（含后台） | — | **\~1.75GB** | ❌ 连锁杀后台/卡顿 |
```

```
### 硬件与算法可行性（2026.07 更新）

来自虹软 & 极感技术评估（详见 KSP 文档：`【NT&虹软】TF 50MP方案 可行性评估`）：

| 指标 | 标准要求 | 7635 预估 | 风险 |
|-|-|-|-|
| 处理时长 | <3s | **7.4s** | ❌ 超标 2.5x |
| 算法内存（不含 buffer） | \~500MB | **800-900MB** | ❌ |
| 图像 Buffer（4 帧 50MP） | — | 400MB | — |
| 内存峰值（含后台） | — | **\~1.75GB** | ❌ 连锁杀后台/卡顿 |
| ZSL | 期望 | **不可用**（10 帧 buffer = 1GB） | 强制 NZSL |
| 预览体验 | 无卡顿 | NZSL 下预览定格 | ❌ 显性体验问题 |
| 功耗/温控 | — | 大型 HDR 算法拉高瞬时功耗，触发降频 | ❌ 降频 → 更慢 → 更卡 |

### 商务决策（2026.07.02 群同步）

| 项目 | SoC | 决策 |
|-|-|-|
```

```
### 商务决策（2026.07.02 群同步）

| 项目 | SoC | 决策 |
|-|-|-|
| 26111 Base (Phone 5a) | SM7635 | **50MP 保留**，算法列表已交商务询价 |
| 26121 Pro (Phone 5a Pro) | SM7750 | **不涉及** — 复用 25111 Pro IMX896，无 200MP sensor |

### 竞品分析

（保持原 v1.1 内容，略）

## 四、需求范围

### 项目范围

- 首上项目：**仅 26111 Base**。26121 Pro 复用 25111 Pro IMX896，不具备 200MP sensor，不涉及本需求。
- 老项目回落：不支持，具体回落计划根据回落排期确认
```

```
### In Scope

- 在 50MP 高像素模式下新增 200MP 选项
- 200MP 拍摄中交互的 **A/B 两套方案**（见第五节）
- 拍摄中的操作限制规则
- 拍摄完成后的恢复逻辑
- 200MP 开关状态记忆规则
- 首次使用引导

### Out of Scope

- 26121 (7750)
- 算法选型（虹软 vs 极感，商务决定）
- RAW 文件输出（独立功能，与本需求无关）

## 五、功能详细说明

### 5.1 入口与开关
```

```
### 5.1 入口与开关

模式位置：Mode Switch 独立入口「高像素」。顶部工具栏常驻当前分辨率规格，支持切换。照片模式移除 Quality（像素选择），专业模式保留。

feature-tree 挂载：`Top Toolbar | 高像素（200MP）`，purpose: `拍摄 / 硬件`

首次进入相机时，对 200MP 入口做引导说明（弹窗/气泡），管理用户对拍摄时长的预期。

### 5.2 像素规格\n\n**26111 Base（200MP HP5）**：\n\n| 规格 | 流水线 | 说明 |\n|---|---|---|\n| 50MP | HW Remosaic → 50MP RAW HDR | 不跑 AI Upscale |\n| 200MP | HW Remosaic → 50MP RAW HDR → AI Upscale → 200MP | 默认推荐 |\n| 200MP Ultra | 50MP RAW HDR 全流程 → AI Upscale → 200MP | 最高画质，RAW域算法全开 |\n\n**26121 Pro（IMX896/JN5）**：\n\n| 规格 | 流水线 | 说明 |\n|---|---|---|\n| 50MP | HW Remosaic → 50MP HDR | 标准高像素 |\n| 50MP Ultra | 50MP RAW HDR 全流程直出 | RAW域算法全开，大幅提升画质 |\n\n**Ultra 定义**：50MP 应用 RAW HDR 算法（泛虹软方案），相比普通 50MP HDR，动态范围显著提升。26111 加跑 AI Upscale 到 200MP。\n\n### 5.3 预览与画幅

200MP 和 50MP 模式预览比例均为 **4:3**，与其他像素模式一致。

### 5.4 功能兼容性\n\n独立模式下大幅简化兼容矩阵：\n\n| 功能 | 200MP | 说明 |\n|---|---|---|\n| HDR | ✗ | 高像素自身含HDR流程 |\n| 夜景 | ✗ | 不适用高像素场景 |\n| 滤镜 | ✓ | 仅叠加，不跑滤镜算法 |\n| 美颜 | ✗ | 人像不适合高像素 |\n| Motion Photo | ✗ | 帧率冲突 |\n| 变焦 | ✗ | 仅支持1x/光变点 |\n| 水印 | ✓ | 正常叠加 |\n| Preset | ✓ | 创建时可选择像素规格 |\n\n### 5.5 照片模式变更\n\n照片模式 Top Toolbar 移除 Quality（像素选择），高像素功能入口统一走独立模式。\n\n### 5.6 专业模式\n\n专业模式保留 Quality（像素选择），支持 12MP/50MP，不包含 200MP。200MP 仅在独立高像素模式下可用。\n\n### 5.7 模式和摄像头支持

 ⚠️ 以下以 **26111 Base (SM7635)** 为例。26111 Base 仅有主摄（200MP HP5）+ 超广角（8MP IMX355），**无长焦**。其他机型（如 26121 Pro 有 IMX896 主摄 + JN5 长焦）的支持情况不同，本表仅为举例，非绝对规则。

| 像素 | 超广 | 主摄 | 前置 | 长焦（无长焦） |
|-|-|-|-|-|
```

```
### 5.2 像素规格\n\n**26111 Base（200MP HP5）**：\n\n| 规格 | 流水线 | 说明 |\n|---|---|---|\n| 50MP | HW Remosaic → 50MP RAW HDR | 不跑 AI Upscale |\n| 200MP | HW Remosaic → 50MP RAW HDR → AI Upscale → 200MP | 默认推荐 |\n| 200MP Ultra | 50MP RAW HDR 全流程 → AI Upscale → 200MP | 最高画质，RAW域算法全开 |\n\n**26121 Pro（IMX896/JN5）**：\n\n| 规格 | 流水线 | 说明 |\n|---|---|---|\n| 50MP | HW Remosaic → 50MP HDR | 标准高像素 |\n| 50MP Ultra | 50MP RAW HDR 全流程直出 | RAW域算法全开，大幅提升画质 |\n\n**Ultra 定义**：50MP 应用 RAW HDR 算法（泛虹软方案），相比普通 50MP HDR，动态范围显著提升。26111 加跑 AI Upscale 到 200MP。\n\n### 5.3 预览与画幅

200MP 和 50MP 模式预览比例均为 **4:3**，与其他像素模式一致。

### 5.4 功能兼容性\n\n独立模式下大幅简化兼容矩阵：\n\n| 功能 | 200MP | 说明 |\n|---|---|---|\n| HDR | ✗ | 高像素自身含HDR流程 |\n| 夜景 | ✗ | 不适用高像素场景 |\n| 滤镜 | ✓ | 仅叠加，不跑滤镜算法 |\n| 美颜 | ✗ | 人像不适合高像素 |\n| Motion Photo | ✗ | 帧率冲突 |\n| 变焦 | ✗ | 仅支持1x/光变点 |\n| 水印 | ✓ | 正常叠加 |\n| Preset | ✓ | 创建时可选择像素规格 |\n\n### 5.5 照片模式变更\n\n照片模式 Top Toolbar 移除 Quality（像素选择），高像素功能入口统一走独立模式。\n\n### 5.6 专业模式\n\n专业模式保留 Quality（像素选择），支持 12MP/50MP，不包含 200MP。200MP 仅在独立高像素模式下可用。\n\n### 5.7 模式和摄像头支持

 ⚠️ 以下以 **26111 Base (SM7635)** 为例。26111 Base 仅有主摄（200MP HP5）+ 超广角（8MP IMX355），**无长焦**。其他机型（如 26121 Pro 有 IMX896 主摄 + JN5 长焦）的支持情况不同，本表仅为举例，非绝对规则。

| 像素 | 超广 | 主摄 | 前置 | 长焦（无长焦） |
|-|-|-|-|-|
| 12MP | ✓ 默认 | ✓ 默认 | ✓ 默认 | ✗ |
| 50MP | ✗ | ✓ | ✗ | ✗ |
| 200MP | ✗ | ✓ | ✗ | ✗ |

支持的拍摄模式：后置普通拍照（Photo）、专业模式（Pro）

### 5.3 功能兼容情况
```

```
### 5.4 功能兼容性\n\n独立模式下大幅简化兼容矩阵：\n\n| 功能 | 200MP | 说明 |\n|---|---|---|\n| HDR | ✗ | 高像素自身含HDR流程 |\n| 夜景 | ✗ | 不适用高像素场景 |\n| 滤镜 | ✓ | 仅叠加，不跑滤镜算法 |\n| 美颜 | ✗ | 人像不适合高像素 |\n| Motion Photo | ✗ | 帧率冲突 |\n| 变焦 | ✗ | 仅支持1x/光变点 |\n| 水印 | ✓ | 正常叠加 |\n| Preset | ✓ | 创建时可选择像素规格 |\n\n### 5.5 照片模式变更\n\n照片模式 Top Toolbar 移除 Quality（像素选择），高像素功能入口统一走独立模式。\n\n### 5.6 专业模式\n\n专业模式保留 Quality（像素选择），支持 12MP/50MP，不包含 200MP。200MP 仅在独立高像素模式下可用。\n\n### 5.7 模式和摄像头支持

 ⚠️ 以下以 **26111 Base (SM7635)** 为例。26111 Base 仅有主摄（200MP HP5）+ 超广角（8MP IMX355），**无长焦**。其他机型（如 26121 Pro 有 IMX896 主摄 + JN5 长焦）的支持情况不同，本表仅为举例，非绝对规则。

| 像素 | 超广 | 主摄 | 前置 | 长焦（无长焦） |
|-|-|-|-|-|
| 12MP | ✓ 默认 | ✓ 默认 | ✓ 默认 | ✗ |
| 50MP | ✗ | ✓ | ✗ | ✗ |
| 200MP | ✗ | ✓ | ✗ | ✗ |

支持的拍摄模式：后置普通拍照（Photo）、专业模式（Pro）

### 5.3 功能兼容情况

| 功能 | 200MP 兼容 | 说明 |
|-|-|-|
| HDR | ✓ | 走 HDR 多帧合成，插帧到高像素 |
| 夜景 | ✓ | 走夜景算法，插帧到高像素 |
```

```
### 5.8 方案决策标准

最终方案选择基于 **26111 7635 算法性能实测数据**：

| 指标 | 方案 A 更适用 | 方案 B 更适用 |
|-|-|-|
| 处理耗时 | <5s | ≥5s |
| 内存峰值（不含 preview） | <1.2GB | ≥1.2GB |
| 6G 内存机型是否支持 | 否 | 是 |

建议算法验证完成后，两套交互各做一版 Demo，PM + 开发共同决定。

## 六、待决事项

| # | 事项 | 状态 |
|-|-|-|
| 1 | 算法选型（虹软 vs 极感）最终确定 | [TBD — 商务询价中] |
| 2 | 200MP vs 50MP 实际清晰度差异 | [TBD — 实机验证] |
```

```
## 六、待决事项

| # | 事项 | 状态 |
|-|-|-|
| 1 | 算法选型（虹软 vs 极感）最终确定 | [TBD — 商务询价中] |
| 2 | 200MP vs 50MP 实际清晰度差异 | [TBD — 实机验证] |
| 3 | 7635 平台实测处理时长与内存数据 | [TBD — 算法移植后测试] |
| 4 | RAW 文件大小和拍摄时长 | [TBD — 待评估] |
| 5 | 6G 内存机型是否支持 200MP | [TBD — 依赖实测内存] |
| 6 | Preview buffer 具体可释放量（方案 B） | [TBD — 开发确认] |

## 七、非功能需求

（保持原 v1.1 内容）

## 八、埋点

| 参数 | 说明 | 值 |
```
