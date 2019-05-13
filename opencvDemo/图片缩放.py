import numpy as np
import matplotlib.pyplot as plt
import  cv2

src=cv2.imread('13112.png')
imgshape=src.shape
hiegh=imgshape[0]
width=imgshape[1]
def resizePic(x):
    lamda=x/100
    global hiegh,width
    hiegh=int(lamda*float(hiegh))
    width=int(lamda*float(width))
    cv2.resize(src,(width,hiegh))
    cv2.imshow('src',imgshape)


cv2.namedWindow('src',cv2.WINDOW_NORMAL)
cv2.createTrackbar('resize','src',50,100,resizePic)
#缩放矩阵
# matscale=np.float32([[0.5,0,0],[0,0.6,0]])
# dst=cv2.warpAffine(src,matscale,(int(width/2),int(hiegh*0.6)))
# cv2.imshow('result',dst)
cv2.waitKey()
cv2.destroyAllWindows()
