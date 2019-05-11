# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 08:47:23 2019

@author: Administrator
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy
#输入训练集
mnist=input_data.read_data_sets(r'C:\Users\Administrator\OneDrive\MyPython\datasets\MNIST_data',one_hot=True)

#每个批次的大小
batch_size=50
#计算一共多少个批次
n_batch=int(mnist.train.num_examples/batch_size)

with tf.name_scope('input'):
    x=tf.placeholder(tf.float32,[None,784],name='x-input')
    y=tf.placeholder(tf.float32,[None,10],name='y-input')
    keep_prob=tf.placeholder(tf.float32)

#创建一个简单的神经网络
with tf.name_scope('layer'):
    w=tf.Variable(tf.zeros([784,10]))
    b=tf.Variable(tf.zeros([10]),name='bb')
    L1=tf.matmul(x,w)+b

prediction=tf.nn.softmax((tf.matmul(x,w)+b))


#二次代价函数
loss=tf.reduce_mean(tf.square(y-prediction))
train_step=tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化变量
with tf.name_scope('init'):
    init=tf.global_variables_initializer()
    
with tf.name_scope('accuracy'):
    correction_prediction=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中的最大值所在的位置
    accuracy=tf.reduce_mean(tf.cast(correction_prediction,tf.float32))#将bool量转化为0和1的float量

with tf.Session() as sess:
    
    sess.run(init)
    train_writer = tf.summary.FileWriter(r"C:\Users\Administrator\AppData\Local\conda\conda\envs\tensorflow\Scripts",sess.graph)       
    for i in range(1,2):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:1.0})
        acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})   
#        train_writer.add_summary(a)
        print('After %d trains ,testaccuracy is %g' % (i,acc))
        tf.add_to_collection("acc",acc)
        tf.add_to_collection('steps',i)
        
    drawAcc=tf.get_collection('acc')
    drawSteps=tf.get_collection('steps')

    fig=plt.figure()
    matra=numpy.ones(len(drawSteps))
    arrar=matra-drawAcc

    ax1=fig.add_subplot(111)
    ax1.plot(drawSteps,drawAcc,c='r')
    ax1.set_title('Value-Loss')
    ax1.set_ylabel('Y Values for Accuracy')
    ax1.annotate('my loss_accuracy', xy = (2, 0.83), xytext = (2,0.85) )
    ax2=ax1.twinx()
    ax2.plot(drawSteps,arrar,c='r')
    ax2.set_ylabel('Y Values for Loss')

tf.reset_default_graph()
