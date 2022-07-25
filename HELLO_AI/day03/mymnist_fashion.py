# 필요한 라이브러리 불러오기
import cv2
from keras import layers
from keras import models
from keras.datasets import fashion_mnist
from keras.utils import to_categorical

import numpy as np

# 1. Fashion MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

cv2.imshow('fashion', train_images[0])
cv2.waitKey(0)
print("train_labels[0]", train_labels[0])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels, epochs=5, batch_size=128)

predict_result = model.predict(train_images)

ai_answer = np.argmax(predict_result[0])

print("ai_answer",ai_answer)