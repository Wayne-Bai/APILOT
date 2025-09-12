import numpy as np
from scipy import ndimage

# create a sample 3D array
array = np.random.rand(10, 10, 10)

# specify the filter size
filter_size = (3, 3, 3)

# Calculate a multidimensional maximum filter
result = ndimage.maximum_filter(array, size=filter_size)

print(result)
