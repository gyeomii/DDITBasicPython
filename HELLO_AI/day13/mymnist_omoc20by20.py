# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
import numpy as np
from keras.utils.np_utils import to_categorical

train_images = np.load("omok_train2.npy")

train_labels = np.load("omok_answer2.npy")

train_labels_c = to_categorical(train_labels, num_classes=400)
print("train_labels_c", train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(400,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(400, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=25)

predict_result = model.predict(train_images)
print(predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    ii = int(ai_answer/20)
    jj = ai_answer%20
    print(ai_answer,ii,jj,end=",")
    print()

model.save('alphao.h5')