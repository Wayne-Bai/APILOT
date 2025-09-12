import tensorflow as tf

# Define the original tensor
original_tensor = tf.constant([[1, 2], [3, 4]])

# Define the number of times to tile the tensor
tiles = 3

# Tile the tensor
tiled_tensor = tf.tile(original_tensor, [tiles, 1])

print(tiled_tensor)
