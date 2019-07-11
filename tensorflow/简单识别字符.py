import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import tensorflow as tf
mnist=read_data_sets(train_dir='MNIST_data',one_hot=True)
print(mnist[0])

batch_size=50
n_batch=mnist.train.num_examples//batch_size

x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])

#插件一个简单的神经网络
W1=tf.Variable(tf.zeros([784,10]))
b1=tf.Variable(tf.zeros([10]))
L1=tf.nn.sigmoid(tf.matmul(x,W1)+b1)

#第二层网络
W2=tf.Variable(tf.zeros([400,10]))
b2=tf.Variable(tf.zeros([10]))
prediction=tf.nn.softmax(tf.matmul(x,W1)+b1)
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))

trainstep=tf.train.AdadeltaOptimizer(0.02).minimize(loss)

init=tf.global_variables_initializer()

correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))

accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(100):
        for batch in range(n_batch):
            batch_x,batch_y=mnist.train.next_batch(batch_size)
            sess.run(trainstep,feed_dict={x:batch_x,y:batch_y})

        acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print('Iter'+str(epoch)+',accuracy'+str(acc))

