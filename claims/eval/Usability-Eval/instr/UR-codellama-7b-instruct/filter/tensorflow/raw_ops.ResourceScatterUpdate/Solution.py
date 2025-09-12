import tensorflow as tf

# Create a variable to be assigned
var = tf.Variable(tf.zeros([3, 3], dtype=tf.float32))

# Assign sparse updates to the variable
indices = [0, 1]
updates = [1, 2]
sparse_update = tf.SparseTensor(indices, updates, dense_shape=var.get_shape())
tf.raw_ops.Assign(resource=var.handle, sparse_update=sparse_update)
