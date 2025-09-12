import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Define the parameters of the uniform distribution
minimum = 0.0
maximum = 10.0

# Generate 10 random samples from the uniform distribution
samples = np.random.uniform(minimum, maximum, 10)

print(samples)
