import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Tile the tensor
tiled_tensor = tf.tile(tensor, multiples=[2, 3])

# Print the tiled tensor
print(tiled_tensor)
