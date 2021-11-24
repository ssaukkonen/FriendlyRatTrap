import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
from numpy import asarray

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="Model\model_1.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on random input data.
input_shape = input_details[0]['shape']
img = cv2.imread('Testikuvat\image.jpg')
img = cv2.resize(img,(224,224))
img = np.expand_dims(img, axis=0)
#img = Image.open('Testikuvat\image.jpg')
#numpydata = asarray(img, dtype=np.float32)
#numpydata2 = np.expand_dims(numpydata, axis=0)
#print(np.shape(numpydata))

input_data = img
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)