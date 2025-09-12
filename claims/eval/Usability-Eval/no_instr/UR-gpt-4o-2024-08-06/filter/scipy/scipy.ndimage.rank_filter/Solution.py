import numpy as np
from scipy.ndimage import rank_filter

# Define a sample multidimensional array (e.g., a 3x3 matrix)
data = np.array([
    [5, 3, 8],
    [9, 7, 1],
    [4, 6, 2]
])

# Define the size of the filter window
footprint = np.ones((3, 3))  # A 3x3 window

# Calculate the rank filter
# rank 4 means that, in a 3x3 window, it will select the 5th smallest element (0-based index)
ranked_data = rank_filter(data, rank=4, footprint=footprint)

print("Original data:")
print(data)

print("\nRank filtered data:")
print(ranked_data)
