import tensorflow as tf

# Create a variable with a resource
resource = tf.resource("Variable:0")
variable = tf.Variable(0.0, name="my_variable", trainable=True)

# Create a sparse update tensor
sparse_update_tensor = tf.constant([[1.0, 0.0], [0.0, 1.0]])

# Create a tf.raw_ops.SparseUpdate operation
tf.raw_ops.SparseUpdate(
    resource,
    variable,
    sparse_update_tensor,
    update_op_name="my_update_op"
)
