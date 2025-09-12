import numpy as np
from scipy.stats.qmc import LatinHypercube

def latin_hypercube_sampling(n_samples, n_dimensions):
    # Initialize the LatinHypercube sampler
    sampler = LatinHypercube(d=n_dimensions)
    
    # Generate samples
    samples = sampler.random(n=n_samples)
    
    return samples

# Example usage
n_samples = 10
n_dimensions = 2
samples = latin_hypercube_sampling(n_samples, n_dimensions)
print(samples)
