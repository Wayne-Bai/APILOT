import numpy as np
from scipy import stats

# Example data
data = np.array([10, 12, 23, 23, 16, 23, 21, 16])

# Calculate the mean and standard deviation
mean_value = np.mean(data)
std_dev = np.std(data, ddof=0)

# Compute the coefficient of variation
coefficient_of_variation = (std_dev / mean_value) * 100

print(f"Coefficient of Variation: {coefficient_of_variation:.2f}%")
