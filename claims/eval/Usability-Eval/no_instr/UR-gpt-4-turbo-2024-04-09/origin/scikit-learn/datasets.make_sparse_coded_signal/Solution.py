import numpy as np
from sklearn.datasets import make_sparse_coded_signal

# Parameters for the generated signal
n_components = 8     # Number of dictionary elements (atoms)
n_features = 100     # Number of features in dictionary atoms
n_nonzero_coefs = 3  # Number of active (nonzero) coefficients in the signal representation

# Generate dataset
Y, D, X = make_sparse_coded_signal(n_samples=1,
                                   n_components=n_components,
                                   n_features=n_features,
                                   n_nonzero_coefs=n_nonzero_coefs,
                                   random_state=42)

# Y is the generated signal as a sparse combination of dictionary D on basis X
print("Generated signal (Y):")
print(Y)
print("\nDictionary (D):")
print(D)
print("\nSparse code (X):")
print(X)
