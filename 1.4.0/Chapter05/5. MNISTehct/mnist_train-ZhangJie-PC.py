import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_inference
import os
import mnist_eval

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.3
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 5000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH="MNIST_model/"
MODEL_NAME="mnist_model"


def train(mnist):

    x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)#传入一个可以填充参数的方法
    y = mnist_inference.inference(x, regularizer)
    global_step = tf.Variable(0, trainable=False)


    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variables_averages_op = variable_averages.apply(tf.trainable_variables())
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        mnist.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY,
        staircase=True)
    '''tf.train.exponential_decay(
    learning_rate,初始学习率
    global_step,当前迭代次数
    decay_steps,衰减速度（在迭代到该次数时学习率衰减为earning_rate * decay_rate）
    decay_rate,学习率衰减系数，通常介于0-1之间。
    staircase=False,(默认值为False,当为True时，（global_step/decay_steps）则被转化为整数) ,选择不同的衰减方式。
    name=None
    decayed_learning_rate = learning_rate * decay_rate ^ (global_step / decay_step)'''
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')


    saver = tf.train.Saver()
    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        for i in range(TRAINING_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)

            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})
            if i % 1000 == 0:
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)

def main(argv=None):
    mnist = input_data.read_data_sets("F:\\Users\\JEE-zhangjie\\OneDrive\\MyPython\\1.4.0\\Chapter05\\5. MNISTehct\\MNIST_model", one_hot=True)
    train(mnist)
    mnist_eval.evaluate(mnist)
    exit()

if __name__ == '__main__':
    main()
#    tf.app.run()

    

   


