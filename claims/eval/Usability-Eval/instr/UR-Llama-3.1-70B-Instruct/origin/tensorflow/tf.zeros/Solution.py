# Importing the necessary library
import tensorflow as tf

# Create a tensor with all elements set to zero
zero_tensor = tf.zeros((3, 4))

# Print the tensor
print(zero_tensor)

# Create a tensor with specific data type
zero_float32_tensor = tf.zeros((3, 4), dtype=tf.float32)

# Print the tensor
print(zero_float32_tensor)
