# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Administrator\OneDrive\MyPython\flower.jpg')
zeros=np.zeros(shape=img.shape,dtype=np.uint8)
def callback(x):
    gamma=x/255
    global img
    global zeros
    img2 = cv2.addWeighted(img, gamma, zeros,1-gamma, 1)
    cv2.imshow('image',img2)

# 创建一副黑色图像
# 设置滑动条组件
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, callback)
cv2.createTrackbar('G', 'image', 0, 255, callback)
cv2.createTrackbar('B', 'image', 0, 255, callback)
# cv2.imshow('image',img)
cv2.waitKey()


# 销毁窗口
cv2.destroyAllWindows()

