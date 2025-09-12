import numpy as np
from scipy import stats

# Example data: your data should be replaced with your actual data
data = np.array([10, 20, 30, 40, 50])

# Calculate sample mean and sample standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Compute coefficient of variation
cv = std_dev / mean

print(f"Coefficient of Variation: {cv:.2f}")
