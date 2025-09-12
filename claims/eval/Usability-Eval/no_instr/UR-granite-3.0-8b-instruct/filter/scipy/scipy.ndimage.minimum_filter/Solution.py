import numpy as np
from scipy.ndimage import minimum_filter

# Assuming 'data' is your multidimensional array
data = np.random.rand(5, 5, 5)

# Apply the minimum filter with a window size of 3
filtered_data = minimum_filter(data, size=3)
