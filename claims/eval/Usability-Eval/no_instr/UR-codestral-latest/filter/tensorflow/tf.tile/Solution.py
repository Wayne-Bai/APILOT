import tensorflow as tf

# Assume we have a tensor 'input_tensor'
input_tensor = tf.constant([1, 2, 3])

# Define the multiples for tiling the input_tensor
multiples = [2]

# Tile the input_tensor
tiled_tensor = tf.tile(input_tensor, multiples)

# Print the tiled tensor
print(tiled_tensor)
