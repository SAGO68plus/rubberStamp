# Image-ColorSplit
一个为橡皮章爱好者设计的小工具：

上传您刻章所需图片，选取分色数量，自动呈现分色结果，包括色板、整体预览及图层。

## 安装
请确保您安装Python最新版本及Python Package Index (PyPI)：

- [Python](https://www.python.org/)

- [Pip Package Manager](https://pypi.org/)

## 项目预览
(ColorSplitApp/assets/web1.png)

## 项目架构
```lua
ColorSplitApp
├─ App
│	├─ app.py -- 程序启动入口
│	├─ main.py	-- 后端分色程序
│	├─ static -- 存放静态文件
│	│	├─ assets
│	│	├─ css
│	│	├─ js
│	│	├─ split -- 分色结果存储文件夹
│	│	└─ upload -- 用户上传文件存储文件夹
│	└─ templates -- 存放模板文件
│	 	└─ index.html -- 模板文件
├─ README.md
└─ requirements.txt

```


## 运行app
```
# 1.克隆项目到本地
$ git clone https://github.com/SAGO68plus/rubberStamp.git
$ cd rubberStamp/ColorSplitApp

# 2.安装项目依赖包
$ python index.py
$ pip install -r requirements.txt

# 3. 运行项目
$ python app.py
```
访问`http://127.0.0.1:5000`即可查看网站
