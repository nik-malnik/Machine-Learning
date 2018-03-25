import os
import math
import numpy as np

def LinReg_ReadInputs(filepath):
	
	XTrain = np.loadtxt(open(filepath + "/LinReg_XTrain.csv", "rb"), delimiter=",")
	yTrain = np.loadtxt(open(filepath + "/LinReg_yTrain.csv", "rb"), delimiter=",")
	XTest = np.loadtxt(open(filepath + "/LinReg_XTest.csv", "rb"), delimiter=",")
	yTest = np.loadtxt(open(filepath + "/LinReg_yTest.csv", "rb"), delimiter=",")
	
	XTest = ((XTest - np.min(XTrain,axis=0))/(np.max(XTrain,axis=0) - np.min(XTrain,axis=0)))
	XTrain = ((XTrain - np.min(XTrain,axis=0))/(np.max(XTrain,axis=0) - np.min(XTrain,axis=0)))
	
	yTrain = yTrain.reshape(yTrain.shape[0],1)
	yTest = yTest.reshape(yTest.shape[0],1)
	
	bias = np.ones((XTrain.shape[0],1),dtype="float")
	XTrain = np.concatenate([bias,XTrain],axis=1)
	
	bias = np.ones((XTest.shape[0],1),dtype="float")
	XTest = np.concatenate([bias,XTest],axis=1)
	
	return (XTrain, yTrain, XTest, yTest)
    
def LinReg_CalcObj(X, y, w):
    w.reshape(w.shape[0],1)
    lossVal = np.power(np.linalg.norm((np.dot(X,w) - y)),2)/X.shape[0] 
    return lossVal

def LinReg_CalcSG(x, y, w):
    
    sg = 2.0*(np.dot(x,w) - y)*x
    return sg

def LinReg_UpdateParams(w, sg, eta):
    
    w = w - eta*sg
    return w
    
def LinReg_SGD(XTrain, yTrain, XTest, yTest):
    
    w = 0.5*np.ones((XTrain.shape[1],1))
    epochs = 100
    trainLoss = []
    testLoss = []
    obs = 0
    for epoch in range(epochs):
		for i in range(XTrain.shape[0]):
			eta = 0.5/math.sqrt(obs + 1.0)
			sg = LinReg_CalcSG(XTrain[i], yTrain[i], w)
			w = LinReg_UpdateParams(w, sg.reshape(sg.shape[0],1), eta)
			obs = obs + 1
		trainLoss.append(LinReg_CalcObj(XTrain, yTrain, w))
		testLoss.append(LinReg_CalcObj(XTest, yTest, w))
		print "Completed epoch: " + str(epoch) + " with training loss: " + str(trainLoss[-1]) + " and test loss: " + str(testLoss[-1])
    return (w, trainLoss, testLoss)
    
def plot(trainLoss,testLoss):     # This function's results should be returned via gradescope and will not be evaluated in autolab.
    import matplotlib.pyplot as plt
    t = np.arange(0, 100, 1) 
    plt.plot(t,trainLoss,t,testLoss)
    plt.show()
    return None

    
'''
import pandas as pd
import statsmodels.formula.api as sm
data = np.concatenate([XTrain, yTrain],axis=1)
data = pd.DataFrame(data,columns=['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','y'])
result = sm.ols(formula="y ~ x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14", data=data).fit()
result.params
'''
