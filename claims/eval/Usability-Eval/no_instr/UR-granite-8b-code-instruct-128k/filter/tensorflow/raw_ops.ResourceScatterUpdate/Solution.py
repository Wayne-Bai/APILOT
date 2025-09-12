import tensorflow as tf

# Define the variable
resource = tf.Variable([1, 2, 3], dtype=tf.float32)

# Define the sparse updates
sparse_updates = tf.SparseTensor(
    indices=[[0, 0], [1, 1]],
    values=[10, 20],
    dense_shape=[2, 2]
)

# Define the operation to assign the sparse updates to the variable
assign_op = tf.raw_ops.ResourceScatterUpdate(
    resource=resource,
    indices=sparse_updates.indices,
    updates=sparse_updates.values
)

# Initialize the variables
init = tf.global_variables_initializer()

# Run the session
with tf.Session() as sess:
    sess.run(init)
    sess.run(assign_op)

    # Print the variable
    print(resource.eval())
