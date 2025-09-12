
import tensorflow as tf

# Define the shape of the original tensor
original_shape = (2, 3)

# Define the number of times the tensor should be tiled
num_tiles = 4

# Create a new tensor by tiling the original tensor
tiled_tensor = tf.tile(tf.range(original_shape), num_tiles)

print(tiled_tensor)
