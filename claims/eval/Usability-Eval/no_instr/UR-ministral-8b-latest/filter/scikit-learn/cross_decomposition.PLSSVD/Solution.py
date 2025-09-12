from sklearn.decomposition import PCA
import numpy as np

# Sample data
X = np.array([[2.5, 2.4],
              [0.5, 0.7],
              [2.2, 2.9],
              [1.9, 2.2],
              [3.1, 3.0],
              [2.3, 2.7],
              [2, 1.6],
              [1, 1.1],
              [1.5, 1.6],
              [1.1, 0.9]])

# Fit the PCA model (2 components in this case)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Original array:\n", X)
print("\nTransformed array:\n", X_pca)
