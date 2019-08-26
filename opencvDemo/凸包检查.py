# 1.先找到轮廓
import cv2
import os, sys

img = cv2.imread('haku.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('original',img)
def callback(x,image=img):
    _, thresh = cv2.threshold(img, x, 255, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    if(len(contours)>0):
        for cintour in contours:
            # 获取最小包围矩形
            rect = cv2.minAreaRect(cintour)
            temphull=cv2.convexHull(cintour)
            # 3.绘制凸包
            # 中心坐标
            tempx, tempy = rect[0]
            cv2.circle(image, (int(tempx), int(tempy)), 3, (0, 255, 0), 5)
            print('当前阀值为：%f,中心坐标为：(%f,%f)'%(x,tempx,tempy))

            # 长宽,总有 width>=height
            width, height = rect[1]
            cv2.polylines(image, [temphull], True, (0, 255, 25), 2)
    cv2.imshow('result', image)

cv2.createTrackbar('threshold','original',100,255,callback)
cv2.waitKey()