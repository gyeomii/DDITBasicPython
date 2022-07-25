# 필요한 라이브러리 불러오기
import cv2
from keras import layers
from keras import models
from keras.datasets import fashion_mnist
from keras.utils import to_categorical

import numpy as np
# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for idx, label in enumerate(train_labels):
    fileRoute = f"train/{label}/{idx}.png"
    cv2.imwrite(fileRoute, train_images[idx])
    print(fileRoute)