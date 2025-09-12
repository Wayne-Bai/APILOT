import numpy as np
from sklearn.datasets import make_sparse_uncorrelated

n_features = 100
n_samples = 50
n_components = 10
n_nonzero_coefs = 5

D = np.random.randn(n_features, n_components)

X = np.zeros((n_components, n_samples))
for i in range(n_samples):
    nonzero_idx = np.random.choice(n_components, n_nonzero_coefs, replace=False)
    X[nonzero_idx, i] = np.random.randn(n_nonzero_coefs)

Y = np.dot(D, X)
