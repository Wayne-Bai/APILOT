import numpy as np

# Read data from text file
data = np.loadtxt('data.txt', delimiter=',', skiprows=1, usecols=(0, 1, 2))

# Handle missing values
# For example, replace missing values with the mean of the column
mean = np.nanmean(data[:, 1])
data[np.isnan(data[:, 1])] = mean

# Print the data
print(data)
