import numpy as np
from scipy.ndimage import maximum_filter

# Example data
data = np.array([[1, 2, 0, 0],
                 [5, 3, 0, 4],
                 [0, 0, 0, 7],
                 [9, 3, 0, 0]])

# Define the size of the filter window
filter_size = (2, 2)

# Apply the maximum filter
result = maximum_filter(data, size=filter_size)

print(result)
