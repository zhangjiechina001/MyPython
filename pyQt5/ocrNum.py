import cv2
import numpy as np
import matplotlib.pyplot as plt

#图像二值化处理
def imgThreshold(img):
    rosource,binary=cv2.threshold(img,121,255,cv2.THRESH_BINARY)
    return binary

#对图片进行水平分割
def horizontalCut(img):
    (x,y)=img.shape #返回的分别是矩阵的行数和列数，x是行数，y是列数
    pointCount=np.zeros(y,dtype=np.uint8)#每行黑色的个数
    x_axes=np.arange(0,y)
    for i in range(0,x):
        for j in range(0,y):
            if(img[i,j]==0):
                pointCount[i]=pointCount[i]+1
    plt.plot(x_axes,pointCount)
    plt.show()
    start=[]
    end=[]
    #对照片进行分割
    print(pointCount)
    for index in range(1,y):
        #上个为0当前不为0，即为开始
        if((pointCount[index]!=0)&(pointCount[index-1]==0)):
            start.append(index)
        #上个不为0当前为0，即为结束
        elif((pointCount[index]==0)&(pointCount[index-1]!=0)):
             end.append(index)
    img1=img[start[0]:end[0],:]
    img2=img[start[1]:end[1],:]
    img3=img[start[2]:end[2],:]
    imgArr=[img1,img2,img3]
    for m in range(3):
        cv2.imshow(str(m),imgArr[m])
    cv2.waitKey()

img = cv2.imread("ocrdetect.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
binary=imgThreshold(img)
cv2.imshow('result',binary)
horizontalCut(binary)#212*200





