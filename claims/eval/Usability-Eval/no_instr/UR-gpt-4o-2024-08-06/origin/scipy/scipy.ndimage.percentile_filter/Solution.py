import numpy as np
from scipy.ndimage import percentile_filter

# Create a sample 3D array (for example, a 5x5x5 cube)
data = np.random.rand(5, 5, 5)

# Define the percentile value
percentile_value = 50  # For median

# Define the size of the filter
size = (3, 3, 3)

# Apply the multidimensional percentile filter
filtered_data = percentile_filter(data, percentile_value, size=size)

print("Original Data:\n", data)
print("\nFiltered Data:\n", filtered_data)
