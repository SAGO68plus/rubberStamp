from flask import Flask, request, render_template, url_for, jsonify, json
from main import ImgSplit
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload():
    global image
    f = request.files.get('img')
    n = int(request.form['input'])
    img_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
    f.save(img_path)
    image = ImgSplit(img_path, secure_filename(f.filename))
    image.colorSplit(n)
    palette = image.showPalette()
    overview = image.showOverview()
    layers = image.showLayers()
    RGB = image.paletteRGB()
    return  jsonify({'signal':1, 'palette':palette,'RGB':RGB, 'overview':overview, 'layers':layers})

@app.route('/replace', methods = ['POST'])
def replace():
    rgb = request.form['color']
    index = int(request.form['index'])
    time = request.form['time']
    new_layer = image.replaceColor(rgb, index, time)
    return jsonify({'signal':2, 'path':new_layer})

@app.route('/reset', methods = ['POST'])
def reset():
    colors = request.form['colors']
    time = request.form['time']
    newImage = image.reset(colors,time)
    return jsonify({'signal':3, 'newImage':newImage})
    
if __name__ == '__main__':
    app.run(port = 8000, host = '0.0.0.0', threaded = True, debug = True)