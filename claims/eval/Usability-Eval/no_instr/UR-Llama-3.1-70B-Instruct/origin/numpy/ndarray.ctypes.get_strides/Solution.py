import numpy as np
import ctypes

# Create a numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Get the strides information from the numpy array
strides = array.strides

# Calculate the size of the elements in the array
element_size = np.dtype(array.dtype).itemsize

# Create a ctypes array to store the strides
strides_array = ctypes.c_intp * array.ndim

# Initialize the ctypes array with the strides information
strides_ctypes = strides_array(*[stride // element_size for stride in strides])

# Print the strides information
print("Strides Information:")
for i, stride in enumerate(strides_ctypes):
    print(f"Dimension {i+1}: {stride} elements")
    print(f"Dimension {i+1}: {stride * element_size} bytes")
    print()
