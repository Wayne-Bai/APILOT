import tensorflow as tf

# Create a tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the tiling pattern
multiples = tf.constant([2, 3])  # Tile the tensor 2 times along the first dimension and 3 times along the second dimension

# Tile the tensor
tiled_tensor = tf.tile(input_tensor, multiples)

# Display the result
tf.print(tiled_tensor)
