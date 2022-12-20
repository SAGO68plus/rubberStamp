配置完第三方库后，运行`python index.py`即可
## 项目结构
- [index.py](App/index.py) 项目启动文件
- [main.py](App/main.py) 处理分色的主程序
- [static/](App/static/) 静态资源文件
  - assets 一些静态页面的图片
  - css
  - [js/](App/static/js)
    - [scripts.js](App/static/js/scripts.js) 一些前端交互的内容，不是很主要。写了固定footer、上传图片、推荐图片显示和读取分色数量的功能
    - split 接收分色之后导出的预览图、色板和各图层的图片
    - upload 接收用户上传的图片
- templates
  - [index.html](App/templates/index.html) 主页面，最下面是实现了上传图片给启动文件[index.py](App/index.py) 接收，启动文件再调用[main.py](App/main.py)主程序处理文件，返回给主页面，同时主页面的样式发生变化
