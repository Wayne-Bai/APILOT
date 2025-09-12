import numpy as np
from sklearn.manifold import Isomap

# Example data: 2D points
X = np.array([[0, 0],
              [1, 1],
              [2, 0],
              [1, -1],
              [0, -2]])

# Create an Isomap object with the number of neighbors and dimensions 
isomap = Isomap(n_neighbors=2, n_components=1)

# Fit and transform the data
X_isomap = isomap.fit_transform(X)

# Output the transformed data
print(X_isomap)
