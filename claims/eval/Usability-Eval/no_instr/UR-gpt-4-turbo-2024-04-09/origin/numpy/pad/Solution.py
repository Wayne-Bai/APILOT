import numpy as np

# Create an example array
array = np.array([1, 2, 3, 4, 5])

# Define padding widths and the padding mode
pad_width = 1  # Pad with one element on each side
pad_value = 0  # Pad using a constant value (0 in this case)

# Pad the array
padded_array = np.pad(array, pad_width, mode='constant', constant_values=pad_value)

print(padded_array)
