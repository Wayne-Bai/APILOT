import numpy as np
from scipy.ndimage import percentile_filter

# Define a sample 3D array (e.g., volumetric data or a stack of 2D images)
data = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

# Define the percentile to compute (e.g., 50 corresponds to the median)
percentile_value = 50

# Define the size of the neighborhood over which to compute the percentile
size = 3

# Compute the percentile filter
result = percentile_filter(data, percentile=percentile_value, size=size)

# Print the result
print("Filtered data:")
print(result)
