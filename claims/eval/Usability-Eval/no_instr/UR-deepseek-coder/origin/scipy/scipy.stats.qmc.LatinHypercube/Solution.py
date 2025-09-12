import numpy as np
from scipy.stats import qmc

# Define the number of samples and the number of dimensions
n_samples = 10
n_dimensions = 2

# Create a LatinHypercube instance
sampler = qmc.LatinHypercube(d=n_dimensions)

# Generate samples
samples = sampler.random(n=n_samples)

# Optionally, scale the samples to a specific range
lower_bounds = [0, 0]
upper_bounds = [10, 10]
scaled_samples = qmc.scale(samples, lower_bounds, upper_bounds)

print("Scaled Samples:\n", scaled_samples)
