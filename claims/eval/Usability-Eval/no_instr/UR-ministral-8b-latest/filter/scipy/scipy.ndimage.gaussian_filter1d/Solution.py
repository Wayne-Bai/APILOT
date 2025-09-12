import numpy as np
import scipy.signal

# Sample input data
data = np.array([1, 2, 0, 4, 5, 3, 6, 7])

# Define the Gaussian filter
def gaussian_kernel_1d(x, sigma=1):
    size = 5
    x = np.arange(-size // 2 + 1., size // 2 + 1.)
    gaussian_kernel = np.exp(-np.power(x, 2.0) / (2.0 * np.power(sigma, 2.0)))
    return gaussian_kernel / np.sum(gaussian_kernel)

# Create a 1-D Gaussian filter
kernel = gaussian_kernel_1d(3)

# Apply the 1-D Gaussian filter to the data
filtered_data = scipy.signal.convolve(data, kernel, mode='same')

print(filtered_data)
