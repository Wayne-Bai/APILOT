
import numpy as np
from scipy.ndimage import gaussian_filter

# Define input multidimensional array
input_array = np.random.rand(5, 5, 5)

# Define the sigma value for Gaussian filter
sigma = 1.5

# Apply the multidimensional Gaussian filter
output_array = gaussian_filter(input_array, sigma=sigma)

print(output_array)
