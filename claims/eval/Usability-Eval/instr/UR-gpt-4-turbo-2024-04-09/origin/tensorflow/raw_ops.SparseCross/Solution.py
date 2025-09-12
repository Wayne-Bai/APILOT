import tensorflow as tf

def generate_sparse_cross(sparse_tensors, dense_tensors):
    # Convert dense tensors to sparse tensors
    converted_sparse_tensors = [tf.sparse.from_dense(tensor) for tensor in dense_tensors]

    # Combine all sparse tensors into a list
    all_sparse_tensors = sparse_tensors + converted_sparse_tensors

    # Use tf.sparse.cross to generate the sparse cross of the tensors
    sparse_cross = tf.sparse.cross(all_sparse_tensors)
    return sparse_cross

# Example usage
# Create sparse tensors
sparse_tensor_a = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
sparse_tensor_b = tf.sparse.SparseTensor(indices=[[0, 1], [1, 1]], values=[3, 4], dense_shape=[3, 4])

# Create dense tensors
dense_tensor_c = tf.constant([[1, 0], [0, 1], [1, 1]])

# Generate sparse cross
result_sparse_cross = generate_sparse_cross([sparse_tensor_a, sparse_tensor_b], [dense_tensor_c])
print(result_sparse_cross)
