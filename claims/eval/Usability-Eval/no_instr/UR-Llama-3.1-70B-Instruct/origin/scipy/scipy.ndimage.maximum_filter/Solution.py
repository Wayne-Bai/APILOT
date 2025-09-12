import numpy as np
from scipy import ndimage

# Create a 2D array
data = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0]
])

# Calculate the multidimensional maximum filter with a footprint of size 3x3
max_filtered = ndimage.maximum_filter(data, size=3, mode='nearest')

print("Original Data:")
print(data)
print("\nMultidimensional Maximum Filter:")
print(max_filtered)
