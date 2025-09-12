from scipy.ndimage import uniform_filter
import numpy as np

# Define the input array
input_array = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]])

# Define the size of the uniform filter
size = (2, 2)

# Apply the uniform filter
result = uniform_filter(input_array, size=size)

result
