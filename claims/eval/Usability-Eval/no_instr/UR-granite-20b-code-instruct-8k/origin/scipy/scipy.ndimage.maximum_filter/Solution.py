import scipy
import numpy as np

# Create a 2D array with random values
arr = np.random.rand(3, 3)

# Apply a multidimensional maximum filter
result = scipy.signal.maximum_filter(arr, size=3)

# Print the result
print(result)
