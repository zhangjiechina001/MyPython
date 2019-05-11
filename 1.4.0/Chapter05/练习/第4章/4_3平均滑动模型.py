import tensorflow as tf
#定义一个变量用于计算滑动平均，这个变量的初始值为0
v1=tf.Variable(0,dtype=tf.float32)
#setp为变量模拟神经网络中迭代的轮数，可以用于动态控制衰减率
step=tf.Variable(0,trainable=False)

ema=tf.train.ExponentialMovingAverage(0.99,step)
#定义一个更新变量华东平均的操作。这里需要给的一个列表，每次执行这个操作时，这个列表都会被更新
maintain_average_op=ema.apply([v1])

with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)

    print(sess.run([v1,ema.average(v1)]))
    #更新变量v1的值到5
    sess.run(tf.assign(v1,5))

    sess.run(maintain_average_op)

    print(sess.run([v1,ema.average(v1)]))

    sess.run(tf.assign(step,10000))

    sess.run(tf.assign(v1,10))

    sess.run(maintain_average_op)
    print(sess.run([v1,ema.average(v1)]))

    sess.run(maintain_average_op)
    print(sess.run([v1,ema.average(v1)]))

    sess.run