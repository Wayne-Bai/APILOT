import numpy as np

# Initialize 3 arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Join a sequence of arrays along a new axis
joined_arrays = np.stack((array1, array2, array3))

print("Joined Arrays:\n", joined_arrays)

# You can also use axis parameter to join along different axes
joined_arrays_vertical = np.stack((array1, array2, array3), axis=1)
print("\nJoined Arrays Vertically:\n", joined_arrays_vertical)

# And with multiple dimensions
array1_2d = np.array([[1, 2], [3, 4]])
array2_2d = np.array([[5, 6], [7, 8]])
array3_2d = np.array([[9, 10], [11, 12]])

joined_arrays_3d = np.stack((array1_2d, array2_2d, array3_2d))
print("\nJoined 2D Arrays:\n", joined_arrays_3d)

joined_arrays_2d_last_axis = np.stack((array1_2d, array2_2d, array3_2d), axis=2)
print("\nJoined 2D Arrays Last Axis:\n", joined_arrays_2d_last_axis)
