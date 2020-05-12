# from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps
# from flask_jsonpify import jsonify
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.spatial

# app = Flask(__name__)
# api = Api(app)

class Bubble():
    fig = plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(1, 1, 1)
    annot = ax.annotate("", xy=(1, 1), xytext=(1, 1))

    def on_press(self,event):
        if event.xdata != None and event.ydata != None:
            if self.ckdtree1.query([event.xdata, event.ydata])[0] < self.ckdtree2.query([event.xdata, event.ydata])[0]:
                ind = self.ckdtree1.query([event.xdata, event.ydata])[1]
                (xd, yd, zd) = (self.x1[ind], self.y1[ind], self.z1[ind])
            else:
                ind = self.ckdtree2.query([event.xdata, event.ydata])[1]
                (xd, yd, zd) = (self.x2[ind], self.y2[ind], self.z2[ind])
            a = '[' + "{:.2f}".format(xd) + ']\n[' + "{:.2f}".format(yd) + ']\n[' + "{:.2f}".format(zd) + ']'
            self.annot.remove()
            self.annot = self.ax.annotate(a, xy=(xd, yd), xytext=(xd + 0.1, yd + 0.1))
            self.fig.canvas.draw_idle()


    def get(self):
        # to set x_axis and y_axis
        # plt.ylim(-105, 105)
        #  plt.yticks(np.arange(-3000, 3000, 100))
        # plt.xticks(np.arange(-3000, 3000, 100))

        # data of two series
        (self.x1,self.y1,self.z1)= (np.random.randn(100)*10000,np.random.randn(100)*1000,np.random.rand(100))
        (self.x2,self.y2,self.z2)=(np.random.randn(100)*10000,np.random.randn(100)*1000,np.random.rand(100))
        (points1,points2) = (np.column_stack([self.x1, self.y1]),np.column_stack([self.x2, self.y2]))
        # df=pd.DataFrame({'x': np.random.randn(100)*10000, 'y':np.random.randn(100)*1000 ,'z':np.random.rand(100)})
        # df1=pd.DataFrame({'x': np.random.randn(100)*10000, 'y':np.random.randn(100)*1000 ,'z':np.random.rand(100)})

        # plotting both series
        self.ax.scatter(self.x1, self.y1, s=self.z1*500 , c='#2ca02c', alpha=0.6, edgecolors="white", linewidth=2)
        self.ax.scatter(self.x2, self.y2 , s=self.z2*500 , c='#9467bd', alpha=0.6, edgecolors="white", linewidth=2)

        #dimension on hover and total no. of ponts on the screen
        self.ckdtree1 = scipy.spatial.cKDTree(points1)
        self.ckdtree2 = scipy.spatial.cKDTree(points2)
        cid= self.fig.canvas.mpl_connect('motion_notify_event', self.on_press)

        plt.show()



Bubble().get()
# api.add_resource(Bubble, '/bubble')
# api.add_resource(hi, '/hi')
#
# if __name__ == '__main__':
#      app.run(port='5002')