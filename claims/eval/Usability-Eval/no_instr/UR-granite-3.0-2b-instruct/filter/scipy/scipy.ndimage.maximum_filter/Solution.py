import numpy as np
from scipy.ndimage import maximum_filter

# Create a 3D array
arr = np.random.rand(5, 5, 5)

# Apply the maximum filter
filtered_arr = maximum_filter(arr, size=3)

print("Original Array:")
print(arr)
print("\nFiltered Array:")
print(filtered_arr)
