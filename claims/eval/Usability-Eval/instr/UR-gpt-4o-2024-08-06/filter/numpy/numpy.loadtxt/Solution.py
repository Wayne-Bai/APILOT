import numpy as np

# Define the file path
file_path = 'data.txt'

# Load data from the text file
data = np.genfromtxt(file_path, delimiter=',')

print(data)
