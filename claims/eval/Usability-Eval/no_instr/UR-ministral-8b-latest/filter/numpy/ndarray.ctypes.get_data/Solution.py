import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Get a pointer to the memory area of the array as a Python integer
memory_pointer = arr.data

print("Memory pointer:", memory_pointer)
