import numpy as np
from scipy.signal import convolve2d

def multidimensional_minimum_filter(image, filter_size=(3, 3)):
    kernel_size = (filter_size[0], filter_size[1])
    kernel = np.ones(kernel_size)/np.prod(kernel_size)
    return convolve2d(image, kernel, mode='same')

# Example usage:
image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filtered_image = multidimensional_minimum_filter(image)
print(filtered_image)
