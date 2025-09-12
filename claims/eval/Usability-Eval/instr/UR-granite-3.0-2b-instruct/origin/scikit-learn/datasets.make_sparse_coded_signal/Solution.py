from sklearn.decomposition import SparsePCA
import numpy as np

# Generate a random dictionary D of shape (n_features, n_components)
n_features, n_components = 100, 50
D = np.random.rand(n_features, n_components)

# Generate a random signal X of shape (n_components, n_samples)
n_nonzero_coefs = 5
X = np.random.rand(n_components, 10)
X[:, :n_nonzero_coefs] = 0  # Set n_nonzero_coefs columns to zero

# Apply SparsePCA to find the sparse representation of X
splpca = SparsePCA(n_components=n_components, alpha=0.1)
Y = splpca.fit_transform(X)

print("Y = DX:\n", Y)
print("\nD shape:", D.shape)
print("X shape:", X.shape)
