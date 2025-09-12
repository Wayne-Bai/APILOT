
from sklearn.metrics import pairwise_distances

# Compute the L1 distances between the vectors in X and Y
X = [[1, 2], [3, 4]]
Y = [[5, 6], [7, 8]]

distances = pairwise_distances(X, Y, metric='manhattan')

print(distances)
