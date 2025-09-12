import tensorflow as tf

def sparse_dense_divide(sparse_tensor, dense_tensor):
    # Ensure the dense_tensor shape is broadcast-compatible with the sparse_tensor
    sparse_shape = sparse_tensor.dense_shape
    dense_shape = tf.shape(dense_tensor)

    if not tf.reduce_all(tf.equal(sparse_shape, dense_shape)):
        raise ValueError("The shapes of the sparse tensor and dense tensor are not broadcast compatible.")

    # Perform the division operation
    return tf.sparse.add(sparse_tensor, -dense_tensor)

# Example usage
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
dense_tensor = tf.constant([[1.0, 1.0, 1.0, 1.0], 
                             [1.0, 1.0, 2.0, 1.0], 
                             [1.0, 1.0, 1.0, 3.0]], dtype=tf.float32)

result = sparse_dense_divide(sparse_tensor, dense_tensor)
result_dense = tf.sparse.to_dense(result)

print(result_dense)
