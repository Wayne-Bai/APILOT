import numpy as np
from scipy.ndimage import median_filter

# Generate a sample 2D array (can be extended to 3D or more dimensions)
array = np.array([[10, 21, 32, 43, 54],
                  [25, 36, 47, 58, 69],
                  [40, 51, 62, 73, 84],
                  [55, 66, 77, 88, 99],
                  [70, 81, 92, 103, 114]])

# Apply a median filter with a window size of 3x3
filtered_array = median_filter(array, size=3)

print("Original Array:")
print(array)

print("\nFiltered Array:")
print(filtered_array)
