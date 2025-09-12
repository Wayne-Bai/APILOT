
import numpy as np

# Create a sample array
arr = np.array([1, 2, 3, 4])

# Pad the array with 0's on both sides
padded_arr = np.pad(arr, (2, 2), mode='constant')
print(padded_arr)
