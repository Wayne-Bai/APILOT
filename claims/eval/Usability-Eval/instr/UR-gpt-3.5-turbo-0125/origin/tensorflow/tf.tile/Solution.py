
import tensorflow as tf

# Define the tensor to be tiled
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the tiling shape
multiples = [2, 3]

# Tile the input tensor
tiled_tensor = tf.tile(input_tensor, multiples)

# Print the tiled tensor
print(tiled_tensor)
