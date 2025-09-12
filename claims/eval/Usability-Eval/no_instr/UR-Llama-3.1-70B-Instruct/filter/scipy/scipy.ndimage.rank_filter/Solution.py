# Import necessary libraries
import numpy as np
from scipy import ndimage

# Create a 2D array
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# Apply a rank filter to the array
# For this example, we'll use a 3x3 window and calculate the 50th percentile (median)
rank_filtered_array = ndimage.rank_filter(array, np.median, size=3)

# Print the original and rank filtered arrays
print("Original array:")
print(array)
print("\nRank filtered array (median):")
print(rank_filtered_array)
