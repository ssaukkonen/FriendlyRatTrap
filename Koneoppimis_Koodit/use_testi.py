import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
import matplotlib.pyplot as plt
import cv2
from PIL import Image

old_model = tf.keras.models.load_model('Model\my_model.h5')
#new_model.summary()

converter = tf.lite.TFLiteConverter.from_keras_model(old_model)
tflite_model = converter.convert()
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()#get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()# Read the image and decode to a tensor

#OpenCV jutut jotka ei oikein toimi

#img = np.zeros((240,320,1))
#img[:,:,0]=cv2.imread('Testikuvat\gray_image.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('Testikuvat\gray_image.png', cv2.IMREAD_GRAYSCALE)
jakaja = np.ones((240,320))*255
img=np.divide(img,jakaja)
#print(img)
print(np.shape(img))
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img,(240,320))#Preprocess the image to required size and cast
input_shape = input_details[0]['shape']

'''
PIL, ei toimi kyl kans oikein
im_frame = Image.open('Testikuvat\gray_image.png')
img = np.array(im_frame.getdata())
img = np.reshape(img,(240,320))
print(np.shape(img))
'''
#input_tensor = np.zeros((1,240,320,1))
#input_tensor[0,:,:,:]=img
input_tensor= np.array(np.expand_dims(img,(0)), dtype=np.float32)#set the tensor to point to the input data to be inferred
#input_tensor= np.array(np.expand_dims(img,3), dtype=np.float32)
input_tensor2=np.expand_dims(input_tensor, axis=3)


#input_tensor2=np.divide
print(np.shape(input_tensor2))
print(input_tensor2)
#print(np.shape(input_tensor2))
#print(input_tensor2)


input_index = interpreter.get_input_details()[0]["index"]
interpreter.set_tensor(input_index, input_tensor2)#Run the inference
interpreter.invoke()
output_details = interpreter.get_output_details()[0]

output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)