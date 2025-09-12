import numpy as np
from scipy.ndimage import rank_filter

# Create a random array
arr = np.random.rand(5, 5)

# Calculate the rank filter
rank_filtered_arr = rank_filter(arr, size=3, rank=1)

# Print the result
print(rank_filtered_arr)
