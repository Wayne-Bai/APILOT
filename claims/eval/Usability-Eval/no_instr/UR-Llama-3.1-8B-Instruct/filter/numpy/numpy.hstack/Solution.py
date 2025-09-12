import numpy as np

# Create two arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Print the original arrays
print("Original Arrays:")
print("Array 1:\n", array1)
print("Array 2:\n", array2)

# Stack arrays in sequence horizontally (column wise)
stacked_array = np.concatenate((array1, array2), axis=1)

# Print the stacked array
print("\nStacked Array (Column Wise):")
print(stacked_array)
