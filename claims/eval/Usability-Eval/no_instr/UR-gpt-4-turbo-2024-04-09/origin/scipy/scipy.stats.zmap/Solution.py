import scipy.stats as stats
import numpy as np

# Sample data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Calculate the z-scores
z_scores = stats.zscore(data)

print("Z-scores:", z_scores)
