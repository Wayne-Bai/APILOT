import tensorflow as tf

# Create a tensor
original_tensor = tf.constant([1, 2, 3], dtype=tf.int32)

# Tile the tensor 3 times
tiling_factor = 3
tiled_tensor = tf.tile(original_tensor, [tiling_factor])

print(tiled_tensor.numpy())
