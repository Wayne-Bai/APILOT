import tensorflow as tf

# Define a sparse update
sparse_update = tf.constant([[1.0, 0.0], [0.0, 1.0]])

# Create a resource variable
resource_var = tf.Variable(tf.initializers.zeros([2, 2]))

# Divide the sparse update into the resource variable
with tf.control_dependencies([resource_var]):
    divised_update = tf.raw_ops.DivideSparseUpdate(sparse_update, resource_var)

# Print the divised_update
print(divised_update)
