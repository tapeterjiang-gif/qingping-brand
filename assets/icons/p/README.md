# Qingping P 姐妹网站图标

从 Qingping 字标提取小写 p 原路径，保持字形比例。与 Q 图标沿用青蓝渐变、白色前景、相同的可见高度和约 20% 圆角。
favicon.svg 用于浏览器标签；PNG 16/32/48 与 favicon.ico 用于兼容。
icon-192.png、icon-512.png 为方形 PWA 图标；icon-maskable-512.png 为具有安全留白的自适应版。
apple-touch-icon.png 为 180 px 方形图标，由系统应用圆角。
icon.svg 和 icon-maskable.svg 为方形矢量源。

将本目录文件一起放到目标网站根目录，添加：
<link rel="icon" type="image/svg+xml" href="./favicon.svg">
<link rel="icon" href="./favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="./apple-touch-icon.png">
<link rel="manifest" href="./site.webmanifest">

Manifest 路径相对自身解析。按目标网站修改 name、short_name、id、start_url、scope。
