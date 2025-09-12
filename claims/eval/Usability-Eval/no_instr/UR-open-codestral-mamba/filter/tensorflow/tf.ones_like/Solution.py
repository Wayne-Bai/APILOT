import tensorflow as tf

# Assume 'input_tensor' is your input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Create a tensor of all ones that has the same shape as the input_tensor
all_ones_tensor = tf.ones_like(input_tensor)

print(all_ones_tensor)
