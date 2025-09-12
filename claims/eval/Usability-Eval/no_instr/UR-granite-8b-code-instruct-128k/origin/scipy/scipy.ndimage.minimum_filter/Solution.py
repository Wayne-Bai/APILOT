from scipy import ndimage
import numpy as np

def minimum_filter(input, size):
    return ndimage.minimum_filter(input, size=size)

input_array = np.array([[5, 2, 9], [1, 3, 7], [4, 6, 8]])
filtered_array = minimum_filter(input_array, size=(2, 2))
print(filtered_array)
