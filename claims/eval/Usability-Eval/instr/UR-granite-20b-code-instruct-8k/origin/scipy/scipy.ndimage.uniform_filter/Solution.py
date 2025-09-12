from scipy import ndimage
import numpy as np

# Generate a random 3D array
arr = np.random.random((100, 100, 100))

# Apply a 3x3x3 uniform filter
result = ndimage.uniform_filter(arr, size=3)

# Print the result
print(result)
