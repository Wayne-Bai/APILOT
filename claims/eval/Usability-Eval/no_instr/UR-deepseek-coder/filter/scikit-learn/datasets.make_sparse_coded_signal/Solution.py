import numpy as np
from sklearn.utils.extmath import randomized_svd

def generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs):
    # Generate a random dictionary D
    D = np.random.randn(n_features, n_components)
    
    # Normalize the dictionary to ensure each column has unit norm
    D /= np.linalg.norm(D, axis=0)
    
    # Initialize the sparse coefficient matrix X
    X = np.zeros((n_components, n_samples))
    
    # Generate sparse coefficients for each sample
    for i in range(n_samples):
        # Randomly select n_nonzero_coefs indices
        nonzero_indices = np.random.choice(n_components, n_nonzero_coefs, replace=False)
        
        # Assign random values to these indices
        X[nonzero_indices, i] = np.random.randn(n_nonzero_coefs)
    
    # Generate the signal Y = DX
    Y = np.dot(D, X)
    
    return Y, D, X

# Example usage
n_features = 100
n_components = 20
n_samples = 50
n_nonzero_coefs = 5

Y, D, X = generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs)

print("Shape of Y:", Y.shape)
print("Shape of D:", D.shape)
print("Shape of X:", X.shape)
