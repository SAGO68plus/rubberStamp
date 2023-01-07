from PIL import Image
import matplotlib as mpl
import os
mpl.use('Agg')
import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MiniBatchKMeans

Basepath=os.path.abspath(os.path.dirname(__file__))


class ImgSplit:
    #构造函数
    def __init__(self, path, filename):
        #图像名称
        self.filename = filename[filename.rfind('/')+1:filename.rfind('.')]
        #图像类型 jpg/jpeg/png
        self.filetype = filename[filename.rfind('.')+1:]
        #像素数据
        self.pixels = np.asarray(Image.open(path))
        #宽度和高度
        self.width = self.pixels.shape[1]
        self.height = self.pixels.shape[0]
        #处理之后的图像 预览
        self.overview = None
        #色板
        self.pallete = None
        #分图层导出，每个图层有一个主题色
        self.layers = []
        #pred 分色后数组，存储每个像素点对应颜色索引/集群索引
        self.pred = None
        #分色数量
        self.n_clusters = 3
        
    #功能 函数成员
    #显示原图 应该返回一个base64比较合理
    def showImage(self, dpi = 1000):
        plt.figure(figsize = (self.width/dpi, self.height/dpi), dpi = dpi)
        plt.axis('off')
        plt.imshow(self.pixels)
    
    def colorSplitForpng(self, n_clusters):
        data = self.pixels/255. 
        data = data.reshape(-1, 4)
        kmeans = MiniBatchKMeans(n_clusters)
        pred = kmeans.fit_predict(data)
        self.pred = pred
        cluster_colors = kmeans.cluster_centers_
        overview_data = cluster_colors[pred]
        self.overview = overview_data.reshape(self.pixels.shape)
        self.palette = cluster_colors.reshape(1,-1,4)
        for i in range(n_clusters):
            temp = np.zeros([n_clusters, 4], dtype = float)
            temp[i] = kmeans.cluster_centers_[i]
            layer_data = temp[pred].reshape([self.pixels.shape[0],self.pixels.shape[1],4])
            self.layers.append([temp[i], layer_data])
    
    def colorSplitForjpg(self, n_clusters):
        data = self.pixels/255. #像素归一化 变为(0,1)，不然会报错
        data = data.reshape(-1, 3)
        kmeans = MiniBatchKMeans(n_clusters)
        #Index of the cluster each sample belongs to.
        pred = kmeans.fit_predict(data)
        self.pred = pred
        #kmeans.cluster_centers_.shape
        #同属一个cluster的像素替换为类中心点的颜色
        cluster_colors = kmeans.cluster_centers_
        overview_data = cluster_colors[pred]
        #将归一化的颜色转换为三维的
        #整体图像预览数据
        self.overview = overview_data.reshape(self.pixels.shape)
        #色板颜色，要导出色板需要rgb格式，m*n*3是三维的，原本是m*3的
        self.palette = cluster_colors.reshape(1,-1,3)
        
        #每个图层的像素保存
        for i in range(n_clusters):
            temp = np.zeros([n_clusters, 4], dtype = float)
            temp[i] = np.append(kmeans.cluster_centers_[i], [1])
            layer_data = temp[pred].reshape([self.pixels.shape[0],self.pixels.shape[1],4])
            self.layers.append([temp[i], layer_data])
    
    def colorSplit(self, n_clusters = 3):
        self.n_clusters = n_clusters
        if self.filetype == "png":
            self.colorSplitForpng(n_clusters)
        else:
            self.colorSplitForjpg(n_clusters)

    #展示色板
    def showPalette(self):
        plt.figure(figsize = (self.palette.shape[1],1), dpi = 100)
        plt.axis('off')
        plt.imshow(self.palette)
        plt.savefig(Basepath+'/static/split/'+self.filename+'_palette.png', bbox_inches='tight',pad_inches=0.0,transparent=True)
        return '../static/split/'+self.filename+'_palette.png'

    def paletteRGBjpg(self):
        f = self.palette.copy()
        for i in np.nditer(f, op_flags=['readwrite']):
            i[...] = int(255 if i>=1.0 else math.floor(i*256.0))
        f = f.astype(np.int32)
        #list形式的色板，形如[[231, 232, 233], [13, 138, 234], [7, 26, 118]]
        paletteRGB = f.tolist()[0]
        for i in range(len(paletteRGB)):
            for j in range(3):
                paletteRGB[i][j] = str(paletteRGB[i][j])
            paletteRGB[i] = 'RGB('+', '.join(paletteRGB[i])+')'
        return paletteRGB
    
    def paletteRGBpng(self):
        #结果仍然是rgb，rgba容易引起混淆
        f = self.palette.copy()
        for i in np.nditer(f, op_flags=['readwrite']):
            i[...] = int(255 if i>=1.0 else math.floor(i*256.0))
        f = f.astype(np.int32)
        paletteRGB = f.tolist()[0]
        for i in range(len(paletteRGB)):
            for j in range(3):
                paletteRGB[i][j] = str(paletteRGB[i][j])
            paletteRGB[i] = 'RGB('+', '.join(paletteRGB[i][:-1])+')'
        return paletteRGB
    
    def paletteRGB(self):
        if self.filetype == "png":
            return self.paletteRGBpng()
        else:
            return self.paletteRGBjpg()

    #预览整体图像
    def showOverview(self, dpi = 1000):
        plt.figure(figsize = (self.width/dpi, self.height/dpi), dpi = dpi)
        plt.axis('off')
        plt.imshow(self.overview)
        plt.savefig(Basepath+'/static/split/'+self.filename+'_overview.png', bbox_inches='tight',pad_inches=0.0,transparent=True)
        return '../static/split/'+self.filename+'_overview.png'
        
    #预览每个图层
    def showLayers(self, dpi = 1000):
        i = 0
        paths = []
        for layer in self.layers:
            plt.figure(figsize = (self.width/dpi, self.height/dpi), dpi = dpi)
            plt.axis('off')
            plt.imshow(layer[1])
            plt.savefig(Basepath+'/static/split/'+self.filename+'_layer'+str(i)+'.png', bbox_inches='tight',pad_inches=0.0, transparent=True)
            paths.append('../static/split/'+self.filename+'_layer'+str(i)+'.png')
            i += 1
        return paths
    
    def replaceColor(self, color, i, time):
        #传入一个rgb字符串以及图层的序号
        #把不等于[0,0,0,0]的替换为传入的color
        newColor = color[5:-1].split(',')
        rgba = list(map(int, newColor))
        rgba = np.asarray(rgba, float)
        for j in range(3):
            rgba[j] = rgba[j]/255.
        temp = np.zeros([self.n_clusters, 4], dtype = float)
        temp[i] = rgba
        layerData = temp[self.pred].reshape([self.pixels.shape[0],self.pixels.shape[1],4])
        plt.figure(figsize = (self.width/1000, self.height/1000), dpi = 1000)
        plt.axis('off')
        plt.imshow(layerData)
        plt.savefig(Basepath+'/static/split/'+self.filename+'_layer_'+time+str(i)+'_new.png', bbox_inches='tight',pad_inches=0.0,transparent=True)
        return '../static/split/'+self.filename+'_layer_'+time+str(i)+'_new.png'
    
    def reset(self, s, time):
        #传入所有的新颜色，以列表的形式
        colors = s[:-1].split('),')
        temp = np.zeros([self.n_clusters, 4], dtype = float)
        for i in range(len(colors)):
            newColor = colors[i][5:].split(', ')
            rgba = list(map(int, newColor))
            rgba = np.asarray(rgba, float)
            for j in range(3):
                rgba[j] = rgba[j]/255.
            temp[i] = rgba
        layerData = temp[self.pred].reshape([self.pixels.shape[0],self.pixels.shape[1],4])
        plt.figure(figsize = (self.width/1000, self.height/1000), dpi = 1000)
        plt.axis('off')
        plt.imshow(layerData)
        plt.savefig(Basepath+'/static/split/'+self.filename+'_reset_'+time+'.png', bbox_inches='tight',pad_inches=0.0,transparent=True)
        return '../static/split/'+self.filename+'_reset_'+time+'.png'
