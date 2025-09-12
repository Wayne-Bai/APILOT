import numpy as np
from sklearn.metrics import pairwise_distances

# Define two sets of vectors
X = np.array([[1, 2], [3, 4]])
Y = np.array([[1, 1], [4, 4]])

# Compute the L1 distance (Manhattan distance)
L1_distances = pairwise_distances(X, Y, metric='manhattan')

print(L1_distances)
