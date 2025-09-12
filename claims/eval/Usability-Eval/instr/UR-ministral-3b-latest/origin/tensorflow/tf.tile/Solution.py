import tensorflow as tf

# Create a tensor
original_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Define the replication shape
replication_shape = (2, 3)  # Example shape with 2 vertical and 3 horizontal replications

# Tile the tensor
tiling_result = tf.tile(original_tensor, replication_shape)

print(tiling_result)
