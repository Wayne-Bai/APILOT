import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Define the repetition factors for tiling
multiples = tf.constant([2, 3], tf.int32)

# Perform the tiling operation
output_tensor = tf.tile(input_tensor, multiples)

# Print the output tensor
print(output_tensor)
