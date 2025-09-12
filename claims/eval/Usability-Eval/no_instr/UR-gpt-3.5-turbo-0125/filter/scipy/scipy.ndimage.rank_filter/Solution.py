
import numpy as np
from scipy.ndimage import rank_filter

# Creating a sample multidimensional array
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
                [[2, 4, 6], [8, 1, 3], [5, 7, 9]]])

# Specify the size of the filter window
size = 2

# Calculate the multidimensional rank filter
result = rank_filter(arr, rank=3, size=size)

print(result)
