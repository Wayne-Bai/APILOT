import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the tensor to be tiled
tile_tensor = tf.constant([[5, 6], [7, 8]])

# Define the number of times the tile_tensor should be tiled
tiles = [2, 1]

# Use tf.tile to construct the output tensor
output_tensor = tf.tile(tile_tensor, tiles)

# Print the output tensor
print(output_tensor)
