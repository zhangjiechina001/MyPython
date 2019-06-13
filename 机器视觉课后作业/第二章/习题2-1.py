#一个球的图像的形状是什么样的？一个圆盘的图像形状是什么样的？
#我们假设1）使用的是透视投影2）圆盘所在的平面可以（相对像平面）发生倾斜
#coding=utf-8
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import hmmlearn

x=np.arange(-1,1,0.1)
y=np.arange(-1,1,0.1)
x,y=np.meshgrid(x,y)
x=x.ravel()
y=y.ravel()
tempx=[]
tempy=[]
tempz=[]
import math
for i in range(len(x)):
    if(x[i]**2+y[i]**2<1):
        tempx.append(x[i])
        tempy.append(y[i])
        z=math.sqrt(1-x[i]**2-y[i]**2)
        tempz.append(z)

fig = plt.figure()
ax = Axes3D(fig)
#高度
ax.plot_surface(tempx,tempy,tempz,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#填充rainbow颜色
ax.contourf(tempx,tempy,tempz,zdir='z',offset=-2,cmap='rainbow')
#绘制3D图形,zdir表示从哪个坐标轴上压下去
plt.show()

