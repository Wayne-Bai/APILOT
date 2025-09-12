
import tensorflow as tf

# Create a tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Tile the tensor
tiled_tensor = tf.tile(input_tensor, [2, 3])

print(tiled_tensor)
