import numpy as np
from scipy.ndimage import uniform_filter

# Example usage:
data = np.random.rand(10, 10)  # Example 2D array
filtered_data = uniform_filter(data, size=3)  # Applying uniform filter with a size of 3

print(filtered_data)
