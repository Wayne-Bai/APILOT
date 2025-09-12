import numpy as np
from scipy.ndimage import gaussian_filter

# Example usage of gaussian_filter for a 2D array
def multidimensional_gaussian_filter(arr, sigma):
    # Apply the gaussian filter
    filtered_arr = gaussian_filter(arr, sigma=sigma)
    return filtered_arr

# Example input array (2D)
input_array = npenerator.randn(100, 100)

# Apply the filter
filtered_array = multidimensional_gaussian_filter(input_array, sigma=3)

# Display the original and filtered arrays
print("Original Array:")
print(input_array)
print("Filtered Array:")
print(filtered_array)
