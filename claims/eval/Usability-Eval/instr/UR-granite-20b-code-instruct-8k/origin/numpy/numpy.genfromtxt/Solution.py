import numpy as np

# Load data from a text file, with missing values handled as specified
data = np.genfromtxt('data.txt', missing_values='?', filling_values=0)
