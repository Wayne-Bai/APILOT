import numpy as np

def pad_array(arr, pad_width, constant_values=0):
    return np.pad(arr, pad_width, mode='constant', constant_values=constant_values)

# Example usage
array = np.array([[1, 2], [3, 4]])
padded_array = pad_array(array, pad_width=1, constant_values=0)
print(padded_array)
