import tensorflow as tf

# Define the function to create sparse cross features
def generate_sparse_cross(sparse_tensors, dense_tensors):
    # Note: tf.sparse.cross is deprecated, instead use tf.sparse.cross_hashed
    return tf.raw_ops.SparseCross(
        indices=sparse_tensors.indices, 
        values=sparse_tensors.values, 
        shapes=sparse_tensors.dense_shape, 
        dense_inputs=dense_tensors, 
        sep='_'
    )

# Example sparse and dense tensors
sparse_indices = tf.constant([[0, 0], [1, 0], [1, 1], [2, 0]])
sparse_values = tf.constant([1, 2, 2, 1], dtype=tf.int64)
sparse_shape = tf.constant([3, 2], dtype=tf.int64)

sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_values, dense_shape=sparse_shape)

dense_tensors = [tf.constant(['a', 'b', 'c']), tf.constant(['d', 'e', 'f'])]

# Generate the sparse cross
sparse_cross_result = generate_sparse_cross(sparse_tensor, dense_tensors)

# To see the output, run within a session if using TF 1.x, or simply print in TF 2.x
print(sparse_cross_result.indices.numpy())
print(sparse_cross_result.values.numpy())
print(sparse_cross_result.dense_shape.numpy())
