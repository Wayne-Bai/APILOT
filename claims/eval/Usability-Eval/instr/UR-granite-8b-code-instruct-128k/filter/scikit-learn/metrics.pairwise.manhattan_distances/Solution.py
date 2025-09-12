from sklearn.metrics import pairwise_distances
import numpy as np
# Create sample vectors
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Y = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# Compute L1 distances
l1_distances = pairwise_distances(X, Y, metric='manhattan')
print(l1_distances)
