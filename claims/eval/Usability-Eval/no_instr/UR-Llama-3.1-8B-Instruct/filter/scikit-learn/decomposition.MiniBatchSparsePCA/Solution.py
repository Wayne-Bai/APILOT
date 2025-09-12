# Import necessary libraries
from sklearn.decomposition import SparsePCA
from sklearn.datasets import load_iris
import numpy as np

# Load iris dataset
iris = load_iris()
X = iris.data

# Create a SparsePCA object with 3 components and alpha set to 1.0
sparse_pca = SparsePCA(n_components=3, alpha=1.0)

# Fit the SparsePCA object to the data
sparse_pca.fit(X)

# Print the explained variance ratio
print(sparse_pca.explained_variance_ratio_)

# Transform the data into a new coordinate system
X_sparse = sparse_pca.transform(X)

# Print the resulting sparse components
print(sparse_pca.components_)
# Print the projected data onto the new coordinate system
print(X_sparse)

# Try reconstructing the data
reconstructed_data = sparse_pca.inverse_transform(X_sparse)

# Print the reconstructed data
print(reconstructed_data)
