
import numpy as np
from scipy.stats import hmean

# Example data
data = np.array([[1, 2], [3, 4]])
weights = np.array([0.5, 0.5])

# Calculate the weighted harmonic mean
hmean_result = hmean(data, weights=weights)

print(hmean_result)
