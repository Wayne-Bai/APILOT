import tensorflow as tf

# Create a sample tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Define the tiling multiples
multiples = [2, 3]

# Use tf.tile() to construct a new tensor by tiling the input tensor
tiled_tensor = tf.tile(input_tensor, multiples)

# Print the tiled tensor
print(tiled_tensor)
