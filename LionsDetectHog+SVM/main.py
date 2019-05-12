#1.样本2.训练3.test 预测
#1.样本
# 1.1 pos正样本 包含所有检测目标 neg不包含obj
# 1.2样本获取 1网络 2公司内部 3自己手机
# 一个好的样本好过一个复杂的神经网络
# 机器学习几千几万就行了 深度学习就是上百万千万了
# 1.1 样本售价一张/元
# 1.2网络自己爬取
# 1.3公司多年积累
# 1.4自会收集视频
#正样本 环境尽可能多变

import  cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.参数设置2.创建一个hog 3svm 4计算hog 5label 6完成训练 7完成当前预测 8draw

PosNum=820
NegNum=1931
winSize=(64,128)
blockSize=(16,16)#105
blockStride=(8,8)#4 cell
cellSize=(8,8)#4 cell
nBin=9#9bin3780

#2 hog create
hog=cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBin)

svm=cv2.ml.SVM_create()

featureNum=int(((128-16)/8+1)*((64-16)/8+1)*4*9)#3780
fetureArray=np.zeros((PosNum+NegNum),featureNum,dtype=np.float32)
labelArray=np.zeros(((PosNum+NegNum),featureNum),dtype=np.float32)