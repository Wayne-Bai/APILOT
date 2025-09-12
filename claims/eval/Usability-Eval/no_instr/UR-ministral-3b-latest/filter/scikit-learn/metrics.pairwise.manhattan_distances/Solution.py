import numpy as np
from sklearn.metrics.pairwise import euclidian_distance

# Assuming X and Y are your numpy arrays containing the vectors
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[7, 8, 9], [10, 11, 12]])

# Compute the L1 distances
L1_distances = np.abs(np.subtract(X, Y))
print(L1_distances)
