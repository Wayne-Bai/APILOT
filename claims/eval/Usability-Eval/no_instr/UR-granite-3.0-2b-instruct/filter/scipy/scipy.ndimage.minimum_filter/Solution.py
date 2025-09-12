import numpy as np
from scipy.ndimage import minimum_filter

# Create a 3D array
arr = np.random.rand(5, 5, 5)

# Apply a 3x3x3 minimum filter
filtered_arr = minimum_filter(arr, size=(3, 3, 3))
