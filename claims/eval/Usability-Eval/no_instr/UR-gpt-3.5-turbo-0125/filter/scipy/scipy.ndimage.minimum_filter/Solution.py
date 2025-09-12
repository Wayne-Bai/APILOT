
import numpy as np
from scipy.ndimage import minimum_filter

# Create a multidimensional array
data = np.array([[1, 3, 2],
                 [4, 2, 5],
                 [7, 8, 6]])

# Define the size of the minimum filter
size = 2

# Apply the multidimensional minimum filter
filtered_data = minimum_filter(data, size=size)

print(filtered_data)
