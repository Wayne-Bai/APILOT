import numpy as np

# Original array
arr = np.array([1, 2, 3, 4, 5])

# Define the padding value
padding_value = 0

# Calculate the number of elements to pad
num_pad = 2

# Pad the array
padded_arr = np.pad(arr, (num_pad, num_pad), 'constant', constant_values=(padding_value,))

print("Original Array:")
print(arr)

print("\nPadded Array:")
print(padded_arr)
