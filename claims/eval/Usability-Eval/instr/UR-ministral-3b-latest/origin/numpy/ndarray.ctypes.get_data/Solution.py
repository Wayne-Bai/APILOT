import numpy as np

# Example array using NumPy
array = np.array([1, 2, 3], dtype=np.int64)

# Get a pointer to the memory area of the array
memory_pointer = id(array)

print(f"Pointer to the memory area: {memory_pointer}")
