import tensorflow as tf

# Create a variable
resource_variable = tf.Variable(tf.random.uniform([3, 3]), resource=True)

# Create sparse updates
sparse_updates = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 3])

# Divide sparse updates into the variable
tf.raw_ops.ResourceSparseApplyGradAccumulator(
    resource=resource_variable.resource_handle,
    accumulate_var=resource_variable,
    accumulate_value=sparse_updates,
    global_step=tf.Variable(0, trainable=False),
    name=None
)
