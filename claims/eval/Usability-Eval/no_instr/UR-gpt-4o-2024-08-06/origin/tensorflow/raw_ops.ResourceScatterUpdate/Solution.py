import tensorflow as tf

# Define a resource-like variable using Variable
resource_var = tf.Variable(initial_value=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)

# Sparse updates - the same values as the resource variable
indices = tf.constant([0, 2], dtype=tf.int32)  # Indices to update
updates = tf.constant([[10, 20, 30], [70, 80, 90]], dtype=tf.int32)  # New values to assign

# Use tf.tensor_scatter_nd_update for sparse assignment
updated_resource = tf.tensor_scatter_nd_update(resource_var, tf.expand_dims(indices, 1), updates)

# Assign the updated values back to the variable
assign_op = resource_var.assign(updated_resource)

# To apply the assignment
tf.print("Before update:", resource_var)
assign_op
tf.print("After update:", resource_var)
