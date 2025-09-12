import tensorflow as tf

# Create a variable with a resource
resource = tf.Variable(tf.resource("MyResource"))

# Create a sparse update tensor
update = tf.constant([[1.0, 0.0], [0.0, 1.0]])

# Create a variable to store the result
result = tf.Variable(tf.zeros_like(resource))

# Use tf.raw_ops.SparseUpdate to apply the update
with tf.control_dependencies([update]):
    result = tf.raw_ops.SparseUpdate(
        resource=resource,
        updates=update,
        use_global_stats=False,
        name="my_update"
    )

# Print the result
print(result.numpy())
