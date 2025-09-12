import numpy as np
from scipy import ndimage

# Create a 3D array
data = np.random.randint(0, 100, size=(5, 5, 5))

# Define the size of the filter
size = (3, 3, 3)

# Calculate the 75th percentile
percentile = 75

# Apply the percentile filter
result = ndimage.percentile_filter(data, percentile, size=size)

# Print the result
print(result)
