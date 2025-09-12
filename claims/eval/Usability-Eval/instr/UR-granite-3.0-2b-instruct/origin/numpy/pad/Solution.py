import numpy as np

# Create a sample array
arr = np.array([1, 2, 3, 4, 5])

# Define the padding value
padding_value = 0

# Pad the array with the specified value
padded_arr = np.pad(arr, (2, 2), 'constant', constant_values=(padding_value,))

# Print the original and padded arrays
print("Original Array:")
print(arr)
print("\nPadded Array:")
print(padded_arr)
