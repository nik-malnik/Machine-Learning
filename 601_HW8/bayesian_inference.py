import matplotlib.pyplot as plt
import numpy as np
import gibbs_sampling as gs

def T():
	return np.random.choice(2,1,p=[0.45,0.55])[0]
	
def C():
	return np.random.choice(2,1,p=[0.2,0.8])[0]
	
def O():
	return np.random.choice(2,1,p=[0.3,0.7])[0]

def H(C):
	if C == 0:
		p = 0.75
	else:
		p = 0.2
	return np.random.choice(2,1,p=[p,1-p])[0]
	
def E(T,C,O):
	if T == 0 and C == 0 and O == 0:
		p = 0.85
	elif T == 0 and C == 0 and O == 1:
		p = 0.8
	elif T == 0 and C == 1 and O == 0:
		p = 0.4
	elif T == 0 and C == 1 and O == 1:
		p = 0.3
	elif T == 1 and C == 0 and O == 0:
		p = 0.6
	elif T == 1 and C == 0 and O == 1:
		p = 0.5
	elif T == 1 and C == 1 and O == 0:
		p = 0.15
	elif T == 1 and C == 1 and O == 1:
		p = 0.1		 
	else:
		throw('Error')
	return np.random.choice(2,1,p=[p,1-p])[0]

def G(E,H):
	grades = ['A','B','C','D','F']
	if E == 0 and H == 0:
		return grades[np.random.choice(5,1,p=[0.05,0.05,0.1,0.2,0.6])[0]]
	elif E == 0 and H == 1:
		return grades[np.random.choice(5,1,p=[0.1,0.3,0.3,0.2,0.1])[0]]
	elif E == 1 and H == 0:
		return grades[np.random.choice(5,1,p=[0.1,0.3,0.3,0.2,0.1])[0]]
	elif E == 1 and H == 1:
		return grades[np.random.choice(5,1,p=[0.6,0.2,0.1,0.05,0.05])[0]]	 
	else:
		throw('Error')

''' Brute Force Sampling '''
sample = []
valid = []
c1 = 0.0
estimate1 = []
for k in range(10000):
	t = T()
	c = C()
	o = O()
	h = H(c)
	e = E(t,c,o)
	g = G(e,h)
	sample.append({'t':t,'c':c,'o':o,'h':h,'e':e,'g':g})
	if g == 'B' and o == 1:
		valid.append({'t':t,'c':c,'o':o,'h':h,'e':e,'g':g})
		if c == 1:
			c1 = c1 + 1.0
	if len(valid) > 0:
		estimate1.append(c1/(1.0*len(valid)))
	else:
		estimate1.append(0)

''' Gibbs Sampling '''

'''
t = c = e = h = 0
o = 1
c1 = 0.0
estimate2 = []
for k in range(10000):
	t = T()
	c = C()
	e = E(t,c,o)
	h = H(c)
	if c == 1:
		c1 = c1 + 1.0
	if k > 0:
		estimate2.append(c1/(k + 1.0))
	else:
		estimate2.append(0)
'''

t = c = e = h = 0
o = 1
c1 = 0.0
estimate2 = []
for k in range(10000):
	t = gs.T_cond(c,e,h)
	c = gs.C_cond(t,e,h)
	e = gs.E_cond(t,c,h)
	h = gs.H_cond(e,t,c)
	if c == 1:
		c1 = c1 + 1.0
	if k > 0:
		estimate2.append(c1/(k + 1.0))
	else:
		estimate2.append(0)

gs.C_OG()	
	
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(range(10000), estimate1, s=1, color='b', marker="s", label='BruteForce')
ax1.scatter(range(10000),estimate2, s=1, color='r', marker="o", label='Gibbs')
plt.legend(loc='upper left');
plt.show()
	
