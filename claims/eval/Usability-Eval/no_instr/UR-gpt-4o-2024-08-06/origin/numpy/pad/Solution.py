import numpy as np

# Example array
array = np.array([1, 2, 3, 4, 5])

# Padding configuration
pad_width = 2  # Number of values padded to the edges of each axis
pad_value = 0  # Value for the padded elements

# Pad the array
padded_array = np.pad(array, pad_width=pad_width, mode='constant', constant_values=pad_value)

print("Original Array:", array)
print("Padded Array:", padded_array)
