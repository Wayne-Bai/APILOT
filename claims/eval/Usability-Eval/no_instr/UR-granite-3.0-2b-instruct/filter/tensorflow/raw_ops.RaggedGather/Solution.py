import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.RaggedTensor.from_tensor(
    tf.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]]),
    ragged_shape=[3, None])

# Create an indices tensor
indices = tf.constant([[0, 0], [1, 1], [2, 0], [2, 1]])

# Gather ragged slices
gathered_tensor = tf.raw_ops.GatherRaggedSlices(
    ragged_tensor, indices, num_namespaces=2)

# Print the gathered tensor
print(gathered_tensor)
