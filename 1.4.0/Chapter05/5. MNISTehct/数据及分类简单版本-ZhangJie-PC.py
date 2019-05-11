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
w=tf.Variable(tf.truncated_normal([784,500], stddev=0.1))
b=tf.Variable(tf.truncated_normal([500], stddev=0.1))
w1=tf.Variable(tf.truncated_normal([500,10], stddev=0.1))
b1=tf.Variable(tf.truncated_normal([10], stddev=0.1))
temp=tf.nn.tanh(tf.matmul(x,w)+b)
prediction=tf.nn.softmax(tf.matmul(temp,w1)+b1)
global_step=tf.Variable(0,trainable=False)

regularizer=tf.contrib.layers.l2_regularizer(0.0001)

regularization=regularizer(w)+regularizer(w1)



#二次代价函数
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))

learning_rate = tf.train.exponential_decay(
    0.1,
    global_step,
    mnist.train.num_examples / batch_size, 
    0.99,
    staircase=True)
train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)

#初始化变量
init=tf.global_variables_initializer()

correction_prediction=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))#argmax返回一维张量中的最大值所在的位置
accuracy=tf.reduce_mean(tf.cast(correction_prediction,tf.float32))#将bool量转化为0和1的float量

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(20):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            sess.run([train_step,global_step],feed_dict={x:batch_xs,y:batch_ys})

        
        acc,learningrate=sess.run([accuracy,learning_rate],feed_dict={x:mnist.test.images,y:mnist.test.labels})
        tf.add_to_collection("acc",acc)
        tf.add_to_collection('steps',epoch)
        
        print('After %d trains ,testaccuracy is %g,learningrate is %g'%(epoch,acc,learningrate))
   
    drawAcc=tf.get_collection('acc')
    drawSteps=tf.get_collection('steps')   
    plt.plot(drawSteps,drawAcc,c='r')
#    plt.plot(drawSteps,1-drawAcc,c='g')
    plt.show()
tf.reset_default_graph()
