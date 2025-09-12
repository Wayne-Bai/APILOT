import tensorflow as tf

# Define the input tensor
tensor = tf.constant([1, 2, 3])

# Define the factors for tiling
replication_factors = [2, 3]

# Use tiled function to tile the tensor
tiled_tensor = tf.tile(tensor, replication_factors)

print(tiled_tensor)
