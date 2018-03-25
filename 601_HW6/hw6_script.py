import os
import csv
import numpy as np
import kmeans

data_dir = os.path.join('','data')

X = np.genfromtxt(os.path.join(data_dir, 'kmeans_test_data.csv'), delimiter=',')

a = kmeans.update_assignments(X, C)
C = kmeans.update_centers(X, C, a)
(C, a) = kmeans.lloyd_iteration(X, C)
obj = kmeans.kmeans_obj(X, C, a)

(best_C, best_a, best_obj) = kmeans.kmeans_cluster(X, 5, "random", 2)

# TODO: Run experiments outlined in HW6 PDF



# For question 9 and 10
# from sklearn.decomposition import PCA
mnist_X = np.genfromtxt(os.path.join(data_dir, 'mnist_data.csv'), delimiter=',')
