import numpy as np
import matplotlib.pyplot as plt
import  cv2

src=cv2.imread(r'D:\E\0.jpg')
cv2.imshow('src',src)
imgshape=src.shape
hiegh=imgshape[0]
width=imgshape[1]
#缩放矩阵
matscale=np.float32([[0.5,0,0],[0,0.6,0]])
dst=cv2.warpAffine(src,matscale,(int(width/2),int(hiegh*0.6)))
cv2.imshow('result',dst)
cv2.waitKey()
cv2.destroyAllWindows()
