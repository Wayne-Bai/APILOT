from sklearn.metrics.pairwise import manhattan_distances

# Assuming X and Y are your matrices
X = ...
Y = ...

# Compute the L1 distances between the vectors in X and Y
l1_distances = manhattan_distances(X, Y)
