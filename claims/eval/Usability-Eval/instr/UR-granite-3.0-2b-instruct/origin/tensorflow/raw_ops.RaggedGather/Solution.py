import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.RaggedTensor.from_tensor(
    tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ragged_shape=[3, None]
)

# Create an indices tensor
indices = tf.constant([[0, 2], [1, 3], [2, 0]])

# Use tf.raw_ops.GatherV2 to gather ragged slices
gathered_tensor = tf.raw_ops.GatherV2(
    indices, ragged_tensor, axis=0, batch_dims=2
)

# Print the gathered tensor
print(gathered_tensor.numpy())
