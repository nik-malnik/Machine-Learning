import numpy as np

def obs(p):
	return np.random.choice(2,1,p=[p,1-p])[0]

def T(v):
	if v == 0:
		return 0.45
	else:
		return 0.55

def C(v):
	if v == 0:
		return 0.2
	else:
		return 0.8

def O(v):
	if v == 0:
		return 0.7
	else:
		return 0.3
	
def E(v,T,C):
	if T == 0 and C == 0:
		p = 0.8
	elif T == 0 and C == 1:
		p = 0.3
	elif T == 1 and C == 0:
		p = 0.5
	elif T == 1 and C == 1:
		p = 0.1		 
	else:
		throw('Error')
	if v == 0:
		return p
	else:
		return (1-p)

def H(v,C):
	if C == 0:
		p = 0.75
	else:
		p = 0.2
	
	if v == 0:
		return p
	else:
		return 1-p

def G(E,H):
	if E == 0 and H == 0:
		return 0.05
	elif E == 0 and H == 1:
		return 0.3
	elif E == 1 and H == 0:
		return 0.3
	elif E == 1 and H == 1:
		return 0.2	 
	else:
		throw('Error')

def T_cond(c,e,h):
	#p = T(0)*E(e,0,c)/((T(0)*E(e,0,c)) + (T(1)*E(e,1,c)))
	p1 = G(e,h)*H(h,c)*E(e,0,c)*O(1)*C(c)*T(0)
	p2 = G(e,h)*H(h,c)*E(e,1,c)*O(1)*C(c)*T(1)
	return obs(p1/(p1+p2))

def C_cond(t,e,h):
	#p = C(0)*H(h,0)*E(e,t,0)/(((C(0)*H(h,0)) + (C(1)*H(h,1)))*((C(0)*E(e,t,0)) + (C(1)*E(e,t,1))))
	p1 = G(e,h)*H(h,0)*E(e,t,0)*O(1)*C(0)*T(t)
	p2 = G(e,h)*H(h,1)*E(e,t,1)*O(1)*C(1)*T(t)
	return obs(p1/(p1+p2))

def E_cond(t,c,h):
	#p = E(0,t,c)*T(t)*O(1)*G(0,h)/((E(0,t,c)*G(0,h)) + (E(1,t,c)*G(1,h)))
	p1 = G(0,h)*H(h,c)*E(0,t,c)*O(1)*C(c)*T(t)
	p2 = G(1,h)*H(h,c)*E(1,t,c)*O(1)*C(c)*T(t)
	return obs(p1/(p1+p2))

def H_cond(e,t,c):
	#p = H(0,c)*G(e,0)/((H(0,c)*G(e,0)) + (H(1,c)*G(e,1)))
	p1 = G(e,0)*H(0,c)*E(e,t,c)*O(1)*C(c)*T(t)
	p2 = G(e,1)*H(1,c)*E(e,t,c)*O(1)*C(c)*T(t)
	return obs(p1/(p1+p2))

def C_OG():
	c = 1
	num = 0.0
	for h in [0,1]:
		for e in [0,1]:
			for t in [0,1]:
				print G(e,h)*H(h,c)*E(e,t,c)*O(1)*C(c)*T(t)
				num += G(e,h)*H(h,c)*E(e,t,c)*O(1)*C(c)*T(t)
	
	print "num:" + str(num)
	den = 0.0
	for h in [0,1]:
		for e in [0,1]:
			for t in [0,1]:
				for c in [0,1]:
					print G(e,h)*H(h,c)*E(e,t,c)*O(1)*C(c)*T(t)
					den += G(e,h)*H(h,c)*E(e,t,c)*O(1)*C(c)*T(t)
	print "den:" + str(den)
	return num/den
	
