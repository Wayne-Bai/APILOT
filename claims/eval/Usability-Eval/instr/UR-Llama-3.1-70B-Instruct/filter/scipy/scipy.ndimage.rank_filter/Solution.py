import numpy as np
from scipy import ndimage

# Generate a random 3D array
data = np.random.rand(10, 10, 10)

# Define a footprint for the filter (a 3x3x3 cube in this case)
footprint = np.ones((3, 3, 3))

# Apply the rank filter (calculating the 5th percentile in this case)
filtered_data = ndimage.rank_filter(data, 5, footprint=footprint)

# Alternatively, you can use the generic_filter1d function
def calculate_percentile(data, percentile):
    return np.percentile(data, percentile)

# Apply the generic filter
filtered_data_generic = ndimage.generic_filter(data, calculate_percentile, size=3, 
                                               extra_arguments=(5,), mode='constant', cval=0.0)

# You can also use the median_filter function to calculate the median
filtered_data_median = ndimage.median_filter(data, size=3)
