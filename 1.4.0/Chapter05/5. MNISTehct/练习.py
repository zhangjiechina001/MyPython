# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:55:04 2019

@author: JEE-zhangjie
"""

import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data

#MNIST数据集相关参数
INPUT_NODE=784
OUT_NODE=10

#配置神经网络的参数
LAYER1_NOdE=500
BATCH_SIZE=100

LEARNING_RATE_BASE=0.8
LEARNING_DECAY=0.99
REGULARZTION_RATE=0.0001
TRAIN_STEPS=3000
MOVING_AVERAGE_DECAY=0.99



def inference(input_tensor,avg_class,weights1,biases1,weights2,biases2):
    #如果没有提供滑动平均损失的话
    if(avg_class==None):
        layer1=tf.nn.relu(tf.matmul(input_tensor,weights1)+biases1)
        
        return tf.matmul(layer1,weights2)+biases2
    else:
        layer1=tf.nn.relu(tf.matmul(input_tensor,avg_class.average(weights1)
        +avg_class.average(biases1)))
    return tf.matmul(layer1,avg_class.average(weights2)
                     +avg_class.average(biases2))

tf.reset_default_graph()
def train(mnist):
    x=tf.placeholder(tf.float32,[None,INPUT_NODE],name='x-input')
    y_=tf.placeholder(tf.float32,[None,OUT_NODE],name='y-output')
    
    weights1=tf.Variable(tf.truncated_normal([INPUT_NODE,LAYER1_NOdE],stddev=0.1))
    biases1=tf.Variable(tf.constant(0.1,shape=[LAYER1_NOdE]))
#    tf.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)       
#    从截断的正态分布中输出随机值。 shape表示生成张量的维度，mean是均值，stddev是标准差。
#    这个函数产生正太分布，均值和标准差自己设定。这是一个截断的产生正太分布的函数，
#    就是说产生正太分布的值如果与均值的差值大于两倍的标准差，那就重新生成。和一般的正太分布的产生随机数据比起来，
#    这个函数产生的随机数与均值的差距不会超过两倍的标准差，但是一般的别的函数是可能的。

    weights2=tf.Variable(tf.truncated_normal([LAYER1_NOdE,OUT_NODE],stddev=0.1))
    biases2=tf.Variable(tf.constant(0.1,shape=[OUT_NODE]))
    
    y=inference(x,None,weights1,biases1,weights2,biases2)
    
    global_step=tf.Variable(0,trainable=False)
    
    variable_averages=tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    
    variable_averages_op=variable_averages.apply(tf.trainable_variables())
    
    average_y=inference(x,variable_averages,weights1,biases1,weights2,biases2)
    
    cross_entropy=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,labels=tf.argmax(y_,1))

    cross_entropy_mean=tf.reduce_mean(cross_entropy)

    regularizer=tf.contrib.layers.l2_regularizer(REGULARZTION_RATE)
    
    regularization=regularizer(weights1)+regularizer(weights2)
    
    loss=cross_entropy_mean+regularization
    
    learning_rate=tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,
                                             mnist.train.num_examples/BATCH_SIZE,
                                             LEARNING_DECAY)
    
    train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step)
    
    with tf.control_dependencies([train_step,variable_averages_op]):
        train_op=tf.no_op(name='train')
        
    correct_prediction=tf.equal(tf.argmax(average_y,1),tf.argmax(y_,1))
    
    accuracy=tf.reduce_mean(tf.cast(correct_prediction ,tf.float32))
    
    with tf.Session() as sess:
        validate_feed={x:mnist.validation.images,
                       y_:mnist.validation.labels}
        
        test_feed={x:mnist.test.images,
                   y_:mnist.test.labels}
        
        for i in range(TRAIN_STEPS):
            
            xs,ys=mnist.train.next_batch(BATCH_SIZE)
#            sess.run(xs)
            sess.run(train_op,feed_dict={x:xs,y_:ys})
            if i%1000==0:
                validate_acc=sess.run(accuracy,feed_dict=validate_feed)
                
                print("After %d trains ,testaccuracy is %g"%(i,validate_acc))
        test_acc=sess.run(accuracy,feed_dict=test_feed)
        print("After %d trains ,testaccuracy is %g"%(TRAIN_STEPS,test_acc))
        
def main(argv=None):
    mnist=mnist=input_data.read_data_sets(r'C:\Users\Administrator\OneDrive\MyPython\datasets\MNIST_data',one_hot=True)
    train(mnist)
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    