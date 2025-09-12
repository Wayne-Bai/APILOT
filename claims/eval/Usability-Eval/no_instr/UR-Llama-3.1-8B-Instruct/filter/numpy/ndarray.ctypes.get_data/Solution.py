import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5], dtype=np.float32)

# Get a pointer to the memory area of the array as a Python integer
ptr = arr.data

print("Memory address of numpy array:", ptr)

# Print information about the numpy array
print("Array flags:", arr.flags)
print("Array dtype:", arr.dtype)

# Example of how to modify the array from the pointer
arr.data = 10  # This is a delicate operation

# Print the modified array
print("Modified numpy array:", arr)
