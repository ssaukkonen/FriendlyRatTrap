import tensorflow
import numpy as np
import tensorflow as tf
from numpy import asarray
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



data_dir = "Projektikuvat"
# Ja tähän sitten kuvien lukeminen tiedostosta.
directory = data_dir
nPictures = 380                # Total number of pictures
split = 0.2                   # 20% test and 80 % training data
nTraining = (int)((1-split)*nPictures) 
nValidation = (int)(split*nPictures)

training_data = tf.keras.preprocessing.image_dataset_from_directory(
directory,                # juurihakemisto, jonka alta löytyy kunkin dataluokan omat hakemistot
batch_size=(nTraining),     # data jaetaan tämän kokoisin batcheihin.
color_mode="grayscale",
shuffle=True,
seed=1,
validation_split = split, # tämän arvo = 0.2
subset = 'training',      # tämä kertoo, että tällä kertaa datasta otetaan 80% eli yksi batch
image_size=(320, 240)
)
x_train = np.zeros((nTraining,320,240,1))
y_train = np.zeros(nTraining)
for image, label in training_data:
    for i in range(nTraining):
        x_train[i,:,:,:] = image[i].numpy().astype('uint8')
        y_train[i]=label[i].numpy().astype('uint8')

validation_data = tf.keras.preprocessing.image_dataset_from_directory(
directory,                # juurihakemisto, jonka alta löytyy kunkin dataluokan omat hakemistot
batch_size=nValidation,     # data jaetaan tämän kokoisin batcheihin.
color_mode="grayscale",
shuffle=True,
seed=2,
validation_split = split, # tämän arvo = 0.2                                                   
subset = 'validation',      # tämä kertoo, että tällä kertaa datasta otetaan 80% eli yksi batch
image_size=(320, 240)
)

x_test = np.zeros((nValidation,320,240,1))
y_test = np.zeros(nValidation)
for image, label in validation_data:
    for i in range(nValidation):
        x_test[i,:,:,:] = image[i].numpy().astype('uint8')
        y_test[i]=label[i].numpy().astype('uint8')



print(x_train.shape)
print(x_test.shape)



# determine the shape of the input images
in_shape = x_train.shape[1:]
# determine the number of classes
n_classes = len(unique(y_train))

print(in_shape, n_classes)
# normalize pixel values
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0



########################################
# 5 step process step 1: Define model
########################################
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', input_shape=in_shape))
model.add(MaxPool2D((2, 2)))
model.add(Conv2D(16, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(MaxPool2D((2, 2)))
model.add(Flatten())
model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
#model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='sigmoid'))
#######################################
# 5 step process step 2: Compile model (define loss and optimizer)
#######################################
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#######################################
# 5 step process step 3: Fit the model = train model
#######################################

model.fit(x_train, y_train, epochs=20, batch_size=10, verbose=2)
#######################################
# 5 step process step 4: Evaluate the model
#######################################
loss, acc = model.evaluate(x_test, y_test, verbose=2)
print('Accuracy: %.3f' % acc)

#######################################
# 5 step process: Make a prediction
#######################################
#model.save('Model/my_model1') #Perusformatti
model.save('Model\my_model.h5') #HDF5 Formatti


for i in range(10):
  plt.figure(1)
  image = x_test[i]
  yhat = model.predict(asarray([image]))
  print((y_test[i]+1))
  print('Predicted: class=%d' % (argmax(yhat)+1))
  plt.imshow(image[:,:,0])
  plt.show()
print(model.summary())