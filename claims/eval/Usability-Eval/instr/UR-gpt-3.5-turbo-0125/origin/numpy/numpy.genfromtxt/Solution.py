
import numpy as np

# Load data from a text file
data = np.genfromtxt('data.txt', delimiter=',', missing_values='NA', filling_values=0)

print(data)
