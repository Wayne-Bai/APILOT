import numpy as np
from scipy.ndimage import minimum_filter

# Assuming 'data' is your multidimensional array
data = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

# Calculate the minimum filter
filtered_data = minimum_filter(data, size=(3, 3))

print(filtered_data)
