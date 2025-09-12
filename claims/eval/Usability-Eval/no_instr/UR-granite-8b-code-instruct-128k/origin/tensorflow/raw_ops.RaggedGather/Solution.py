import tensorflow as tf

# Create a params tensor with shape [2, None]
params = tf.ragged.constant([[1, 2, 3], [4, 5]])

# Create an indices tensor with shape [3]
indices = tf.constant([0, 1, 0])

# Use tf.raw_ops.GatherRagged() to gather the ragged slices
output = tf.raw_ops.GatherRagged(params=params, indices=indices, axis=0)

# Print the output tensor
print(output)
