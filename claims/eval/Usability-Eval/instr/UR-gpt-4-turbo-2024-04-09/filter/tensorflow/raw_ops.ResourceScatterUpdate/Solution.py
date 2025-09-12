import tensorflow as tf

# Create a variable
variable = tf.Variable(initial_value=[0, 1, 2, 3, 4], dtype=tf.int32)

# Define the indices for the sparse update
indices = tf.constant([[1], [3]])

# Define the updates
updates = tf.constant([9, 10])

# Update the variable
updated_variable = tf.tensor_scatter_nd_update(variable, indices, updates)

# Evaluate the variable
print("Before update:", variable.numpy())
variable.assign(updated_variable)
print("After update:", variable.numpy())
