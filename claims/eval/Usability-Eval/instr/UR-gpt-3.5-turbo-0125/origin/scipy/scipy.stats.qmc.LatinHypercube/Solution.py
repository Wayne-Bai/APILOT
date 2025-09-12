
# Latin Hypercube Sampling (LHS) without using outdated scipy APIs

import numpy as np

def latin_hypercube(n, d):
    samples = np.random.rand(n, d)
    for i in range(d):
        samples[:, i] = (samples[:, i] + np.random.permutation(samples[:, i])) / n
    
    return samples

# Example usage
num_samples = 10
num_dimensions = 2
lhs_samples = latin_hypercube(num_samples, num_dimensions)
print(lhs_samples)
