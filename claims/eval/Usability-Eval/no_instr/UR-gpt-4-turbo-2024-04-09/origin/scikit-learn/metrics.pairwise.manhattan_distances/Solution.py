import numpy as np
from sklearn.metrics import pairwise_distances

# Sample data
X = np.array([[0, 1], [2, 3]])
Y = np.array([[1, 1], [3, 2]])

# Compute the L1 distance (Manhattan distance)
l1_distances = pairwise_distances(X, Y, metric='manhattan')
print(l1_distances)
