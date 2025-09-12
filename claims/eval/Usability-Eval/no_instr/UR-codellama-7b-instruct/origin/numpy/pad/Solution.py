import numpy as np

# Define the original array
arr = np.array([1, 2, 3])

# Pad the array with a size of 2 on both sides
padded_arr = np.pad(arr, (2, 2), mode='constant', constant_values=0)

print(padded_arr)
