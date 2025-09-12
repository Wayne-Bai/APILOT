import numpy as np
from scipy.ndimage import uniform_filter

# Example of a 3D NumPy array
data = np.random.rand(5, 5, 5)

# Apply a multidimensional uniform filter with size 3x3x3
filtered_data = uniform_filter(data, size=(3, 3, 3))

print("Original Data:\n", data)
print("\nFiltered Data:\n", filtered_data)
