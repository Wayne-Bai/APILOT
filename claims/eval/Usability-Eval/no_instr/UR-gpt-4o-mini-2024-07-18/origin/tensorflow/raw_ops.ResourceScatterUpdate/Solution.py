import tensorflow as tf

# Assuming you have a variable to which you want to assign sparse updates
variable = tf.Variable(tf.zeros([5, 5]), trainable=True)

# Create sparse updates
indices = tf.constant([[0, 0], [1, 2], [3, 4]])  # Indices to update
updates = tf.constant([1.0, 2.0, 3.0])  # Values to assign to the indices

# Create a sparse update operation
sparse_update = tf.experimental.numpy.zeros_like(variable)

# Assigning sparse updates to the variable
assign_op = tf.tensor_scatter_nd_update(variable, indices, updates)

# To execute the update, use a session in eager execution or simply run it in a function
print("Before update:", variable.numpy())
variable.assign(assign_op)
print("After update:", variable.numpy())
