import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#变成200行一列的数据
x_data=np.linspace(-1,1,1000)[:,np.newaxis]
noise=np.random.normal(0,0.01,x_data.shape)
y_data=np.square(x_data)+noise

#定义两个placeholder
x=tf.placeholder(tf.float32,[None,1])
y=tf.placeholder(tf.float32,[None,1])

#定义神经网络中间层
weight_1=tf.Variable(tf.random_normal([1,10]))
biases_1=tf.Variable(tf.zeros([1,10]))
Wx_plus_b_l1=tf.matmul(x,weight_1)+biases_1
#第一层的输出
L1=tf.nn.softmax(Wx_plus_b_l1)

#定义神经网络输出层
weight_2=tf.Variable(tf.random_normal([10,1]))
biases_2=tf.Variable(tf.zeros([1,1]))
Wx_plus_b_l2=tf.matmul(L1,weight_2)+biases_2
prediction=Wx_plus_b_l2

loss=tf.reduce_mean(tf.square(y-prediction))
#使用梯度下降法
train_step=tf.train.GradientDescentOptimizer(0.3).minimize(loss)

with tf.Session() as sess:
    #变量初始化
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})
        #获得预测值
        if(i%100==0):
            print('after %s trains'%str(i))
    prediction_val=sess.run(prediction,feed_dict={x:x_data})
    #预测结果
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction_val,'r-',lw=5)
    plt.show()