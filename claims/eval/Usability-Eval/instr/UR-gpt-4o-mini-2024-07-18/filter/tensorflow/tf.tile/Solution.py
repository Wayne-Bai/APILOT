import tensorflow as tf

# Create a sample tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Specify the number of times to tile the tensor
multiples = [2, 3]  # For example, tile 2 times along the first axis and 3 times along the second

# Tile the tensor
tiled_tensor = tf.tile(input_tensor, multiples)

# Display the result
print(tiled_tensor)
