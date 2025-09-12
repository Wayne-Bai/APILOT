import tensorflow as tf

# Create a resource variable
resource = tf.Variable(tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# Define indices for slicing
indices = tf.constant([0, 2])

# Use tf.gather to slice the variable
sliced_resource = tf.gather(resource, indices)

# Print the sliced resource
print(sliced_resource)
