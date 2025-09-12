import numpy as np
from sklearn.datasets import make_sparse_coded_signal

# Parameters
n_components = 3  # Number of dictionary elements
n_samples = 100   # Number of samples
n_features = 10   # Number of features
n_nonzero_coefs = 2  # Non-zero coefficients per sample

# Generate a sparse coded signal
D, X, Y = make_sparse_coded_signal(n_samples=n_samples, n_components=n_components, 
                                    n_features=n_features, n_nonzero_coefs=n_nonzero_coefs)

# D is the dictionary (shape: n_features, n_components)
# X is the sparse code (shape: n_components, n_samples)
# Y is the generated signal (shape: n_features, n_samples)

print("Dictionary D:\n", D)
print("Sparse code X:\n", X)
print("Generated signal Y:\n", Y)
