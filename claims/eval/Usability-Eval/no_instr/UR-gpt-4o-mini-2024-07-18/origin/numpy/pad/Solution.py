import numpy as np

# Create an example array
array = np.array([[1, 2], [3, 4]])

# Define the padding width
pad_width = 1

# Pad the array with zeros
padded_array = np.pad(array, pad_width, mode='constant', constant_values=0)

print("Original array:")
print(array)

print("\nPadded array:")
print(padded_array)
