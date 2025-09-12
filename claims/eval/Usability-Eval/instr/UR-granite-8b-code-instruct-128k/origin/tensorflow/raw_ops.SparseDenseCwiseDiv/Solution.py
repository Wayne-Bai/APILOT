
import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Create a dense tensor
dense_tensor = tf.constant([[3, 0, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])

# Use the tf.raw_ops.SparseTensorDenseDiv component-wise divide the SparseTensor by the dense Tensor
result = tf.raw_ops.SparseTensorDenseDiv(sp_a=sparse_tensor, tb=dense_tensor)

# Print the result
print(result)
