import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the number of times to tile each axis
num_tiles = [2, 3]

# Tile the input tensor along both axes
tiled_tensor = tf.tile(input_tensor, num_tiles)

# Print the result
print(tiled_tensor)
