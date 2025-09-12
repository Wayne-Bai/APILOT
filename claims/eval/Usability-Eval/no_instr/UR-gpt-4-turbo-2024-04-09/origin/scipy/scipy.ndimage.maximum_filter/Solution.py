import scipy.ndimage as ndimage
import numpy as np

def multidimensional_maximum_filter(data, size=3):
    filtered_data = ndimage.maximum_filter(data, size=size)
    return filtered_data

# Example usage:
data = np.random.rand(4, 4, 4)  # A random 3D array
size = 2  # Size of the filter
result = multidimensional_maximum_filter(data, size)
print("Original Data:\n", data)
print("Filtered Data:\n", result)
