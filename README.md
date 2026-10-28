# Qingping Brand

青萍品牌规范、素材与单页网站。

- 品牌色：**青萍青** `#1FB6AE`，RGB `31, 182, 174`
- Logo：白色 Qingping 字标，保留原始青蓝渐变背景
- Favicon：白色单字母 Q，包含 ICO 与多个尺寸 PNG

## 文件

- `index.html`：品牌规范页面
- `style.css`、`app.js`：页面样式与色值复制功能
- `assets/qingping-logo-vector.svg`：渐变背景矢量 Logo
- `assets/qingping-wordmark-white.svg`：透明底白色矢量字标（路径，无字体依赖）
- `assets/qingping-logo-vector-grid.svg`：矢量 Logo 网格参考图
- `assets/favicon/`：Favicon 素材和说明
- `assets/qingping-color.txt`：品牌色值
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

品牌色与现有素材已确认。页面中的使用原则为建议；已采用用户提供的已完成渐变背景和透明底白色 SVG，和网格参考 SVG。Logo 区域使用品牌包的七种 SVG 预览，并提供 SVG 与常用尺寸 PNG 下载；网格 SVG 供参考。品牌标准色为 #1FB6AE，品牌包字标青蓝色为 #009DB5。印刷色值、安全留白及最小使用尺寸待补充确认。

## 发布

页面入口和素材位于仓库根目录。运行 `python3 build.py` 将页面复制到忽略提交的 `dist/`，供 Sites 发布使用。
