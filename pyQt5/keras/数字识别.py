import cv2
import tensorflow as tf
import keras
import os
os.environ["PATH"] += os.pathsep + r'F:\Program Files (x86)\Graphviz2.38\bin'
categories = ['Dog', 'Cat']


def prepare(path):
    img_size = 28
    img_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    w,h=img_array.shape
    img_array=img_array[:,0:15]
    cv2.imshow('temp',img_array)

    new_array = cv2.resize(img_array, (img_size, img_size))
    cv2.imshow('5',new_array)
    cv2.waitKey()
    return new_array.reshape(-1, img_size, img_size,1)

num5=cv2.imread('5.png',cv2.IMREAD_GRAYSCALE)
num5=cv2.resize(num5,(28,28))
num5=num5.reshape(-1,1,28,28)
model = keras.models.load_model('CNNModel.h5')
from keras.utils import plot_model
plot_model(model,to_file='model.jpg')
prediction = model.predict([prepare('0__10.jpg')])

print(prediction)