import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    return tf.raw_ops.RaggedToSparse(ragged_tensor)

# Example usage
ragged_tensor = tf.RaggedTensor.from_row_splits([tf.ragged.constant([0, 1, 2]), tf.ragged.constant([3, 4])], num_rows=5)
sparse_tensor = ragged_to_sparse(ragged_tensor)
print(sparse_tensor)
