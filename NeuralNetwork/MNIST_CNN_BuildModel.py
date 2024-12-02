# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from tensorflow import keras as kr
#import matplotlib as plt
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models, losses
import os
import datetime
import numpy as np

import pandas as pd
import math 
import itertools

from sklearn.metrics import confusion_matrix

# def plot_confusion_matrix(cm, classes,
#                           normalize=False,
#                           title='Confusion matrix',
#                           cmap=plt.cm.Blues):
    
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=90)
#     plt.yticks(tick_marks, classes)

#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

#     thresh = cm.max() / 2.
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         plt.text(j, i, cm[i, j],
#                  horizontalalignment="center",
#                  color="white" if cm[i, j] > thresh else "black")

#     plt.tight_layout()
#     plt.ylabel('True label')
#     plt.xlabel('Predicted label')
    
    
# Read MNIST dataset
(x_train, y_train), (x_test, y_test)=tf.keras.datasets.mnist.load_data()
 
print('Train shape:', x_train.shape) #(60000,28,28)
print('Train samples:', x_train.shape[0]) #60000
print('Test samples:', x_test.shape[0], ) #10000
print('Image shape:', x_train[0].shape) # (28,28)

# Add pad to extend size for input matrix
#them chieu 0 (so 60000): [0,0] tuc khong them pad 
#them chieu 1 [2,2]: them 2 so 0 vao dau va cuoi 28-->32
#them chieu 3 [2,2]: them 2 so 0 vao dau va cuoi 28-->32  
x_train = tf.pad(x_train, [[0, 0], [2,2], [2,2]])/255
x_test = tf.pad(x_test, [[0, 0], [2,2], [2,2]])/255
print("x_train.shape=",x_train.shape)# (60000,32,32)

# Add dimension for input matrix
#them chieu thu 3 (RGB) gia cho anh (28x28)
x_train = tf.expand_dims(x_train, axis=3, name=None)
x_test = tf.expand_dims(x_test, axis=3, name=None)
print("x_train.shape=",x_train.shape) #(60000,32,32,1), moi them 1 chieu

# Validation data extraction 
#lay 2000 mau cuoi de valid
x_val = x_train[-2000:,:,:,:]
y_val = y_train[-2000:]
#lay tat ca mau tru 2000 mau cuoi de train
x_train = x_train[:-2000,:,:,:]
y_train = y_train[:-2000]

# Build the CNN model
#xay dung model nhu ly thuyet mang LeNet-5 Lecun

model = models.Sequential()
############lop tich chap thu 1
#input_shape = x_train.shape[1:] = (32,32,1)
#lop input 32x32 nut
#them lop Conv 6 filters, kernel 5x5 (f=5), stride=1 va pad=0
model.add(layers.Conv2D(6, 5, activation='tanh', input_shape=x_train.shape[1:]))
#Pooling = max, pool size (kernel) = 2 tuc la (2x2) va stride = 1 tuc la (1,1)
model.add(layers.MaxPool2D(2))
#dau ra la 14x14x6 
#ap dung ham sigmoid cho du lieu smooth hon - khong co cung duoc
###########model.add(layers.Activation('sigmoid'))
############lop tich chap thu 2
#input shape 14x14x6; ap dung 16 kernel 5x5 --> (10,10,16)
model.add(layers.Conv2D(16, 5, activation='tanh'))
#ap dung max pooling kernel = 2x2, stride=1 --> (5x5x16)
model.add(layers.MaxPool2D(2))
###############model.add(layers.Activation('sigmoid'))

#la phang bang 1 lop convolution 120 kernel (5,5) --> (1,120)
model.add(layers.Conv2D(120, 5, activation='tanh'))
#la phang bang ham Flatten()
model.add(layers.Flatten())
#lam fully connected 120 nut noi voi 84 nut 
model.add(layers.Dense(84, activation='tanh'))
#chuyen qua 10 nut tuong ung 10 lop dau ra
model.add(layers.Dense(10, activation='softmax'))
model.summary()

# Configures the CNN model for training
model.compile(optimizer='adam', loss=losses.sparse_categorical_crossentropy, metrics=['accuracy'])


# Store log for TensorBoard
logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)

###############################################################
# Training the CNN model with the given inputs
history = model.fit(x=x_train, y=y_train, batch_size=64, epochs=5, validation_data=(x_val, y_val), callbacks=[tensorboard_callback])
#print('history = ', history)
score = model.evaluate(x_test, y_test, verbose=0)
#print('score = ',score)
# Plot results with Matplotlib
fig, axs = plt.subplots(2, 1, figsize=(8,13))
 
axs[0].plot(history.history['loss'])
axs[0].plot(history.history['val_loss'],ls='--')
axs[0].set_xlabel('Number of training iterations')
axs[0].set_ylabel('Error')
axs[0].legend(['Train', 'Validation'])
 
axs[1].plot(history.history['accuracy'])
axs[1].plot(history.history['val_accuracy'],ls='--')
axs[1].set_xlabel('Number of training iterations')
axs[1].set_ylabel('Accuracy')
axs[1].legend(['Train', 'Validation'])
 
# Show figure
plt.savefig('LeNet5.png', format="png", dpi=600)
plt.show()

###############################################
#save trained model 
model.save('CNN_MNIST_model_5')
###############################################


#model evaluating
# score = model.evaluate(x_test, y_test)
# print('Loss: {:.4f}'.format(score[0]))
# print('Accuracy: {:.4f}'.format(score[1]))



