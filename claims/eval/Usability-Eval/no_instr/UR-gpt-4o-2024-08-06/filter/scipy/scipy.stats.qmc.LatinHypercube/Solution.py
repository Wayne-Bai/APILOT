import numpy as np
from scipy.stats.qmc import LatinHypercube

# Define number of dimensions and samples
n_dimensions = 3
n_samples = 10

# Create a LatinHypercube sampler instance
sampler = LatinHypercube(d=n_dimensions)

# Generate samples
samples = sampler.random(n=n_samples)

print("Generated Latin Hypercube Samples:")
print(samples)
