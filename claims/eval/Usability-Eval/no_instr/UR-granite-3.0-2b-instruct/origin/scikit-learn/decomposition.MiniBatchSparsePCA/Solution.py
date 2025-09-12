from sklearn.decomposition import SparsePCA
from sklearn.datasets import make_sparsedata

# Generate a sparse dataset
X, _ = make_sparsedata(n_samples=100, n_features=20, n_sparse=10, random_state=42)

# Initialize SparsePCA with alpha=0.1
spca = SparsePCA(alpha=0.1)

# Fit the model to the data
spca.fit(X)

# Print the explained variance ratio
print("Explained Variance Ratio:", spca.explained_variance_ratio_)

# Print the components
print("Components:\n", spca.components_)
