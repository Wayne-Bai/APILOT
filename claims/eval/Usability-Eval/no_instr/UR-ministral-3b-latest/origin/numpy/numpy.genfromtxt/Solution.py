import numpy as np

# Load data from a text file
data = np.loadtxt('data.txt')

# Fill missing values with the mean of the respective column
data = np.nan_to_num(data, nan=np.nanmean(data, axis=0))

# Convert the missing values to zero again for consistency
data = np.where(np.isnan(data), 0, data)

# Print the data
print(data)
