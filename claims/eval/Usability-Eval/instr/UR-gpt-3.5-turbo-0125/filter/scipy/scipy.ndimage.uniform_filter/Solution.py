
import numpy as np
from scipy.ndimage import uniform_filter

# Create a sample multidimensional array
array = np.random.randint(0, 10, (5, 5, 5))

# Apply the multidimensional uniform filter
filtered_array = np.mean(array, axis=0)

print(filtered_array)
