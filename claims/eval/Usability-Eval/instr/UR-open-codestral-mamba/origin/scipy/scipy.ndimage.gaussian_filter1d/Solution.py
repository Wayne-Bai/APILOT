from scipy.ndimage import gaussian_filter1d
import numpy as np

# Define input array
input_array = np.array([1, 2, 3, 4, 5])

# Define sigma for Gaussian filter
sigma = 1

# Apply Gaussian filter
output_array = gaussian_filter1d(input_array, sigma)

print("Input Array: ", input_array)
print("Output Array: ", output_array)
