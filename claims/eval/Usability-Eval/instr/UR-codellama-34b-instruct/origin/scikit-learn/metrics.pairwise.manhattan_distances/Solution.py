from sklearn.metrics import pairwise_distances

# Compute the L1 distances between vectors in X and Y
X = [[0, 1], [2, 3]]
Y = [[4, 5], [6, 7]]
L1_distances = pairwise_distances(X, Y, metric='manhattan')

print(L1_distances)
