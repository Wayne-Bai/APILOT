# Import necessary tensorflow library
import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Create a dense Tensor
dense_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                            [5.0, 6.0, 7.0, 8.0],
                            [9.0, 10.0, 11.0, 12.0]])

# Use tf.raw_ops.SparseTensorDenseMatMul for component-wise division
result = tf.raw_ops.SparseTensorDenseMatDiv(sparse_indices=sparse_tensor.indices,
                                            sparse_values=sparse_tensor.values,
                                            dense_shape=sparse_tensor.dense_shape,
                                            dense_tensor=dense_tensor)

# Print the result
print(result)
