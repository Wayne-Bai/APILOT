# Import necessary libraries
from sklearn.decomposition import SparsePCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Load iris dataset
iris = load_iris()
X = iris.data

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create an instance of SparsePCA with 2 components and alpha set to 0.0001
sparse_pca = SparsePCA(n_components=2, alpha=0.0001, random_state=42)

# Fit and transform the data
X_sparse_pca = sparse_pca.fit_transform(X_scaled)

# Print the explained variance ratio
print("Explained variance ratio:", sparse_pca.explained_variance_ratio_)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X_sparse_pca[:, 0], X_sparse_pca[:, 1], c=iris.target)
plt.title("Sparse PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

# Get the components
components = sparse_pca.components_
print("Sparse PCA components shape:", components.shape)
print("Sparse PCA components:\n", components)

# Get the non-zero coefficients for each component
non_zero_coefficients = np.count_nonzero(components, axis=1)
print("Number of non-zero coefficients for each component:", non_zero_coefficients)
