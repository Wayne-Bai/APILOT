import scipy.stats as stats
import numpy as np

# Define the data
data = np.array([[1, 2, 3], [4, 5, 6]])

# Define the weights
weights = np.array([[0.2, 0.3, 0.5], [0.4, 0.3, 0.3]])

# Calculate the weighted harmonic mean along the specified axis
weighted_harmonic_mean = stats.hmean(data, axis=1, weights=weights)

print("Weighted harmonic mean along axis 1:", weighted_harmonic_mean)
