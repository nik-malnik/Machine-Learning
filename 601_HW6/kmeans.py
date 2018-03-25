import numpy as np
import math

def update_assignments(X, C):
	
	a = np.zeros(X.shape[0])
	D = np.zeros((X.shape[0],C.shape[0]))
	for i in range(C.shape[0]):
		D[:,i] = np.sum(np.square(X - C[i,:]),axis=1)
	a = np.argmin(D,axis=1)
	return a

def update_centers(X, C, a):
	
	freq = np.zeros(C.shape[0])
	C_new = np.zeros((C.shape[0],C.shape[1]))
	for i in range(X.shape[0]):
		C_new[a[i],:] += X[i,:]
		freq[a[i]] += 1

	for i in range(C.shape[0]):
		if freq[i] == 0:
			C_new[i,:] = C[i,:]
		else:
			C_new[i,:] = C_new[i,:]/freq[i]
	C = C_new
	return C

def lloyd_iteration(X, C):
  
  C_old = np.zeros((C.shape[0],C.shape[1]))
  iterations = 0
  while iterations < 1 or np.sum(C - C_old) != 0.0:
	  C_old = np.array(C)
	  a = update_assignments(X, C)
	  C = update_centers(X, C, a)
	  iterations += 1

  return (C, a)

def kmeans_obj(X, C, a):
	
	obj = 0.0
	for i in range(X.shape[0]):
		obj += np.sum(np.square(X[i,:] - C[a[i]]))
	return obj

def kmeans_cluster(X, k, init, num_restarts):
  n = X.shape[0]
  # Variables for keeping track of the best clustering so far
  best_C = None
  best_a = None
  best_obj = np.inf
  for i in range(num_restarts):
    if init == "random":
      perm = np.random.permutation(range(n))
      C = np.copy(X[perm[0:k]])
    elif init == "kmeans++":
      C = kmpp_init(X, k)
    elif init == "fixed":
      C = np.copy(X[0:k])
    else:
      print "No such module"
    # Run the Lloyd iteration until convergence
    (C, a) = lloyd_iteration(X, C)
    # Compute the objective value
    obj = kmeans_obj(X, C, a)
    if obj < best_obj:
      best_C = C
      best_a = a
      best_obj = obj
  return (best_C, best_a, best_obj)

def kmpp_init(X, k):
  n = X.shape[0]
  sq_distances = np.ones(n)
  center_ixs = list()
  for j in range(k):
    # Choose a new center index using D^2 weighting
    ix = discrete_sample(sq_distances)
    # Update the squared distances for all points
    deltas = X - X[ix]
    for i in range(n):
      sq_dist_to_ix = np.power(np.linalg.norm(deltas[i], 2), 2)
      sq_distances[i] = min(sq_distances[i], sq_dist_to_ix)
    # Append this center to the list of centers
    center_ixs.append(ix)
  # Output the chosen centers
  C = X[center_ixs]
  return np.copy(C)


def discrete_sample(weights):
  total = np.sum(weights)
  t = np.random.rand() * total
  p = 0.0
  for i in range(len(weights)):
    p = p + weights[i];
    if p > t:
      ix = i
      break
  return ix
