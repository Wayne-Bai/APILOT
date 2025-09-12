
import numpy as np
from sklearn.decomposition import sparse_encode

# Generate a random dictionary matrix D
n_features, n_components = 100, 50
D = np.random.rand(n_features, n_components)

# Generate a random signal X as a sparse combination of the dictionary elements
X = np.zeros((n_components, 10))
for i in range(n_components):
    nonzero_indices = np.random.choice(np.arange(n_features), size=5, replace=False)
    X[i] = D[nonzero_indices] @ np.random.rand(n_samples)

# Encode the signal using sparse_encode
Y = sparse_encode(X, D, n_nonzero_coefs=5)
