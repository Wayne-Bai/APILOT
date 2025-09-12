import numpy as np

# Load data from a text file
data = np.loadtxt('path_to_file.txt')

# Handle missing values
# Assuming missing values are represented by '#'
data = np.where(data == '#', np.nan, data)

# Display the data without missing values
print(data)
