import tensorflow as tf

# Define the input tensor and indices
input_tensor = tf.constant([1, 2, 3, 4, 5])
indices = tf.constant([2, 0, 4])

# Create a resource variable
resource = tf.Variable(input_tensor)

# Use tf.raw_ops.GatherV2 to gather slices
gathered_slices = tf.raw_ops.GatherV2(resource, indices, axis=0)

# Print the result
print(gathered_slices)
