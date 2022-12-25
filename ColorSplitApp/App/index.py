from flask import Flask, request, render_template, url_for, jsonify
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
    
if __name__ == '__main__':
    app.run(port = 5000, host = '0.0.0.0', threaded = True, debug = True)