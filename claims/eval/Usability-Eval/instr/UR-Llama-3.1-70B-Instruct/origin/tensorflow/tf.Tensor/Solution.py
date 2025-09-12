# Importing the necessary library
import tensorflow as tf

# Creating a 1D array
array_1d = tf.constant([1, 2, 3, 4, 5])
print("1D Array: ", array_1d)

# Creating a 2D array
array_2d = tf.constant([[1, 2], [3, 4]], shape=[2, 2])
print("\n2D Array: \n", array_2d)

# Creating a 3D array
array_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], shape=[2, 2, 2])
print("\n3D Array: \n", array_3d)

# Creating a 4D array
array_4d = tf.constant([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]], shape=[2, 2, 2, 2])
print("\n4D Array: \n", array_4d)

# Getting the dimensions of the arrays
print("\nDimensions of array_1d: ", tf.rank(array_1d))
print("Dimensions of array_2d: ", tf.rank(array_2d))
print("Dimensions of array_3d: ", tf.rank(array_3d))
print("Dimensions of array_4d: ", tf.rank(array_4d))
