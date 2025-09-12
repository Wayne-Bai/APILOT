from sklearn.decomposition import PCA
import numpy as np

# Generate some sample data
X = np.random.rand(100, 5)

# Center the data but not scale it
X_centered = X - X.mean(axis=0)

# Perform SVD on the centered data
U, sigma, Vt = np.linalg.svd(X_centered, full_matrices=False)

# Keep only the top k eigenvectors
k = 2
eigenvectors = U[:, :k]

# Project the original data onto the new coordinate system defined by the eigenvectors
Y = np.dot(X, eigenvectors)

# Plot the original and projected data
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1])
plt.scatter(Y[:, 0], Y[:, 1])
plt.xlabel('Original data')
plt.ylabel('Projected data')
plt.show()
