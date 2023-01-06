# Image-ColorSplit
一个为橡皮章爱好者设计的小工具：

上传您刻章所需图片，选取分色数量，自动呈现分色结果，包括色板、整体预览及图层，同时可以根据您的需求改变图层色彩，合并生成新的图像。

## 安装
请确保您安装Python最新版本及Python Package Index (PyPI)：

- [Python](https://www.python.org/)

- [Pip Package Manager](https://pypi.org/)


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
└─ requirements.txt

```

## 运行项目
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
访问`http://127.0.0.1:8000`即可查看网站

## 使用说明
1. 打开页面
![index preview](https://raw.githubusercontent.com/SAGO68plus/rubberStamp/master/ColorSplitApp/App/static/assets/web1.png?token=GHSAT0AAAAAAB4QFQCNYJGIVVXB2YIVG2RQY5YHMIA)

2. 上传图片、选择分色数量
![upload](https://raw.githubusercontent.com/SAGO68plus/rubberStamp/master/ColorSplitApp/App/static/assets/web2.png?token=GHSAT0AAAAAAB4QFQCMTN4ROFNFAJEFTUD6Y5YHMXA)

3. 查看分色结果，包括色板、图像整体预览、各图层
![rgb and overview](https://raw.githubusercontent.com/SAGO68plus/rubberStamp/master/ColorSplitApp/App/static/assets/web3.png?token=GHSAT0AAAAAAB4QFQCNZJXRDXH42BSZODJIY5YHM3A)

![layers](https://raw.githubusercontent.com/SAGO68plus/rubberStamp/master/ColorSplitApp/App/static/assets/web4.png?token=GHSAT0AAAAAAB4QFQCMJQCATAVUXRBHK6WSY5YHOBQ)

4. 改变图层颜色，生成新图像
![replace color](https://raw.githubusercontent.com/SAGO68plus/rubberStamp/master/ColorSplitApp/App/static/assets/web5.png?token=GHSAT0AAAAAAB4QFQCMF2F33KYVB6NZGNWWY5YHPEQ)
![reset image](https://raw.githubusercontent.com/SAGO68plus/rubberStamp/master/ColorSplitApp/App/static/assets/web6.png?token=GHSAT0AAAAAAB4QFQCNNNTZ2YXCW7KGOVKIY5YHPGA)
