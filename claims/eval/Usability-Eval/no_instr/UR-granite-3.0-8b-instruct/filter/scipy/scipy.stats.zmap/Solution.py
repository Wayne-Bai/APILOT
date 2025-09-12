import numpy as np
from scipy.stats import zscore

# Assuming 'data' is your dataset
data = np.array([1, 2, 3, 4, 5])

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std_dev = np.std(data)

# Calculate the z-scores
z_scores = (data - mean) / std_dev

# Calculate the relative z-scores
relative_z_scores = z_scores / np.abs(z_scores).max()

print(relative_z_scores)
