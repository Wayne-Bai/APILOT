# importing the necessary library
import numpy as np

# Load data from text file
data = np.loadtxt("filename.txt")

# Find indices of missing values in the data
missing_values = np.isnan(data)

# Compute the mean of the non-missing values in each column
mean_values = np.nanmean(data, axis=0)

# Replace the missing values with the mean of the corresponding column
data[missing_values] = np.take(mean_values, np.argwhere(missing_values)[:, 1])
