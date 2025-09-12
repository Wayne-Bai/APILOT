import tensorflow as tf

# Define a RaggedTensor to convert to a SparseTensor
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4, 5], [6, 7]])

# Convert RaggedTensor to SparseTensor
sparse_tensor = tf.raw_ops.RaggedTensorToSparseTensor(
    ragged_tensor, dtype=tf.int32
)

print("SparseTensor:")
print(sparse_tensor)
