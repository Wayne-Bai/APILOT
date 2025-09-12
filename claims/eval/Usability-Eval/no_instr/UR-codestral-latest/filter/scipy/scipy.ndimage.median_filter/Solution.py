import numpy as np
from scipy import ndimage

# assume 'data' is your multidimensional data
data = np.random.rand(100, 100)

# Define the size of the filter. Here, it's a 3x3 filter
size = (3, 3)

# Apply median filter
filtered_data = ndimage.median_filter(data, size=size)
