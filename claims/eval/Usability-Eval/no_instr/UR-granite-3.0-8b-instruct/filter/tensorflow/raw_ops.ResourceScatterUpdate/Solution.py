import tensorflow as tf

# Create a variable
var = tf.Variable([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

# Create a sparse tensor
sp_indices = tf.constant([[0, 0], [3, 4]], dtype=tf.int64)
sp_values = tf.constant([7.0, 8.0], dtype=tf.float32)
sp_shape = tf.constant([6, 6])
sparse_tensor = tf.SparseTensor(sp_indices, sp_values, sp_shape)

# Perform sparse updates
assign_op = tf.scatter_nd_update(var, sp_indices, sp_values)

# Initialize the variables
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    sess.run(assign_op)
    print(var.eval())
