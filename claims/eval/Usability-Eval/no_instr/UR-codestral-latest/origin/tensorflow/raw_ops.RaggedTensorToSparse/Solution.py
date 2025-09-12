import tensorflow as tf

# Define a RaggedTensor
ragged_tensor = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])

# Convert the RaggedTensor to SparseTensor
sparse_tensor = tf.sparse.from_ragged(ragged_tensor)

# Printing the SparseTensor
print(tf.sparse.to_dense(sparse_tensor))
