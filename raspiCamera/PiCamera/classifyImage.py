from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

#from PIL import Image
from tflite_runtime.interpreter import Interpreter

class ClassifyImage:
    def __init__(self):
        self.interpreter = Interpreter('Model/model_1.tflite')
        self.interpreter.allocate_tensors()
        _, self.height, self.width, _ = self.interpreter.get_input_details()[0]['shape']

    def set_input_tensor(self, image):
        tensor_index = self.interpreter.get_input_details()[0]['index']
        input_tensor = self.interpreter.tensor(tensor_index)()[0]
        input_tensor[:, :] = image


    def classify_image(self, image, top_k=1):
        """Returns a sorted array of classification results."""
        self.set_input_tensor(image)
        self.interpreter.invoke()
        output_details = self.interpreter.get_output_details()[0]
        output = np.squeeze(self.interpreter.get_tensor(output_details['index']))

        # If the model is quantized (uint8 data), then dequantize the results
        if output_details['dtype'] == np.uint8:
            scale, zero_point = output_details['quantization']
            output = scale * (output - zero_point)

        ordered = np.argpartition(-output, top_k)
        return [(i, output[i]) for i in ordered[:top_k]]