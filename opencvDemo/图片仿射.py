import numpy as np
import matplotlib.pyplot as plt
import  cv2
#左上角，左下角，右上角

src=cv2.imread('DPlayer.png')
cv2.imshow('src',src)
imgshape=src.shape
hiegh=imgshape[0]
width=imgshape[1]
#三个位置分别为左上角，左下角，右上角
srcmat=np.float32([[0,0],[0,hiegh-1],[width-1,0]])
dstmat=np.float32([[0,0],[20,hiegh-50],[width-50,20]])
transmat=cv2.getAffineTransform(srcmat,dstmat)
dst=cv2.warpAffine(src,transmat,(width,hiegh))
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()