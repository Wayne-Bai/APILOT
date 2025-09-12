import tensorflow as tf

# Create a tensor resource
resource = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)

# Create a tensor of indices
indices = tf.constant([[0, 0], [1, 2]], dtype=tf.int32)

# Use tf.raw_ops.Gather to gather slices from the resource according to the indices
gathered_slices = tf.raw_ops.Gather(resource, indices)

print(gathered_slices)
