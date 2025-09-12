import numpy as np
from scipy.ndimage import uniform_filter

# Example 3D array
array_3d = np.random.rand(10, 10, 10)

# Apply the uniform filter with a 3x3x3 window
filtered_array = uniform_filter(array_3d, size=3)

print(filtered_array)
