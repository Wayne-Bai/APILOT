import numpy as np
from scipy.signal import convolve, boxcar

def gaussian_filter(input_array, sigma):
    # Generate a 1-dimensional Gaussian filter kernel
    kernel = np.exp(-(np.linspace(-3*sigma, 3*sigma, num=len(input_array)))**2 / (2 * sigma**2))
    kernel /= np.sum(kernel)
    
    # Convolve the input array with the kernel
    output = convolve(input_array, kernel, mode='same')
    return output
