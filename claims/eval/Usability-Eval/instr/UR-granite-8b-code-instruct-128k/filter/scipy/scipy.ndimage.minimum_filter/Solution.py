import numpy as np
from scipy.ndimage import minimum_filter

# Create a 2D array to filter
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply a 3x3 minimum filter to the array
filtered_arr = minimum_filter(arr, size=(3, 3))

print(filtered_arr)
