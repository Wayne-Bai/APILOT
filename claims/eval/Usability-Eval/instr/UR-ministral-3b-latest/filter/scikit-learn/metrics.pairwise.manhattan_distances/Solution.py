from math import sqrt
from scipy.spatial.distance import pdist, squareform

# Sample data
X = [[1, 2], [3, 4], [5, 6]]
Y = [[7, 8], [9, 10], [11, 12]]

# Compute the L1 distance between each vector in X and corresponding vector in Y
distance_matrix = squareform(pdist(X, Y, metric='manhattan'))

distance_matrix
