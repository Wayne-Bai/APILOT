
import tensorflow as tf

# Create a tensor to be tiled
input_tensor = tf.constant([[1, 2], [3, 4]])

# Tile the tensor along axis 0 (repeat 2 times) and axis 1 (repeat 3 times)
tiled_tensor = tf.tile(input_tensor, [2, 3])

print(tiled_tensor)
