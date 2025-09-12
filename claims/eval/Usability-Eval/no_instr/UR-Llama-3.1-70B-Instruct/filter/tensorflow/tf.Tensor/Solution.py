# Import necessary libraries
import tensorflow as tf

# Create a multidimensional array
array_1d = tf.constant([1, 2, 3, 4, 5])  # 1-dimensional array
print("1D Array: ", array_1d)

array_2d = tf.constant([[1, 2], [3, 4], [5, 6]])  # 2-dimensional array
print("2D Array: \n", array_2d)

array_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3-dimensional array
print("3D Array: \n", array_3d)

# Perform various array operations
print("Shape of array_1d: ", array_1d.shape)
print("Rank of array_1d: ", tf.rank(array_1d))

# Data type
array_float = tf.constant([1.1, 2.2, 3.3], dtype=float)
print("Data Type of array_float: ", array_float.dtype)

# Basic operations
print("Add array_1d and array_float: ", tf.add(array_1d, tf.cast(array_float, dtype=tf.int32)))
print("Multiply array_1d and array_float: ", tf.multiply(array_1d, tf.cast(array_float, dtype=tf.int32)))

# Array reshaping
array_reshaped = tf.reshape(array_1d, [1, 5])
print("Reshaped array: \n", array_reshaped)

# Transpose
array_transposed = tf.transpose(array_2d)
print("Transposed array: \n", array_transposed)

# Expand dimensions
array_expanded = tf.expand_dims(array_1d, axis=0)
print("Expanded array: \n", array_expanded)
