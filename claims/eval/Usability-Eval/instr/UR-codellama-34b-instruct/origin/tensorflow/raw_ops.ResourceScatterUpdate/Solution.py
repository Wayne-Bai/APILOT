
import tensorflow as tf

# Define the variable to be updated
var = tf.Variable([0, 0], dtype=tf.float32)

# Define the sparse update values
sparse_updates = [[1, 0], [0, 1]]

# Define the indices of the sparse updates
indices = [0, 1]

# Assign the sparse updates to the variable using tf.scatter_nd_update()
tf.scatter_nd_update(var, indices, sparse_updates)
