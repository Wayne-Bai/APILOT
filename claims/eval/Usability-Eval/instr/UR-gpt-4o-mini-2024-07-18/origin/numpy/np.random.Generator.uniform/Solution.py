import numpy as np

# Parameters for the uniform distribution
low = 0.0    # lower bound
high = 1.0   # upper bound
size = 10    # number of samples to draw

# Draw samples from a uniform distribution
samples = np.random.uniform(low, high, size)

# Output the samples
print(samples)
