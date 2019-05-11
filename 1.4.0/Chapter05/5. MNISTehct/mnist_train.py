import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_inference
import os
import matplotlib.pyplot as plt

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 3000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH="MNIST_model/"
MODEL_NAME="mnist_model"

xs=[0,0]
ys=[0,0]
def train(mnist):

    tf.reset_default_graph()
    x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    y = mnist_inference.inference(x, regularizer)
    global_step = tf.Variable(0, trainable=False)


    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
#    tf.trainable_variables返回的是需要训练的变量列表
    variables_averages_op = variable_averages.apply(tf.trainable_variables())
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        mnist.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY,
        staircase=True)
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

#    gapreset=tf.reset_default_graph()
#    saver = tf.train.Saver()
    with tf.Session() as sess:
        
        tf.global_variables_initializer().run()

        for i in range(TRAINING_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})
            if i % 50 == 0:
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                tf.add_to_collection('x',step)
                tf.add_to_collection('y',loss_value)
#                 xs[0]=xs[1]

    x=tf.get_collection('x')
    y=tf.get_collection('y')
#    print(w)
    plt.plot(x,y)


def main(argv=None):
    mnist = input_data.read_data_sets(r'C:\Users\Administrator\OneDrive\MyPython\datasets\MNIST_data',one_hot=True)
    train(mnist)

if __name__ == '__main__':
    main()

   


