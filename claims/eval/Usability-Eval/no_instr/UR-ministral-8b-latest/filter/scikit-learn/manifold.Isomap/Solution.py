import numpy as np
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances

# Example data: If you have data in high-dimensional space, store it in X.
X = np.array([[0, 1], [1, 0], [2, 1], [1, 2], [0, 1]])

# Compute the pairwise distance matrix
dist_matrix = pairwise_distances(X, metric='euclidean')

# Create an Isomap object with 2 components (for 2D embedding)
isomap = MDS(n_components=2, dissimilarity='precomputed', random_state=42)

# Fit the model on the distance matrix
embedded_data = isomap.fit_transform(dist_matrix)

# Print the embedded data
print("Embedded Data:")
print(embedded_data)
