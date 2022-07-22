# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

google_train_label = train_labels
google_train_image = train_images

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
arr0 = [0,0,0,0,0, 0,0,0,0,0]
arr1 = [0,0,0,0,0, 0,0,0,0,0]
arr2 = [0,0,0,0,0, 0,0,0,0,0]
arr3 = [0,0,0,0,0, 0,0,0,0,0]
arr4 = [0,0,0,0,0, 0,0,0,0,0]
arr5 = [0,0,0,0,0, 0,0,0,0,0]
arr6 = [0,0,0,0,0, 0,0,0,0,0]
arr7 = [0,0,0,0,0, 0,0,0,0,0]
arr8 = [0,0,0,0,0, 0,0,0,0,0]
arr9 = [0,0,0,0,0, 0,0,0,0,0]
for idx, label in enumerate(google_train_label):
    ai_label = np.argmax(predict_result[idx])
    if(label == ai_label):
        continue
    else:
        if(label == 0):
            arr0[ai_label] += 1
        elif(label == 1):
            arr1[ai_label] += 1
        elif(label == 2):
            arr2[ai_label] += 1
        elif(label == 3):
            arr3[ai_label] += 1
        elif(label == 4):
            arr4[ai_label] += 1
        elif(label == 5):
            arr5[ai_label] += 1
        elif(label == 6):
            arr6[ai_label] += 1
        elif(label == 7):
            arr7[ai_label] += 1
        elif(label == 8):
            arr8[ai_label] += 1
        elif(label == 9):
            arr9[ai_label] += 1

print("0",arr0)
print("1",arr1)
print("2",arr2)
print("3",arr3)
print("4",arr4)
print("5",arr5)
print("6",arr6)
print("7",arr7)
print("8",arr8)
print("9",arr9)