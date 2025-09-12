import numpy as np

# Create an array
array = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros
padded_array = np.pad(array, (2, 3), 'constant', constant_values=0)

print(padded_array)
