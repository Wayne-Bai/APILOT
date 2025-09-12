import numpy as np
from scipy.ndimage import maximum_filter

# Example usage
data = np.array([[1, 2, 0, 0],
                 [5, 3, 0, 4],
                 [0, 0, 0, 7],
                 [9, 3, 0, 0]])

# Apply a maximum filter with a 3x3 window
filtered_data = maximum_filter(data, size=3)

print(filtered_data)
