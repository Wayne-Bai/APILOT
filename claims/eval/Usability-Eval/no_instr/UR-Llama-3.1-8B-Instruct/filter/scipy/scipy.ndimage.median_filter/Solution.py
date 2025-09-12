# Import necessary libraries
import numpy as np
from scipy import ndimage

# Generate a sample 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the filter size (even number for median filter)
filter_size = 3

# Apply median filter to the array
filtered_arr = ndimage.median_filter(arr, size=filter_size)

print(filtered_arr)
