import tensorflow as tf

# Define the sparse tensor updates
sparse_updates = tf.SparseTensor(indices=[[0, 0]], values=[10], dense_shape=[1, 1])

# Define the variable to be updated
var = tf.Variable([[1]])

# Use the tf.raw_ops.ResourceScatterDiv op to perform the update
update = tf.raw_ops.ResourceScatterDiv(
    resource=var.handle,
    indices=sparse_updates.indices,
    updates=sparse_updates.values,
    use_locking=False
)

# Initialize the variable and run the update operation
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    sess.run(update)

    # Print the updated variable
    print(var.eval())
