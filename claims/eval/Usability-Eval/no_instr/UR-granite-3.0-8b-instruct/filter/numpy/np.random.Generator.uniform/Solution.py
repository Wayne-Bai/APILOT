import numpy as np

# Set the range for the uniform distribution
low = 0
high = 10

# Set the number of samples to draw
num_samples = 1000

# Draw samples from the uniform distribution
samples = np.random.uniform(low, high, num_samples)

# Print the samples
print(samples)
