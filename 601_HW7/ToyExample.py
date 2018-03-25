import numpy as np
from scipy.signal import convolve2d
import math

X = L1 = np.array([[0,0,4,0],[0,2,5,0],[0,0,1,0],[0,0,2,0]])
f1 = np.array([[0,2],[1,1]])	#Inverted on purpose
f2 = np.array([[2,0],[1,2]])	#Inverted on purpose
b = np.array([0,0,0])
W = np.array([[1,0.5,1,2,-1,1,1,-1],[0.5,1,2,1,-0.5,0.5,-1,1],[0.25,-1,1,1,0.5,-1,-1,-1]])

L2 = np.zeros((3,3,2))
L2[:,:,0] = convolve2d(L1, f1,mode="valid",boundary="symm")
L2[:,:,1] = convolve2d(L1, f2,mode="valid",boundary="symm")

print L2[0,0,1]

L3 = np.zeros((2,2,2))
for k in range(2):
    for i in range(2):
        for j in range(2):
			max_val = -1
			for i_s in range(2):
				for j_s in range(2):
					if L2[i+i_s,j+j_s,k] > max_val:
						max_val = L2[i+i_s,j+j_s,k]
			L3[i,j,k] = max_val

print L3[1,0,0]

L3 = np.append(L3[:,:,0].flatten(), L3[:,:,1].flatten())
L4 = np.dot(L3,np.transpose(W)) + b

L5 = np.zeros(3)
for i in range(3):
	if L4[i] > 0:
		L5[i] = L4[i]

print L5[1]

L6 = np.exp(L5)/np.sum(np.exp(L5))

print L6[1]

loss = -math.log(L6[1])

print loss

print (L3[0]/L6[1])*(np.exp(L5[0])*np.exp(L5[1]))/np.power(np.sum(np.exp(L5)),2)
print -1*(np.exp(L5[0])*np.exp(L5[1]))/np.power(np.sum(np.exp(L5)),2)*(1/L6[1])*(4 + 10 - 8 - 5)
print -1*(np.exp(L5[0])*np.exp(L5[1]))/np.power(np.sum(np.exp(L5)),2)*(1/L6[1])*(4 + 4 - 8 - 2)
