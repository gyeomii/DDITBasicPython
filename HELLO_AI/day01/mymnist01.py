# 필요한 라이브러리 불러오기
import cv2
from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils import to_categorical


# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

for idx, img in enumerate(train_images):
    filename = 'train/'+str(idx)+'.png'
    cv2.imwrite(filename, img)
