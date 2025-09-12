import numpy as np

# Create two 1-dimensional arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Join the two arrays along a new axis (axis=0)
# This will create a 2-dimensional array with array1 and array2 as rows
new_array1 = np.array([array1, array2])

print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
print("Joined Array:")
print(new_array1)

# Join the two arrays along a new axis (axis=1)
# This will create a 2-dimensional array with array1 and array2 as columns
new_array2 = np.array([array1, array2]).T

print("\nJoined Array (axis=1):")
print(new_array2)

# Join multiple arrays
array3 = np.array([7, 8, 9])
array4 = np.array([10, 11, 12])

new_array3 = np.array([array1, array2, array3, array4])

print("\nArray 3:")
print(array3)
print("Array 4:")
print(array4)
print("Joined Array:")
print(new_array3)

# You can use np.stack() to join the arrays
new_array4 = np.stack((array1, array2, array3, array4), axis=0)

print("\nJoined Array (np.stack()):")
print(new_array4)

# Alternatively, you can use np.stack() with axis=1 to join the arrays column-wise
new_array5 = np.stack((array1, array2, array3, array4), axis=1)

print("\nJoined Array (np.stack() with axis=1):")
print(new_array5)
