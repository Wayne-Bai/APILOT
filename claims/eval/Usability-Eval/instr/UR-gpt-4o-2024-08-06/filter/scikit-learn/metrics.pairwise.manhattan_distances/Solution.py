from sklearn.metrics import pairwise_distances
import numpy as np

# Example vectors
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[1, 0, 1], [0, 2, 3]])

# Compute L1 distances (Manhattan distances) between vectors in X and Y
l1_distances = pairwise_distances(X, Y, metric='manhattan')

print("L1 Distances:\n", l1_distances)
