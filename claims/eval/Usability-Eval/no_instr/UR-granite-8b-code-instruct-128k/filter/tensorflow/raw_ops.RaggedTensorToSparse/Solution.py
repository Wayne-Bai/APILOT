import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.raw_ops.RaggedTensorToSparse(ragged_tensor=ragged_tensor)

# Print the SparseTensor
print(sparse_tensor)
