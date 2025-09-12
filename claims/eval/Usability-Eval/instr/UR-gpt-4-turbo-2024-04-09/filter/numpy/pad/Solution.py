import numpy as np

# Sample array
array = np.array([1, 2, 3, 4, 5])

# Pad the array
padded_array = np.pad(array, pad_width=(2, 3), mode='constant', constant_values=(0, 0))

print(padded_array)
