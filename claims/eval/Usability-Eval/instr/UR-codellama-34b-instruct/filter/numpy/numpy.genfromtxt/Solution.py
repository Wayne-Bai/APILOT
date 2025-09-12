import numpy as np

# Load data from a text file
data = np.loadtxt('data.txt', dtype=np.float64)

# Handle missing values by setting them to NaN
missing_value = np.nan
data[np.isnan(data)] = missing_value

# Print the resulting array with missing values handled
print(data)
