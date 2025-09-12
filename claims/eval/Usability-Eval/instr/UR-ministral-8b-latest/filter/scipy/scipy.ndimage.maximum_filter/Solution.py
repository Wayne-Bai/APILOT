import numpy as np
from scipy.ndimage import maximum_filter

# Example usage:
data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
output = maximum_filter(data, size=3)
print(output)
