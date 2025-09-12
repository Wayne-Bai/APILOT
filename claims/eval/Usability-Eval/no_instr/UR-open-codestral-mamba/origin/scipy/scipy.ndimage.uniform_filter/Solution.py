from scipy.ndimage import uniform_filter
import numpy as np

# Let's take a 3D array for this example
input_array = np.random.random((5, 5, 5))

# Define the size of the uniform filter
size = 3

# Apply the uniform filter
output_array = uniform_filter(input_array, size=size)

print(output_array)
