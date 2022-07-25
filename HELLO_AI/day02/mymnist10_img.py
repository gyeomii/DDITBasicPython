from keras import layers
from keras import models
from keras.datasets import mnist
from keras_preprocessing import image
import numpy as np
import cv2

img = cv2.imread('0_0_1.png')
train_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
train_image = train_image.reshape((1,784))
print(train_image.shape)

model = models.load_model('mnist.h5')

predict_result = model.predict(train_image)

ai_answer = np.argmax(predict_result[0])
print("ai_answer", ai_answer)