import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Define the parameters of the uniform distribution
low = 0
high = 10

# Draw samples from the uniform distribution
samples = np.random.uniform(low, high, 10)

# Print the samples
print("Samples from the uniform distribution:")
print(samples)

# Calculate the minimum, maximum, mean and standard deviation of the samples
min_val = np.min(samples)
max_val = np.max(samples)
mean = np.mean(samples)
std_dev = np.std(samples)

# Print the calculated values
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")
print(f"Mean: {mean}")
print(f"Standard deviation: {std_dev}")
