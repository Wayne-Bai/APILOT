import numpy as np

# Example input array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the pad width (padding will occur on both sides)
pad_width = 2

# Define the mode for padding (constant)
mode = 'constant'

# Define the constant value for padding (0 by default)
constant_values = 0

# Pad the array
padded_array = np.pad(array, pad_width, mode=mode, constant_values=constant_values)

print(padded_array)
