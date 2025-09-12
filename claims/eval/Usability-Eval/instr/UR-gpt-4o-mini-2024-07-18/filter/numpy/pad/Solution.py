import numpy as np

# Create a sample array
array = np.array([1, 2, 3])

# Pad the array with zeros on both sides
padded_array = np.pad(array, pad_width=2, mode='constant', constant_values=0)

print(padded_array)
