# Importing necessary libraries
import tensorflow as tf

# Creating a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Tiling the tensor
tiled_tensor = tf.tile(tensor, [3, 2])

# Printing the original and tiled tensors
print("Original Tensor:")
print(tensor)

print("\nTiled Tensor:")
print(tiled_tensor)
