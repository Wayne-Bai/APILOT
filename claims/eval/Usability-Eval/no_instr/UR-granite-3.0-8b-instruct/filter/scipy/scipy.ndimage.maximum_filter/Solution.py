import numpy as np
from scipy.ndimage import maximum_filter

# Assuming 'arr' is your multidimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the maximum filter
filtered_arr = maximum_filter(arr, size=(2, 2))

print(filtered_arr)
