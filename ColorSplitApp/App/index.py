from flask import Flask, request, render_template, Response, redirect, url_for, flash, jsonify
#从库里面引入Flask类
from main import ImgSplit
import os
import json
from werkzeug.utils import secure_filename

#创建了一个对象，形参是应用模块或者包的名字
#__name__ 是一个适用于大多数情况的快捷方式。有了这个参数， Flask 才能知道在哪里可以找到模板和静态文件等东西
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload/'

#使用route() 装饰器告诉 Flask 什么样的URL能触发我们的函数
@app.route('/')
#函数返回需要在用户浏览器中显示的信息。默认的内容类型是 HTML ，因此字 符串中的 HTML 会被浏览器渲染。
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload():
    f = request.files.get('img')
    n = int(request.form['input'])
    img_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
    f.save(img_path)
    image = ImgSplit(img_path)
    image.colorSplit(n)
    palette = image.showPalette()
    overview = image.showOverview()
    layers = image.showLayers()
    return  jsonify({'signal':1, 'palette':palette, 'overview':overview, 'layers':layers})
    
if __name__ == '__main__':
    app.run(port = 5500, host = '0.0.0.0', threaded = True, debug = True)