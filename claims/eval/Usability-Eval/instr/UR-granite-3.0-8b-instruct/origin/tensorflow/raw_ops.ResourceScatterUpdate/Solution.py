import tensorflow as tf

# Create a variable
var = tf.Variable([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

# Create a sparse update
sparse_updates = tf.scatter_nd([[0, 1, 2], [3, 4, 5]], [7.0, 8.0, 9.0], [6, 3])

# Perform the sparse update
var.scatter_nd_update(sparse_updates)

# Print the updated variable
print(var)
