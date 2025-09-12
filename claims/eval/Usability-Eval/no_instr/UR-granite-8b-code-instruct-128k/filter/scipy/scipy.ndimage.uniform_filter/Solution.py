import numpy as np
from scipy.ndimage import uniform_filter

# Create a 2D array to filter
arr = np.random.rand(10, 10)

# Apply the multidimensional uniform filter
filtered_arr = uniform_filter(arr, size=(3, 3))

# Print the original and filtered arrays
print("Original array:")
print(arr)
print("Filtered array:")
print(filtered_arr)
