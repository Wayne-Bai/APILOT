from scipy.ndimage import gaussian_filter
import numpy as np

# Generate a random 3D array as input
input_array = np.random.rand(100, 100, 100)

# Apply the multidimensional Gaussian filter
output_array = gaussian_filter(input_array, sigma=2)
