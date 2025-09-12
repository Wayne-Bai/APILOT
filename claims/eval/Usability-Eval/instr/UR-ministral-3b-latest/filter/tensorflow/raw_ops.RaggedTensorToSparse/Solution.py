import tensorflow as tf

# Assuming you have a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7]])

# Conver to SparseTensor with the same values
sparse_tensor = tf.raw_ops.RaggedToSparse(data=ragged_tensor, ragged_row_splits=None, dense_shape=None)

print(sparse_tensor)
