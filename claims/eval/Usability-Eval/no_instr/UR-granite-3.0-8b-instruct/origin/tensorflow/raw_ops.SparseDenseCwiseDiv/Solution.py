import tensorflow as tf

# Assuming 'sparse_tensor' is your SparseTensor and 'dense_tensor' is your dense Tensor
sparse_tensor = tf.SparseTensor(...)  # replace ... with your SparseTensor
dense_tensor = tf.constant(...)  # replace ... with your dense Tensor

# Component-wise division
result = tf.raw_ops.SparseTensorDenseDiv(sparse_tensor, dense_tensor)

# Print the result
print(result)
