# Import the necessary library
import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Tile the tensor
tiled_tensor = tf.tile(tensor, [2, 3])

# Print the original tensor
print("Original Tensor:")
print(tensor)

# Print the tiled tensor
print("\nTiled Tensor:")
print(tiled_tensor)
