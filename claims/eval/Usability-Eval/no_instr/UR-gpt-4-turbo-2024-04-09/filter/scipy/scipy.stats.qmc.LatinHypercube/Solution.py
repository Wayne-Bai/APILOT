import numpy as np
from scipy.stats import qmc

# Define the number of samples and dimensions
num_samples = 10
dimensions = 2

# Create a Latin hypercube sampler
sampler = qmc.LatinHypercube(d=dimensions)

# Generate samples
samples = sampler.random(n=num_samples)

# Optionally, scale the sample to a different range
lower_bounds = [0, 10]
upper_bounds = [1, 20]
scaled_samples = qmc.scale(samples, lower_bounds, upper_bounds)

print("Latin Hypercube Sampling (LHS) Results:")
print(scaled_samples)
