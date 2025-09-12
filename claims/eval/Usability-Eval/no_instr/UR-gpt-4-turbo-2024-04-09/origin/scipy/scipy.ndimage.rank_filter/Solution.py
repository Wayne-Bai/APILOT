import numpy as np
from scipy.ndimage import rank_filter

# Example data: a 3x3x3 multidimensional array
data = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

# Applying rank filter
# rank=3 means third element in the sorted data within the footprint
filtered_data = rank_filter(data, rank=3, size=2)

print("Original Data:")
print(data)
print("Filtered Data:")
print(filtered_data)
