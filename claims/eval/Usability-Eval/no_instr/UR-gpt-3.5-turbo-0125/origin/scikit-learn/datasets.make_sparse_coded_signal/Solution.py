
import numpy as np

def generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs):
    D = np.random.randn(n_features, n_components)
    X = np.zeros((n_components, n_samples))
    
    for i in range(n_samples):
        indices = np.random.choice(n_components, n_nonzero_coefs, replace=False)
        values = np.random.randn(n_nonzero_coefs)
        X[indices, i] = values
    
    Y = np.dot(D, X)
    
    return Y

# Example usage
n_features = 10
n_components = 5
n_samples = 100
n_nonzero_coefs = 2

Y = generate_sparse_signal(n_features, n_components, n_samples, n_nonzero_coefs)
print(Y)
