import tensorflow as tf

# Create a TensorFlow variable
variable = tf.Variable([[1, 2], [3, 4], [5, 6]], dtype=tf.int32)

# Define the indices and updates for the scatter operation
indices = tf.constant([[0, 1], [2, 0]])
updates = tf.constant([9, 8])

# Use tf.tensor_scatter_nd_update to update the variable
updated_variable = tf.tensor_scatter_nd_update(variable, indices, updates)

# To apply the updates directly to the variable, a simple assign operation would be used like:
variable.assign(updated_variable)

# Print the updated variable
print(variable.numpy())
