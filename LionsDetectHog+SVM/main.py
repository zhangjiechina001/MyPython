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

#2 hog create创建一个hog对象
hog=cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBin)

svm=cv2.ml.SVM_create()

featureNum=int(((128-16)/8+1)*((64-16)/8+1)*4*9)#3780
fetureArray=np.zeros(((PosNum+NegNum),featureNum),dtype=np.float32)
labelArray=np.zeros((((PosNum+NegNum),1)),dtype=np.int32)

for i in range(0,PosNum):
    fileNmae='pos\\'+str(i+1)+'.jpg'
    img=cv2.imread(fileNmae)
    img=cv2.cvtColor(img,cv2.CV_32SC1)
    his=hog.compute(img,(8,8))
    for j in range(0,featureNum):
        fetureArray[i,j]=his[j]
    labelArray[i,0]=1
        #z正样本label 1

for i in range(0,NegNum):
    fileNmae='neg\\'+str(i+1)+'.jpg'
    img = cv2.imread(fileNmae)
    img=cv2.cvtColor(img,cv2.CV_32SC1)
    his = hog.compute(img, (8, 8))
    for j in range(0, featureNum):
        fetureArray[i+PosNum,j] = his[j]
    labelArray[i+PosNum, 0] = -1

svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

# train
ret=svm.train(fetureArray,cv2.ml.ROW_SAMPLE,labelArray)
#7检测
alpha=np.zeros((1),np.float32)
rho=svm.getDecisionFunction(0,alpha)
# rho=svm.getDecisionFunction(0,)
print(rho)
print(alpha)
alphaArray=np.zeros((1,1),np.float32)
supportVArray=np.zeros((1,featureNum),np.float32)
resultArray=np.zeros((1,featureNum),np.float32)
alphaArray[0,0]=alpha

mydetect=np.zeros((3781),np.float32)
for i in range(0,3781-1):
    mydetect[i]=resultArray[0,1]
mydetect[3780]=rho[0]
#构建hog
myHog=cv2.HOGDescriptor()
myHog.setSVMDetector(mydetect)

imgSrc=cv2.imread('Test2.jpg')
objs=myHog.detectMultiScale(imgSrc,0,(8,8),(32,32),1.05,2)
x=int(objs[0][0][0])
y=int(objs[0][0][1])
w=int(objs[0][0][2])
h=int(objs[0][0][3])
cv2.rectangle(imgSrc,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('result',imgSrc)
cv2.waitKey()
