import numpy as np
from scipy.ndimage import minimum_filter

# Create a sample multidimensional array
array = np.array([[5, 7, 3, 8],
                  [2, 4, 6, 9],
                  [0, 1, 5, 7],
                  [3, 6, 8, 2]])

# Define the size of the filter footprint
footprint_size = 3

# Apply the minimum filter
filtered_array = minimum_filter(array, size=footprint_size)

print("Original Array:")
print(array)

print("\nFiltered Array with Minimum Filter:")
print(filtered_array)
