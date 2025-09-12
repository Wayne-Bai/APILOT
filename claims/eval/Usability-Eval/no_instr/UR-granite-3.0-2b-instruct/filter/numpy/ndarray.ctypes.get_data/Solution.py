import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Get the memory address of the array
mem_address = id(arr)

# Get the size of the array in bytes
mem_size = np.append(arr, 0)

# Print the memory address and size
print(f"Memory address: {mem_address}")
print(f"Memory size: {mem_size} bytes")
