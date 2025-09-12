import numpy as np
from scipy.ndimage import uniform_filter

# Define a multidimensional array
data = np.random.rand(5, 5)

# Define the filter size
filter_size = 2

# Apply the uniform filter
filtered_data = uniform_filter(data, size=filter_size)

# Print the original and filtered data
print("Original Data:\n", data)
print("\nFiltered Data:\n", filtered_data)
