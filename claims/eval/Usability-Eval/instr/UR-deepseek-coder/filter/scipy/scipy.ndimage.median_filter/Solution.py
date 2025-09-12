import numpy as np
from scipy.ndimage import median_filter

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filtered_data = median_filter(data, size=3)

print(filtered_data)
