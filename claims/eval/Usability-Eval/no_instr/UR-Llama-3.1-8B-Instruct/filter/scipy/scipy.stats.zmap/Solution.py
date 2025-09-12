import numpy as np
from scipy import stats

# Let's assume we have the following data
data = np.array([1, 2, 3, 4, 5])

# If you want to calculate the relative z-scores for the entire dataset
mean = np.mean(data)
std_dev = np.std(data)
relative_z_scores = (data - mean) / std_dev

print("Original Data: ", data)
print("Mean: ", mean)
print("Standard Deviation: ", std_dev)
print("Relative Z-Scores: ", relative_z_scores)

# If you want to calculate the relative z-scores for a specific value
value = 3
mean = np.mean(data)
std_dev = np.std(data)
relative_z_score = (value - mean) / std_dev
print("Relative Z-Score for {} is: {}".format(value, relative_z_score))
