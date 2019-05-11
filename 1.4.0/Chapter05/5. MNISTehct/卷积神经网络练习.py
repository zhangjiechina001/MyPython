# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:54:37 2019

@author: Administrator
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#输入训练集
mnist=input_data.read_data_sets(r'C:\Users\Administrator\OneDrive\MyPython\datasets\MNIST_data',one_hot=True)
#每个批次的大小
batch_size=100
#计算一共有多少批次
n_batch=mnist.train.num_examples//batch_size

#初始化权值
def weight_variable(shape):
    inital=tf.truncated_normal(shape,stddev=0.1)#生成一个截断的正态分布
    return tf.Variable(inital)

def biase_variable(shape):
    biase=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(biase)

#定义卷积层操作[batch,height,width,channels ]
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding="SAME")

def max_pool_4(x):
    #ksize为窗口大小，1,2两个参数有用
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])

#-1代表批次，1代表通道为1
x_image=tf.reshape(x,[-1,28,28,1])

#初始化第一个卷积层和偏执，5，5未采样窗口，1位通道，32位卷积核个数
W_convl=weight_variable([5,5,1,32])
b_convl=weight_variable([32])

#把x_image和权值向量进行卷积
h_conve1=tf.nn.relu(conv2d(x_image,W_convl)+b_convl)
h_pool1=max_pool_4(h_conve1)

#把28*28的图片第一次卷积后大小不变
W_conv2=weight_variable([5,5,32,64]) 
b_conv2=biase_variable([64])

#把池化层
h_conve2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
h_pool2=max_pool_4(h_conve2)

#全连接层，定义连接层1参数，偏执参数
W_fc1=weight_variable([7*7*64,10])
b_fc1=biase_variable([10])

#把输出的二维图像转化为一位数组，前面-1的参数就是生成7*7*64列的数组
h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64])
h_fc1=tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)

keep_prob=tf.placeholder(tf.float32)
h_fc1_drop=tf.nn.dropout(h_fc1,keep_prob)
prediction=tf.nn.softmax(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)
#第二层全连接层
W_fc2=weight_variable([1024,10])
b_fc2=biase_variable([10])
#计算输出
#prediction=tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

#交叉熵可以知道预测值和实际值的相关程度
cross_entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
train_step=tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)
correct_prediction=tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            #0.7为丢弃70%的神经元
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7})
            
        acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels,keep_prob:1.0})
        print("after %d trainings,Testaccuracy is %g" %(epoch,acc))
