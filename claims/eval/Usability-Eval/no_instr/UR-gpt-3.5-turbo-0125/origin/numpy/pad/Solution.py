
import numpy as np

# Define array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Pad array with zeros
padded_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)

print(padded_arr)
