import numpy as np

# Load data from a text file with missing values handled as specified
data = np.loadtxt('data.txt', delimiter=',', usecols=[0, 1, 2], skiprows=1, dtype=str)

# Print the loaded data
print(data)
