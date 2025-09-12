import numpy as np

# Create a 1D array
array = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros at the beginning and end
padded_array = np.pad(array, (2, 2), 'constant', constant_values=(0))

print(padded_array)
