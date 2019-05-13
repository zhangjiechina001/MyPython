# import cv2
# src=cv2.imread('num_4.png')
# res=cv2.cartToPolar(src,src)
# cv2.imshow('result',res[0])
# cv2.waitKey()
# cv2.destroyAllWindows()
import math
import cv2
import numpy as np
import sys
x=[2,4]
center=[4,0]
r=math.sqrt(math.pow(x[0]-center[0],2)+math.pow(x[1]-center[1],2))
theta=math.atan2(x[1]-center[1],x[0]-center[0])/math.pi*180#转换为角度
print (r,theta)
#opencv也提供了极坐标变换的函数
x1=np.array([[0,1,2],[0,1,2],[0,1,2]],np.float32)
y1=np.array([[0,0,0],[1,1,1],[2,2,2]],np.float32)
#真实转换坐标为（0,0）,（1,0），（2,0），（0,1），（1,1）.。。。。，# 变换中心为原点，若想为（2,3）需x1-2,y1-3
# the default center is (0,0),if you want to change it to (2,3),you should let x minus 2 and y minus 3
#when the angleInDegrees=True,that means the return is measured by angle , if not, it is radian.
r1,theta1=cv2.cartToPolar(x1,y1,angleInDegrees=True)
cv
print (r,theta)
#下面为反变换，即将极坐标变为笛卡尔坐标。（r,theta）变换为（x,y）
r=np.array([1,2,1],np.float32)
theta=np.array([30,45,90],np.float32)
x,y=cv2.polarToCart(r,theta,angleInDegrees=True)
print (x,y)