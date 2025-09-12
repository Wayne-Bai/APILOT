import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a resource
resource = tf.Resource(tensor)

# Create indices
indices = tf.constant([[0, 1], [1, 2]])

# Gather slices
gathered_slices = tf.raw_ops.GatherN(resource, indices)

# Print the result
print(gathered_slices)
