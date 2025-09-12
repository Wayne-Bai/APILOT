import numpy as np
from scipy.signal import max_filter

# Create a sample 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Apply a maximum filter to the array with a size of 3x3
max_arr = max_filter(arr, size=(3, 3))

print(max_arr)
