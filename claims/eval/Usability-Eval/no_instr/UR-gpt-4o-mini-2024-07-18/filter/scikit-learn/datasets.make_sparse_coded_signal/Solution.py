import numpy as np
from sklearn.utils import check_random_state

def generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs, random_state=None):
    rng = check_random_state(random_state)
    
    # Generate the dictionary D
    D = rng.randn(n_features, n_components)
    
    # Generate a sparse matrix X
    X = np.zeros((n_components, n_samples))
    
    for i in range(n_samples):
        # Randomly choose n_nonzero_coefs indices to set to non-zero values
        nonzero_indices = rng.choice(n_components, n_nonzero_coefs, replace=False)
        # Assign random values to those indices
        X[nonzero_indices, i] = rng.randn(n_nonzero_coefs)
    
    # Generate the signal Y
    Y = D @ X
    
    return Y, D, X

# Example usage
n_features = 10
n_components = 5
n_samples = 3
n_nonzero_coefs = 2
Y, D, X = generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs)
