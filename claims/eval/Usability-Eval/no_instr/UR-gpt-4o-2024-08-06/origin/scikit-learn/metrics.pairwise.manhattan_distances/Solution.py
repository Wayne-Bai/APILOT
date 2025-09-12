import numpy as np
from sklearn.metrics import pairwise_distances

# Sample data
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[7, 8, 9], [10, 11, 12]])

# Compute L1 (Manhattan) distances
l1_distances = pairwise_distances(X, Y, metric='manhattan')

print("L1 distances between vectors in X and Y:")
print(l1_distances)
