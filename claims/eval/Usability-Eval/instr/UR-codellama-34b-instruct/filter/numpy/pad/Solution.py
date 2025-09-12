
import numpy as np

# Create a sample array
arr = np.array([[1, 2], [3, 4]])

# Pad the array with a value of 0 at the beginning and end
padded_arr = np.pad(arr, (1, 1), 'constant')

print(padded_arr)
