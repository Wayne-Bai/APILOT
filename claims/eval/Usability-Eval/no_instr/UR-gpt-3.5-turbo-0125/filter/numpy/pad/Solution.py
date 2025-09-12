
import numpy as np

def pad_array(arr, pad_width, mode='constant', constant_values=0):
    return np.pad(arr, pad_width, mode, constant_values)

# Example Usage
arr = np.array([[1, 2], [3, 4]])
padded_arr = pad_array(arr, 1, 'constant', constant_values=0)
print(padded_arr)
