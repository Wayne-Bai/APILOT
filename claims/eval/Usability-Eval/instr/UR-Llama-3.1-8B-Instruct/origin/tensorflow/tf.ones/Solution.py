# Import the necessary tensorflow module
import tensorflow as tf

# Create a tensor with all elements set to one (1)
tensor_with_ones = tf.ones((3, 3))

# Print the tensor
print(tensor_with_ones)

# Create a scalar tensor with all elements set to one (1)
scalar_tensor_with_ones = tf.ones(())

# Print the scalar tensor
print(scalar_tensor_with_ones)

# Create a tensor with all elements set to one (1) and specify the data type
tensor_with_ones_float32 = tf.ones((3, 3), dtype='float32')

# Print the tensor
print(tensor_with_ones_float32)
