# Qingping Brand · 青萍品牌规范

[在线查看品牌说明页面](https://tapeterjiang-gif.github.io/qingping-brand/) · [下载全部品牌素材](assets/qingping-brand-assets.zip)

青萍的品牌色、矢量 Logo、字标与 Q Logo 素材中心。说明页面提供色值复制和 SVG 单独下载，支持桌面及手机浏览。

## 品牌色

| 名称 | HEX | RGB |
| --- | --- | --- |
| 青萍绿 | `#1FB6AE` | 31, 182, 174 |
| 青萍青 | `#009DB5` | 0, 157, 181 |
| 青萍蓝 | `#073B53` | 7, 59, 83 |
| 亮青 | `#35ECDD` | 53, 236, 221 |

各色的 CMYK 和 Pantone 参考详见在线说明页及 [色彩规范](assets/qingping-color.txt)。CMYK 按 Apple Generic CMYK Profile 相对比色转换；Pantone 为涂布纸近似候选，正式印刷需使用实体色卡及打样核准。

## 矢量素材

- **Logo**：[渐变背景版](assets/qingping-logo-vector.svg)、[网格参考版](assets/qingping-logo-vector-grid.svg)、[透明底白色版](assets/qingping-logo-white.svg)。
- **字标 Wordmark**：[青萍绿](assets/qingping-wordmark-green.svg)、[青萍青](assets/qingping-wordmark-cyan.svg)、[青萍蓝](assets/qingping-wordmark-blue.svg)、[白色文字版](assets/qingping-wordmark-white.svg)。透明背景，裁去多余留白，路径与字距沿用现有 Logo。
- **Q Logo**：[渐变背景版](assets/qingping-q-vector.svg)、[网格参考版](assets/qingping-q-vector-grid.svg)、[透明底白色版](assets/qingping-q-white.svg)。Q 字形直接提取自现有 Logo，等比缩放并居中。

SVG 为真实矢量路径，不依赖字体，可等比缩放。白色版本请放在深色背景上查看；网格版供比例与位置参考。完整品牌包还包含七种应用版本、30 个尺寸 PNG 和使用说明。

## 使用建议

1. 等比缩放，保持字形、字距和配色。
2. 渐变背景版保留完整画面；紧裁切字标按使用场景设置留白。
3. 小尺寸场景优先使用 Q Logo，并检查实际显示效果。
4. 完整字标建议显示宽度不低于 120 px；安全留白及正式最小尺寸待确认。

原 Favicon 分类已从页面和当前全部素材包中移除，历史素材保留在仓库中。

## 网站图标

提供 [SVG favicon](assets/icons/favicon.svg)、PWA 192 / 512 PNG、自适应 Maskable 512 PNG 及其 SVG 源文件。引用方式见 [图标说明](assets/icons/README.md)，网站入口已接入 [site.webmanifest](site.webmanifest)。图标支持现代浏览器与 PWA 场景，不包含旧格式兼容导出。

## 本地查看

无需安装依赖，在此目录运行：

```sh
python3 -m http.server 8765
```

打开 <http://localhost:8765>。

## 网页发布

GitHub Pages 从 `main` 分支根目录发布。根目录的 `.nojekyll` 使页面按静态 HTML、CSS、JavaScript 和 SVG 文件直接提供，后续推送到 `main` 后会自动更新。

- `index.html`：品牌说明页面。
- `style.css`、`app.js`：页面样式与色值复制功能。
- `assets/`：矢量及 PNG 素材、色彩规范和下载包。
- `build.py`：为原有 Sites 发布生成 `dist/`。
- `.openai/hosting.json`：原有 Sites 配置。

原有 Sites 页面：<https://qingping-brand-guide.violetgleam9.chatgpt.site/>。

Q 轮廓已修补：尾巴使用直线轮廓与清晰锐角，保持圆圈自然衔接，Logo、字标、Q Logo 及品牌包导出文件保持一致。

网站图标圆角：SVG favicon 背景约 20%（rx=251 / 1254）；PWA 和 Maskable 图标保留完整方形背景。

Android 原生 App 图标素材包、预览与接入说明位于 `assets/android/`。
