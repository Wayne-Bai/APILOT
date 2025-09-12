import numpy as np

# Generate random data
data = np.random.rand(3, 4)

# Set the padding parameters
pad_width = (1, 1)  # left and right padding
pad_value = 0.0     # value to fill the padding with

# Pad the array using numpy.pad() function
padded_data = np.pad(data, pad_width, mode='constant', constant_values=pad_value)
