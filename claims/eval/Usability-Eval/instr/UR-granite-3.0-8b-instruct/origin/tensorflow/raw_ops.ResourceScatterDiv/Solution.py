import tensorflow as tf

# Define the variable and the sparse updates
variable = tf.Variable([1.0, 2.0, 3.0])
sparse_updates = tf.SparseTensor(indices=[[0, 0]], values=[4.0], dense_shape=[2, 1])

# Use tf.raw_ops.ResourceScatterDiv to divide the variable by the sparse updates
result = tf.raw_ops.ResourceScatterDiv(
    ref=variable.handle,
    sparse_delta=sparse_updates.values,
    use_locking=False,
    name=None
)

# Print the result
print(result)
