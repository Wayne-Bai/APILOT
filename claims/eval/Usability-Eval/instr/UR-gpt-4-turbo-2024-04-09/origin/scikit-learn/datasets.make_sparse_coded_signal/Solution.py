import numpy as np
from sklearn.datasets import make_sparse_coded_signal

n_components = 5    # Number of dictionary elements (atoms)
n_features = 10     # Number of features of each atom
n_nonzero_coefs = 3 # Number of nonzero coefficients in the linear combination
n_samples = 100     # Number of signals to generate

# Generate the sparse coded signal
Y, D, X_true = make_sparse_coded_signal(n_samples=n_samples,
                                        n_components=n_components,
                                        n_features=n_features,
                                        n_nonzero_coefs=n_nonzero_coefs,
                                        random_state=42)

print("Dictionary matrix (D) shape:", D.shape)
print("Sparse code matrix (X) shape:", X_true.shape)
print("Signal matrix (Y) shape:", Y.shape)
