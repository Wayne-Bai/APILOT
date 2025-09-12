import tensorflow as tf

# Create a simple variable with shape [4, 4]
variable = tf.Variable([[1.0, 2.0, 3.0, 4.0],
                        [5.0, 6.0, 7.0, 8.0],
                        [9.0, 10.0, 11.0, 12.0],
                        [13.0, 14.0, 15.0, 16.0]], dtype=tf.float32)

# Indices where we want to apply sparse updates
indices = tf.constant([0, 2])

# Sparse updates: the new values we want to "divide" into the specified parts of the variable
updates = tf.constant([[0.5, 0.5, 0.5, 0.5],
                       [2.0, 2.0, 2.0, 2.0]])

# Using tf.raw_ops.ResourceScatterDiv to divide sparse updates into the variable
tf.raw_ops.ResourceScatterDiv(
    resource=variable.handle, indices=indices, updates=updates
)

print("Updated variable:\n", variable.numpy())
