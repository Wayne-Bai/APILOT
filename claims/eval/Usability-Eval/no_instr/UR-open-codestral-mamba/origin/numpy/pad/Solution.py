import numpy as np

# Original array
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(arr)

# Padding array with zeros
padded_arr = np.pad(arr, (2, 2), 'constant', constant_values=0)
print("\nArray after padding with 2 zeros:")
print(padded_arr)

# Padding array with a specific value
padded_arr_val = np.pad(arr, (1, 1), 'constant', constant_values=99)
print("\nArray after padding with 1 '99':")
print(padded_arr_val)
