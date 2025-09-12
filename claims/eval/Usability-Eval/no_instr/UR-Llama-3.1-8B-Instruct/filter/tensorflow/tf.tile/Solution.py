# Import necessary libraries
import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Tile the tensor by a factor of 2 in the first dimension
tiled_tensor = tf.tile(tensor, [2, 1])

# Print the original tensor
print("Original Tensor:")
print(tensor)

# Print the tiled tensor
print("\nTiled Tensor:")
print(tiled_tensor)
