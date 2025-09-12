import tensorflow as tf

# Create a dense tensor
dense_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Create a sparse tensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1], [2, 2]], values=[1.0, 2.0, 3.0], dense_shape=[3, 3])

# Perform component-wise division
result = tf.raw_ops.SparseComponentwiseDiv(sparse_tensor, dense_tensor)

# Print the result
print(result.numpy())
