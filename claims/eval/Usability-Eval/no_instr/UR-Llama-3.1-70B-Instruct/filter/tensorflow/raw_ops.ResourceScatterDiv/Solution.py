import tensorflow as tf

# Create a resource variable
resource_var = tf.Variable(1.0, name='var', dtype=tf.float32)

# Create sparse delta updates for the resource variable
sparse_delta = tf.sparse.SparseTensor(indices=[[0]], values=[0.5], dense_shape=[1])

# Apply the sparse updates
update_op = tf.raw_ops.ResourceScatterDiv(
    ref=resource_var.handle,
    indices=sparse_delta.indices,
    updates=sparse_delta.values,
    name='update_op'
)

# Create a session and initialize the variable
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Apply the update
    sess.run(update_op)

    # Print the updated value
    print(sess.run(resource_var))
