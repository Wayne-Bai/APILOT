import tensorflow as tf

# Define the original tensor
original_tensor = tf.constant([1, 2, 3])

# Define the number of tiles
num_tiles = 3

# Tile the original tensor
tiled_tensor = tf.tile(original_tensor, [num_tiles])

print(tiled_tensor)
