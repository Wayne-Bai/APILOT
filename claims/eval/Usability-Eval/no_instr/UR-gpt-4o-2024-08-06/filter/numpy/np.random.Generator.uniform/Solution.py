import numpy as np

# Parameters for the uniform distribution
low = 0.0    # Lower boundary of the output interval
high = 1.0   # Upper boundary of the output interval
size = 1000  # Number of samples to draw

# Draw samples from a uniform distribution
samples = np.random.uniform(low, high, size)

# Display the samples
print(samples)
