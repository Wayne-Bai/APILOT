import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Stack arrays in sequence horizontally (column wise)
stacked_array = np.concatenate((array1, array2), axis=1)

print("Stacked Array:")
print(stacked_array)
