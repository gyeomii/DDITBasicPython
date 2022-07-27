# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
import numpy as np
from keras.utils.np_utils import to_categorical

train_images_a = [
    [1,0,0], #가위
    [0,1,0], #바위
    [0,0,1]  #보
]

train_labels_a = [
    1, 2, 0 #바위, 보, 가위
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c", train_labels_c)

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(3,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=100, batch_size=6)

predict_result = model.predict(train_images)

model.save('mnist_gawi.h5')
