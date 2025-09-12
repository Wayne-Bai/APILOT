# Import the necessary tensorflow module
import tensorflow as tf

# Create a tensor filled with a scalar value
tensor = tf.constant(5.0)

# Print the tensor
print(tensor)

# Create a tensor filled with a list of values
tensor_list = tf.constant([1, 2, 3, 4, 5])

# Print the tensor
print(tensor_list)

# Create a tensor filled with a 2D list of values
tensor_2d = tf.constant([[1, 2], [3, 4]])

# Print the tensor
print(tensor_2d)
