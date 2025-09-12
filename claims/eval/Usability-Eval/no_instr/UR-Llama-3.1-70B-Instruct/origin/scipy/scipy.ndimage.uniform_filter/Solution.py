import numpy as np
from scipy.ndimage import uniform_filter

# Create a 3D numpy array
arr = np.random.randint(0, 100, size=(5, 5, 5))

# Define the size of the filter
size = 2

# Apply the uniform filter
result = uniform_filter(arr, size=size)

# Print the original array and the filtered result
print("Original array:")
print(arr)
print("\nFiltered result:")
print(result)
