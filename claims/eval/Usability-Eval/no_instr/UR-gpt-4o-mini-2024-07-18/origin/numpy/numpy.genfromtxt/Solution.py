import numpy as np

# Load data from a text file, replace missing values with NaN
data = np.loadtxt('data.txt', delimiter=',', dtype=float, missing_values='NaN')

# For example, if you want to replace missing values with the mean of each column
means = np.nanmean(data, axis=0)
indices = np.where(np.isnan(data))
data[indices] = np.take(means, indices[1])
