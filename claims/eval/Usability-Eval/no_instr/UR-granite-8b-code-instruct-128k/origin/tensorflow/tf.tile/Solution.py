import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the tile multiples
tile_multiples = [2, 2]

# Construct the tensor by tiling the input tensor
output_tensor = tf.tile(input_tensor, tile_multiples)

# Print the output tensor
print(output_tensor)
