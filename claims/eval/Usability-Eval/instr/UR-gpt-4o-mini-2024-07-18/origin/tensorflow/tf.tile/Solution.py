import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Define the number of repetitions for each dimension
multiples = tf.constant([2, 3])  # Repeat rows 2 times and columns 3 times

# Use tf.tile to tile the tensor
tiled_tensor = tf.tile(tensor, multiples)

# Print the result
print(tiled_tensor)
