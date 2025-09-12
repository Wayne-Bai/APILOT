import tensorflow as tf

# Define a tensor
original_tensor = tf.constant([1, 2, 3, 4])

# Tile the tensor
tiled_tensor = tf.tile(original_tensor, [2, 3])

print(tiled_tensor)
