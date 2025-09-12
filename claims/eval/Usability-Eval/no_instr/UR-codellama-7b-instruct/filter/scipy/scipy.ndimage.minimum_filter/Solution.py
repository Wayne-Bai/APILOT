
import numpy as np
from scipy import ndimage

# Generate data
data = np.random.rand(10, 10)

# Calculate the multidimensional minimum filter
filtered_data = ndimage.minimum_filter(data, size=(3, 3))

# Print the filtered data
print(filtered_data)
