import numpy as np
from scipy import stats

# Assuming we have an array of data
data = np.array([1, 2, 3, 4, 5, 6])

mean = np.mean(data)
std_dev = np.std(data)

z_scores = stats.zscore(data)

print("Mean: ", mean)
print("Standard Deviation: ", std_dev)
print("Relative z-scores: ", z_scores)
