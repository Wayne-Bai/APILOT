import numpy as np

# Define the shape for the output. In this case, it will be a 1-dimensional array with 10 elements.
size = 10

# Set the low and high of the uniform distribution.
low = 0
high = 1

# Generate the samples.
samples = np.random.uniform(low, high, size)

# Print the samples.
print(samples)
