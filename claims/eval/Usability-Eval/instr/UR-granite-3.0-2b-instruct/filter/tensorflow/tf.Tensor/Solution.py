import tensorflow as tf

# Create a multidimensional array of elements
array_1d = tf.constant([1, 2, 3, 4, 5])
array_2d = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_3d = tf.constant([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Print the arrays
print("Array 1D:")
print(array_1d)
print("\nArray 2D:")
print(array_2d)
print("\nArray 3D:")
print(array_3d)
