from scipy.stats.distributions import uniform
import numpy as np

def latin_hypercube_sampling(dim, n_samples):
    if n_samples > dim:
        raise ValueError("Number of samples should be less than or equal to the dimension.")

    samples = np.zeros((dim, n_samples))

    for i in range(dim):
        U = uniform.rvs(size=n_samples)
        samples[i] = U

    return samples

# Example usage:
dim = 3  # Dimension of the problem
n_samples = 10  # Number of samples to generate

samples = latin_hypercube_sampling(dim, n_samples)
print(samples)
