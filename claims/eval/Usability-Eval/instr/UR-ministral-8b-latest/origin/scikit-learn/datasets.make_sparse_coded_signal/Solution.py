import numpy as np
from sklearn.decomposition import TruncatedSVD

# Generate signal as a sparse combination of dictionary elements
def generate_signal(dim, n_components, n_samples, n_nonzero_coefs):
    # Generate random data for the dictionary
    D = np.random.randn(dim, n_components)

    # Introduce sparsity by setting non-zero coefficients
    np.fill_diagonal(D, 0)
    nonzeros = np.random.rand(n_samples) < 0.1  # Set sparsity level
    X = np.random.randn(n_components, n_samples)

    # Restrict X to have n_nonzero_coefs non-zero elements per column
    for i in range(n_samples):
        non_zero_idx = np.random.choice(n_components, n_nonzero_coefs, replace=False)
        X[:, i] = 0  # Reset X for this sample
        X[non_zero_idx, i] = np.random.randn(n_nonzero_coefs)

    # Apply D to X to generate the signal
    Y = np.dot(D, X)

    return Y, D

# Example usage
dim = 100    # Dimensionality of dictionary elements
n_components = 20  # Number of dictionary components
n_samples = 50  # Number of samples
n_nonzero_coefs = 5  # Number of non-zero coefficients per normalized column

Y, D = generate_signal(dim, n_components, n_samples, n_nonzero_coefs)

print("Generated matrix Y shape:", Y.shape)
print("Dictionary matrix D shape:", D.shape)
