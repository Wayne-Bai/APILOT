import tensorflow as tf

# Create a tf.Variable
variable = tf.Variable([[1, 2], [3, 4], [5, 6]], dtype=tf.float32)

# Create some sparse updates
indices = tf.constant([0, 2], dtype=tf.int32)  # Update rows at index 0 and 2
updates = tf.constant([[9, 8], [7, 6]], dtype=tf.float32)  # New values for the selected rows

# Use the `tf.tensor_scatter_nd_update` to apply sparse updates
updated_variable = tf.tensor_scatter_nd_update(variable, tf.expand_dims(indices, 1), updates)

# Print the result
print("Updated variable:")
print(updated_variable.numpy())
