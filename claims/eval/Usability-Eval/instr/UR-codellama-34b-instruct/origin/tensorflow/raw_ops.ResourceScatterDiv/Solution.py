
import tensorflow as tf

# Create a variable and a tensor of indices
variable = tf.Variable(tf.zeros([10], dtype=tf.int32))
indices = tf.constant([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]], dtype=tf.int64)

# Create a tensor of updates
updates = tf.zeros_like(indices)

# Perform sparse updates on the variable using tf.scatter_nd_update()
sparse_updates = tf.scatter_nd_update(variable, indices, updates)

print("Sparse updates:", sparse_updates)
