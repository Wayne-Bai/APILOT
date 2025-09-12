# Import necessary libraries
import tensorflow as tf

# Create a 2D tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Tile the tensor
tiled_tensor = tf.tile(input=tensor, multiples=[2, 3])

# Print the original and tiled tensor
print("Original Tensor: ")
print(tensor)
print("Tiled Tensor: ")
print(tiled_tensor)
