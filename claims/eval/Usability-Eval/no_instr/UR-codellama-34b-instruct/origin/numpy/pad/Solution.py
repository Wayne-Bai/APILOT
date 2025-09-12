
import numpy as np

# Define the original array
arr = np.array([1, 2, 3])

# Define the padding size
padding_size = 2

# Pad the array with zeros
padded_arr = np.pad(arr, (padding_size,), 'constant')

print(padded_arr)
