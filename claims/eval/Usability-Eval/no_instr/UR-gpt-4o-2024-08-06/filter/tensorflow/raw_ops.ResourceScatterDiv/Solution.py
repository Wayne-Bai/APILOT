import tensorflow as tf

# Create a sample variable
variable = tf.Variable(initial_value=[[3.0, 3.0], [3.0, 3.0], [3.0, 3.0]], dtype=tf.float32)

# Indices representing the entries of the variable to update
indices = tf.constant([0, 2], dtype=tf.int32)

# Updates that will be divided into specific parts of the variable
updates = tf.constant([[1.0, 1.0], [0.5, 0.5]], dtype=tf.float32)

# Atomic operation to divide updates into the respective parts of the variable
resource_scatter_div = tf.raw_ops.ResourceScatterDiv(
    resource=variable.handle, 
    indices=indices, 
    updates=updates
)

# Run the operation
tf.print("Updated variable after ResourceScatterDiv:")
tf.print(variable)
