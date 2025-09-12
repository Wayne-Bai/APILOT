import tensorflow as tf

# Create a SparseTensor
values = tf.constant([1, 2, 3, 4, 5])
indices = tf.constant([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])
dense_shape = tf.constant([5, 5])
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Reshape the SparseTensor
reshaped_sparse_tensor = tf.raw_ops.SparseToDense(
    sparse_tensor,
    output_shape=tf.constant([10, 10]),
    default_value=0,
    name="reshape_sparse_tensor"
)

# Print the reshaped SparseTensor
print(reshaped_sparse_tensor)
