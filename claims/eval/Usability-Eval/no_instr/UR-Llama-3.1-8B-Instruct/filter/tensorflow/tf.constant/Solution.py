# Import the necessary library
import tensorflow as tf

# Create a constant tensor from a Python list
const_tensor_list = tf.constant([1, 2, 3, 4, 5])

# Print the constant tensor
print("Constant Tensor from Python List:")
print(const_tensor_list)

# Create a constant tensor from a NumPy array
import numpy as np

const_tensor_numpy = tf.constant(np.array([10, 20, 30, 40, 50]))

# Print the constant tensor
print("\nConstant Tensor from NumPy Array:")
print(const_tensor_numpy)

# Create a constant tensor from a dictionary
const_tensor_dict = tf.constant({0: 10, 1: 20, 2: 30})

# Print the constant tensor
print("\nConstant Tensor from Dictionary:")
print(const_tensor_dict)

# Create a constant tensor from a scalar value
const_tensor_scalar = tf.constant(50)

# Print the constant tensor
print("\nConstant Tensor from Scalar Value:")
print(const_tensor_scalar)
