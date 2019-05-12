import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


img = cv2.imread(r'C:\Users\Administrator\OneDrive\MyPython\flower.jpg',cv2.IMREAD_GRAYSCALE)
def Calu(x,y):
    global img
    return img[x,y]
fig=plt.figure()
ax=Axes3D(fig)
x,y=img.shape
x=np.arange(0,x,10)
y=np.arange(0,y,10)
x,y=np.meshgrid(x,y)
r=np.sqrt(x**2+y**2)
z=255-Calu(x,y)
#高度
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#填充rainbow颜色
ax.contourf(x,y,z,zdir='z',offset=-2,cmap='rainbow')
#绘制3D图形,zdir表示从哪个坐标轴上压下去
plt.show()
#显示图片