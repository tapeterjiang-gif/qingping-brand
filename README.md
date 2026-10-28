# Qingping Brand

青萍品牌规范、素材与单页网站。

- 主色：**青萍青** `#1FB6AE`；文字色：**字标青蓝** `#009DB5`
- 辅助色：**青萍蓝** `#006AB7`、**亮青** `#35ECDD`
- 各色提供 HEX / RGB / CMYK（指定配置参考）/ PANTONE C（近似候选，待实体打样核准）
- Logo：白色 Qingping 字标，保留原始青蓝渐变背景
- Favicon：白色单字母 Q，包含 ICO 与多个尺寸 PNG

## 文件

- `index.html`：品牌规范页面
- `style.css`、`app.js`：页面样式与色值复制功能
- `assets/qingping-q-vector.svg`、`assets/qingping-q-vector-grid.svg`、`assets/qingping-q-white.svg`：三种 Q Logo
- `assets/qingping-q-logos.zip`：Q Logo 矢量套装与说明
- `assets/qingping-logo-vector.svg`：渐变背景矢量 Logo
- `assets/qingping-wordmark-white.svg`：透明底白色矢量字标（路径，无字体依赖）
- `assets/qingping-logo-vector-grid.svg`：矢量 Logo 网格参考图
- `assets/favicon/`：Favicon 素材和说明
- `assets/qingping-color.txt`：色彩规范及印刷参考说明
- `assets/qingping-colors.json`：结构化色彩值、转换配置和 Pantone 参考来源
- `assets/qingping-brand-kit 2/`：用户提供的 7 SVG、30 个尺寸 PNG、总览图及使用说明
- `assets/qingping-brand-kit.zip`：品牌包下载（原文件保持不变）
- `assets/qingping-brand-assets.zip`：全部素材下载包
- `.openai/hosting.json`：Sites 发布配置

## 本地查看

在仓库目录运行：

```sh
python3 -m http.server 8765
```

打开 http://localhost:8765 。页面无需安装依赖或构建。

## 规范状态

品牌色与现有素材已确认。页面中的使用原则为建议；已采用用户提供的已完成渐变背景和透明底白色 SVG，和网格参考 SVG。Logo 区域展示 qingping-logo-vector.svg、qingping-logo-vector-grid.svg、qingping-wordmark-white.svg 三个原版 SVG，以及提取自同一 Q 路径的渐变、网格、透明底白色三个 Q Logo。完整品牌包保留于素材下载中。品牌标准色为 #1FB6AE，品牌包字标青蓝色为 #009DB5。CMYK 以 Apple Generic CMYK Profile 相对比色转换，Pantone 为近似专色候选；正式印刷规格需打样核准。安全留白及最小使用尺寸待补充确认。

## 发布

页面入口和素材位于仓库根目录。运行 `python3 build.py` 将页面复制到忽略提交的 `dist/`，供 Sites 发布使用。
