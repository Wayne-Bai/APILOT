import numpy as np

# Assuming arr is your array and pad_width is the number of values to be added at the beginning and end of each axis
def pad_array(arr, pad_width):
    return np.pad(arr, pad_width, mode='constant')

# Example usage:
arr = np.array([1, 2, 3])
pad_width = (2, 2)
padded_arr = pad_array(arr, pad_width)
print(padded_arr)
