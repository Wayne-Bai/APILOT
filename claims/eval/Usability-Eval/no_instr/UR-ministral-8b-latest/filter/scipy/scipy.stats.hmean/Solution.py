import numpy as np
from scipy.stats import hmean

# Example data: Replace these with your actual data
weights = np.array([1.0, 2.0, 3.0])
values = np.array([10, 20, 30])

# Calculate the weighted harmonic mean along axis 0
weighted_harmonic_mean = hmean(values, weights)

print("Weighted Harmonic Mean:", weighted_harmonic_mean)
