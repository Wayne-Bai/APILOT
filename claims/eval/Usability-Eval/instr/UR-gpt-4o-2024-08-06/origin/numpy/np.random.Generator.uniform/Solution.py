import numpy as np

# Define the parameters for the uniform distribution
low = 0.0  # Lower boundary of the output interval
high = 1.0  # Upper boundary of the output interval
size = 10  # Number of samples to draw

# Draw samples from a uniform distribution
samples = np.random.uniform(low, high, size)

# Print the samples
print("Samples drawn from a uniform distribution:", samples)
