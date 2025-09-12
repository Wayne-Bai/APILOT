import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Define the range for the uniform distribution
low = 0.0
high = 1.0

# Generate 10 samples from a uniform distribution
samples = np.random.uniform(low, high, 10)

print(samples)
