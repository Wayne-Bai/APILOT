# Import necessary libraries
from sklearn.decomposition import SparsePCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the dataset
iris = load_iris()
X = iris.data

# Scale the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create a SparsePCA instance with a specified alpha value
sparse_pca = SparsePCA(n_components=2, alpha=0.0001, ridge_alpha=0.01)

# Fit the SparsePCA to the scaled data
sparse_pca.fit(X_scaled)

# Transform the scaled data
X_sparse = sparse_pca.transform(X_scaled)

# Print the explained variance by each principal component
print("Explained variance:", sparse_pca.explained_variance_ratio_)

# Print the shape of the transformed data
print("Transformed data shape:", X_sparse.shape)

# Access and print the components (i.e., the sparse loading vectors)
print("Components:\n", sparse_pca.components_)

# Reconstruction of the original data from the sparse transformed data
X_sparse_reconstructed = sparse_pca.inverse_transform(X_sparse)

# Print the shape of the reconstructed data
print("Reconstructed data shape:", X_sparse_reconstructed.shape)
