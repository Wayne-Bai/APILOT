# Import the TensorFlow library
import tensorflow as tf

# Create a constant tensor from a tensor-like object (list)
constant_tensor_from_list = tf.constant([1, 2, 3, 4, 5])
print("Constant tensor from list:")
print(constant_tensor_from_list)

# Create a constant tensor from a tensor-like object (tuple)
constant_tensor_from_tuple = tf.constant((6, 7, 8, 9, 10))
print("\nConstant tensor from tuple:")
print(constant_tensor_from_tuple)

# Create a constant tensor from a tensor-like object (numpy array)
import numpy as np
numpy_array = np.array([11, 12, 13, 14, 15])
constant_tensor_from_numpy_array = tf.constant(numpy_array)
print("\nConstant tensor from numpy array:")
print(constant_tensor_from_numpy_array)
