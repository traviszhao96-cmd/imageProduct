# 三方相机使用埋点

> 新增日期: 2026-07-07
> 状态: 待上线

## 新增参数

| event_name | key | key_note | label | label_note | string_value | value_note | 默认值 | 备注 | 当前状态 |
|---|---|---|---|---|---|---|---|---|---|
| NTCamera | third_party_camera | 三方应用调用相机时上报，记录调用时长、摄像头、应用包名和页面信息 | camera_duration | 第三方应用使用相机的时长 | xxx | 毫秒数，如 5000 表示 5 秒 | | 新增 | 待上线 |
| NTCamera | third_party_camera | 同上 | camera_id | 第三方应用使用的摄像头 | 0 | 0=主摄, 1=前置, 2=超广角, 3=长焦 | | 新增 | 待上线 |
| NTCamera | third_party_camera | 同上 | camera_package | 调用相机的第三方应用包名 | xxx | 如 com.instagram.android | | 新增 | 待上线 |
| NTCamera | third_party_camera | 同上 | camera_activity | 调用相机时的 Activity 页面 | xxx | 完整 Activity 类名 | | 新增 | 待上线 |

## 代码参考

```java
private static final String trackingDomain = "NtCamTracker";
public static final String CAMERA_DURATION = "camera_duration";
public static final String CAMERA_CAMERA_ID = "camera_id";
public static final String CAMERA_PACKAGE = "camera_package";
public static final String CAMERA_ACTIVITY = "camera_activity";
```

## Bitable 操作

Bitable key 字段为 select 类型，API 不支持自动新增选项值。
需在飞书 Bitable 中手动添加 `third_party_camera` 选项后，再导入以上 4 条记录。
Bitable: https://nothing-tech.sg.larksuite.com/base/N2azb9muvaqqmwsIB7IlPmFGgpg?table=tblh05JLoheZIXfr
