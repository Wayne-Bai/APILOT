import numpy as np

# Load data from text file
data = np.loadtxt('file.txt', skiprows=1)

# Handle missing values by replacing them with NaN
data[np.isnan(data)] = np.nanmean(data)

# Print the resulting array
print(data)
