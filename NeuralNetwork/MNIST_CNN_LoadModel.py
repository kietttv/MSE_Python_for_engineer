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
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

def precision_recall_f1(y_test, y_pred):
    # Tính accuracy: (tp + tn) / (p + n)
    accuracy = accuracy_score(y_test, y_pred)
    #print('Accuracy: %f' % accuracy)
    # Tính precision tp / (tp + fp)
    precision = precision_score(y_test, y_pred, average='macro')
    #print('Precision: %f' % precision)
    # Tính recall: tp / (tp + fn)
    recall = recall_score(y_test, y_pred, average='macro')
    #print('Recall: %f' % recall)
    # Tính f1: 2 tp / (2 tp + fp + fn)
    f1 = f1_score(y_test, y_pred, average='macro')
    #print('F1 score: %f' % f1)
    return accuracy, precision, recall, f1


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    
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

###############################################################
# Load trained model 
model = tf.keras.models.load_model('CNN_MNIST_model_5')

# evaluate the model

score = model.evaluate(x_test, y_test, verbose=0)
print('score = ',score)
print('Loss: {:.4f}'.format(score[0]))
print('Accuracy: {:.4f}'.format(score[1]))

#model evaluating
# score = model.evaluate(x_test, y_test)
# print('Loss: {:.4f}'.format(score[0]))
# print('Accuracy: {:.4f}'.format(score[1]))


# Predict the values from the validation dataset
Y_pred = model.predict(x_test)
#print('Y_pred = ', Y_pred, 'shape =', Y_pred.shape)
# Convert predictions classes to one hot vectors 
Y_pred_classes = np.argmax(Y_pred,axis = 1) 
#print('Y_pred_classes',Y_pred_classes, 'shape: ', Y_pred_classes.shape)
# Convert validation observations to one hot vectors
#Y_true = np.argmax(y_test,axis = 1)    #với FMNIST
Y_true = y_test             #với MNIST
#print('Y_true = ', Y_true, 'shape: ', Y_true.shape)
#calculate precision, recall, F1-score

accuracy, precison, recall, f1 = precision_recall_f1(Y_true, Y_pred_classes)
print('accuracy = {} \nprecison = {} \nrecall= {} \nf1={}'.format(accuracy, precison, recall, f1))
# compute the confusion matrix
confusion_mtx = confusion_matrix(Y_true, Y_pred_classes) 
# plot the confusion matrix
# plot_confusion_matrix(confusion_mtx, 
#             classes = ['T-shirt/Top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle Boot'])
plot_confusion_matrix(confusion_mtx, 
            classes = [0,1,2,3,4,5,6,7,8,9])

#visualization predict sample
#get 4 correct sample
correct = []
for i in range(len(y_test)):
    if(Y_pred_classes[i] == Y_true[i]):
        correct.append(i)
    if(len(correct) == 4):
        break
    
fig, ax = plt.subplots(2,2, figsize=(12,6))
fig.set_size_inches(10,10)
ax[0,0].imshow(x_test[correct[0]], cmap='gray')
ax[0,0].set_title("Predicted Label : " + str(Y_pred_classes[correct[0]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[0]]))
ax[0,1].imshow(x_test[correct[1]], cmap='gray')
ax[0,1].set_title("Predicted Label : " + str(Y_pred_classes[correct[1]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[1]]))
ax[1,0].imshow(x_test[correct[2]], cmap='gray')
ax[1,0].set_title("Predicted Label : " + str(Y_pred_classes[correct[2]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[2]]))
ax[1,1].imshow(x_test[correct[3]], cmap='gray')
ax[1,1].set_title("Predicted Label : " + str(Y_pred_classes[correct[3]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[3]]))

#get 4 incorrect sample
correct = []
for i in range(len(y_test)):
    if(Y_pred_classes[i] != Y_true[i]):
        correct.append(i)
    if(len(correct) == 4):
        break
    
fig, ax = plt.subplots(2,2, figsize=(12,6))
fig.set_size_inches(10,10)
ax[0,0].imshow(x_test[correct[0]], cmap='gray')
ax[0,0].set_title("Predicted Label : " + str(Y_pred_classes[correct[0]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[0]]))
ax[0,1].imshow(x_test[correct[1]], cmap='gray')
ax[0,1].set_title("Predicted Label : " + str(Y_pred_classes[correct[1]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[1]]))
ax[1,0].imshow(x_test[correct[2]], cmap='gray')
ax[1,0].set_title("Predicted Label : " + str(Y_pred_classes[correct[2]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[2]]))
ax[1,1].imshow(x_test[correct[3]], cmap='gray')
ax[1,1].set_title("Predicted Label : " + str(Y_pred_classes[correct[3]]) + "\n"+"Actual Label : " + 
                 str(Y_true[correct[3]]))