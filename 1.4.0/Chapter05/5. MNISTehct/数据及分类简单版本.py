# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 08:47:23 2019

@author: Administrator
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

#输入训练集
mnist=input_data.read_data_sets(r'C:\Users\Administrator\OneDrive\MyPython\datasets\MNIST_data',one_hot=True)

#每个批次的大小
batch_size=100
#计算一共多少个批次
n_batch=int(mnist.train.num_examples/batch_size)

x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])

#创建一个简单的神经网络
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
prediction=tf.nn.softmax(tf.matmul(x,w)+b)

regularizer = tf.contrib.layers.l2_regularizer(0.001)

#二次代价函数
loss=tf.reduce_mean(tf.square(y-prediction))+regularizer(w)
train_step=tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化变量
init=tf.global_variables_initializer()

correction_prediction=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中的最大值所在的位置
accuracy=tf.reduce_mean(tf.cast(correction_prediction,tf.float32))#将bool量转化为0和1的float量

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        
        acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        tf.add_to_collection("acc",acc)
        tf.add_to_collection('steps',epoch)
        
        print('After %d trains ,testaccuracy is %g'%(epoch,acc))
   
    drawAcc=tf.get_collection('acc')
    drawSteps=tf.get_collection('steps')   
    plt.plot(drawSteps,drawAcc,c='r')
#    plt.plot(drawSteps,1-drawAcc,c='g')
    plt.show()
tf.reset_default_graph()
