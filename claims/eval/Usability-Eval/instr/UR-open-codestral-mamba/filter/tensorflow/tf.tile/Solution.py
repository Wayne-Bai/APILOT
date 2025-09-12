import tensorflow as tf

# Define a simple 3x3 tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)

# Tile the tensor 2 times in the first dimension, 3 times in the second dimension
tiled_tensor = tf.tile(input_tensor, [2, 3])

# Print the tiled tensor
print(tiled_tensor)
