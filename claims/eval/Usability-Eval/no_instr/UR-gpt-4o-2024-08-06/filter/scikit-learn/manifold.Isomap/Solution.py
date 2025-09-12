from sklearn.manifold import Isomap
import numpy as np

# Example data
X = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])

# Initialize Isomap
isomap = Isomap(n_neighbors=2, n_components=2)

# Fit transform the data
X_transformed = isomap.fit_transform(X)

print("Original shape:", X.shape)
print("Transformed shape:", X_transformed.shape)
print("Transformed data:\n", X_transformed)
