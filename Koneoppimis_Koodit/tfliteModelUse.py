import numpy as np
import tensorflow as tf
from PIL import Image

# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="Model/model_1.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test the model on random input data.
floating_model = input_details[0]['dtype'] == np.float32
input_shape = input_details[0]['shape']
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]
img = Image.open('Testikuvat/nettikuva1.jpg').resize((width, height))
print(img)
input_data = np.expand_dims(img, axis=0)
print(np.shape(input_data))
if floating_model:
    input_data = (np.float32(input_data) - 127.5) / 127.5
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data[0])
results=np.squeeze(output_data)
#print(results)
top_k = results.argsort()[-5:][::-1]
#print(top_k)

if top_k[0]==0:
    print("se on hiiri")
if top_k[1]==0:
    print("joku muu kuin hiiri")    