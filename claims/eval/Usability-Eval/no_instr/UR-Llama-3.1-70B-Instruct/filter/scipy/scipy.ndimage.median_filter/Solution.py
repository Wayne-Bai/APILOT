import numpy as np
from scipy import ndimage

# Generate a random 3D array with some outliers
np.random.seed(0)
arr = np.random.normal(loc=5, scale=2, size=(5, 5, 5))
arr[2, 2, 2] = 100  # Add an outlier

# Calculate the multidimensional median filter
filtered_arr = ndimage.median_filter(arr, size=3)

print("Original Array:")
print(arr)
print("\nFiltered Array:")
print(filtered_arr)
