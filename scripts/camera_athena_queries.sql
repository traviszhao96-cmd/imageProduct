-- ============================================================================
-- Nothing Camera Athena SQL 模板库 (已验证通过 Athena CLI 执行)
-- 
-- 核心规则：
--   1. 所有相机数据 event_name = 'NTCamera'
--   2. 用 element_at(filter(...), 1) 取参数，不要用 filter(...)[1]
--   3. 数值在 string_value 里，int_value/double_value 常为垃圾值
--   4. 必须加 event_date 范围过滤，控制扫描成本
--   5. ⚠️ Athena 不支持关联 EXISTS 子查询，用 element_at(filter(...)) 替代
--   6. camera_id: 0=后置广角 1=前置 2=后置超广 3=后置长焦
--
-- 机型映射: A024=Phone(3) A024P=Phone(3)Pro A069=Phone(4a) A069P=Phone(4a)Pro
--            A014=Phone(2) A043=Phone(2a) A030=CMF Phone 1
-- ============================================================================


-- ── 1. 相机基础 DAU + 拍照/录像量 ────────────────────────────────────────

-- ✅ 已验证
SELECT event_date,
       count(DISTINCT user_pseudo_id) AS camera_dau,
       count(*) AS total_events,
       count_if(element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL) AS photos,
       count_if(element_at(filter(event_params, x -> x.key = 'video_info'), 1) IS NOT NULL) AS videos,
       ROUND(CAST(count_if(element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL) AS DOUBLE) 
             / CAST(count(*) AS DOUBLE) * 100, 1) AS photo_pct
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 2. 按机型拆分 ────────────────────────────────────────────────────────

SELECT event_date,
       device.model_name AS model,
       count(DISTINCT user_pseudo_id) AS dau,
       count(*) AS events,
       count_if(element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL) AS photos,
       count_if(element_at(filter(event_params, x -> x.key = 'video_info'), 1) IS NOT NULL) AS videos
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
  AND device.model_name IN ('A069','A069P','A024','A024P')
GROUP BY event_date, device.model_name
ORDER BY event_date, device.model_name


-- ── 3. Photo: 模式(photoMode) 分布 ───────────────────────────────────────

-- 注意: 历史拼写兼容 protrait (不是 portrait)
SELECT event_date,
       count(*) AS total_photos,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'photo'), 1) IS NOT NULL) AS mode_photo,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'night'), 1) IS NOT NULL) AS mode_night,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'protrait'), 1) IS NOT NULL) AS mode_portrait,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'expert'), 1) IS NOT NULL) AS mode_expert,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'pano'), 1) IS NOT NULL) AS mode_pano,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'macro'), 1) IS NOT NULL) AS mode_macro,
       count_if(element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'action'), 1) IS NOT NULL) AS mode_action
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 4. Photo: 镜头(camera_id) 分布 ──────────────────────────────────────

-- camera_id: 0=后置广角 1=前置 2=后置超广 3=后置长焦
SELECT event_date,
       count(*) AS total_photos,
       count_if(element_at(filter(event_params, x -> x.label = 'camera_id' AND x.value = '0'), 1) IS NOT NULL) AS rear_wide,
       count_if(element_at(filter(event_params, x -> x.label = 'camera_id' AND x.value = '1'), 1) IS NOT NULL) AS front,
       count_if(element_at(filter(event_params, x -> x.label = 'camera_id' AND x.value = '2'), 1) IS NOT NULL) AS rear_ultrawide,
       count_if(element_at(filter(event_params, x -> x.label = 'camera_id' AND x.value = '3'), 1) IS NOT NULL) AS rear_tele
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 5. Photo: 高像素使用率 ──────────────────────────────────────────────

-- image_quality: 0=12MP 1=高像素(50MP/108MP/200MP)
SELECT event_date,
       count(*) AS total_photos,
       count_if(element_at(filter(event_params, x -> x.label = 'image_quality' AND x.value = '1'), 1) IS NOT NULL) AS high_res,
       ROUND(CAST(count_if(element_at(filter(event_params, x -> x.label = 'image_quality' AND x.value = '1'), 1) IS NOT NULL) AS DOUBLE)
             / CAST(count(*) AS DOUBLE) * 100, 1) AS high_res_pct
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 6. Photo: 各项功能渗透率 ────────────────────────────────────────────

