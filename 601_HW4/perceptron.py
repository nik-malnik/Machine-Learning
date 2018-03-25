import numpy as np
import math

def perceptron_predict(w, x):
	z = np.dot(x,w)
	if z <= 0:
		return -1
	else:
		return 1


def perceptron_train(w0, XTrain, yTrain, num_epoch):
	for epoch in range(num_epoch):
		mistake_count = 1
		for obs in range(len(XTrain)):
			y_pred = perceptron_predict(w0, XTrain[obs])
			if y_pred != yTrain[obs]:
				w0 = w0 + yTrain[obs]*XTrain[obs]
				mistake_count += 1
		print "Completed epoch: " + str(epoch + 1) + " with " + str(mistake_count) + " mistakes"
	return w0


def RBF_kernel(X1, X2, sigma):
	if len(X1.shape) == 2:
		n = X1.shape[0]
	else:
		n = 1
		X1 = np.reshape(X1, (1, X1.shape[0]))
	if len(X2.shape) == 2:
		m = X2.shape[0]
	else:
		m = 1  
		X2 = np.reshape(X2, (1, X2.shape[0]))
		
	K = np.zeros((n,m))
	for i in range(len(X1)):
		for j in range(len(X2)):
			K[i,j] = math.exp(-1.0*np.sum(np.square(X1[i] - X2[j]))/(2.0*sigma*sigma))  
	  
	return K

def kernel_perceptron_predict(a, XTrain, yTrain, x, sigma):
	K = RBF_kernel(x,XTrain,sigma)
	z  = np.sum(a*yTrain*K[0])
	if z <= 0:
		return -1
	else:
		return 1

def kernel_perceptron_train(a0, XTrain, yTrain, num_epoch, sigma):
	for epoch in range(num_epoch):
		mistake_count = 1
		for obs in range(len(XTrain)):
			y_pred = kernel_perceptron_predict(a0, XTrain,yTrain,XTrain[obs],sigma)
			if y_pred != yTrain[obs]:
				a0[obs] = a0[obs] + 1
				mistake_count += 1
		print "Completed epoch: " + str(epoch + 1) + " with " + str(mistake_count) + " mistakes"
	return a0
