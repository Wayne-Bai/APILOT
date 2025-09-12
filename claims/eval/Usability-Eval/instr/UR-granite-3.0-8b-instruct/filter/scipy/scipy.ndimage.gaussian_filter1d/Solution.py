import scipy.ndimage as ndimage

# Define the size of the kernel
kernel_size = 5

# Define the standard deviation of the Gaussian distribution
sigma = 1.0

# Generate the 1-D Gaussian filter
gaussian_filter = ndimage.gaussian_filter1d(np.eye(kernel_size), sigma, axis=0)

# Print the filter
print(gaussian_filter)
