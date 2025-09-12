from sklearn.random_projection import SparseRandomProjection
import numpy as np
import scipy.sparse as sparse

# Generate a random sparse matrix with n_samples samples, n_features features,
# and n_nonzero_coefs non-zero coefficients per sample
n_samples, n_features, n_nonzero_coefs = 100, 1000, 10
X = sparse.random(n_samples, n_features, density=0.01, format='csr')

# Generate a random dictionary with n_components components and
# n_features features
n_components = 100
D = np.random.rand(n_features, n_components)

# Project the data onto the sparse random projection subspace
model = SparseRandomProjection(n_components=n_components)
Y = model.fit_transform(X)
