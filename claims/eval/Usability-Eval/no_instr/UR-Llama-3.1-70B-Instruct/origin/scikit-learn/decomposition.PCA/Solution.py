# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = np.random.rand(100, 5)

# Create a PCA object and apply dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Print explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Plot the original data and the transformed data
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1])
plt.title("Original Data")

plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title("PCA Transformed Data")
plt.show()

# Inverse transform to original space
X_inverse = pca.inverse_transform(X_pca)
print("Original Shape:", X.shape)
print("Inverse Transform Shape:", X_inverse.shape)
