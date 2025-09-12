import numpy as np

def pad_array(array, pad_width):
    return np.pad(array, pad_width, mode='constant')

# Usage
a = np.array([[1, 2, 3], [4, 5, 6]])
print(pad_array(a, ((1, 2), (2, 1))))
