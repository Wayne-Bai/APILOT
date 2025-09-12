import numpy as np
from scipy.stats import qmc

# Define the number of samples and dimensions
n = 1000
d = 3

# Define the lower and upper bounds for each dimension
l_bounds = np.array([0, 0, 0])
u_bounds = np.array([1, 1, 1])

# Create the latin hypercube sampling object
sampler = qmc.LatinHypercube(d)

# Generate sample points
sample = sampler.random(n)

# Scale the sample points to the desired range
lhs = qmc.scale(sample, l_bounds, u_bounds)
