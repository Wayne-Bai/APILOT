import numpy as np
from scipy.stats import qmc

# Number of samples
n_samples = 10

# Number of dimensions
n_dimensions = 2

# Create a Latin Hypercube Sampling (LHS) instance
sampler = qmc.LatinHypercube(d=n_dimensions)

# Generate samples
samples = sampler.random(n=n_samples)

# Optionally scale samples to a different range
# For example, scale to [0, 1] range
scaled_samples = qmc.scale(samples, 0, 1)

print("LHS Samples:")
print(samples)
print("Scaled Samples:")
print(scaled_samples)
