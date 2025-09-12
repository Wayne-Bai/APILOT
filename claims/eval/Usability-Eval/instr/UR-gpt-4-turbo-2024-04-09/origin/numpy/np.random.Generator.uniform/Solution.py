import numpy as np

# Parameters for the uniform distribution range
low = 0    # lower boundary of the output interval
high = 1   # upper boundary of the output interval
size = 1000  # number of samples

# Drawing samples from a uniform distribution
samples = np.random.default_rng().uniform(low, high, size)
