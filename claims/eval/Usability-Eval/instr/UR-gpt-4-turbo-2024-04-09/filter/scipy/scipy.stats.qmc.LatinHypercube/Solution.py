import numpy as np
from scipy.stats import qmc

# Define the sample size and dimension
sample_size = 10
dimensions = 2

# Create a Latin Hypercube Sampler
sampler = qmc.LatinHypercube(d=dimensions)

# Generate samples
samples = sampler.random(n=sample_size)

# Transform samples to real scale if necessary, here using uniform distribution as an example
lower_bounds = [0, 0]
upper_bounds = [1, 1]
samples_scaled = qmc.scale(samples, lower_bounds, upper_bounds)

print(samples_scaled)
