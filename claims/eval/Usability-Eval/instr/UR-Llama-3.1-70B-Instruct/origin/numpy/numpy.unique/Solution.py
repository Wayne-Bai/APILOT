import numpy as np

# Create a numpy array with some duplicate elements
array = np.array([1, 2, 3, 2, 4, 5, 2, 6, 2, 7, 8, 8, 9])

# Find the unique elements in the array
unique_elements = np.unique(array)

print("Original array:")
print(array)

print("\nUnique elements in the array:")
print(unique_elements)
