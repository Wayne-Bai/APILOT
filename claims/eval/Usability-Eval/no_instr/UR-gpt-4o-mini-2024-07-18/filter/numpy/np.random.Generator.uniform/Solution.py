import numpy as np

# Draw samples from a uniform distribution between a and b
a = 0  # lower bound
b = 1  # upper bound
size = 10  # number of samples

samples = np.random.uniform(a, b, size)
print(samples)
