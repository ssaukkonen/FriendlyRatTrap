import numpy as np
import tensorflow as tf
from numpy import unique
from numpy import argmax
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
import matplotlib.pyplot as plt

old_model = tf.keras.models.load_model('Model\my_model.h5')
#new_model.summary()


converter = tf.lite.TFLiteConverter.from_keras_model(old_model)
tflite_model = converter.convert()
with open('Model\model.tflite', 'wb') as f:
  f.write(tflite_model)