
import tensorflow as tf
# Create a SparseTensor
sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1, 2],
    dense_shape=[3, 4]
)
# Use the tf.raw_ops.SparseTensorToDense method to split the SparseTensor into elements row-wise
dense_tensor = tf.raw_ops.SparseTensorToDense(
    sparse_tensor=sparse_tensor,
    output_shape=[3, 4],
    default_value=0
)
# Print the result
print(dense_tensor)
