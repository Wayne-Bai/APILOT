import numpy as np
from scipy import ndimage

# Define the dimensions of the input array
n, m = (100, 100)

# Create a 2D array with random values
arr = np.random.rand(n, m)

# Calculate the rank filter using scipy's ndimage module
rank_filter = ndimage.filters.generic_filter(arr, np.median, footprint=np.ones((5, 5)))

# Display the output
print(rank_filter)
