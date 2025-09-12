
import numpy as np
from scipy.ndimage import filters

# Define the data array
data = np.random.rand(10, 10)

# Apply the maximum filter to each dimension separately
filtered_data = np.apply_along_axis(filters.maximum_filter, data, axis=0)
filtered_data = np.apply_along_axis(filters.maximum_filter, filtered_data, axis=1)
