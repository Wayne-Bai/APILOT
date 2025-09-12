import numpy as np

# Create an example array
data = np.array([1, 2, 3, 4, 5], dtype=np.float32)

# Get the integer pointer to the memory area of the array
pointer = id(data)
