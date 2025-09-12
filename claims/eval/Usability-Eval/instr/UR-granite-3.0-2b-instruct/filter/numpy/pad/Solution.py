import numpy as np

# Original array
arr = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros on the right side
padded_arr = np.pad(arr, (0, 2), 'constant')

print("Original Array:")
print(arr)

print("\nPadded Array:")
print(padded_arr)
