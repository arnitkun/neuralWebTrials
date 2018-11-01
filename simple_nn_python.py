# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ldjkwml0E3pZnaXlQBoRGPvaxuh7Ez91
"""

import numpy as np

x = np.array(([2, 9], [1, 5], [3, 6]), dtype = float)
y = np.array(([92], [86], [89]), dtype = float)
xPredicted = np.array(([4,8]), dtype=float)

x = x / np.max(x, axis = 0)
y = y/100
xPredicted = xPredicted/np.amax(xPredicted, axis=0) # maximum of xPredicted (our input data for the prediction)

class Neural_Network(object):
 
  def __init__(self):
    self.inputsize = 2
    self.outputsize = 1
    self.hiddensize = 3
    self.W1 = np.random.randn(self.inputsize, self.hiddensize)
    self.W2 = np.random.randn(self.hiddensize, self.outputsize)
    
  def forward(self, x):
    self.z = np.dot(x,self.W1)
    self.z2 = self.sigmoid(self.z)
    self.z3 = np.dot(self.z2, self.W2)
    o = self.sigmoid(self.z3)
    return o
  
  def sigmoidPrime(self, s):
  #derivative of sigmoid
    return s * (1 - s)
  
  def sigmoid(self, s):
    return 1/(1+np.exp(-s))
  
  def backward(self, X, y, o):
  # backward propagate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights
  
  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self):
    print "Predicted data based on trained weights: ";
    print "Input (scaled): \n" + str(xPredicted);
    print "Output: \n" + str(self.forward(xPredicted));

NN = Neural_Network()
# o = NN.forward(x)
# print "Predicted Output: \n" + str(o)
# print "Actual Output: \n" + str(y)
for i in xrange(1000): # trains the NN 1,000 times
  print "# " + str(i) + "\n"
  print "Input (scaled): \n" + str(x)
  print "Actual Output: \n" + str(y)
  print "Predicted Output: \n" + str(NN.forward(x))
  print "Loss: \n" + str(np.mean(np.square(y - NN.forward(x)))) # mean sum squared loss
  print "\n"
  NN.train(x, y)

NN.saveWeights()
NN.predict()

