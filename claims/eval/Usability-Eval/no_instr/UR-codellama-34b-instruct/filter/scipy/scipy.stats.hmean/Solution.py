
import numpy as np
from scipy import stats

# Generate some sample data
data = np.random.rand(10, 4)
weights = np.array([2, 3, 5, 7])

# Calculate the weighted harmonic mean along the second axis (axis=1)
mean = stats.weighted_harmonic_mean(data, weights, axis=1)

print(mean)
