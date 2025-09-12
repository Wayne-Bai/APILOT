import numpy as np

# Define a 2D array
my_array = np.array([[1, 2], [3, 4]])

# Pad the array with zeros
padded_array = np.pad(my_array, (0, 2), 'constant')

print(padded_array)
