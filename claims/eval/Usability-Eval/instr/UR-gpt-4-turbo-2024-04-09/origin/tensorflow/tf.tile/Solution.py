import tensorflow as tf

# Sample input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Specify the multiples for tiling
multiples = [2, 3]  # This will tile the tensor 2 times along the first dimension and 3 times along the second dimension

# Tile the tensor
tiled_tensor = tf.tile(input_tensor, multiples)

print(tiled_tensor)
