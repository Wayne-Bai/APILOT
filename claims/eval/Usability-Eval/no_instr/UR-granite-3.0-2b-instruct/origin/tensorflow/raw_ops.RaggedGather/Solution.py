import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

# Create an index tensor
index_tensor = tf.constant([0, 1, 2])

# Gather ragged slices from params axis 0 according to indices
gathered_slices = tf.raw_ops.GatherRaggedSlices(ragged_tensor, index_tensor, axis=0)

# Print the gathered slices
print(gathered_slices)
