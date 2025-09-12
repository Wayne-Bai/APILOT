import numpy as np

# Define an array
arr = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros to the left
padded_arr_left = np.pad(arr, (2, 0), 'constant', constant_values=0)
print("Padded array on left:", padded_arr_left)

# Pad the array with zeros to the right
padded_arr_right = np.pad(arr, (0, 2), 'constant', constant_values=0)
print("Padded array on right:", padded_arr_right)

# Pad the array with zeros both sides
padded_arr_both = np.pad(arr, (1, 1), 'constant', constant_values=0)
print("Padded array on both sides:", padded_arr_both)
