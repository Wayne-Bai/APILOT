import numpy as np

# Create a sample array
arr = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros
padded_arr = np.pad(arr, (2, 2), 'constant')

print(padded_arr)
