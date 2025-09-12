import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Create a resource
resource = tf.raw_op.Resource(tensor)

# Create indices
indices = tf.constant([2, 3])

# Gather slices
gathered_slices = tf.raw_op.Gather(resource, indices)

# Print the gathered slices
print(gathered_slices)
