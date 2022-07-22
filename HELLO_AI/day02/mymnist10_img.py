from keras import layers
from keras import models
from keras.datasets import mnist
from keras_preprocessing import image

import numpy as np


test_image = image.load_img('0_0_1.png')

model = models.load_model('mnist.h5')

predict_result = model.predict(test_image)

ai_answer = np.argmax(predict_result[0])
print("ai_answer", ai_answer)