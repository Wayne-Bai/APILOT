# Import the necessary library
import tensorflow as tf

# Create a tensor with all elements set to zero
zero_tensor = tf.zeros([3, 4], dtype=tf.float32)

# Print the tensor
print(zero_tensor)

# Alternatively, you can create a tensor with a specified shape and data type
tensor_shape = (3, 4)
tensor_data_type = tf.float32

# Create the tensor
zero_tensor = tf.Variable(tf.zeros(tensor_shape), dtype=tensor_data_type)

# Print the tensor
print(zero_tensor)

# To keep the tensor unchanged after its initial creation, you can make it a constant
zero_tensor = tf.constant(tf.zeros(tensor_shape), dtype=tensor_data_type)

# Print the tensor
print(zero_tensor)
