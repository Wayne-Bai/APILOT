
import numpy as np
from scipy.ndimage import uniform_filter

# Define the size of the kernel
kernel_size = (3, 3)

# Define the input array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply the uniform filter to the input array
filtered_arr = uniform_filter(arr, kernel_size)

# Print the filtered array
print(filtered_arr)