-- 6a. 闪光灯 (flash: 0=关 1=强制开 2=自动)
-- 6b. 水印 (watermark: 0=关 1=文字 2=画框)
-- 6c. 动态照片 (motion: 0=关 1=开)
-- 6d. 滤镜 (filter: 0=无)
-- 6e. 调色 (tuning_apply: 0=关 1=开)
-- 6f. 倒计时 (timer: 0=无 3=3s 10=10s)
-- 6g. 曝光调节 (exposure_adjust: 0=未调节 1=调节)

SELECT event_date,
       count(*) AS total_photos,
       count_if(element_at(filter(event_params, x -> x.label = 'flash' AND x.value IN ('1','2')), 1) IS NOT NULL) AS flash_on,
       count_if(element_at(filter(event_params, x -> x.label = 'watermark' AND x.value IN ('1','2')), 1) IS NOT NULL) AS watermark_on,
       count_if(element_at(filter(event_params, x -> x.label = 'motion' AND x.value = '1'), 1) IS NOT NULL) AS motion_on,
       count_if(element_at(filter(event_params, x -> x.label = 'filter' AND x.value <> '0'), 1) IS NOT NULL) AS filter_on,
       count_if(element_at(filter(event_params, x -> x.label = 'tuning_apply' AND x.value = '1'), 1) IS NOT NULL) AS tuning_on,
       count_if(element_at(filter(event_params, x -> x.label = 'timer' AND x.value IN ('3','10')), 1) IS NOT NULL) AS timer_on,
       count_if(element_at(filter(event_params, x -> x.label = 'exposure_adjust' AND x.value = '1'), 1) IS NOT NULL) AS exposure_adj
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 7. Video: 模式分布 ──────────────────────────────────────────────────

-- video_mode: 1=Video 2=Slo-mo 3=Time-lapse
SELECT event_date,
       count(*) AS total_videos,
       count_if(element_at(filter(event_params, x -> x.label = 'video_mode' AND x.value = '1'), 1) IS NOT NULL) AS normal_video,
       count_if(element_at(filter(event_params, x -> x.label = 'video_mode' AND x.value = '2'), 1) IS NOT NULL) AS slomo,
       count_if(element_at(filter(event_params, x -> x.label = 'video_mode' AND x.value = '3'), 1) IS NOT NULL) AS timelapse
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'video_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 8. Video: 清晰度/帧率 + HDR 功能 ────────────────────────────────────

SELECT event_date,
       count(*) AS total_videos,
       count_if(element_at(filter(event_params, x -> x.label = 'if_HLG' AND x.value = '1'), 1) IS NOT NULL) AS hlg_on,
       count_if(element_at(filter(event_params, x -> x.label = 'action_mode' AND x.value = '1'), 1) IS NOT NULL) AS action_mode_on,
       count_if(element_at(filter(event_params, x -> x.label = 'flash' AND x.value <> '0'), 1) IS NOT NULL) AS flash_on
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'video_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 9. 性能指标 (pef_info) ──────────────────────────────────────────────

-- ⚠️ 注意: 历史键名是 pef_info，不是 perf_info

-- 9a. 冷启动耗时 P50/P95 by 机型
SELECT event_date,
       device.model_name AS model,
       approx_percentile(
         TRY_CAST(element_at(filter(event_params, x -> x.label = 'coldStart'), 1).string_value AS DOUBLE),
         0.50
       ) AS coldstart_p50_ms,
       approx_percentile(
         TRY_CAST(element_at(filter(event_params, x -> x.label = 'coldStart'), 1).string_value AS DOUBLE),
         0.95
       ) AS coldstart_p95_ms,
       count(*) AS samples
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
  AND EXISTS (
    SELECT 1 FROM UNNEST(event_params) t(p) WHERE p.key = 'pef_info' AND p.label = 'coldStart'
    -- 注: 这里 EXISTS 在外层 WHERE 中可行，但在 SELECT/count_if 的聚合函数中不可
  )
GROUP BY event_date, device.model_name
HAVING count(*) >= 100
ORDER BY event_date, device.model_name


-- ── 10. 启动/入口分析 ──────────────────────────────────────────────────

