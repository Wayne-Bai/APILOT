import numpy as np
from scipy.ndimage import uniform_filter

# Example usage of multidimensional uniform filter
# Create a sample 3D array
data = np.random.rand(5, 5, 5)

# Apply the uniform filter with a size of 3 along each dimension
filtered_data = uniform_filter(data, size=3)

print("Original Data:\n", data)
print("Filtered Data:\n", filtered_data)
