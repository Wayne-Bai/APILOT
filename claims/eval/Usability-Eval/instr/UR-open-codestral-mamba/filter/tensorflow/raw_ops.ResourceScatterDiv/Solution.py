import tensorflow as tf

# Define a variable
var = tf.Variable([1, 2, 3, 4, 5], dtype=tf.float32)

# Define the update value
update_value = tf.SparseTensor(indices=[[0], [2]], values=[10, 20], dense_shape=[5])

# Define the update function
update_func = tf.raw_ops.SparseApplyAdd(lhs_shape=var.shape, indices=update_value.indices, updates=update_value.values, handle=var.handle)

# Perform the update
with tf.control_dependencies([update_func]):
    var_update = var.assign(tf.identity(var))

# Open a session and run the variable update
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(var_update))
