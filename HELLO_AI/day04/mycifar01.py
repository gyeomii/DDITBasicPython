import cv2
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models

import matplotlib.pyplot as plt
import numpy as np


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
print('train_images', train_images.shape)
print('train_labels', train_labels.shape)
print('test_images', test_images.shape)
print('test_labels', test_labels.shape)

for idx, label in enumerate(train_labels):
    fileRoute = f"train/{label[0]}/{idx}.png"
    cv2.imwrite(fileRoute, train_images[idx])
    print(fileRoute)