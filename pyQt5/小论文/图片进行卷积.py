import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

#对原图片进行卷积，得出定位点
dst_img=cv2.imread('bestimg.jpg',cv2.IMREAD_GRAYSCALE)
dst_img=dst_img[30:90,2500:5000]
h,w=dst_img.shape
src=cv2.bitwise_not(dst_img)
cv2.namedWindow('src',cv2.WINDOW_NORMAL)
cv2.imshow('src',dst_img)
kernel=np.ones((h,850),dtype=np.float32)
result=signal.convolve2d(src,kernel,'valid')

hist=result[0].ravel()
plt.subplot(211)
plt.plot(hist)
plt.xlabel('(a)卷积投影分布',fontproperties='SimHei',fontsize=15)
plt.xlim((0,w))

plt.subplot(212)
plt.imshow(cv2.cvtColor(cv2.imread('afterCutImg.png',cv2.IMREAD_GRAYSCALE),cv2.COLOR_GRAY2RGB))
plt.xlabel('(b)分割后图片',fontproperties='SimHei',fontsize=15)
plt.xticks([])
plt.yticks([])
maxIdx=np.argmax(hist)
cutimg=dst_img[:,maxIdx:maxIdx+860]
cv2.imwrite('afterCutImg.png',cutimg)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()