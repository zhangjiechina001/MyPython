import tensorflow as tf
a=tf.constant(3.0,dtype=tf.float32,name='a')
b=tf.constant(4.0,dtype=tf.float32,name='b')
total=a+b
print(total)
sess=tf.Session()
print(tf.__version__)