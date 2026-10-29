# Qingping 网站图标资源

使用已确认的锐角 Q 字形与青蓝渐变背景，仅提供现代 SVG 和 PWA 图标资源。

| 文件 | 场景 |
| --- | --- |
| favicon.svg | 浏览器标签、收藏夹；背景圆角约 20%（1254 画幅，rx=251） |
| icon-192.png | 192 × 192 常规 PWA 图标 |
| icon-512.png | 512 × 512 常规 PWA 图标 |
| icon-maskable.svg | 自适应图标的矢量源 |
| icon-maskable-512.png | 512 × 512 自适应 PWA 图标 |
| ../../site.webmanifest | 网站安装外观、名称、路径与图标配置 |

## 引用

将 site.webmanifest 放在网站入口同级，图标放在 assets/icons/，在 HTML 的 head 内加入：

```html
<link rel="icon" type="image/svg+xml" sizes="any" href="./assets/icons/favicon.svg">
<link rel="manifest" href="./site.webmanifest">
<meta name="theme-color" content="#1FB6AE">
```

manifest 的 id、start_url、scope 均为 ./，图标路径相对 manifest 解析，可用于域名根目录和 GitHub Pages 项目子目录。迁移时修改 name、short_name 与 description 以匹配具体产品。

## Maskable

自适应图标独立导出，Q 在中心等比缩小到常规版的 84%，置于中央直径 80% 的安全圆内；渐变背景铺满画布并保持不透明。圆形、圆角矩形等裁切由系统执行，源文件不预裁圆角。

未包含旧浏览器 ICO、Apple Touch 图标或 16/32 px PNG。这里提供图标和 manifest；未加入离线缓存，安装入口是否出现由浏览器决定。

规范参考：https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons

圆角规则：仅 SVG favicon 的背景使用约 20% 圆角。常规 PWA PNG、Maskable PNG 与其 SVG 源文件继续保留方形、不透明背景，由系统裁切。
