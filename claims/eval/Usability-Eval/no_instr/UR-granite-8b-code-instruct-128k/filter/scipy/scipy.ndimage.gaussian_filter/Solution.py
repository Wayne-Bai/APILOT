import numpy as np
from scipy.ndimage import gaussian_filter

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply a 2D Gaussian filter to the array
filtered_arr = gaussian_filter(arr, sigma=1)

# Print the filtered array
print(filtered_arr)
