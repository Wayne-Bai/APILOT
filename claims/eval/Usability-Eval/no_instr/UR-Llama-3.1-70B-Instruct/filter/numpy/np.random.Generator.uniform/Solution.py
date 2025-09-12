# Import the numpy library
import numpy as np

# Define the lower and upper bounds of the uniform distribution
lower_bound = 0
upper_bound = 100

# Define the number of samples to draw from the uniform distribution
num_samples = 10

# Draw samples from a uniform distribution
samples = np.random.uniform(lower_bound, upper_bound, num_samples)

# Print the drawn samples
print("Samples drawn from a uniform distribution:")
print(samples)

# Print specific statistics about the samples if desired
print("\nStatistics about the samples:")
print(f"Mean: {np.mean(samples)}")
print(f"Median: {np.median(samples)}")
print(f"Standard Deviation: {np.std(samples)}")
