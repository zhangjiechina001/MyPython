from sklearn.datasets import load_digits
import numpy as np
import cv2
digits=load_digits()
print("数据集量及单个数据的大小：",digits.data.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.5,random_state=33)
# X_train=np.resize(X_train,(8,8))
# y_train=np.resize(y_train,(8,8))
print("训练数据量:",y_train.shape)
print("测试数据量:",y_test.shape)

from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
# num_5=cv2.imread('5.jpg',cv2.IMREAD_GRAYSCALE)
# num_5=num_5[80:150,80:150]
# num_5=np.resize(num_5,(8,8))
# num_5=num_5.ravel()
# _,num_5=cv2.threshold(num_5,100,255,cv2.THRESH_BINARY)
# cv2.imshow('binary',num_5)
# cv2.waitKey()
# 0,0,0,1,0,0,0,0,
num_1=np.array([[  0. ,  0. ,  4. , 15. , 13. ,  3.  , 0. ,  0. ,  0. ,  0. ,  7.,  14.,  16. ,  9. ,  0.,
   0. ,  0.  , 0. ,  0. , 12.,  16.  , 8. ,  0.,   0. ,  0. ,  0. ,  0.,   6.,  16. ,  6.,
   0.  , 0. ,  0.  , 0. ,  0.,   9.,  16. ,  6. ,  0. ,  0. ,  0. ,  0. ,  0.  ,12.  ,16.,
   3. ,  0. ,  0. ,  0.,   0.,   0.,  13. , 16.,   3. ,  0. ,  0. ,  0. ,  0. ,  0. , 15.,
  16. , 11.,   0.  , 0.]],np.float)

X_test=ss.transform(X_test)

lsvc=LinearSVC()
lsvc.fit(X_train,y_train)
y_predict=lsvc.predict(X_test)
y_testpredict=lsvc.predict(num_1)
print(str(y_testpredict))
print('The accuracy of Linear SVC is:',lsvc.score(X_test,y_test))
from sklearn.metrics import classification_report
classification=classification_report(y_test,y_predict, target_names=digits.target_names.astype(str))
print(classification)