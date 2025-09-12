import numpy as np
from scipy.stats import uniform

def lhs_sampling(n_samples, n_dim, low, high):
    # Create a Latin hypercube design matrix
    lhs = np.zeros((n_samples, n_dim))
    for j in range(n_dim):
        lhs[:, j] = np.linspace(low, high, n_samples)
        np.random.shuffle(lhs[:, j])
    return lhs

# Example usage:
n_samples = 100
n_dim = 3
low = 0
high = 1
lhs = lhs_sampling(n_samples, n_dim, low, high)
print(lhs)
