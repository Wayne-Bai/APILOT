import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Specify the tiling pattern
# For example, to repeat the original tensor 2 times along the rows and 3 times along the columns
tile_pattern = [2, 3]

# Construct the tiled tensor
tiled_tensor = tf.repeat(tf.repeat(tensor, tile_pattern[0], axis=0), tile_pattern[1], axis=1)

# Print the tiled tensor
print(tiled_tensor)
