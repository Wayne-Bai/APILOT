import numpy as np

def pad_array(arr, side=1):
    result = np.pad(arr, ((side, side), (side, side)), mode='constant', constant_values=0)
    return result

# Example usage:
array = np.array([[1, 2, 3], [4, 5, 6]])
padded_array = pad_array(array, side=2)
print(padded_array)
