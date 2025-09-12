import numpy as np

# Load data from a text file
data = np.loadtxt('file.txt', delimiter=',', skiprows=1)

# Handle missing values
data[np.isnan(data)] = np.mean(data)

# Print the data
print(data)
