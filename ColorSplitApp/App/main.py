from PIL import Image
import matplotlib as mpl
import os
#matplotlib默认运行GUI，会打断主程序，必须采用非交互形式
mpl.use('Agg')
import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MiniBatchKMeans

Basepath=os.path.abspath(os.path.dirname(__file__))

'''
更新：
1. 图片名称保存去掉本名，如layer1，layer2
2. 新增返回色板颜色rgb功能，以list对象返回
3. 图片保存为png
4. 去除图片白边
'''

class ImgSplit:
    #构造函数
    def __init__(self, path):
        #self.filename = path[path.rfind('/')+1:path.rfind('.')]
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
        
    #功能 函数成员
    #显示原图 应该返回一个base64比较合理
    def showImage(self, dpi = 1000):
        plt.figure(figsize = (self.width/dpi, self.height/dpi), dpi = dpi)
        plt.axis('off')
        plt.imshow(self.pixels)
    
    def colorSplit(self, n_clusters = 3):
        #处理数据，从三维到二维
        data = self.pixels/255. #像素归一化 变为(0,1)，不然会报错
        data = data.reshape(-1, 3)
        kmeans = MiniBatchKMeans(n_clusters)
        #提前设定的中心点？？ 现在已经压缩完成 pred是每个像素对应的cluster编号 值就是0-2这些 结构如[0,2,1,2]这样
        #Index of the cluster each sample belongs to.
        pred = kmeans.fit_predict(data)
        #聚类得到的几个中心点 3个 是一个3*3的矩阵
        #kmeans.cluster_centers_.shape
        #同属一个cluster的像素替换为类中心点的颜色
        cluster_colors = kmeans.cluster_centers_
        overview_data = cluster_colors[pred]
        #将归一化的颜色转换为三维的
        #整体图像预览数据
        self.overview = overview_data.reshape(self.pixels.shape)
        #色板颜色，要导出色板需要rgb格式，m*n*3是三维的，原本是m*3的
        self.palette = cluster_colors.reshape(1,-1,3)
        
        #return self.overview
        #每个图层的像素保存
        for i in range(n_clusters):
            #temp[i] 是当前的颜色，除了当前颜色外都是透明色
            #rgba
            temp = np.zeros([n_clusters, 4], dtype = float)
            temp[i] = np.append(kmeans.cluster_centers_[i], [1])
            #每个图层的像素，m*n*4
            layer_data = temp[pred].reshape([self.pixels.shape[0],self.pixels.shape[1],4])
            self.layers.append([temp[i], layer_data])

    #展示色板
    def showPalette(self):
        plt.figure(figsize = (self.palette.shape[1],1), dpi = 100)
        plt.axis('off')
        plt.imshow(self.palette)
        #plt.savefig('ColorSplitApp/App/static/split/'+self.filename+'_palette.jpeg', bbox_inches='tight',pad_inches=0.0)
        plt.savefig(Basepath+'/static/split/'+'palette.jpeg', bbox_inches='tight',pad_inches=0.0,transparent=True)
        #返回palette数组
        return '../static/split/'+'palette.jpeg'

    def paletteRGB(self):
        #更改部分
        f = self.palette
        #将色板由[0-1]再转换为[0-255]区间，深复制
        for i in np.nditer(f, op_flags=['readwrite']):
            i[...] = int(255 if i>=1.0 else math.floor(i*256.0))
        f = f.astype(np.int32)
        #list形式的色板，形如[[231, 232, 233], [13, 138, 234], [7, 26, 118]]
        paletteRGB = f.tolist()[0]
        for i in range(3):
            for j in range(3):
                paletteRGB[i][j] = str(paletteRGB[i][j])
            paletteRGB[i] = 'RGB('+', '.join(paletteRGB[i])+')'
        return paletteRGB
        #可以改为返回一个list，在前端显示颜色
        #更改部分

    #预览整体图像
    def showOverview(self, dpi = 1000):
        plt.figure(figsize = (self.width/dpi, self.height/dpi), dpi = dpi)
        plt.axis('off')
        plt.imshow(self.overview)
        #plt.savefig('ColorSplitApp/App/static/split/'+self.filename+'_overview.jpeg', bbox_inches='tight',pad_inches=0.0)
        #return '../static/split/'+self.filename+'_overview.jpeg'
        plt.savefig(Basepath+'/static/split/'+'overview.png', bbox_inches='tight',pad_inches=0.0,transparent=True)
        return '../static/split/'+'overview.png'
        
    #预览每个图层
    def showLayers(self, dpi = 1000):
        i = 0
        paths = []
        for layer in self.layers:
            #key是颜色
            #plt.figure(figsize = (1,1), dpi = 100)
            #plt.axis('off')
            #保存每一张图层的主题色，没放在界面，或许可以return rgb数值然后前端直接显示颜色？
            #plt.imshow(layer[0].reshape(1,1,3))
            #plt.savefig('recolored/'+img_name+'_palette'+str(i)+'.jpeg')
            #value是图像像素
            plt.figure(figsize = (self.width/dpi, self.height/dpi), dpi = dpi)
            plt.axis('off')
            plt.imshow(layer[1])
            #plt.savefig('ColorSplitApp/App/static/split/'+self.filename+'_layer'+str(i)+'.png', bbox_inches='tight',pad_inches=0.0)
            #paths.append('../static/split/'+self.filename+'_layer'+str(i)+'.png')
            plt.savefig(Basepath+'/static/split/'+'layer'+str(i)+'.png', bbox_inches='tight',pad_inches=0.0, transparent=True)
            paths.append('../static/split/'+'layer'+str(i)+'.png')
            i += 1
        return paths