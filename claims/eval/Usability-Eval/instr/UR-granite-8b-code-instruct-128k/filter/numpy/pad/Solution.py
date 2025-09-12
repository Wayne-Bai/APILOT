import numpy as np

# Example array
arr = np.array([1, 2, 3])

# Pad the array with zeros
padded_arr = np.pad(arr, (3, 4), 'constant', constant_values=0)

print(padded_arr)
