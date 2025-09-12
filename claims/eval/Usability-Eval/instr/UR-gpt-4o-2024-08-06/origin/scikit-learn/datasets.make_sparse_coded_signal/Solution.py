import numpy as np
from sklearn.linear_model import OrthogonalMatchingPursuit

def generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs, random_state=None):
    rng = np.random.RandomState(random_state)

    # Create a random dictionary D
    D = rng.randn(n_features, n_components)

    # Normalize columns to have unit norm
    D /= np.sqrt((D ** 2).sum(axis=0))

    # Initialize X with zeros
    X = np.zeros((n_components, n_samples))

    for i in range(n_samples):
        # Randomly select indices for non-zero elements
        non_zero_indices = rng.choice(n_components, n_nonzero_coefs, replace=False)
        X[non_zero_indices, i] = rng.randn(n_nonzero_coefs)

    # Generate the signal Y
    Y = np.dot(D, X)

    return Y, D, X

# Parameters
n_features = 10
n_components = 5
n_samples = 8
n_nonzero_coefs = 2

# Generate the sparse signal
Y, D, X = generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs, random_state=0)

print("Dictionary D:")
print(D)
print("\nSparse code X:")
print(X)
print("\nGenerated signal Y:")
print(Y)
