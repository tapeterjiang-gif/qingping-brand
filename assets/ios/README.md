# Qingping iOS / iPadOS 图标

基于现有完整 Qingping 矢量 Logo，保留原字标、比例、留白及青蓝渐变，不使用单字母 Q。

## 接入 Xcode

将 `Assets.xcassets/AppIcon.appiconset` 拖入工程现有的 Assets.xcassets，并在 Target 的 App Icons 中选择 AppIcon。如已有同名资源，请先备份或改名。

- 提供 iPhone 与 iPad 的主屏幕、设置、通知和 Spotlight 图标尺寸。
- `Qingping-iOS-1024.png` 为 1024 × 1024 px、无 Alpha 的 RGB PNG，可用于 Xcode 单尺寸图标输入。
- `AppIcon.appiconset/Contents.json` 配齐各尺寸槽位及 App Store 1024 px 槽位。
- 所有正式 PNG 均为完整方形，无透明边角；由系统应用圆角。
- `sources/Qingping-logo.svg` 保留可编辑矢量源文件。
- `previews/` 中的圆角只是显示示意，不是实际系统截图。

此包为标准平面 AppIcon 素材，不包含另行设计的 Dark、Tinted 或 Liquid Glass 分层版本；需要时可在 Xcode 或 Icon Composer 中进一步配置。

已检查各槽位尺寸、RGB 模式与文件引用，并通过本机 Xcode actool 的 iPhone/iPad 资源编译（最低系统参数 iOS 13.0）。这项检查不等同于完整 App 打包或 App Store 审核。

官方参考：
https://developer.apple.com/documentation/xcode/configuring-your-app-icon
https://developer.apple.com/design/human-interface-guidelines/app-icons
