import tensorflow as tf

# Define a function to generate sparse cross
def sparse_cross(sparse_tensors, dense_tensors):
    # Convert dense tensors to sparse tensors
    dense_tensors = [tf.convert_to_tensor(t, dtype=tf.float32) for t in dense_tensors]
    dense_tensors = [tf.sparse.from_dense(t) for t in dense_tensors]

    # Concatenate sparse tensors
    sparse_tensor = tf.sparse.concat(0, sparse_tensors)

    # Perform sparse cross operation
    sparse_cross = tf.sparse.sparse_dense_matmul(sparse_tensor, dense_tensors[0])

    # Return the result
    return sparse_cross

# Example usage
sparse_tensors = [tf.sparse.SparseTensor([[0, 0], [1, 2]], [1, 2], [3, 4])]
dense_tensors = [tf.constant([[1, 2], [3, 4], [5, 6]])]

result = sparse_cross(sparse_tensors, dense_tensors)
print(result)
