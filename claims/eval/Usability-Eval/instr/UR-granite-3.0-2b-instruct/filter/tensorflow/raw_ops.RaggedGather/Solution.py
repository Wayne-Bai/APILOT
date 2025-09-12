import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.RaggedTensor.from_tensor(tf.random.normal([3, 4]))

# Create an index tensor
indices = tf.constant([[0, 1, 2], [1, 2, 3], [2, 3, 4]])

# Use the GatherRagged op to gather slices from the ragged tensor
gathered_tensor = tf.raw_ops.GatherRagged(ragged_tensor, indices, axis=0)

# Print the gathered tensor
print(gathered_tensor)