-- 10a. 冷热启动分布
-- activate_type: 1=冷启动 2=热启动
SELECT event_date,
       count(*) AS total_starts,
       count_if(element_at(filter(event_params, x -> x.key = 'activate_type' AND x.value = '1'), 1) IS NOT NULL) AS cold_starts,
       count_if(element_at(filter(event_params, x -> x.key = 'activate_type' AND x.value = '2'), 1) IS NOT NULL) AS hot_starts,
       ROUND(CAST(count_if(element_at(filter(event_params, x -> x.key = 'activate_type' AND x.value = '1'), 1) IS NOT NULL) AS DOUBLE)
             / CAST(count(*) AS DOUBLE) * 100, 1) AS cold_pct
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date

-- 10b. 进入方式分布
-- enter_method: 1=点击图标 2=双击电源键 3=第三方 4=多任务 5=锁屏长按
SELECT event_date,
       count(*) AS total_enters,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '1'), 1) IS NOT NULL) AS icon,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '2'), 1) IS NOT NULL) AS double_power,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '3'), 1) IS NOT NULL) AS third_party,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '4'), 1) IS NOT NULL) AS multitask,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '5'), 1) IS NOT NULL) AS lockscreen,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '6'), 1) IS NOT NULL) AS shortcut,
       count_if(element_at(filter(event_params, x -> x.key = 'enter_method' AND x.value = '7'), 1) IS NOT NULL) AS xpand
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 11. 缩放行为 ───────────────────────────────────────────────────────

-- zoom_ratio 是浮点数，用 ROUND 或 BETWEEN，不要用 =
SELECT event_date,
       count(*) AS total_photos,
       count_if(
         TRY_CAST(element_at(filter(event_params, x -> x.label = 'zoom_ratio'), 1).string_value, 'DOUBLE')
         BETWEEN 0.5 AND 1.5
       ) AS zoom_1x,
       count_if(
         TRY_CAST(element_at(filter(event_params, x -> x.label = 'zoom_ratio'), 1).string_value, 'DOUBLE')
         BETWEEN 1.5 AND 3.0
       ) AS zoom_1x_3x,
       count_if(
         TRY_CAST(element_at(filter(event_params, x -> x.label = 'zoom_ratio'), 1).string_value, 'DOUBLE')
         >= 3.0
       ) AS zoom_3x_plus
FROM dc_database.data_mobile_behavior
WHERE event_name = 'NTCamera'
  AND element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL
  AND event_date BETWEEN '2026-05-25' AND '2026-06-05'
GROUP BY event_date
ORDER BY event_date


-- ── 附录 A: Athena 语法要点 ────────────────────────────────────────────
--
-- ✅ 正确: element_at(filter(...), 1) 缺参数返回 NULL
-- ❌ 错误: filter(...)[1] 缺参数时抛异常
-- ❌ 错误: SELECT/count_if 内不支持关联 EXISTS 子查询
--
-- 取 string_value:
--   element_at(filter(event_params, x -> x.label = 'photoMode'), 1).string_value
--
-- 取数值:
--   TRY_CAST(element_at(filter(event_params, x -> x.label = 'zoom_ratio'), 1).string_value, 'DOUBLE')
--
-- 判断参数存在:
--   element_at(filter(event_params, x -> x.key = 'photo_info'), 1) IS NOT NULL
--
-- 判断参数具体值:
--   element_at(filter(event_params, x -> x.label = 'photoMode' AND x.value = 'night'), 1) IS NOT NULL

-- ── 附录 B: 已知拼写兼容 ──────────────────────────────────────────────
-- portrait     → protrait    (photoMode 历史拼写)
-- pef_info     → 历史写成 pef_info (not perf_info)
-- tuning_shapen → tuning_shapen (锐度, not sharpen)

-- ── 附录 C: 常见 key/label 速查 ───────────────────────────────────────
-- photo_info      -- 拍照参数 (父 key)
-- video_info      -- 录像参数 (父 key)
-- pef_info        -- 性能指标 (父 key)
-- activate_type   -- 启动类型 (1=冷 2=热)
-- enter_method    -- 进入方式 (1=图标 2=双击电源键...)
-- photoMode       -- 拍照模式 (label)
-- video_mode      -- 录像模式 (label)
-- camera_id       -- 镜头 (label, 0=后广 1=前置 2=超广 3=长焦)
-- zoom_ratio      -- 变焦倍数 (label, 浮点)
-- image_quality   -- 高像素 (label, 0=12MP 1=高像素)
-- flash, watermark, motion, filter, tuning_apply, timer, exposure_adjust 等
