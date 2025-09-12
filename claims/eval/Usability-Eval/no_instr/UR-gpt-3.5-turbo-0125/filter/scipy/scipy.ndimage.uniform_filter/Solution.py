
import numpy as np
from scipy import ndimage

def multidimensional_uniform_filter(input_array, filter_size):
    output_array = ndimage.uniform_filter(input_array, size=filter_size)
    return output_array

# Example usage
input_array = np.random.rand(10, 10, 10)  # Generating a random 3D array for demonstration
filter_size = (3, 3, 3)  # Filter size in each dimension
output_array = multidimensional_uniform_filter(input_array, filter_size)
print(output_array)
