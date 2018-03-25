import os
import csv
import numpy as np
import perceptron
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Point to data directory here
# By default, we are pointing to '../data/'
data_dir = os.path.join('perceptron_starter_codes','data')

# Load numeric data files into numpy arrays
XTrain = np.genfromtxt(os.path.join(data_dir, 'XTrain.csv'), delimiter=',')
yTrain = np.genfromtxt(os.path.join(data_dir, 'yTrain.csv'), delimiter=',')
XTest = np.genfromtxt(os.path.join(data_dir, 'XTest.csv'), delimiter=',')
yTest = np.genfromtxt(os.path.join(data_dir, 'yTest.csv'), delimiter=',')

# Visualize the image
'''
idx = 0
datapoint = XTrain[idx, 1:]
plt.imshow(datapoint.reshape((28,28), order = 'F'), cmap='gray')
plt.show()
'''

# TODO: Test perceptron_predict function, defined in perceptron.py
yPred = perceptron.perceptron_predict(w,XTrain[0])

# TODO: Test perceptron_train function, defined in perceptron.py
w = np.zeros(XTrain.shape[1])
w = perceptron.perceptron_train(w,XTrain,yTrain,10)

# TODO: Test RBF_kernel function, defined in perceptron.py
K = perceptron.RBF_kernel(XTrain[0:5],XTrain[0:5],10.0)

# TODO: Test kernel_perceptron_predict function, defined in perceptron.py
a = np.zeros(XTrain.shape[0])
yPred = perceptron.kernel_perceptron_predict(a, XTrain,yTrain,XTrain[0],10.0)

# TODO: Test kernel_perceptron_train function, defined in perceptron.py
a = np.zeros(XTrain.shape[0])
a0 = perceptron.kernel_perceptron_train(a,XTrain,yTrain,5,100)

# TODO: Run experiments outlined in HW4 PDF
w = np.zeros(XTrain.shape[1])
w = perceptron.perceptron_train(w,XTrain,yTrain,10)
yPred = np.zeros(len(yTest))
for i in range(len(XTest)):
    yPred[i] = perceptron.perceptron_predict(w,XTest[i])
np.sum(np.abs(yTest - yPred))/(2.0*len(XTest))

for sigma in [0.01,0.1,1.0,10.0,100.0,1000.0]:
	a = np.zeros(XTrain.shape[0])
	a0 = perceptron.kernel_perceptron_train(a,XTrain,yTrain,2,sigma)
	yPred = np.zeros(len(yTest))
	for i in range(len(XTest)):
		yPred[i] = perceptron.kernel_perceptron_predict(a0, XTrain,yTrain,XTest[i],sigma)
	print "For sigma=" + str(sigma) + " error rate=" + str(np.sum(np.abs(yTest - yPred))/(2.0*len(XTest)))
