import numpy as np
from sklearn.decomposition import MiniBatchSparsePCA

# Generate a random dictionary D
n_features, n_components, n_samples = 100, 10, 1000
D = np.random.rand(n_features, n_components)

# Generate a sparse matrix X
n_nonzero_coefs = 5
X = np.zeros((n_components, n_samples))
for i in range(n_components):
    indices = np.random.choice(n_features, n_nonzero_coefs, replace=False)
    X[i, :] = np.random.rand(n_samples)
    X[i, :] *= 0
    X[i, indices] = np.random.rand(n_nonzero_coefs)

# Generate the signal Y = DX
Y = np.dot(D, X)
