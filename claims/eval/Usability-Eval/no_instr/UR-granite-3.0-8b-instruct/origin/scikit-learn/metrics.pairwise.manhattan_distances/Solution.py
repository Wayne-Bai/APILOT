from sklearn.metrics.pairwise import manhattan_distances

# Assuming X and Y are your numpy arrays
X = ...
Y = ...

# Compute L1 distances
distances = manhattan_distances(X, Y)
