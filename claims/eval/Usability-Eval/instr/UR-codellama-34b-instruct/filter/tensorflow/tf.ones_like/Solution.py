
import tensorflow as tf

# Define the shape of the input tensor
input_shape = (3, 4)

# Create a tensor of all ones with the same shape as the input
ones_tensor = tf.ones(input_shape, dtype=tf.float32)

print(ones_tensor)
