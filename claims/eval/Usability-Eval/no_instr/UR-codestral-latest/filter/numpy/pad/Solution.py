import numpy as np

# Assume this is your array
array = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros at the beginning and end
padded_array = np.pad(array, pad_width=(5, 5), mode='constant', constant_values=(0, 0))

print(padded_array)
