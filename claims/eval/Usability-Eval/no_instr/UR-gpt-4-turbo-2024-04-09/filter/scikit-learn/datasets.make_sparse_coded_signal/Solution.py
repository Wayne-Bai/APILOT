import numpy as np
from sklearn.datasets import make_sparse_coded_signal

n_samples = 100
n_components = 50
n_features = 20
n_nonzero_coefs = 5

Y, D, X = make_sparse_coded_signal(n_samples=n_samples,
                                   n_components=n_components,
                                   n_features=n_features,
                                   n_nonzero_coefs=n_nonzero_coefs,
                                   random_state=42)

print("Matrix Y (signal):", Y.shape)
print("Dictionary matrix D (basis components):", D.shape)
print("Coefficient matrix X (sparse code):", X.shape)
