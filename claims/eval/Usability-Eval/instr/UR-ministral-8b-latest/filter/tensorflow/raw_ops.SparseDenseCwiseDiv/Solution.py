import tensorflow as tf

# Assume you have a SparseTensor and a dense Tensor
sparse_tensor = tf.raw_ops.SparseTensor(indices=[[0, 1], [1, 2]], values=[2.0, 3.0], dense_shape=[2, 3])
dense_tensor = tf.constant([1.0, 2.0, 3.0])

# Ensure the dense tensor shape matches the dense_shape of the SparseTensor
assert dense_tensor.shape == sparse_tensor.dense_shape

# Perform the component-wise division using tf.raw_ops
result = tf.raw_ops.Div(x=sparse_tensor, y=dense_tensor)

print(result)
