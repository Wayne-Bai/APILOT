
import numpy as np
from scipy.ndimage import median_filter

# Define your input data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Define the footprint (neighborhood) for the median filter
footprint = np.ones((3, 3))

# Apply median filter
result = median_filter(data, footprint=footprint)

print(result)
