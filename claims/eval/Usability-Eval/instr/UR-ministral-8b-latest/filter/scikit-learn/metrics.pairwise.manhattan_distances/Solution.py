import numpy as np
from sklearn.metrics.pairwise import manhattan_distances

# Sample data
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

# Compute L1 (Manhattan) distances between vectors in X and Y
distances = manhattan_distances(X, Y)

print(distances)
