import tensorflow as tf

# Define the resource variable
resource = tf.Variable([1.0, 2.0, 3.0, 4.0, 5.0])

# Define the indices to gather
indices = tf.constant([0, 2, 4])

# Use tf.gather_nd to gather slices from the resource variable according to the indices
gathered_values = tf.gather_nd(resource, indices)

# Print the gathered values
print(gathered_values)
