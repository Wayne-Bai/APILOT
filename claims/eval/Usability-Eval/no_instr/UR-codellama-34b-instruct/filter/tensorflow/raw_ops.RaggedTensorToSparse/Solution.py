
import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged_tensor(tf.range(12))

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.sparse_tensor_from_ragged(ragged_tensor)

# Print the SparseTensor
print(sparse_tensor)
