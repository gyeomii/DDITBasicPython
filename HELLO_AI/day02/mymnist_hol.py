# 필요한 라이브러리 불러오기
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images_a = [
    [1,0,1,0],
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,0]
    ]

train_labels_a = [
    0,1,1,0
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c", train_labels_c)

model = models.Sequential()
model.add(layers.Dense(10, activation='relu', input_shape=(4,)))
model.add(layers.Dense(2, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=20, batch_size=4)

predict_result = model.predict(train_images)
print("predict_result", predict_result)