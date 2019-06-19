import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#1.读取数据文件
pdData=pd.read_csv('LogiReg_data.txt',header=None,names=['Exam 1','Exam 2','Admitted'])
# print(pdData.head(),len(pdData))
positive=pdData[pdData['Admitted']==1]
negative=pdData[pdData['Admitted']==0]
#2.画出数据点
# fig,ax=plt.subplots(figsize=(10,5))
# ax.scatter(positive['Exam 1'],positive['Exam 2'],s=30,color='b',marker='o',label='Admitted')
# ax.scatter(negative['Exam 1'],negative['Exam 2'],s=30,color='r',marker='x',label='Not Admitted')
# ax.set_xlabel('Exam 1 Score')
# ax.set_ylabel('Exam 2 Score')
# plt.show()

#3.建立分类器9 求解出三个参数
#要完成的模块1.sigmoid:映射到概率的函数  2.model:返回预测结果值  3.cost：根据参数计算损失  4.gradient：计算每个参数的梯度方向
#5.descent:进行参数更新  6.accuracy:计算精度
def sigmoid(z):
    return 1/(1+np.exp(-z))
# nums = np.arange(-10, 10, step=1) #creates a vector containing 20 equally spaced values from -10 to 10
# fig, ax = plt.subplots(figsize=(12,4))
# ax.plot(nums, sigmoid(nums), 'r')
# plt.show()

pdData.insert(0,'Ones',1)
orig_data=pdData.as_matrix()
cols=orig_data.shape[1]
X=orig_data[:,0:cols-1]#参数
y=orig_data[:,cols-1:cols]#标签

threta=np.zeros([1,3])


def model(X, theta):
    return sigmoid(np.dot(X, theta.T))
#定义损失函数
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1 - y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / (len(X))
#计算梯度
def gradient(X,y,theta):
    grad=np.zeros(threta.shape)
    error=(model(X,threta)-y).ravel()
    for j in range(len(theta.ravel())):  # for each parmeter
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)

    return grad

STOP_ITER = 0
STOP_COST = 1
STOP_GRAD = 2

def stopCriterion(type, value, threshold):
    #设定三种不同的停止策略
    if type == STOP_ITER:        return value > threshold
    elif type == STOP_COST:      return abs(value[-1]-value[-2]) < threshold
    elif type == STOP_GRAD:      return np.linalg.norm(value) < threshold

import numpy.random
#洗牌
def shuffleData(data):
    np.random.shuffle(data)
    cols=data.shape[1]
    X=data[:,0:cols-1]
    y=data[:,cols-1:]
    return X,y

import time
def descent(data,threta,batchSize,stopType,thresh,alpha):
    #梯度下降求解
    init_time=time.time()
    i=0
    k=0
    X,y=shuffleData(data)
    grad=np.zeros(threta.shape)
    costs=[cost(X,y,threta)]

    while True:
        grad=gradient(X[k:k+batchSize],y[k:k+batchSize],threta)
        k=batchSize+k
        if k>=n:
            k=0
            X,y=shuffleData(data)
        threta=threta-alpha*grad
        costs.append(cost(X,y,threta))
        i=i+1

        if stopType == STOP_ITER:
            value = i
        elif stopType == STOP_COST:
            value = costs
        elif stopType == STOP_GRAD:
            value = grad
        if stopCriterion(stopType, value, thresh): break

    return threta, i - 1, costs, grad, time.time() - init_time

def runExpe(data, theta, batchSize, stopType, thresh, alpha):
    #import pdb; pdb.set_trace();
    theta, iter, costs, grad, dur = descent(data, theta, batchSize, stopType, thresh, alpha)
    name = "Original" if (data[:,1]>2).sum() > 1 else "Scaled"
    name += " data - learning rate: {} - ".format(alpha)
    if batchSize==n: strDescType = "Gradient"
    elif batchSize==1:  strDescType = "Stochastic"
    else: strDescType = "Mini-batch ({})".format(batchSize)
    name += strDescType + " descent - Stop: "
    if stopType == STOP_ITER: strStop = "{} iterations".format(thresh)
    elif stopType == STOP_COST: strStop = "costs change < {}".format(thresh)
    else: strStop = "gradient norm < {}".format(thresh)
    name += strStop
    print ("***{}\nTheta: {} - Iter: {} - Last cost: {:03.2f} - Duration: {:03.2f}s".format(
        name, theta, iter, costs[-1], dur))
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(np.arange(len(costs)), costs, 'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title(name.upper() + ' - Error vs. Iteration')
    return theta

#选择的梯度下降方法是基于所有样本的
n=10
runExpe(orig_data, threta, 100, STOP_GRAD, thresh=500000, alpha=0.000001)
plt.show()