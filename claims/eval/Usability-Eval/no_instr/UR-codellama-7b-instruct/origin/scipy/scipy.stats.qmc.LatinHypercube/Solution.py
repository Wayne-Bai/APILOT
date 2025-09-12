
import numpy as np
from scipy import linalg

def latin_hypercube_sampling(dim, num_samples):
    # Generate a random orthonormal matrix using the qr decomposition
    Q = linalg.qr(np.random.randn(dim, dim))[0]
    
    # Compute the Latin hypercube sampling points
    X = np.zeros((num_samples, dim))
    for i in range(num_samples):
        x = np.random.rand(dim)
        X[i, :] = Q @ x + (np.random.rand(1, dim) - 0.5) / num_samples
    
    return X
