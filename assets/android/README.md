# Qingping Android 原生 App 图标

使用现有品牌 Q 与青蓝渐变背景。桌面应用名称建议显示为 Qingping。

## 接入 Android 项目

将 `res/` 中的内容合并到 App 模块的 `src/main/res/`。如项目已有同名文件，先备份或改用自定义资源名称。

在现有 AndroidManifest.xml 的 `<application>` 上设置：

```xml
android:icon="@mipmap/ic_launcher"
android:roundIcon="@mipmap/ic_launcher_round"
```

- Android 8.0+：`mipmap-anydpi-v26/` 自适应图标，使用矢量前景和渐变背景。
- Android 13+：`mipmap-anydpi-v33/` 增加 monochrome 层，使用品牌 Q 轮廓，颜色由系统主题决定。
- 旧版兼容：mdpi、hdpi、xhdpi、xxhdpi、xxxhdpi 分别提供 48、72、96、144、192 px PNG；另附圆形兼容图标。
- Google Play：`google-play/ic_launcher-512.png`，512 × 512 px、RGBA PNG，无预裁圆角、无外部阴影。

## 尺寸与设计

自适应前景和背景均为 108 × 108 dp。品牌 Q 居中放置，位于圆形安全区内。前景透明，背景不透明且铺满。圆角和自适应外轮廓由系统裁切。

`sources/` 包含 SVG 与 432 × 432 px 前景/背景参考图；工程直接引用 `res/` 中的矢量 XML，无需重复导入 PNG 层。

`previews/` 中的裁切和主题示意仅供检查，不是工程资源。模拟的主题颜色不代表新增品牌色。

## 官方参考

- https://developer.android.com/develop/ui/compose/system/icon_design_adaptive
- https://developer.android.com/distribute/google-play/resources/icon-design-specifications
