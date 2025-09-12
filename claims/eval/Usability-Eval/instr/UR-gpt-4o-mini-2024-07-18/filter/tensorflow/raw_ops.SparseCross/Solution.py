import tensorflow as tf

def generate_sparse_cross(dense_tensor, sparse_tensors):
    """
    Generates sparse cross from a list of sparse and dense tensors.

    Args:
        dense_tensor: A dense tensor.
        sparse_tensors: A list of sparse tensors.

    Returns:
        A sparse tensor representing the cross of the input tensors.
    """
    
    # Create a list to store the sparse tensors
    sparse_tensors_list = [tf.SparseTensor(indices=sparse_tensor.indices,
                                            values=sparse_tensor.values,
                                            dense_shape=sparse_tensor.dense_shape) 
                           for sparse_tensor in sparse_tensors]
    
    # Create a sparse cross using tf.sparse.sparse_csr_matrix
    sparse_cross = tf.sparse.sparse_dense_matmul(sparse_tensors_list, tf.expand_dims(dense_tensor, axis=0))

    return sparse_cross

# Example usage
dense_tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)
sparse_tensor_1 = tf.sparse.SparseTensor(indices=[[0, 0], [1, 1]], values=[10, 20], dense_shape=[2, 2])
sparse_tensors = [sparse_tensor_1]

sparse_cross_result = generate_sparse_cross(dense_tensor, sparse_tensors)
print(sparse_cross_result)
