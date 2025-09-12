import scipy.ndimage as ndimage
import numpy as np

# Define a multidimensional array
data = np.array([[1, 2, 3, 4, 5],
                 [5, 4, 3, 2, 1],
                 [1, 2, 1, 2, 1],
                 [5, 4, 3, 4, 5]])

# Apply a multidimensional maximum filter
filtered_data = ndimage.maximum_filter(data, size=3)

print("Original Data:\n", data)
print("Filtered Data:\n", filtered_data)
