import numpy as np

# Load data from a text file
data = np.genfromtxt('data.txt', delimiter=',', missing_values=[-999.0, -999.9, -9999.0], filling_values=[0.0, 0.001, 0.0001])

# Print the data
print(data)
