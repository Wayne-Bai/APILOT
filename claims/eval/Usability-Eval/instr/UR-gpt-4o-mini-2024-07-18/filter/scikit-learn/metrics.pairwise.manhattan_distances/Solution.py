import numpy as np
from sklearn.metrics import pairwise

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6]])
Y = np.array([[1, 1], [2, 2], [3, 3]])

# Compute L1 distances
l1_distances = pairwise.distances(X, Y, metric='l1')

print(l1_distances)
