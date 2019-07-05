import tensorflow as tf
import numpy as np

x_data=np.random.rand(100)
y_data=0.1*x_data+0.2

k=tf.Variable(0.)
b=tf.Variable(0.)
y=k*x_data+b
loss=tf.reduce_mean(tf.square(y_data-y))
#定义一个学习器
optimiter=tf.train.GradientDescentOptimizer(0.2)

train=optimiter.minimize(loss)

#初始化变量
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(20000):
        sess.run(train)
        if(i%10==0):
            print(i,sess.run([k,b]))

