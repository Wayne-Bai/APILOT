
import tensorflow as tf

# Define input tensors
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1]], values=[1, 2], dense_shape=[3, 3])
dense_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Define output tensor and operation
output_tensor = tf.raw_ops.ComponentWiseDiv(sparse_indices=sparse_tensor.indices, sparse_values=sparse_tensor.values, sparse_shape=sparse_tensor.dense_shape, dense=dense_tensor)
operation = output_tensor.op

# Print the output tensor
print(output_tensor)
