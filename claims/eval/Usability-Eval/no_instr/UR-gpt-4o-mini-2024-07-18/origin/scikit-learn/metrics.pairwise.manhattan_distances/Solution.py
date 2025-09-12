from sklearn.metrics import pairwise

# Example input vectors
X = [[1, 2], [3, 4], [5, 6]]
Y = [[7, 8], [9, 10]]

# Compute the L1 distances
l1_distances = pairwise.pairwise_distances(X, Y, metric='manhattan')

print(l1_distances)
