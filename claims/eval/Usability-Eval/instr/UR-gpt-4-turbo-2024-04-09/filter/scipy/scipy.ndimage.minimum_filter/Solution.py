import scipy.ndimage as ndimage
import numpy as np

# Creating an example 2D array
data = np.array([[1, 2, 3, 4, 5],
                 [5, 4, 3, 2, 1],
                 [1, 2, 1, 2, 1],
                 [5, 4, 5, 4, 3],
                 [1, 1, 1, 1, 1]])

# Applying the minimum filter with a size of 3x3
filtered_data = ndimage.minimum_filter(data, size=3)

print("Original Data:\n", data)
print("Filtered Data:\n", filtered_data)
