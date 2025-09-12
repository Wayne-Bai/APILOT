import numpy as np
from scipy.stats import hmean

# Assuming 'data' is your input array and 'weights' is the corresponding weight array
data = np.array([1, 2, 3, 4, 5])
weights = np.array([0.1, 0.2, 0.3, 0.2, 0.2])

# Calculate the weighted harmonic mean along the specified axis
weighted_harmonic_mean = hmean(data, weights)

print("Weighted Harmonic Mean:", weighted_harmonic_mean)
