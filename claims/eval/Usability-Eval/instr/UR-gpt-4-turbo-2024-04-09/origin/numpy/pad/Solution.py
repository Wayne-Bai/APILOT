import numpy as np

# Example array
array = np.array([1, 2, 3])

# Padding configuration
pad_width = 1  # Padding by 1 on both sides of the array
pad_value = 0  # Fill with zeros

# Using np.pad to pad the array
padded_array = np.pad(array, pad_width, constant_values=pad_value)

print(padded_array)
