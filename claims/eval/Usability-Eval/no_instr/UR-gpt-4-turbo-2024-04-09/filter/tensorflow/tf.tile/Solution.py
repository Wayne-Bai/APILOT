import tensorflow as tf

# Create a tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define multiples for tiling the tensor
multiples = [2, 3]

# Tile the tensor
tiled_tensor = tf.tile(input_tensor, multiples)

# Run and print the output
print("Original Tensor:\n", input_tensor.numpy())
print("Tiled Tensor:\n", tiled_tensor.numpy())
