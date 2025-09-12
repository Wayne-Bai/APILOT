# Import necessary libraries
import tensorflow as tf

# Create a tensor
params = tf.constant([[1, 2], [3, 4], [5, 6]])

# Create indices for gathering slices
indices = tf.constant([[0, 1], [1]])

# Gather ragged slices from params along axis 0
gathered_slices = tf.raw_ops.GatherNd(params=params, indices=indices)

# Convert to a RaggedTensor
ragged_gathered_slices = tf.RaggedTensor.from_row_splits(
    values=gathered_slices,
    row_splits=tf.constant([0, 2, 3], dtype=tf.int64)
)

# Print the gathered and sliced tensor
print(ragged_gathered_slices)
