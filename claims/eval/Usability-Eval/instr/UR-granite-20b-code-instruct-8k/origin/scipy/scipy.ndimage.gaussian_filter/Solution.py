from scipy import ndimage
import numpy as np

# Define the 2D Gaussian kernel
sigma = 2
x, y = np.meshgrid(np.linspace(-1, 1, 512), np.linspace(-1, 1, 512))
kernel_2D = np.exp(-(x**2 + y**2)/(2*sigma**2))

# Normalize the kernel
kernel_2D /= np.sum(kernel_2D)

# Apply the 2D Gaussian filter to a 3D array (e.g., a stack of images)
# Replace `input_array` with the actual array you want to apply the filter to
filtered_array = ndimage.convolve(input_array, kernel_2D, mode='mirror')
