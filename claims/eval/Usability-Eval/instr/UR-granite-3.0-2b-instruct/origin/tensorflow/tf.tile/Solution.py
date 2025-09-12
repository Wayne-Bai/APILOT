import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the tile dimensions
tile_dim = (2, 2)

# Tile the input tensor
tiling_tensor = tf.tile(input_tensor, tile_dim)

# Print the original and tiled tensors
print("Original Tensor:")
print(input_tensor)
print("\nTiled Tensor:")
print(tiling_tensor)
