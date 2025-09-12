import numpy as np

# Number of random samples
size = 1000

# Define the uniform distribution range
low = 0.0
high = 1.0

# Draw samples
uniform_samples = np.random.uniform(low, high, size)

# Print the first 10 samples
print(uniform_samples[:10])
