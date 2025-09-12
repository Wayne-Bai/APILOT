
import numpy as np

# Create an array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Pad the array with zeros to size (3, 4)
padded_arr = np.pad(arr, ((0, 1), (0, 1)), 'constant')

print(padded_arr)
