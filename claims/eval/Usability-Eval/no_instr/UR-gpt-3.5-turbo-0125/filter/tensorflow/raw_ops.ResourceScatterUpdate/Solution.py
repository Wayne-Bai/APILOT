
import tensorflow as tf

# Define the variable to be updated
var = tf.Variable(tf.constant([[1.0, 2.0], [3.0, 4.0]]))

# Define the indices and updates for the sparse update
indices = tf.constant([[0, 0], [1, 1]])
updates = tf.constant([10.0, 20.0])

# Perform the sparse update operation
output = tf.tensor_scatter_nd_update(var, indices, updates)

# Print the updated variable
print(output)
