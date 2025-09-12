import numpy as np
from scipy.ndimage import minimum_filter

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filter_size = (2, 2)

# Apply the minimum filter
result = minimum_filter(data, size=filter_size)

print(result)
