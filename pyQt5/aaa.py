# encoding=utf-8

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding

from keras.utils import plot_model

model = Sequential()
model.add(Embedding(input_dim=1024, output_dim=256, input_length=50))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

plot_model(model, to_file='model_test.png', show_shapes=True)
