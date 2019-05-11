# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Administrator\OneDrive\MyPython\flower.jpg')
def nothing(x):
    r =x
    img[:,:,1] = r
    cv2.imshow('image',img)



# 创建一副黑色图像


# 设置滑动条组件
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.imshow('image',img)
cv2.waitKey()


# 销毁窗口
cv2.destroyAllWindows()

