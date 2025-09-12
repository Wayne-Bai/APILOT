import numpy as np
from scipy import stats

# Assuming you have some data
data = np.array([10, 21, 18, 19, 22, 16, 23, 21, 17, 20])

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data, ddof=0)  # Calculate standard deviation

# Calculate z-scores
z_scores = stats.zscore(data)

# Calculate relative z-scores
relative_z_scores = np.abs(z_scores) / np.nanstd(z_scores)

print("Z-scores:", z_scores)
print("Relative Z-scores:", relative_z_scores)
