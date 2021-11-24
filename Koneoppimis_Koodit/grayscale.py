import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Testikuvat\image.jpg',cv2.IMREAD_COLOR)
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result=cv2.imwrite('Testikuvat\gray_image.png', grayscale)

'''
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(grayscale)

plt.show()
'''