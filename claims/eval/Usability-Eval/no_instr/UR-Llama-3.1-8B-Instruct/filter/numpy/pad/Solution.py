# Importing the numpy library
import numpy as np

# Define the array to be padded
array = np.array([1, 2, 3])

# Define the length of the padded array
padded_length = 5

# Calculate the number of elements to be padded on each side
padding = (padded_length - array.shape[0]) // 2

# Pad the array with zeros
padded_array = np.pad(array, (padding, padding + (array.size - padding * 2)))

print(padded_array)
