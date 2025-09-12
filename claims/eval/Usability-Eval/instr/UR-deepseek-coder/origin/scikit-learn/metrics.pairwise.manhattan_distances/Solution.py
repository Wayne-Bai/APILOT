import numpy as np
from sklearn.metrics.pairwise import manhattan_distances

# Example data
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

# Compute L1 distances
l1_distances = manhattan_distances(X, Y)

print(l1_distances)
