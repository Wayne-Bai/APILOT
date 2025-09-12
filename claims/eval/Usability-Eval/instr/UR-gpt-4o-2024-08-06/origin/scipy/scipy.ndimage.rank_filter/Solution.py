import numpy as np
from scipy.ndimage import rank_filter

# Create a sample 3D numpy array (for demonstration)
data = np.random.rand(5, 5, 5)

# Define the size of the filter window
footprint_size = (3, 3, 3)

# Define the rank (0 for minimum, footprint_elements - 1 for maximum, footprint_elements // 2 for median)
rank = np.prod(footprint_size) // 2

# Apply the multidimensional rank filter
result = rank_filter(data, rank=rank, footprint=np.ones(footprint_size))

# Print the filtered result
print("Original data:\n", data)
print("\nFiltered data:\n", result)
