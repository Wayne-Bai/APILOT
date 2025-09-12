import tensorflow as tf

# Create a resource variable
resource_var = tf.Variable(tf.constant(1.0), name='resource_var')

# Create a sparse update operation
sparse_update = tf.raw_ops.SparseUpdateV2(
    resource_var,
    updates=[tf.constant(2.0)],
    use_resource=True
)

# Run the operation
with tf.Session() as sess:
    sess.run(sparse_update)
