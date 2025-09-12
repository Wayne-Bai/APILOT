import numpy as np
from scipy import signal
from scipy.special import kv

def gaussian_filter_2d(arr, sigma, size):
    """
    Multidimensional Gaussian filter.

    Parameters:
    arr (numpy.ndarray): Input array.
    sigma (float): Standard deviation of the Gaussian filter.
    size (int): Size of the filter (must be an odd number).

    Returns:
    filtered_arr (numpy.ndarray): Filtered array.
    """

    # Create a 2D Gaussian filter kernel
    x = np.linspace(-size//2 + 1, size//2, size)
    gaussian = np.exp(-((x/sigma)**2))
    
    gaussian_kernel = gaussian[:, np.newaxis] * gaussian[newaxis, :]
    
    # Change the shape of the kernel so it can be passed to convolve2d
    kernel = gaussian_kernel / np.sum(gaussian_kernel)
    
    # Apply the Gaussian filter
    filtered_arr = signal.convolve2d(arr, kernel, mode='same')
    
    return filtered_arr

# Example usage
arr = np.random.rand(10, 10)
sigma = 2
size = 5

filtered_arr = gaussian_filter_2d(arr, sigma, size)

print("Original array:")
print(arr)
print("\nFiltered array:")
print(filtered_arr)
