# Qingping Brand

青萍品牌规范、素材与单页网站。

- 品牌色：**青萍青** `#1FB6AE`，RGB `31, 182, 174`
- Logo：白色 Qingping 字标，保留原始青蓝渐变背景
- Favicon：白色单字母 Q，包含 ICO 与多个尺寸 PNG

## 文件

- `index.html`：品牌规范页面
- `style.css`、`app.js`：页面样式与色值复制功能
- `assets/logo.png`：原始 Logo
- `assets/favicon/`：Favicon 素材和说明
- `assets/qingping-color.txt`：品牌色值
- `assets/qingping-brand-assets.zip`：全部素材下载包
- `.openai/hosting.json`：Sites 发布配置

## 本地查看

在仓库目录运行：

```sh
python3 -m http.server 8765
```

打开 http://localhost:8765 。页面无需安装依赖或构建。

## 规范状态

品牌色与现有素材已确认。页面中的使用原则为建议；矢量 Logo、透明底与单色版本、印刷色值、安全留白及最小使用尺寸待补充确认。

## 发布

页面入口和素材位于仓库根目录。运行 `python3 build.py` 将页面复制到忽略提交的 `dist/`，供 Sites 发布使用。
