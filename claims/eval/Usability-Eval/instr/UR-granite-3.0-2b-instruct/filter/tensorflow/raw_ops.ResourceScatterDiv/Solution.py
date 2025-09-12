import tensorflow as tf

# Define a sparse update operation
sparse_update = tf.raw_ops.SparseUpdateV2(
    resource_name='my_resource',
    updates=tf.constant([[1.0, 2.0], [3.0, 4.0]]),
    index=tf.constant([0, 1])
)

# Create a variable with a resource name
var = tf.Variable(tf.zeros([2, 2]), name='my_variable')

# Apply the sparse update
with tf.control_dependencies([sparse_update]):
    var.assign(sparse_update)

# Print the updated variable
print(var)
