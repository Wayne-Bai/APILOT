import tensorflow as tf

# Assuming 'ragged_tensor' is your RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [], [4, 5]])

# Convert RaggedTensor to SparseTensor
sparse_tensor = tf.raw_ops.sparse_to_dense_ragged(ragged_tensor)

print(sparse_tensor)
