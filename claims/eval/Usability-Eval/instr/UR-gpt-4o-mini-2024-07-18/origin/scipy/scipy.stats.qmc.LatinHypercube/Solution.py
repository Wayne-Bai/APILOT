import numpy as np
from scipy.stats import qmc

def latin_hypercube_sampling(n_samples, n_dimensions):
    # Create a Latin Hypercube Sampling object
    sampler = qmc.LatinHypercube(d=n_dimensions)
    # Generate samples
    sample = sampler.random(n=n_samples)
    return sample

# Example usage
n_samples = 10  # Number of samples
n_dimensions = 3  # Number of dimensions
samples = latin_hypercube_sampling(n_samples, n_dimensions)
print(samples)
