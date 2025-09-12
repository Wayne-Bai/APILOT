import numpy as np
import scipy.ndimage

def multidim_median_filter(input_data, filter_size):
    # Apply median filter to each dimension individually
    filtered_data = scipy.ndimage.median_filter(input_data, size=filter_size)
    return filtered_data

# Example usage:
input_array = np.array([[4, 0, 0, 0, 0, 0, 7, 0, 0],
                        [0, 6, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 9, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 8, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 5, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1]])

filter_size = 3
filtered_array = multidim_median_filter(input_array, filter_size)
print(filtered_array)
