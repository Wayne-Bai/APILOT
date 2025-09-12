import tensorflow as tf

# Create a TensorFlow constant tensor
original_tensor = tf.constant([1, 2, 3, 4])

# Define the tiling pattern
# tile_dims: [2, 2] means we will tile the tensor along the first dimension 2 times and the second dimension 2 times

tile_dims = [2, 2]

# Use the tensorflow.py_function to construct a tensor by tiling the original_tensor
tiling_tensor = tf.py_function(lambda x: tf.reshape(tf.tile(x, tile_dims), [-1]),
                               [original_tensor], tf.int32)

# Print the tiled tensor
print(tiling_tensor)
