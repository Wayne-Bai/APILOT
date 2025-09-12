import numpy as np

# Load data from text file
data = np.loadtxt('data.txt')

# Handle missing values
data[np.isnan(data)] = 0

# Print data
print(data)
