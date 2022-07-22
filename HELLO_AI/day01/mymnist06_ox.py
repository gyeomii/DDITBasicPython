# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

google_train_label = train_labels

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

"""
epochs : 학습 횟수, batch_size : 전체 데이터를 그룹화 할 때 한 그룹의 데이터 수
"""
model.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('test_acc: ', test_acc, 'test_loss:', test_loss)     

predict_result = model.predict(train_images)


cnt_o = 0
cnt_x = 0

for idx, label in enumerate(google_train_label):
    ai_label = np.argmax(predict_result[idx])
    
    if(label == ai_label):
        cnt_o += 1
    else:
        cnt_x += 1

corr = (cnt_o / 60000)
worng = (cnt_x / 60000)
print(f"correct :{cnt_o}, wrong : {cnt_x}, count All : {cnt_o + cnt_x}")
print(f"correct : {corr} , worng : {worng}")

