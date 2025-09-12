import tensorflow as tf

def sparse_cross_sparse_dense_tensors(sparse_tensors, dense_tensors):
    return tf.raw_ops.SparseCross(sparse_inputs=sparse_tensors, dense_inputs=dense_tensors)

# Example usage
# Note: Actual tensors should be properly defined as either sparse or dense for applying this operation.
sparse_tensor_a = tf.sparse.from_dense([[0, 0], [1, 2]])
dense_tensor_b = [[1.0, 2.0], [3.0, 4.0]]

result = sparse_cross_sparse_dense_tensors([sparse_tensor_a], [dense_tensor_b])
print("Result of Sparse Cross: ", result)
