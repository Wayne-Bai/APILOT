import numpy as np

# Load data from a text file using np.genfromtxt
data = np.genfromtxt('data.txt', delimiter=',', skip_header=1)

# Display the loaded data
print(data)
