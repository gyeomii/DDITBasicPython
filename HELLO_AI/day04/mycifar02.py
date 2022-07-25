import numpy as np
import cv2
import tensorflow
from tensorflow import keras
from keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
cifar_test_images = test_images
cifar_test_labels = test_labels
 
train_images = train_images.reshape((50000, 32, 32, 3))
test_images = test_images.reshape((10000, 32, 32, 3)) 
 
train_images = train_images/255.0
test_images = test_images/255.0
 
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
 
model.fit(train_images, train_labels, epochs=10)
 
test_loss, test_acc = model.evaluate(test_images, test_labels)
 
print('Test accuracy:', test_acc)
 
predict_result = model.predict(test_images)

for idx, label in enumerate(cifar_test_labels):
    ai_label = np.argmax(predict_result[idx])
    if(label == ai_label):
        filename = f"test/o/{label[0]}_{ai_label}_{idx}.png"
        cv2.imwrite(filename, cifar_test_images[idx])
    else:
        filename = f"test/x/{label[0]}_{ai_label}_{idx}.png"
        cv2.imwrite(filename, cifar_test_images[idx])