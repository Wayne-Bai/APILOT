import numpy as np
from scipy import stats

# Sample data
data = [10, 20, 30, 40, 50]

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std_dev = np.std(data)

# Calculate the z-scores for the data
z_scores = stats.zscore(data)

# Output the z-scores
print("Z-scores:", z_scores)
