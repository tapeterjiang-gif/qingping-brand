# Qingping iOS / iPadOS 图标

使用现有品牌 Q 与青蓝渐变背景。桌面应用名称建议显示为 Qingping。

## 接入 Xcode

将 `Assets.xcassets/AppIcon.appiconset` 拖入工程现有的 Assets.xcassets，并在 Target 的 App Icons 中选择 AppIcon。如已有同名资源，请先备份或改名。

- 提供 iPhone 与 iPad 的主屏幕、设置、通知和 Spotlight 图标尺寸。
- `Qingping-iOS-1024.png` 为 1024 × 1024 px、无 Alpha 的 RGB PNG，可用于 Xcode 单尺寸图标输入。
- `AppIcon.appiconset/Contents.json` 配齐各尺寸槽位及 App Store 1024 px 槽位。
- 所有正式 PNG 均为完整方形，无透明边角；由系统应用圆角。
- `sources/Qingping-logo.svg` 为品牌 Q 图标源文件；`sources/Qingping-logo-original.svg` 保留原始矢量文件。
- `previews/` 中的圆角只是显示示意，不是实际系统截图。

此包为标准平面 AppIcon 素材，不包含另行设计的 Dark、Tinted 或 Liquid Glass 分层版本；需要时可在 Xcode 或 Icon Composer 中进一步配置。

官方参考：
https://developer.apple.com/documentation/xcode/configuring-your-app-icon
https://developer.apple.com/design/human-interface-guidelines/app-icons
