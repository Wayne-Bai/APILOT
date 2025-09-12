import numpy as np
from scipy.ndimage import percentile_filter

# Example data
data = np.random.random((100, 100))

# Applying a multidimensional percentile filter
# Here we are using a size of 5 for the footprint, and calculating the 50th percentile (median)
filtered_data = percentile_filter(data, 50, size=5)

# Display the result
print(filtered_data)
