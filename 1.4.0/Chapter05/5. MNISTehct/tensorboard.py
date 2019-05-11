# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:39:56 2019

@author: Administrator
"""

import tensorflow as tf
with tf.name_scope('input1'):
    input1=tf.constant([1.0,2.0,3.0],name="input1")
with tf.name_scope('input2'):
    input2=tf.Variable(tf.random_uniform([3]),name="input2")
output=tf.add_n([input1,input2],name="add")
writer=tf.summary.FileWriter(r"D:\InstalledList\anaconda3\Scripts",tf.get_default_graph())
writer.close()
