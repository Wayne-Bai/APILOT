import tensorflow as tf

# Create a variable
resource = tf.Variable([1, 2, 3, 4, 5, 6])

# Define the indices
indices = tf.constant([0, 2, 4])

# Use tf.raw_ops.ResourceGather to gather slices from the variable
gather = tf.raw_ops.ResourceGather(resource=resource, indices=indices)

# Print the result
print(gather.numpy())
