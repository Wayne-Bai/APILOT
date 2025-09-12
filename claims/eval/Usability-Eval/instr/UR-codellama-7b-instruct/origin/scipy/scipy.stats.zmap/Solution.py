
import numpy as np
from scipy import stats

# Define the data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the mean and standard deviation of each column
mean_0 = np.mean(data[:, 0])
std_0 = np.std(data[:, 0])
mean_1 = np.mean(data[:, 1])
std_1 = np.std(data[:, 1])
mean_2 = np.mean(data[:, 2])
std_2 = np.std(data[:, 2])

# Calculate the relative z-scores
rel_z_score_0 = (data[:, 0] - mean_0) / std_0
rel_z_score_1 = (data[:, 1] - mean_1) / std_1
rel_z_score_2 = (data[:, 2] - mean_2) / std_2

# Print the relative z-scores
print(rel_z_score_0)
print(rel_z_score_1)
print(rel_z_score_2)
