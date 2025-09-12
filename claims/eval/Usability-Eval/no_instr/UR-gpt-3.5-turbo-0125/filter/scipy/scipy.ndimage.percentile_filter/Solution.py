
import numpy as np
from scipy.ndimage import percentile_filter

# Generate random 3D array
data = np.random.rand(5, 5, 5)

# Define the percentile and size of the filter
percentile = 50
size = 3

# Apply the multidimensional percentile filter
result = percentile_filter(data, percentile=percentile, size=size)

print(result)
