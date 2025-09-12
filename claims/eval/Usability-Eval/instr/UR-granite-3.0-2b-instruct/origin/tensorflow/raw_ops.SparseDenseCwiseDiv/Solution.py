import tensorflow as tf
from tensorflow.python.framework import raw_ops

# Create a dense Tensor
dense_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Create a SparseTensor
sparse_tensor = tf.SparseTensor(values=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], indices=[[0, 0], [1, 1]], dense_shape=[2, 3])

# Perform component-wise division using tf.raw_ops
divided_sparse_tensor = raw_ops.SparseTensorDenseDivide(
    sparse_tensor=sparse_tensor,
    dense_tensor=dense_tensor,
    name="SparseTensorDenseDivide"
)

# Print the result
print(divided_sparse_tensor)
