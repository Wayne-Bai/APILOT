
# Import the necessary library
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Tile the input tensor
tiled_tensor = tf.tile(input_tensor, multiples=[2, 3])

# Print the tiled tensor
print(tiled_tensor)
